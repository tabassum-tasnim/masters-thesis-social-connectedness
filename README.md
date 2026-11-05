# Language-Based Indicators of Social Connectedness in German Audio-Diary Text
 
Master's thesis — [Institute of Sociology / Chair of Computational Social Systems, RWTH Aachen University]
 
**Author:** Tasnim Tabassum
**First Supervisor:** Dr. Heike Krüger
**Second Supervisor:** Prof. Dr. Thomas U. Grund
**Submitted:** September 2026

 
---
 
## Overview
 
This repository contains the analysis code and **aggregate** results for a master's thesis
on language-based indicators of perceived social connectedness. The core instrument is an
**LLM-based annotation pipeline** that scores German-language audio-diary entries for
social-connectedness signals; those scores are then validated against human coding and used
to model their relationship with momentary mood (positive/negative affect) and with
well-being measures (PHQ, GAD).
 
The analytical pipeline covers:
 
- **Validation** of the LLM annotations against human coders (inter-rater agreement,
  repeated-run stability).
- **Family 1 — Mood models:** separate positive- and negative-affect sensitivity models.
- **Family 2 — Mixed models:** random-intercept / participant-clustered specifications.
- **Family 3 — Clinical models:** PHQ and GAD, estimated separately and jointly.
- **Figures:** within-friends LLM prediction curves for positive and negative affect.
All models reported in the thesis use a common analytic sample of **429 entries**
(see *Data availability* for the participant-level exclusion logic).
 
## Repository structure
 
```
.
├── README.md
├── .gitignore
├── LICENSE
├── requirements.txt
├── code/                  # analysis scripts and notebooks
├── results/               # aggregate statistical outputs (the .xlsx tables)
│   ├── Family1_separate_mood_models_full_common429.xlsx
│   ├── Family2_mixed_models_common429.xlsx
│   ├── Family3_separate_models_full_common429.xlsx
│   ├── Family3_joint_PHQ_GAD_common429.xlsx
│   ├── Table_2_expanded_correlations_common429.xlsx
│   └── Table_5_Family3_separate_PHQ_GAD_common429.xlsx
├── figures/               # exported plots
│   ├── Figure_PA_within_friends_LLM_prediction_data.xlsx
│   └── Figure_NA_within_friends_LLM_prediction_data.xlsx
└── data/                  # NOT tracked — see "Data availability"
```
 
## Data availability
 
The underlying observation-level data — raw German audio-diary text, participant
identifiers, and friendship rosters — are **not included** in this repository. They are
restricted under the study's ethics approval and data-protection requirements (GDPR) and
cannot be shared publicly.
 
The `data/` directory is intentionally empty here and excluded via `.gitignore`. Only
**de-identified aggregate outputs** (model tables, correlation tables, figure-prediction
data) are included under `results/` and `figures/`.
 
Access to the restricted dataset may be possible for legitimate research purposes, subject
to approval. Please contact the author.
 
## Reproducing the analysis
 
1. Clone the repository and create an environment:
```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
```
2. Place the restricted data files in `data/` using the filenames expected by the scripts
   (see the header of each script/notebook in `code/`).
3. Run the notebooks / scripts in `code/` in order.
Without the restricted data, the code is provided for inspection and transparency; the
aggregate outputs in `results/` and `figures/` document the executed results.
 

 
## License
 
Code is released under the MIT License (see `LICENSE`). The license covers the **code only**;
it does **not** grant any rights to the underlying data, which remain restricted.
 
## Contact
 
tasnim.tabassum@rwth-aachen.de
