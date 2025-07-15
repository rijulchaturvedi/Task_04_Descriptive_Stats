# Task 04: Descriptive Statistics & Visualization – 2024 US Presidential Election Social Media Analysis

This project provides an exploratory and descriptive analysis of three datasets from Facebook and Twitter related to the 2024 US Presidential Election. It includes statistical summaries and visual narratives aimed at identifying key social and political trends based on user engagement.

## 📁 Datasets Used

* `2024_fb_ads_president_scored_anon.csv`
* `2024_fb_posts_president_scored_anon.csv`
* `2024_tw_posts_president_scored_anon.csv`

## 📚 Code Files

* `pure_python_stats_fb_ads.py`: Pure Python script for descriptive stats (no Pandas).
* `pandas_stats.py`: Statistical analysis using Pandas.
* `polars_stats.py`: Statistical analysis using Polars.
* `visual_summary.py`: Generates histograms, bar plots, and box plots.

## 📈 Visuals & Outputs

* `visualizations/`: Contains image files for histograms and box plots.
* `summary_visualizations_*.pdf`: Compiled visual summaries per dataset.
* `Bonus Challenges_Social_Media_Descriptive_Analysis_Presentation.pptx`: PowerPoint with narrative-based findings.

## ⚡ How to Run

### 1. Environment Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # matplotlib, seaborn, pandas, polars, fpdf
```

### 2. Running Scripts

* Descriptive Stats:

```bash
python pure_python_stats_fb_ads.py
python pandas_stats.py
python polars_stats.py
```

* Visualization:

```bash
python visual_summary.py
```

## 📊 Key Insights

### Facebook Ads:

* *Health* and *governance* topics dominate high ad spend and impressions.
* Reactions like "Angry" and "Love" were more prominent on issues of *COVID-19* and *election integrity*.

### Facebook Posts:

* Interaction spikes seen during debates and campaign events (late 2023).
* Videos outperform images in generating Total Interactions.

### Twitter Posts:

* Retweet spikes on topics tagged with *fraud* and *immigration*.
* High reply chains point to discourse/controversy.

## 🔗 Git & Contribution

```bash
git clone https://github.com/rijulchaturvedi/Task_04_Descriptive_Stats.git
cd Task_04_Descriptive_Stats
```

## 📅 Timeline & Tools

* Timeline: July 2025
* Tools: Python, Pandas, Polars, Seaborn, Matplotlib, FPDF

---

Made for the iSchool Research Assistant Task at Syracuse University.
