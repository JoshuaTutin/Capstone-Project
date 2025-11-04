# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# 🧠 Lichess + FIDE Ratings Analysis + Interactive Dashboard
An end-to-end data analysis and visualization project that streams real Lichess game data, processes FIDE player rating data, and builds an interactive dashboard for exploring the relationship between Lichess and FIDE ratings across different time controls.

## Project overview
This project aims to:

Download and parse a large Lichess rated games dataset (compressed .zst PGN format).

Collect and analyze unique player ratings across time controls: bullet, blitz, rapid, and classical.

Download and process FIDE official rating lists (Standard, Rapid, Blitz).

Generate comparative statistical plots and percentile-based mappings between Lichess and FIDE ratings.

Provide an interactive dashboard (via Plotly Dash) for exploring the rating correlations visually.

## Business Case
Online chess platforms like Lichess and organizations like FIDE use separate rating systems, each with its own player population, scaling, and inflation dynamics.
As a result, players and coaches often struggle to interpret how a Lichess rating translates to an equivalent FIDE rating — especially across Bullet, Blitz, Rapid, and Classical time controls.

This project provides a data-driven mapping between the two ecosystems, allowing:

Players to understand their likely FIDE-equivalent strength.

Coaches to set performance benchmarks for online students.

Organizers and federations to improve seeding, pairing, and qualification models.

Researchers to study rating system behavior, inflation, and correlation over time.

By quantifying the relationship between these rating systems, this project bridges the gap between online and over-the-board competitive chess.

## Data Management
Sources:

Lichess.org
 monthly public rated games dump (.pgn.zst format).

FIDE Ratings Database
 official player lists (.zip format).

Cleaning & Processing:

Removal of incomplete or unparseable PGN headers.

Extraction of unique player ratings and classification by time control.

Normalization of rating formats and percentile-based alignment between datasets.

Storage & Versioning:

Processed data stored in structured CSV files (e.g., lichess_fide_mapping_points.csv).

Generated plots and dashboards versioned via GitHub for reproducibility.

Ethics & Compliance:

Only public and anonymized data is used.

No personally identifiable information (PII) is collected or displayed.

Fully compliant with GDPR and open data usage policies.

## Methodology
Data Ingestion

Streamed large-scale Lichess game data directly from .zst archives using zstandard.

Parsed PGN games via python-chess to extract ratings, time controls, and players.

Data Aggregation

Collected unique user ratings per time control (Bullet, Blitz, Rapid, Classical).

Downloaded and parsed the FIDE player list, extracting Standard, Rapid, and Blitz ratings.

Statistical Analysis

Computed rating percentiles for both datasets to ensure consistent comparison.

Merged percentiles to derive Lichess ↔ FIDE equivalence tables.

Performed linear regression and correlation (Pearson r) analyses to quantify relationships.

Visualization & Dashboarding

Generated Seaborn plots for rating distributions (histograms and boxplots).

Built an interactive Plotly Dash dashboard for exploring mappings dynamically within Jupyter.

## Results
Strong positive correlation between Lichess and FIDE ratings (r ≈ 0.9 across time controls).

Systematic rating inflation observed on Lichess — approximately +100–200 Elo above FIDE equivalents for mid-range players.

Rapid and Classical controls exhibit the highest consistency between systems.

Percentile mapping provides an accurate conversion framework for estimating FIDE ratings from online performance.

## Ethical Considerations
All analyses use public, aggregated data — no individual-level tracking or identification.

Results are statistical approximations, not deterministic conversions.

The study avoids subjective evaluation of player skill or platform quality.

Findings are intended for educational, analytical, and research purposes only.


## Technologies Used
Category	Tools / Libraries
Data Handling	Python, Pandas, NumPy
Statistical Analysis	SciPy, Pearson Correlation, Linear Regression
Visualization	Matplotlib, Seaborn, Plotly
Dashboard	JupyterDash, Dash Bootstrap Components
Data Sources	Lichess .pgn.zst, FIDE .zip archives
Utilities	python-chess, zstandard, requests

## Version Control
The project follows modular version control via GitHub.

Each major addition — data cleaning, visualization, percentile mapping, dashboard — is committed separately with descriptive messages (e.g.,
"Added FIDE–Lichess percentile correlation analysis").

All generated datasets and plots are reproducible from the main script.

## Future Development
Integrate live Lichess API data for real-time rating updates.

Add historical trend tracking across multiple monthly datasets.

Implement confidence intervals around percentile-based mapping.

Extend the dashboard to include national federations or demographic filters.

Optionally deploy the dashboard as a web-hosted app (e.g., via Render or Hugging Face Spaces).


## Project Maintenance & Evaluation

To ensure the dashboard and analysis remain up-to-date and reliable:

1. **Data Updates**
   - Lichess monthly game data will be streamed from `.pgn.zst` archives.
   - FIDE rating lists will be downloaded quarterly.
   - New datasets will be processed using existing pipelines and stored in structured CSVs.

2. **Dashboard Refresh**
   - The Plotly Dash dashboard will be updated after each new data ingestion.
   - Version control via GitHub ensures reproducibility of all generated plots and mappings.

3. **Validation & Evaluation**
   - Check for missing or corrupted PGN/FIDE data before processing.
   - Recompute percentiles and mapping tables to ensure consistency with previous versions.
   - Statistical summaries (mean, median, correlation) will be compared across versions to monitor rating inflation or changes in correlation patterns.

4. **Future Enhancements**
   - Incorporate confidence intervals for percentile-based mapping.
   - Extend filtering options (national federations, demographics).
   - Optionally deploy as a live web app (e.g., Render or Hugging Face Spaces) with automated updates.
   - Bonus: If this was a hobby without deadlines rather than an assigned project where the main objective for me is to achieve a pass mark, I'd also try and analyse how reliable the current ELO system is by calculating probabilities using the ELO formula to estimate the chance of one player beating, drawing or losing to another given the formula (and their ratings) then compare it to empirical data using hypothesis tests and possibly use maching learning to try and guess ELO of players using machine learning given win/loss/draw data with recent similar opponents then assess how good the model is. If the model was good, I'd then try and estimate the sample size of number of games needed to test such a thing reliably. I'd also try and use empirical data to see if there was a way to potentially improve the ELO calculation itself since some of the data collected in the graphs appears skewed rather than symmetrical also.


## Reflection
Processing multi-gigabyte chess data streams, aligning two rating ecosystems, and visualizing percentile relationships required a combination of data engineering, statistical analysis, and dashboard design skills.

This project demonstrated how open data can be transformed into actionable insight — bridging the gap between online analytics and real-world competitive benchmarks.

Through this work, I enhanced my ability to:

Handle large-scale streaming datasets.

Apply statistical modeling for rating alignment.

Design interactive analytical tools that communicate insights effectively.
