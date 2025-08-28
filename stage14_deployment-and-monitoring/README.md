# Stage 14 — Deployment & Monitoring

## Reflection

Deploying machine learning models into production introduces several risks that must be carefully managed. For this project, the most credible risks include **schema drift** (input features changing in format or meaning), **increasing null values or missingness**, **label delay or leakage**, and **model performance degradation over time** due to shifting market or behavioral conditions. Additionally, system failures such as batch job errors or high latency can threaten availability and user trust.

To mitigate these risks, monitoring must be designed across four layers. At the **data layer**, I would track data freshness (e.g., max delay of 15 minutes since last batch), schema hash consistency, and null rate thresholds (>5% nulls triggering alerts). At the **model layer**, performance would be monitored through rolling metrics such as AUC or MAE, with thresholds (e.g., 2-week rolling AUC < 0.65) that prompt retraining or rollback. The **system layer** requires metrics like job success rate (>99%), p95 latency under 500ms, and resource utilization alerts. Finally, the **business layer** must track KPIs such as approval rate or engagement rate; a sudden 10% drop would be escalated to business analysts for investigation.

Ownership is divided clearly: the **platform engineering team** maintains system uptime and dashboards, the **data science team** reviews data and model quality weekly, and the **business team** monitors downstream KPIs. Alerts first notify the platform on-call, with handoffs to data science if the root cause is model-related. Issues are logged in a shared ticketing system, and retraining is triggered either on a fixed cadence (monthly) or when drift metrics exceed thresholds. Rollbacks require joint approval between engineering and product owners, ensuring accountability and continuity of operations.

---
**Deliverables:**  
- `reflection.md` (this file)  
- (Optional) `dashboard_sketch.png` — wireframe of monitoring panels  
- (Optional) `handoff_plan.md` — runbook bullets for escalation  
