"""Small demo package used by CI and by the self-improvement agent."""

from .quality import evaluate_repository_health, suggest_improvements

__all__ = ["evaluate_repository_health", "suggest_improvements"]
