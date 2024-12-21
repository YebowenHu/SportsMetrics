"""
    This script is used as a sample to process the tasks for the evaluation.
"""
import json

from tqdm import tqdm

from sportsmetrics import GeneralTaskLoader
from utils.CallAPI import CallGPT


def message_wrapper(model_name, task_instance):
    sys_msg = task_instance['system_message']
    user_msg = task_instance['user_message']
    if "gpt" in model_name or "llama" in model_name:
        messages = [
            {"role": "system", "content": sys_msg},
            {"role": "user", "content": user_msg}
        ]
    elif "mistral" in model_name:
        messages = f"<s>[INST]{sys_msg}\n{user_msg}[/INST]"
    else:
        messages = f"System Message: {sys_msg}\n\nUser Message: {user_msg}"
    return messages

def main(task_path, model, batch_size=False):
    task = GeneralTaskLoader(task_path)
    client = CallGPT(model)
    output = []
    output_path = "results.json"
    if not batch_size:
        # load the task instance one by one
        for i in tqdm(task.iter_instance()):
            messages = message_wrapper(model, i)
            # feed to model to get response
            response = client.json_chat(messages)
            if response is not None:
                i['model_response'] = response
                output.append(i.copy())
                break
    else:
        # load the task instance by batch, for multi-process evaluation
        for i in task.iter_batch(batch_size):
            print(len(i))
    
    # save the output
    with open(output_path, "w") as w:
        json.dump(output, w, indent=4)

    return

if __name__ == "__main__":
    task = "data/NBA/reasoning-team_points_tracking.json"
    model = "gpt-4o"
    main(task, model, batch_size=False)