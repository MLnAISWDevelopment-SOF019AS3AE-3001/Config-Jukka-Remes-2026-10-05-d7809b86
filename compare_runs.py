import sys
from mlflow.tracking import MlflowClient

TRACKING_URI = "http://127.0.0.1:5000"
EXPERIMENT = "demo-notebook"
METRICS = ("rmse", "r2", "mae")

def row(client, experiment_id, label, commit):
    runs = client.search_runs(
        [experiment_id],
        # Stored hashes are full SHAs. A short prefix such as 34d91b5 still matches.
        filter_string=f"params.git_commit_hash LIKE '{commit}%'",
        max_results=1,
    )
    values = [f"{label} `{commit}`"]
    metrics = runs[0].data.metrics if runs else {}
    values.extend(str(metrics.get(name, "")) for name in METRICS)
    return "| " + " | ".join(values) + " |"

baseline, modified = sys.argv[1], sys.argv[2]
client = MlflowClient(TRACKING_URI)
experiment = client.get_experiment_by_name(EXPERIMENT)
lines = [
    "# Exercise 1 comparison",
    "",
    "| run | rmse | r2 | mae |",
    "| --- | ---: | ---: | ---: |",
    row(client, experiment.experiment_id, "baseline", baseline),
    row(client, experiment.experiment_id, "modified", modified),
    "",
]
text = "\n".join(lines)
open("comparison.md", "w", encoding="utf-8").write(text)
print(text)
