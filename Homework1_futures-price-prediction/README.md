# Short-Term Futures Price Prediction
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Junior futures desk traders experience intraday price volatility uncertainty and have limited quantitative guidelines on timing trade entry/exit points. In the absence of real-time predictive assistance, they use subjective discretion and senior guidance that may fail to capture high-probability trades or subject them to unnecessary exposure. Hence, this project proposes to develop a model to predict the next 1–5 minute price direction for chosen futures contracts (e.g., E-mini S&P 500, crude oil) based on order book depth, tick data, and recent price trends.
Precise, timely predictions can assist traders in enhancing entry and exit timing, minimizing exposure to unfavorable moves, and managing risk capital more effectively during the trading session.

## Stakeholder & User
**Decision-maker:** Junior futures traders.  
**Users:** Same as decision-makers.  
**Timing & workflow:** Intraday, with updates every 1–5 minutes. Predictions must integrate into existing charting tools or dashboards with minimal disruption to the trader’s workflow.

## Useful Answer & Decision
**Type:** Predictive.  
**Metric:** Directional signal accuracy ≥ 55% on a rolling 2-week window, Sharpe ratio improvement ≥ 0.3 over baseline discretionary trading.  
**Artifact:** Real-time directional signal (+1 = long, 0 = hold, –1 = short) with probability score, delivered via API feed or dashboard overlay.

## Assumptions & Constraints
- Live tick/order book data feed is available via broker API.
- Prediction latency ≤ 500ms for each update.
- Model output must be explainable enough for trader adoption.
- Integrates into existing charting platforms (e.g., TradingView, Bloomberg).
- No proprietary data leaves the local environment.

## Known Unknowns / Risks
- Regime shifts caused by macroeconomic events.
- Sudden drops in liquidity or order book depth.
- Temporary market data feed outages.
- Potential overfitting to historical intraday patterns.
- Mitigation strategies include fallback to simple moving-average-based signals and continuous backtesting.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Define scope, stakeholders, and success metrics → Problem Framing & Scoping (Stage 01) → README.md + stakeholder memo + one-pager
- Build baseline predictive model → EDA & Baselines (Stage 02) → exploratory notebook + baseline model report
- Tune model for live deployment → Modeling & Validation (Stage 03) → validated model + deployment script
- Integrate into trader workflow → Delivery & Handoff (Stage 04) → dashboard/API + usage guide

## Repo Plan
- `/data/` : Historical and real-time futures price/order book data.
- `/src/` : Data processing, feature engineering, and model scripts.
- `/notebooks/` : EDA, model prototyping, and backtesting notebooks.
- `/docs/` : Stakeholder memo, one-pager, and project documentation.
- **Update cadence:** Weekly commits; continuous integration for model updates once live.
