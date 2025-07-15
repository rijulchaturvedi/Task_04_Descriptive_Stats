import pandas as pd

def load_dataset(filepath):
    df = pd.read_csv(filepath)
    print(f"\n✅ Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
    return df

def describe_columns(df):
    print("\n📊 Descriptive Statistics (Numeric Columns):")
    print(df.describe())

    print("\n📊 Descriptive Statistics (All Columns):")
    print(df.describe(include='all'))

def analyze_categorical(df):
    print("\n🔍 Unique Values and Most Frequent Entries:")
    for col in df.columns:
        print(f"\nColumn: {col}")
        print(f"  Unique values: {df[col].nunique()}")
        print(f"  Most frequent:\n{df[col].value_counts().head(3)}")

def guess_grouping_keys(df):
    grouping_keys = []
    for col in df.columns:
        if 'id' in col.lower() or 'page' in col.lower() or 'state' in col.lower():
            grouping_keys.append(col)
    return grouping_keys

def group_and_describe(df, group_cols):
    if all(col in df.columns for col in group_cols):
        grouped = df.groupby(group_cols)
        print(f"\n📚 Grouped Summary by {group_cols} (first 3 groups):")
        for name, group in list(grouped)[0:3]:
            print(f"\nGroup: {name}")
            print(group.describe())
    else:
        print(f"\n⚠️ Skipping grouping. Columns {group_cols} not found in dataset.")

if __name__ == "__main__":
    #filepath = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_ads_president_scored_anon.csv"  # Update path here
    #filepath = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_posts_president_scored_anon.csv"  # Update path here
    filepath = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_tw_posts_president_scored_anon.csv"  # Update path here

    df = load_dataset(filepath)

    describe_columns(df)
    analyze_categorical(df)

    suggested_keys = guess_grouping_keys(df)
    if suggested_keys:
        group_and_describe(df, [suggested_keys[0]])
    if len(suggested_keys) >= 2:
        group_and_describe(df, suggested_keys[:2])