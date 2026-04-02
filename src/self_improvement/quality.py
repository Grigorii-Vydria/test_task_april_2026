from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RepositoryHealth:
    documentation_score: int
    test_score: int
    automation_score: int

    @property
    def total(self) -> int:
        return self.documentation_score + self.test_score + self.automation_score


def evaluate_repository_health(
    documentation_score: int,
    test_score: int,
    automation_score: int,
) -> RepositoryHealth:
    """Return a strongly-typed repository health snapshot."""
    for name, value in {
        "documentation_score": documentation_score,
        "test_score": test_score,
        "automation_score": automation_score,
    }.items():
        if not 0 <= value <= 10:
            raise ValueError(f"{name} must be between 0 and 10")
    return RepositoryHealth(documentation_score, test_score, automation_score)


def suggest_improvements(health: RepositoryHealth) -> list[str]:
    improvements: list[str] = []
    if health.documentation_score < 8:
        improvements.append("Improve README examples or architecture docs")
    if health.test_score < 8:
        improvements.append("Add or strengthen automated tests")
    if health.automation_score < 8:
        improvements.append("Improve CI/CD automation or guardrails")
    return improvements or ["Repository is in good shape; make only tiny safe refinements"]
