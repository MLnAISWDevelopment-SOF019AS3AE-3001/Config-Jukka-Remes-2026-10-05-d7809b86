# Exercise 1 — Baseline and Modified Pipeline Comparison

## Experiment

The purpose of this experiment was to evaluate how changing the ElasticNet regularization parameter `alpha` affects model performance.

Two versions of the pipeline were executed using the `exercise-1-120` branch. The baseline used `alpha = 0.5`, while the modified version used `alpha = 0.2`. The `l1_ratio` parameter remained unchanged at `0.5`.

## Git Commits

- **Baseline:** `a5d811a47c159bccdd8b144345728c68b2215ff7`
- **Modified:** `c1acb8dc928f1655d0a91ffa0565811e9038111b`

## Evaluation Results

| Metric | Baseline (alpha = 0.5) | Modified (alpha = 0.2) |
| RMSE | 0.804 | 0.683 |
| R² | 0.115 | 0.297 |
| MAE | 0.662 | 0.540 |

## Analysis

Reducing the `alpha` parameter from `0.5` to `0.2` improved all three recorded evaluation metrics.

RMSE decreased from 0.804 to 0.683, a reduction of approximately 15.0%. MAE decreased from 0.662 to 0.540, an improvement of approximately 18.4%.

R² increased from 0.115 to 0.297, indicating that the modified model explained a larger proportion of variance in the evaluation data.

These results suggest that reducing the regularization strength improved the ElasticNet model's predictive performance for this experiment.

## Conclusion

The modified model performed better than the baseline according to RMSE, MAE, and R². The experiment demonstrates how changing a model hyperparameter can affect evaluation results.

Both versions successfully logged their parameters and metrics in MLflow. The baseline Kubeflow run completed training and evaluation, although the deployment stage reported a failure.