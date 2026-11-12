# ScamShield — Experiment Results

## Experiment 1: Classical ML Baselines

**Dataset:** UCI SMS Spam Collection

**Task:** Binary spam/ham classification (not yet scam-specific detection)

**Preprocessing:** Removed exact duplicate SMS messages.

**Features:** TF-IDF, word unigrams and bigrams.

**Split:** Stratified 80/20 training/validation split, random state 42.

### Validation Results

| Model | Precision | Recall | F1 | Average Precision |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.8955 | 0.9160 | 0.9057 | 0.9588 |
| LinearSVC | 0.9297 | 0.9084 | 0.9189 | 0.9739 |

### Cross-validation


Metric	Mean	Std
0	Precision	0.9589	0.0136
1	Recall	0.9310	0.0114
2	F1	0.9446	0.0065
3	AP	0.9779	0.0064
LinearSVC was evaluated using five-fold stratified cross-validation on the training partition.

Record the actual cross-validation means and standard deviations here.

### Observations

- LinearSVC achieved higher validation precision, F1 and average precision.
- Logistic Regression achieved slightly higher recall.
- LinearSVC is the current leading classical ML candidate.
- These results measure English SMS spam classification, not multilingual scam detection.

### Next Experiments

- Build a multilingual scam-specific dataset.
- Evaluate English, Hindi and Hinglish separately.
- Implement an LLM classifier using LangChain and Pydantic.
- Compare classical ML, LLM and hybrid approaches.