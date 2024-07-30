# SportsMetrics
Benchmark data to evaluate numerical reasoning and information fusion of LLMs.

[SportsMetrics: Blending Text and Numerical Data to Understand Information Fusion in LLMs](https://arxiv.org/abs/2402.10979)  \
Yebowen Hu, Kaiqiang Song, Sangwoo Cho, Xiaoyang Wang, Hassan Foroosh, Dong Yu, Fei Liu   \
[*In proceeding to ACL 2024 Main Conference, Bangkok, Thailand.*](https://2024.aclweb.org/program/main_conference_papers/)

## Usage of Benchmark
1. Select the task from data/
2. Import GeneralTaskLoader from sportsmetrics.py
```python
from sportsmetrics import GeneralTaskLoader

batch_size = False # by default
if not batch_size:
    # load the task instance one by one
    for i in task.iter_instance():
        yiled i['system_message'], i['user_message']
else:
    # load the task instance by batch
    for i in task.iter_batch(batch_size):
        yiled i['system_message'], i['user_message']
```

Instance from TaskLoader
```python
{
    "id": str,
    "system_message": str,
    "user_message": str,
    "ground_truth": dict()
}
```

## Benchmark Tasks

The LLM is mandatorily required to generate responses in JSON format.

### Reasoning Task
- **reasoning-team_points_tracking**: Tracking team points in one match.  
- **reasoning-key_stats_tracking**: Tracking the key statistics for sports analytics.

### Conflicts Task
- **conflict-one_point_rule**: All scoring actions in the competition are set to be worth only one point.  
- **conflict-swap_{num}_players**: Swap {num} of spalyer between two teams.

### Robustness Task
- **robustness-duplicate_{prob}**: Replicate the non-scoring move with a probability of {prob}.  
- **robustness-remove_{prob}**: Remove the non-scoring move with a probability of {prob}.  
- **robustness-shuffled_pbp**: Shuffle the order of all moves in play-by-play descriptions while maintain the original order of timestamps.  
- **robustness-{num}_fiction_names**: Randomly select {num} of players from both teams and replace them with names from fiction movies. 


**Bibtex**
```
@misc{hu2024sportsmetricsblendingtextnumerical,
      title={SportsMetrics: Blending Text and Numerical Data to Understand Information Fusion in LLMs}, 
      author={Yebowen Hu and Kaiqiang Song and Sangwoo Cho and Xiaoyang Wang and Hassan Foroosh and Dong Yu and Fei Liu},
      year={2024},
      eprint={2402.10979},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2402.10979}, 
}
```
