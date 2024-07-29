"""
    Module to process the task instance of SportsMetrics from file in data/.
"""

import json

from itertools import chain

def batchit(data_list, size=128):
    assert hasattr(data_list, "__iter__")
    assert size is None or isinstance(size, int) and size > 0
    batch = []
    for row in data_list:
        batch.append(row)
        if len(batch) == size:
            yield batch.copy()
            batch.clear()
    if len(batch) > 0:
        yield batch


class BasicLoader:
    def __init__(self, fpath):
        self.fpath = fpath
        self._load_data()
        self.data=self._preprocess()

    def _load_data(self):
        with open(self.fpath, "r") as f:
            self.data = json.load(f)
        return

    def _preprocess(self):
        pass # do some preprocessing after load the data file

    def iter_instance(self): # iter the benchmark
        for instance in self.data:
            yield instance
    
    def iter_batch(self, batch_size):
        if len(self.data) == 0:
            print("No data loaded.")
        else:
            for i in batchit(self.data, batch_size):
                yield i
    

class GeneralTaskLoader(BasicLoader):
    """Most used data loader for all tasks"""
    def __init__(self, fpath):
        super().__init__(fpath)

    def _preprocess(self):
        _processed_data = []
        for _instance in self.data:
            # load play-by-play data
            _pbp_header = _instance['game_input'][0]
            _pbp_content = "\n".join(chain.from_iterable(_instance['game_input'][1:]))
            _game_input = f"{_pbp_header}\n{_pbp_content}"
            _user_message = f"{_instance['prompt']}\n\nTeam-Player Table:\n{_instance['player_affiliation']}\n\nGame Input:\n{_game_input}"

            _processed_data.append(
                {
                    "id": _instance['gameID'],
                    "system_message": _instance['sys_msg'],
                    "user_message": _user_message,
                    "ground_truth": _instance['ground_truth'],
                }
            )
        return _processed_data

class ConflictTaskLoader(BasicLoader):
    """extra information for task: conflict-swap_players"""
    def __init__(self, fpath):
        super().__init__(fpath)

    def _preprocess(self):
        _processed_data = []
        for _instance in self.data:
            # load play-by-play data
            _pbp_header = _instance['game_input'][0]
            _pbp_content = "\n".join(chain.from_iterable(_instance['game_input'][1:]))
            _game_input = f"{_pbp_header}\n{_pbp_content}"
            _user_message = f"{_instance['prompt']}\n\nTeam-Player Table:\n{_instance['player_affiliation']}\n\nGame Input:\n{_game_input}"

            _processed_data.append(
                {
                    "id": _instance['gameID'],
                    "system_message": _instance['sys_msg'],
                    "user_message": _user_message,
                    "ground_truth": _instance['ground_truth'],
                    "changed_names": _instance['changed_name'],
                }
            )
        return _processed_data