import math

import pytest

from bottleneck_alpha.rubric import METRICS, classify, score


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
    assert result.quality_score == 22
    assert result.mispricing_score == 11
    assert result.capital_score == 4
    assert result.position_type == "Watchlist / moonshot"


def test_nvda_like_core_compounder_is_not_flattened_into_total_only():
    scores = {
        "cycle_strength": 5,
        "bottleneck_strength": 5,
        "validation": 5,
        "financial_conversion": 5,
        "valuation_gap": 1.5,
        "market_discovery": 0.5,
        "scaling_path": 5,
        "capital_structure": 5,
        "catalyst_density": 4,
        "risk_control": 3.5,
    }
    result = score("NVDA", scores)
    assert result.total == 39.5
    assert result.category == "Worth tracking / small-to-medium position candidate"
    assert result.quality_score == 28.5
    assert result.mispricing_score == 6
    assert result.capital_score == 5
    assert result.position_type == "Core compounder"


def test_nebius_like_ramp_is_high_beta_bottleneck():
    scores = {
        "cycle_strength": 5,
        "bottleneck_strength": 3.5,
        "validation": 4.5,
        "financial_conversion": 4,
        "valuation_gap": 3,
        "market_discovery": 2.5,
        "scaling_path": 4,
        "capital_structure": 2.5,
        "catalyst_density": 4.5,
        "risk_control": 2.5,
    }
    result = score("NBIS", scores)
    assert result.total == 36
    assert result.category == "Worth tracking / small-to-medium position candidate"
    assert result.quality_score == 23.5
    assert result.mispricing_score == 10
    assert result.capital_score == 2.5
    assert result.position_type == "High beta bottleneck"


def test_invalid_metric_range():
    scores = {metric: 3 for metric in METRICS}
    scores["cycle_strength"] = 6
    with pytest.raises(ValueError):
        score("TEST", scores)


def test_invalid_non_finite_score():
    scores = {metric: 3 for metric in METRICS}
    scores["cycle_strength"] = math.nan
    with pytest.raises(ValueError):
        score("TEST", scores)


def test_invalid_boolean_score():
    scores = {metric: 3 for metric in METRICS}
    scores["cycle_strength"] = True
    with pytest.raises(ValueError):
        score("TEST", scores)
