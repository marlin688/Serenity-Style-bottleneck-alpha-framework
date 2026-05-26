import pytest

from bottleneck_alpha.rubric import classify, score


def test_classify():
    assert classify(45) == "High-conviction bottleneck candidate"
    assert classify(35) == "Worth tracking / small-to-medium position candidate"
    assert classify(28) == "Watchlist / small satellite only"
    assert classify(20) == "Avoid or research-only"


def test_score_total():
    scores = {
        "cycle_strength": 5,
        "bottleneck_strength": 4,
        "validation": 4,
        "financial_conversion": 3,
        "valuation_gap": 3,
        "market_discovery": 4,
        "scaling_path": 3,
        "capital_structure": 4,
        "catalyst_density": 4,
        "risk_control": 3,
    }
    result = score("TEST", scores)
    assert result.total == 37
    assert result.category == "Worth tracking / small-to-medium position candidate"


def test_invalid_metric_range():
    scores = {metric: 3 for metric in [
        "cycle_strength",
        "bottleneck_strength",
        "validation",
        "financial_conversion",
        "valuation_gap",
        "market_discovery",
        "scaling_path",
        "capital_structure",
        "catalyst_density",
        "risk_control",
    ]}
    scores["cycle_strength"] = 6
    with pytest.raises(ValueError):
        score("TEST", scores)
