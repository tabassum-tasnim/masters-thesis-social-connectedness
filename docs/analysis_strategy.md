
# Statistical Analysis Strategy

This document summarizes the final analytical approach implemented in `code/Data_Analysis_&_Exploration.ipynb`.

## Analytical Sample

The original analysis panel contained 430 diary entries from 40 participants. The final common complete-case sample used in the main models contained 429 diary entries from the same 40 participants.

## Language-Based Outcomes

Four indicators were compared:

- `social_conn_llm`: LLM-rated expressed social connectedness
- `sent_score`: German BERT sentiment score
- `social_density`: Social-word density
- `neg_emotion_density`: Negative-emotion word density

## Longitudinal Modeling

Random-intercept linear mixed-effects models accounted for repeated observations nested within participants.

Positive and negative mood were decomposed into:

- Within-person variation: deviations from a participant's own average mood
- Between-person variation: differences in average mood across participants

The models included gender, family socioeconomic position and diary word count as covariates.

## Model Families

**Family 1 — Mood associations**

Examined associations of within-person and between-person positive and negative mood with the four language-based outcomes.

**Family 2 — Friendship-network moderation**

Examined whether the number of nominated friends moderated associations between mood and language-based outcomes.

Friendship-network size was standardized at the participant level rather than across repeated diary observations.

**Family 3 — Depression and anxiety**

Examined associations between baseline PHQ-9 depression scores, GAD-7 anxiety scores and the language-based outcomes.

## Interpretation

The analyses are observational and cannot establish causality.

The LLM ratings should be interpreted as indicators of expressed social connectedness rather than validated direct measurements of an underlying psychological state.

The original notebook requires restricted research checkpoints and cannot be fully executed from the public repository alone. A separate synthetic example demonstrates the within-person and between-person modeling approach without using participant data.
