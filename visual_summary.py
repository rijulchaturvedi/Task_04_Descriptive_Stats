import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Optional: for nicer plot styles
sns.set(style="whitegrid")

# Load dataset

#FILEPATH = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_posts_president_scored_anon.csv"
#FILEPATH = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_ads_president_scored_anon.csv"
FILEPATH = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_tw_posts_president_scored_anon.csv"

df = pd.read_csv(FILEPATH)

# Create output folder
output_dir = os.path.join(os.path.dirname(__file__), "visualizations")
os.makedirs(output_dir, exist_ok=True)

# Separate numeric and categorical columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()


for col in numeric_cols:
    print(f"### {col}")
    fig_hist, ax_hist = plt.subplots()
    sns.histplot(df[col], bins=30, kde=True, ax=ax_hist)
    fig_hist.savefig(os.path.join(output_dir, f"{col}_histogram.png"))
    plt.close(fig_hist)

    cleaned = df[col].dropna()
    if cleaned.shape[0] > 0 and cleaned.nunique() > 1:
        fig_box, ax_box = plt.subplots()
        sns.boxplot(x=cleaned.values, ax=ax_box)
        fig_box.savefig(os.path.join(output_dir, f"{col}_boxplot.png"))
        plt.close(fig_box)

for col in categorical_cols:
    vc = df[col].value_counts().head(10)
    if len(vc) > 1:
        print(f"### {col}")
        fig_bar, ax_bar = plt.subplots()
        sns.barplot(x=vc.values, y=vc.index, hue=vc.index, palette="viridis", legend=False, ax=ax_bar)
        fig_bar.savefig(os.path.join(output_dir, f"{col}_barplot.png"))
        plt.close(fig_bar)

from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

for img_file in sorted(os.listdir(output_dir)):
    if img_file.endswith(".png"):
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=img_file.replace('_', ' ').replace('.png', '').title(), ln=True, align='C')
        pdf.image(os.path.join(output_dir, img_file), x=10, y=30, w=180)

pdf_output_path = os.path.join(output_dir, "summary_visualizations.pdf")
pdf.output(pdf_output_path)
print(f"✅ PDF created at {pdf_output_path}")