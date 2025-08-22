# Memo: Short-Term Futures Price Prediction
**Audience:** Junior traders on the futures desk  
**Decision cadence:** Intraday, every 1–5 minutes  
**Pain points:** Subjective setups, missed reversals, weak probability quantification  
**Output:** Signal (+1 long, 0 hold, –1 short) + confidence score via dashboard/API  
**Assumptions:** Live tick/order book data; latency <1s; explainable ML  
**Constraints:** Prediction runtime ≤500ms; integrates with existing charts/workflow  
**Risks/Tests:** Macro regime shifts, data outages, thin liquidity → fallback to simple technicals
