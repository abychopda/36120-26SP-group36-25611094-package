# Group 36 Data Science Helper Package

A reusable Python package developed for the UTS Data Science project. The package provides common utilities used across the project's experiment notebooks to support consistent and reproducible data science workflows.

## Package Purpose

The package was created to centralise reusable data science functionality used across multiple experiments. This reduces repetitive code and allows experiment notebooks to focus on experiment-specific decisions, analysis, and interpretation.

The package is intended to support a clear separation between:

- **Reusable functionality** — maintained within the package.
- **Experiment-specific decisions** — maintained within the experiment notebooks.

## Features

The package provides reusable utilities supporting:

- Exploratory data analysis
- Data preprocessing
- Correlation analysis
- Machine learning modelling
- Model evaluation
- Model visualisation
- Kaggle submission generation

## Package Structure

```text
group36_25611094_package/
│
├── helpers/
│
└── __init__.py
```

The `helpers` module contains the reusable functionality used throughout the project.

## Project Workflow

The package supports the following general workflow:

```text
Data
  ↓
Exploratory Analysis
  ↓
Preprocessing
  ↓
Modelling
  ↓
Evaluation
  ↓
Visualisation
  ↓
Submission
```

This structure allows common operations to be reused consistently across different experiments.

## Design Philosophy

The package follows a simple principle:

> Reusable functionality belongs in the package; experiment-specific decisions remain in the notebooks.

This means that the package focuses on general-purpose functionality, while the experiment notebooks contain the hypotheses, modelling decisions, feature-selection choices, experimental comparisons, and interpretation of results.

## Project Context

This package was developed as part of a UTS Master of Data Science and Innovation project involving machine learning experimentation and Kaggle-based model evaluation.

It is intended to support reproducible and consistent experimentation across the project.

## Authors

**Abhishek Chopda**

**Master of Data Science and Innovation**  
**University of Technology Sydney (UTS)**
