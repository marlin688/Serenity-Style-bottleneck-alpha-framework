from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Mapping

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

@dataclass(frozen=True)
class ScoreResult:
    ticker: str
    total: float
    category: str
    scores: Dict[str, float]


def validate_scores(scores: Mapping[str, float]) -> None:
    missing = [metric for metric in METRICS if metric not in scores]
    if missing:
        raise ValueError(f"Missing score metrics: {', '.join(missing)}")

    for metric in METRICS:
        value = float(scores[metric])
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


def score(ticker: str, scores: Mapping[str, float]) -> ScoreResult:
    validate_scores(scores)
    normalized = {metric: float(scores[metric]) for metric in METRICS}
    total = sum(normalized.values())
    return ScoreResult(
        ticker=ticker,
        total=total,
        category=classify(total),
        scores=normalized,
    )


def format_result(result: ScoreResult) -> str:
    lines = [
        "Bottleneck Alpha Score",
        "----------------------",
        f"Ticker: {result.ticker}",
        f"Total: {result.total:.1f} / 50",
        f"Category: {result.category}",
        "",
        "Breakdown:",
    ]
    for metric in METRICS:
        label = METRIC_LABELS.get(metric, metric)
        lines.append(f"- {label} ({metric}): {result.scores[metric]:.1f} / 5")
    return "\n".join(lines)
