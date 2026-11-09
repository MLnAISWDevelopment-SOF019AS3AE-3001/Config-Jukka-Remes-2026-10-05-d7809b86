# Exercise 1 comparison

| run | rmse | r2 | mae |
| --- | ---: | ---: | ---: |
| baseline `8324dd9` | 0.7808609497432865 | 0.12815896645721192 | 0.6437104204166308 |
| modified `f0dc22a` | 0.666472958458254 | 0.3015665641635322 | 0.5398714879501239 |

## Summary

I changed `alpha` from 0.5 to 0.2 and left `l1_ratio` at 0.5. All three metrics improved: RMSE dropped from 0.781 to 0.666, MAE dropped from 0.644 to 0.540, and R2 rose from 0.128 to 0.302.

A lower `alpha` means weaker regularization in the ElasticNet model. With `alpha` at 0.5 the coefficients were probably shrunk too much, so the model underfit. With 0.2 it can use the features more, which explains the lower error and the higher R2.

R2 is still low at 0.302, so the model explains only a small part of the variance in wine quality. The split also has no fixed `random_state`, so part of the difference could come from a different random split and not only from `alpha`.