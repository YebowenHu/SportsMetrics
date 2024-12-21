import os
import sys
import json
import yaml
import time

from time import sleep
from openai import OpenAI
from openai._exceptions import APIError, APIConnectionError, RateLimitError


ROOT_DIR = os.getcwd()

# rise when accur errors, try three times
# error list [502, 504, 500]
def stable_request(client, parameters, max_retries=10):
    # print("stable request max_token: ",parameters['max_tokens'])
    i = 0
    response = None
    while i < max_retries:
        try:
            response = client.chat.completions.create(**parameters)
            break
        except APIError as e:
            print(f"OpenAI API error: {e}")
        except APIConnectionError as e:
            print(f"OpenAI API Connection error: {e}")
        except RateLimitError:
            print("OpenAI API rate limit exceeded.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
        i += 1
        time.sleep(1)
    if i >= max_retries or response is None:
        return None
    return response

def msg_json(client, parameters, content_desc=None):
    while True:        
        response = stable_request(client, parameters)
        if not response:
            return None
        # * check the stop reason, if the output JSON is cut off, increase the max_length
        finish_reason = response.choices[0].finish_reason
        if finish_reason == "content_filter":
            print("Content filter detected")
            moderation = client.moderations.create(input=json.dumps(parameters['messages']))
            print("moderation %s", moderation)
            break
        else:
            break
    response = response.choices[0].message.content.strip()
    return response

class CallGPT:
    def __init__(self, model, 
                 max_tokens=1024,
                 config_file=os.path.join(ROOT_DIR, "openai.yaml")):
        
        print(f"using api from config {config_file}")

        self.model_name = model
        self.config = yaml.safe_load(open(config_file))
        self.parameters = self.config["parameters"]
        self.parameters.update(
            {"model":model,"max_tokens":max_tokens}
        )

        # initial client
        self.client = OpenAI(api_key=self.config["api-key"])
        
    def json_chat(self, messages, content_desc=None):
        self.parameters.update({
            "messages": messages,
            "response_format":{"type":"json_object"}})
        response = msg_json(self.client, self.parameters, content_desc=content_desc)
        return response