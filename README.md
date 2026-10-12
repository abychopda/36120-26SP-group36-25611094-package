# NBA Career ML Toolkit

A small, reusable Python package that powers the experiments in
[**nba-career-longevity-prediction**](https://github.com/abychopda/nba-career-longevity-prediction) —
predicting which college players will last three or more NBA seasons.

It keeps the boilerplate (loading, cleaning, EDA, preprocessing, modelling, evaluation, plotting and
Kaggle submission files) in one tested place, so each experiment notebook only contains the decisions
that are specific to that experiment.

> Reusable functionality belongs in the package; experiment-specific decisions stay in the notebooks.

## What's inside

```text
src/group36_25611094_package/helpers/
├── io.py              # dataset loading and saving
├── cleaning.py        # dataset cleaning utilities
├── eda.py             # exploratory data analysis summaries
├── features.py        # feature construction
├── preprocessing.py   # encoding and transformation
├── importance.py      # correlation and feature-importance analysis
├── modeling.py        # model training and evaluation
├── visualization.py   # plotting utilities
├── submission.py      # Kaggle submission file generation
└── utils.py           # shared general-purpose utilities
```

## Workflow it supports

```text
Data → EDA → Preprocessing → Modelling → Evaluation → Visualisation → Submission
```

## Installation

The package is published to TestPyPI under its original distribution name:

```bash
pip install --index-url https://test.pypi.org/simple/ \
            --extra-index-url https://pypi.org/simple/ \
            36120-26sp-group36-25611094-package
```

For local development (uses [uv](https://docs.astral.sh/uv/)):

```bash
uv sync
uv build
```

## Related

- [nba-career-longevity-prediction](https://github.com/abychopda/nba-career-longevity-prediction) — the experiments and results this package supports
- [mlkit-aby](https://github.com/abychopda/mlkit-aby) — a later, generalised version of this toolkit used in the Sydney Weather Intelligence project

## About

Written by **Abhishek Chopda** as part of 36120 Advanced Machine Learning Application at the
University of Technology Sydney (Spring 2026).
