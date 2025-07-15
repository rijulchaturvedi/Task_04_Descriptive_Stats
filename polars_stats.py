import polars as pl

def load_dataset(filepath):
    df = pl.read_csv(filepath)
    print(f"\n✅ Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
    return df

def describe_columns(df):
    print("\n📊 Descriptive Statistics:")
    print(df.describe())

def analyze_categorical(df):
    print("\n🔍 Unique Values and Most Frequent Entries:")
    for col in df.columns:
        series = df[col]
        print(f"\nColumn: {col}")
        print(f"  Unique values: {series.n_unique()}")
        if series.dtype == pl.Utf8 or series.dtype == pl.Categorical:
            print("  Top 3 Frequent:")
            print(series.value_counts().sort("count", descending=True).head(3))

def guess_grouping_keys(df):
    grouping_keys = []
    for col in df.columns:
        if 'id' in col.lower() or 'page' in col.lower() or 'state' in col.lower():
            grouping_keys.append(col)
    return grouping_keys

def group_and_describe(df, group_cols):
    if all(col in df.columns for col in group_cols):
        print(f"\n📚 Grouped Summary by {group_cols} (first 3 groups):")
        groups = df.group_by(group_cols)
        grouped_df = groups.agg([
            *[pl.col(c).count().alias(f"{c}_count") for c in df.columns if c not in group_cols],
            *[pl.col(c).mean().alias(f"{c}_mean") for c in df.columns if c not in group_cols and df[c].dtype in [pl.Float32, pl.Float64, pl.Int32, pl.Int64]],
            *[pl.col(c).std().alias(f"{c}_std") for c in df.columns if c not in group_cols and df[c].dtype in [pl.Float32, pl.Float64, pl.Int32, pl.Int64]],
            *[pl.col(c).min().alias(f"{c}_min") for c in df.columns if c not in group_cols and df[c].dtype in [pl.Float32, pl.Float64, pl.Int32, pl.Int64]],
            *[pl.col(c).max().alias(f"{c}_max") for c in df.columns if c not in group_cols and df[c].dtype in [pl.Float32, pl.Float64, pl.Int32, pl.Int64]]
        ])
        print(grouped_df.head(3))
    else:
        print(f"\n⚠️ Skipping grouping. Columns {group_cols} not found in dataset.")

if __name__ == "__main__":
    filepath = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_ads_president_scored_anon.csv"  # Update path
    #filepath = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_posts_president_scored_anon.csv"  # Update path
    #filepath = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_ads_president_scored_anon.csv"  # Update path

    df = load_dataset(filepath)

    describe_columns(df)
    analyze_categorical(df)

    suggested_keys = guess_grouping_keys(df)
    if suggested_keys:
        group_and_describe(df, [suggested_keys[0]])
    if len(suggested_keys) >= 2:
        group_and_describe(df, suggested_keys[:2])