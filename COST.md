# Cost estimate

The target idea is to keep cost at **0.xx EUR/month** by using an ephemeral runner.

## Assumptions

- Hetzner minimal instance class around the lowest-cost tier
- runner exists only during test execution
- 12 runs/day (every 2 hours)
- 5-10 minutes average VM lifetime per run

## Estimate

### 5 minutes per run
- 12 runs/day = 60 minutes/day
- ~30 hours/month
- at roughly €0.004-0.006/hour => about **€0.12-0.18/month**

### 10 minutes per run
- 12 runs/day = 120 minutes/day
- ~60 hours/month
- about **€0.24-0.36/month**

## Why this is cheap

A permanently running server would cost the full monthly price.
An ephemeral runner pays only for active runtime during tests.
