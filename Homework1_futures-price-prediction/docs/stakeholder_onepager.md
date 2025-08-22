# Stakeholder One-Pager: Short-Term Futures Price Prediction

**Audience:** Junior traders on the futures desk  
**Decision cadence:** Intraday, every 1–5 minutes  

## Problem
Junior traders rely heavily on subjective setups and ad-hoc guidance, which can miss reversals and make risk sizing inconsistent during fast markets.

## Proposed Solution
A real-time predictive signal for the next 1–5 minute move on selected futures (e.g., ES, CL). The output is a directional call and confidence score surfaced inside the trader’s existing charting workflow.

- **Signal:** +1 = long, 0 = hold, −1 = short  
- **Confidence:** probability score (0–1)  
- **Update rate:** every 1–5 minutes  
- **Delivery:** lightweight dashboard/API overlay

## Assumptions
- Live tick/order book data is available from the broker API  
- Latency budget under ~1s end-to-end  
- Model explanations (feature attributions) available for trader trust

## Constraints
- Prediction runtime ≤ 500ms per update  
- Must integrate with TradingView/Bloomberg workflows without extra windows  
- No proprietary data leaves the local environment

## Risks & Mitigations
- **Regime shifts / macro events:** fall back to robust technical baselines on flagged event windows  
- **Thin liquidity / microstructure noise:** throttle trading in off-hours; volatility-aware filters  
- **Data outages:** failover to naive baselines; alerting

## Success Metrics
- **Sharpe improvement** ≥ 0.3 vs. discretionary baseline over a rolling 2-week window  
- **Directional hit rate** ≥ 55% for 1–5 minute horizon  
- **Adoption:** traders keep the widget active during primary session hours

## Next Steps
1. Ship baseline features + backtest (Stage 02)  
2. Calibrate thresholds for signal → action mapping  
3. Add event-aware guards for macro releases
