# Security

## Public exposure

Goal: **no public SSH exposure**.

Recommended setup:
- Hetzner firewall: deny inbound SSH from the public internet
- UFW on VM: default deny incoming
- private/debug access only through **Tailscale** (or another private tunnel solution)
- GitHub runner communicates outbound only

## Secrets

Use GitHub Actions Secrets / local `.env` only.
Never hardcode:
- Hetzner token
- GitHub PAT / registration tokens
- OpenAI API key
- Tailscale auth key

## LLM automation guardrails

The self-improvement agent should:
- propose only tiny changes
- never modify secrets or auth configuration
- never self-approve destructive changes
- prefer PRs over direct pushes to main

## Operational safety

Cleanup must run with `if: always()`.
Additionally, a scheduled janitor workflow is recommended later to delete any stale Hetzner servers tagged `ephemeral=true`.
