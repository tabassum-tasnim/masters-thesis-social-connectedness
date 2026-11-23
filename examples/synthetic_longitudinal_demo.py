
"""Synthetic example of within- and between-person analysis.

All observations are simulated.
No real thesis data or participant records are used.
This does not reproduce the original thesis results.
"""

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# Generate synthetic longitudinal observations
rng = np.random.default_rng(2026)

n_people = 40
entries_per_person = 12

participant_id = np.repeat(
    np.arange(n_people), entries_per_person
)

baseline_mood = rng.normal(0, 0.8, n_people)
random_intercept = rng.normal(0, 0.6, n_people)
momentary_change = rng.normal(0, 1, len(participant_id))

sample = pd.DataFrame({
    "participant_id": participant_id,
    "mood": (
        np.repeat(baseline_mood, entries_per_person)
        + momentary_change
    ),
    "connectedness_score": (
        2.0
        + 0.55 * momentary_change
        + 0.20 * np.repeat(baseline_mood, entries_per_person)
        + np.repeat(random_intercept, entries_per_person)
        + rng.normal(0, 0.5, len(participant_id))
    )
})

# Separate within-person and between-person variation
sample["mood_between"] = (
    sample.groupby("participant_id")["mood"].transform("mean")
)

sample["mood_within"] = (
    sample["mood"] - sample["mood_between"]
)

# Verify within-person centering
assert np.allclose(
    sample.groupby("participant_id")["mood_within"].mean(),
    0
)

# Fit random-intercept mixed-effects model
model = smf.mixedlm(
    "connectedness_score ~ mood_within + mood_between",
    data=sample,
    groups=sample["participant_id"]
)

result = model.fit(reml=True, method="lbfgs")

print(
    f"Synthetic observations: {len(sample)} "
    f"from {n_people} participants"
)
print(result.summary())
