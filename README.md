# SportsMetrics
Benchmark data for numerical reasoning and information fusion of LLMs.

[SportsMetrics: Blending Text and Numerical Data to Understand Information Fusion in LLMs](https://arxiv.org/abs/2402.10979)  \
Yebowen Hu, Kaiqiang Song, Sangwoo Cho, Xiaoyang Wang, Hassan Foroosh, Dong Yu, Fei Liu   \
In proceeding to ACL 2024 Main Conference, Bangkok, Thailand. [Long Paper](https://2024.aclweb.org/program/main_conference_papers/)

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
### Reasoning Task
reasoning-team_points_tracking (NBA), reasoning-key_stats_tracking (NBA), reasoning-key_stats_tracking (NFL)

### Conflicts Task

### Robustness Task


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
