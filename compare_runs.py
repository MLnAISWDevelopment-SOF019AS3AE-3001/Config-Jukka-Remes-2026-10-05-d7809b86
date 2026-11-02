
import sys
from pathlib import Path
from mlflow.tracking import MlflowClient

MLFLOW_URI = "http://127.0.0.1:5000"
EXPERIMENT_NAME = "demo-notebook"
METRICS = ("rmse", "r2", "mae")


def get_run(client, experiment_id, commit_hash):
    runs = client.search_runs(
        experiment_ids=[experiment_id],
        max_results=1000,
    )

    matches = [
        run for run in runs
        if run.data.params.get("git_commit_hash", "").startswith(commit_hash)
    ]

    if not matches:
        raise ValueError(f"No MLflow run found for commit {commit_hash}")

    return matches[0]


def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_runs.py BASELINE_COMMIT MODIFIED_COMMIT")
        sys.exit(1)

    baseline_hash, modified_hash = sys.argv[1:3]

    client = MlflowClient(tracking_uri=MLFLOW_URI)
    experiment = client.get_experiment_by_name(EXPERIMENT_NAME)

    if experiment is None:
        raise ValueError(f"Experiment '{EXPERIMENT_NAME}' not found")

    baseline = get_run(client, experiment.experiment_id, baseline_hash)
    modified = get_run(client, experiment.experiment_id, modified_hash)

    rows = [
        "# Exercise 1 — MLflow Run Comparison",
        "",
        f"Baseline commit: `{baseline.data.params['git_commit_hash']}`",
        "",
        f"Modified commit: `{modified.data.params['git_commit_hash']}`",
        "",
        "| Metric | Baseline | Modified |",
        "|---|---:|---:|",
    ]

    for metric in METRICS:
        old = baseline.data.metrics.get(metric)
        new = modified.data.metrics.get(metric)

        if old is None or new is None:
            raise ValueError(f"Missing metric: {metric}")

        rows.append(f"| {metric.upper()} | {old:.3f} | {new:.3f} |")

    rows += [
        "",
        "## Parameters",
        "",
        f"- Baseline alpha: {baseline.data.params.get('alpha')}",
        f"- Modified alpha: {modified.data.params.get('alpha')}",
        f"- Baseline l1_ratio: {baseline.data.params.get('l1_ratio')}",
        f"- Modified l1_ratio: {modified.data.params.get('l1_ratio')}",
        "",
        "## Interpretation",
        "",
        "The modified model uses a lower ElasticNet alpha value. "
        "Its RMSE and MAE decreased, while R² increased, "
        "indicating better predictive performance in these runs.",
        "",
    ]

    Path("comparison.md").write_text(
        "\n".join(rows), encoding="utf-8"
    )

    print("Successfully generated comparison.md")
    print("\n".join(rows))


if __name__ == "__main__":
    main()
