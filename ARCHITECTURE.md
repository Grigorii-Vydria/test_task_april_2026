# Architecture

## 1. Self-improvement loop

```text
GitHub schedule (every 2h)
  -> checkout repo
  -> build repository snapshot
  -> call LLM with tight guardrails
  -> apply tiny safe change
  -> run lint + tests
  -> open PR
```

### Guardrails

- limit changed files
- limit changed lines
- do not touch secrets or infrastructure auth
- do not modify workflows unless explicitly allowed
- require successful validation before PR

## 2. Ephemeral Hetzner test runner

```text
GitHub-hosted job
  -> Hetzner API: create VM
  -> cloud-init bootstrap
  -> optional Tailscale join
  -> GitHub runner registration
  -> tests on self-hosted runner
  -> destroy VM (always)
```

## 3. Components

- `scripts/provision_hetzner.py` — create server through Hetzner API
- `cloud-init/runner-cloud-init.yaml` — install packages and bootstrap runtime
- `scripts/wait_for_runner.py` — poll GitHub API until runner is online
- `scripts/destroy_hetzner.py` — guaranteed cleanup
- `scripts/self_improve.py` — snapshot and future LLM orchestration entrypoint
