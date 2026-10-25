# DSLR — Data Science x Logistic Regression

A Python implementation of a multi-class logistic regression classifier, built from scratch, that plays the role of Hogwarts' Sorting Hat: given a student's course grades, it predicts their house.

## Problem

The Sorting Hat is broken. All we have is a dataset of students with:

- **Features:** grades in 13 courses (Arithmancy, Astronomy, Herbology, Defense Against the Dark Arts, Divination, Muggle Studies, Ancient Runes, History of Magic, Transfiguration, Potions, Care of Magical Creatures, Charms, Flying)
- **Target:** one of 4 houses (Gryffindor, Hufflepuff, Ravenclaw, Slytherin)

The goal is to:

1. Explore and understand the data.
2. Train a classifier on `dataset_train.csv`.
3. Predict the houses of the students in `dataset_test.csv`.

Constraint: core logic (statistics, gradient descent) is written by hand, with no ready-made ML or stats functions.

## Solution

### 1. Data analysis

| Step | What it does |
|---|---|
| `describe` | Re-implements pandas' `describe()` by hand: count, mean, std, min, 25% / 50% / 75% percentiles, max for every numerical feature |
| `histogram` | Score distribution per house, to find which course is homogeneous across houses (a poor feature) |
| `scatter_plot` | Compares feature pairs to find the two most similar (redundant) features |
| `pair_plot` | Scatter/histogram matrix of all features, used to choose which ones to train on |

These plots drive feature selection: courses with a homogeneous distribution across houses or redundant with another are dropped, since they add noise rather than signal.

### 2. Preprocessing

- Missing values handled (dropped or filled with the feature mean).
- Features **standardized** (zero mean, unit variance) so gradient descent converges quickly and evenly.

### 3. Training: one-vs-all logistic regression

Since logistic regression is binary, we train **one classifier per house**, each answering "is this student in house X or not?".

For each house:

- Hypothesis: `h(x) = sigmoid(θ · x)`, where `sigmoid(z) = 1 / (1 + e^-z)`
- Loss: binary cross-entropy `J(θ) = -1/m Σ [ y·log(h) + (1-y)·log(1-h) ]`
- Optimization: gradient descent, `θ ← θ - α · 1/m · Xᵀ(h - y)`

The learned weights (θ) for the 4 houses, plus the normalization parameters, are saved to a file.

### 4. Prediction

For each student, compute the probability from each of the 4 classifiers and pick the house with the **highest probability** (`argmax`). Results are written to `houses.csv`:

```
Index,Hogwarts House
0,Hufflepuff
1,Ravenclaw
...
```

## Usage

```bash
# Analysis
python3 describe.py dataset_train.csv
python3 histogram.py
python3 scatter_plot.py
python3 pair_plot.py

# Train (saves the weights)
python3 logreg_train.py dataset_train.csv

# Predict (outputs houses.csv)
python3 logreg_predict.py dataset_test.csv weights
```

> Adjust script names and arguments to match your repo.

## Result

The classifier is expected to reach at least **98% accuracy** on the test set, as required by the subject.

## Concepts covered

- Descriptive statistics and data visualization
- Feature selection and standardization
- Sigmoid function and cross-entropy loss
- Gradient descent
- One-vs-all multi-class classification
