# Exercise 1 — MLflow Run Comparison

Baseline commit: `a5d811a47c159bccdd8b144345728c68b2215ff7`

Modified commit: `c1acb8dc928f1655d0a91ffa0565811e9038111b`

| Metric | Baseline | Modified |
|---|---:|---:|
| RMSE | 0.804 | 0.683 |
| R2 | 0.115 | 0.297 |
| MAE | 0.662 | 0.540 |

## Parameters

- Baseline alpha: 0.5
- Modified alpha: 0.2
- Baseline l1_ratio: 0.5
- Modified l1_ratio: 0.5

## Interpretation

The modified model uses a lower ElasticNet alpha value. Its RMSE and MAE decreased, while R² increased, indicating better predictive performance in these runs.
