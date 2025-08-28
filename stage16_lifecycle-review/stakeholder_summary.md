# Stakeholder Summary (Non-Technical)

**Project:** Cross‑Asset Correlation Analysis (equities vs bonds)  
**Goal:** Understand how correlations shift across regimes to improve diversification and risk management.

**What we did**
- Collected historical price/return data for major equity and bond benchmarks.
- Cleaned and standardized series; removed obvious data errors and aligned calendars.
- Explored rolling correlations and stress windows; identified regimes with correlation breakdowns.
- Built simple regime-aware rules to illustrate allocation implications.

**What it means**
- Equity–bond correlation is not stable. It tends to rise during inflation shocks and fall during growth scares.
- Static diversification assumptions can understate risk in certain regimes.

**Limitations & Next Steps**
- Use broader asset set (credit, commodities), add macro covariates, and stress-testing.
- Formalize regime detection (HMM/Markov switching) and validate out-of-sample.
