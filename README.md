# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# ♟️ Chess Performance Analytics Dashboard

## Overview
This project explores how player rating differences influence game outcomes using real Lichess data. It applies probability, data analysis, and visualization principles to uncover how the Elo model translates to real-world results.

## Business Case
Understanding win/draw/loss probabilities across rating tiers can inform:
- Coaching and training focus by rating group.
- Online platform matchmaking algorithms.
- Performance benchmarks and variance modelling.

## Data Management
- Source: Public, anonymised Lichess data.
- Cleaning: Removal of incomplete entries, normalization of ratings.
- Storage: CSV format, structured by version control.
- Ethics: Complies with GDPR; no identifying data used.

## Methodology
- Data cleaning and preprocessing with Pandas.
- Probability modelling via observed frequencies.
- Elo theory cross-reference (expected score function).
- Visualization with Seaborn and Streamlit dashboard.

## Results
Lower-rated players’ win probability declines exponentially with rating difference — confirming Elo’s non-linear scaling. Draws remain proportionally stable up to ~400 points, suggesting competitive balance in mid-tier matchups.

## Ethical Considerations
- All data is anonymised.
- No individual identity exposed.
- Findings are presented objectively, avoiding bias or value judgment.

## Technologies Used
Python, Pandas, Numpy, Matplotlib, Seaborn, Streamlit, Git

## Version Control
Each feature and update is committed separately in GitHub with clear commit messages (e.g., “Added rating difference probability calculation”).

## Future Development
- Add Stockfish accuracy integration.
- Include live rating updates via API.
- Deploy Streamlit dashboard online.

## Reflection
Challenges included large dataset cleaning and real-time probability computation. Adapted new methods (Streamlit caching, modular plotting). This project improved my ability to apply data science for real analytical insight.
