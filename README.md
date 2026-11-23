# Language-Based Indicators of Social Relationship Perception in Depression and Anxiety

**A Computational Social Science Approach Using NLP**  
*M.Sc. Thesis in Computational Social Systems (Social Data Science), RWTH Aachen University (2026)*  
**Author:** Tasnim Tabassum | [Portfolio](https://tabassum-tasnim.github.io/) | [Google Scholar](https://scholar.google.com/citations?hl=en&user=iG6eCN8AAAAJ) | [LinkedIn](https://www.linkedin.com/in/towmony)

---

## Overview

This repository contains the statistical modeling notebooks, evaluation outputs, and figures for my Master's thesis at RWTH Aachen University. The study investigates whether a Large Language Model (LLM) can serve as a valid, reproducible measurement instrument for a latent relational construct—**expressed social connectedness**—in naturalistic open-ended diary language, and what it adds beyond sentiment and lexical baselines.

### Key Methodology & Findings
* **Intensive Longitudinal EMA Dataset:** Analyzed **429 naturalistic German audio-diary transcripts** from **40 university students** in the *PeerSmart Network Study* (a one-week smartphone ecological momentary assessment with momentary mood ratings and baseline `PHQ-9` depression and `GAD-7` anxiety scores).
* **Structured LLM Instrument & Empirical Facet Selection:** Evaluated four dimensions of expressed social connectedness (*direct social connection*, *engagement with others*, *relationship quality*, and *belonging*) on a `0–4` scale using Azure OpenAI (`gpt-5-chat`). Excluded *belonging* on empirical grounds due to weaker inter-prompt correlations and a distinct distributional pattern, yielding a high-consistency **3-item composite ($\alpha = .976$)**.
* **Psychometric Validation & Run Reproducibility:** Validated LLM-derived ratings against blinded human coding (**$\text{ICC}(A,1) = .807$** in the primary codable validation sample) and tested repeated-run stability across two sampling conditions (**Pearson $r = .980$**).
* **Discriminant Validity & Multilevel Modeling:** Estimated within-between random-effects (`REWB`) linear mixed-effects models (with cluster-robust OLS robustness checks) in Python (`statsmodels`), comparing the LLM indicator against **`oliverguhr/german-sentiment-bert`** and custom German lexical-density baselines:
  * Higher-than-usual **within-person positive mood** predicted higher LLM-rated social connectedness (**$b = 0.228, p < .001$**), while higher **within-person negative mood** predicted lower ratings in separate models (**$b = -0.186, p < .001$**).
  * Neither baseline `PHQ-9` nor `GAD-7` was clearly associated with LLM-rated connectedness—whereas general BERT sentiment captured broader within- and between-person affective and symptom-level variance, and lexical-density indicators were sparser and less stable.

---

## Key Results & Visualizations

### Within-Person Association: Social Connectedness & Positive Affect (`PA`)
![Within-person positive affect and LLM-measured social connectedness](figures/Figure_PA_within_friends_LLM_common429.png)

### Within-Person Association: Social Connectedness & Negative Affect (`NA`)
![Within-person negative affect and LLM-measured social connectedness](figures/Figure_NA_within_friends_LLM_common429.png)

---

## Repository Structure

```text
├── code/
│   └── Data_Analysis_&_Exploration.ipynb        # Data preparation, reliability checks & REWB mixed-effects models
├── data/
│   └── README.md                                # Data governance, anonymization & GDPR access restrictions
├── figures/
│   ├── Figure_PA_within_friends_LLM_common429.png
│   ├── Figure_PA_within_friends_LLM_prediction_data.xlsx
│   ├── Figure_NA_within_friends_LLM_common429.png
│   └── Figure_NA_within_friends_LLM_prediction_data.xlsx
├── results/
│   ├── Family1_separate_mood_models_full_common429.xlsx
│   ├── Family2_mixed_models_common429.xlsx
│   ├── Family3_joint_PHQ_GAD_common429.xlsx
│   ├── Family3_separate_models_full_common429.xlsx
│   ├── Table_2_expanded_correlations_common429.xlsx
│   └── Table_5_Family3_separate_PHQ_GAD_common429.xlsx
├── requirements.txt
└── LICENSE
```

---

## Data Availability & Privacy

Due to participant privacy and GDPR data-protection regulations governing audio-diary transcripts from the *PeerSmart Network Study*, raw text transcripts cannot be shared publicly. See [`data/README.md`](data/README.md) for dataset schema details, and refer to `figures/` and `results/` for aggregated model predictions and regression tables.

---

## Setup & Reproducibility

```bash

git clone https://github.com/tabassum-tasnim/masters-thesis-social-connectedness.git
cd masters-thesis-social-connectedness

python -m venv .venv
source .venv/bin/activate
# On Windows: .venv\Scripts\activate

pip install -r requirements.txt

jupyter notebook "code/Data_Analysis_&_Exploration.ipynb"

```
**Reproducibility note:** The public notebook begins from restricted analytical checkpoints generated during the original research workflow. These checkpoints are not distributed with the repository. Consequently, the complete analysis cannot be rerun using public files alone. Aggregate results and figures are provided for inspection.
---

## Citation

```bibtex
@mastersthesis{tabassum2026connectedness,
  author  = {Tabassum, Tasnim},
  title   = {Language-Based Indicators of Social Relationship Perception in Depression and Anxiety: A Computational Social Science Approach Using NLP},
  school  = {RWTH Aachen University},
  year    = {2026},
  type    = {M.Sc. Thesis in Computational Social Systems}
}
```
