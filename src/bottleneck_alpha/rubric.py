from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Dict, Mapping

METRICS = [
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
]

METRIC_LABELS = {
    "cycle_strength": "大周期强度",
    "bottleneck_strength": "瓶颈强度",
    "validation": "验证程度",
    "financial_conversion": "财务转化",
    "valuation_gap": "估值错配",
    "market_discovery": "市场未发现程度",
    "scaling_path": "扩产 / 技术路径",
    "capital_structure": "资本结构",
    "catalyst_density": "催化剂密度",
    "risk_control": "风险可控性",
}

QUALITY_METRICS = [
    "cycle_strength",
    "bottleneck_strength",
    "validation",
    "financial_conversion",
    "scaling_path",
    "risk_control",
]

MISPRICING_METRICS = [
    "valuation_gap",
    "market_discovery",
    "catalyst_density",
]


@dataclass(frozen=True)
class ScoreResult:
    ticker: str
    total: float
    category: str
    position_type: str
    quality_score: float
    mispricing_score: float
    capital_score: float
    scores: Dict[str, float]


def validate_scores(scores: Mapping[str, float]) -> None:
    missing = [metric for metric in METRICS if metric not in scores]
    if missing:
        raise ValueError(f"Missing score metrics: {', '.join(missing)}")

    for metric in METRICS:
        if isinstance(scores[metric], bool):
            raise ValueError(f"Score for {metric} must be numeric, got boolean")
        value = float(scores[metric])
        if not isfinite(value):
            raise ValueError(f"Score for {metric} must be finite, got {value}")
        if value < 0 or value > 5:
            raise ValueError(f"Score for {metric} must be between 0 and 5, got {value}")


def classify(total: float) -> str:
    if total >= 40:
        return "High-conviction bottleneck candidate"
    if total >= 32:
        return "Worth tracking / small-to-medium position candidate"
    if total >= 25:
        return "Watchlist / small satellite only"
    return "Avoid or research-only"


def infer_position_type(
    *,
    total: float,
    quality_score: float,
    mispricing_score: float,
    capital_score: float,
    risk_control: float,
) -> str:
    if total < 25 or quality_score < 18 or capital_score <= 1:
        return "Avoid or research-only"
    if quality_score >= 27 and capital_score >= 4 and risk_control >= 3.5:
        return "Core compounder"
    if quality_score >= 23 and mispricing_score >= 8 and capital_score >= 2:
        return "High beta bottleneck"
    if quality_score >= 20:
        return "Watchlist / moonshot"
    return "Avoid or research-only"


def score(ticker: str, scores: Mapping[str, float]) -> ScoreResult:
    validate_scores(scores)
    normalized = {metric: float(scores[metric]) for metric in METRICS}
    total = sum(normalized.values())
    quality_score = sum(normalized[metric] for metric in QUALITY_METRICS)
    mispricing_score = sum(normalized[metric] for metric in MISPRICING_METRICS)
    capital_score = normalized["capital_structure"]
    return ScoreResult(
        ticker=ticker,
        total=total,
        category=classify(total),
        position_type=infer_position_type(
            total=total,
            quality_score=quality_score,
            mispricing_score=mispricing_score,
            capital_score=capital_score,
            risk_control=normalized["risk_control"],
        ),
        quality_score=quality_score,
        mispricing_score=mispricing_score,
        capital_score=capital_score,
        scores=normalized,
    )


def format_result(result: ScoreResult) -> str:
    lines = [
        "Bottleneck Alpha Score",
        "----------------------",
        f"Ticker: {result.ticker}",
        f"Total: {result.total:.1f} / 50",
        f"Category: {result.category}",
        f"Position Type: {result.position_type}",
        f"Quality Score: {result.quality_score:.1f} / 30",
        f"Mispricing Score: {result.mispricing_score:.1f} / 15",
        f"Capital Score: {result.capital_score:.1f} / 5",
        "",
        "Breakdown:",
    ]
    for metric in METRICS:
        label = METRIC_LABELS.get(metric, metric)
        lines.append(f"- {label} ({metric}): {result.scores[metric]:.1f} / 5")
    return "\n".join(lines)
