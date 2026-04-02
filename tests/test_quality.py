import pytest

from self_improvement.quality import evaluate_repository_health, suggest_improvements


def test_repository_health_total():
    health = evaluate_repository_health(7, 8, 9)
    assert health.total == 24


def test_suggest_improvements_returns_items_for_weak_areas():
    health = evaluate_repository_health(6, 9, 5)
    suggestions = suggest_improvements(health)
    assert any("README" in item or "architecture" in item for item in suggestions)
    assert any("automation" in item.lower() for item in suggestions)


@pytest.mark.parametrize("value", [-1, 11])
def test_scores_are_validated(value: int):
    with pytest.raises(ValueError):
        evaluate_repository_health(value, 5, 5)
