import csv
import math
from collections import defaultdict, Counter

# 1. Load CSV
def load_csv(filepath):
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

# 2. Type checker
def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

# 3. Descriptive stats
def compute_column_stats(values):
    stats = {}
    numeric_vals = [float(v) for v in values if is_float(v)]
    count = len(values)
    stats['count'] = count
    
    if numeric_vals:
        mean = sum(numeric_vals) / len(numeric_vals)
        stats.update({
            'mean': round(mean, 2),
            'min': min(numeric_vals),
            'max': max(numeric_vals),
            'std_dev': round(math.sqrt(sum((x - mean) ** 2 for x in numeric_vals) / len(numeric_vals)), 2)
        })
    else:
        stats['unique'] = len(set(values))
        most_common = Counter(values).most_common(1)
        stats['most_frequent'] = most_common[0] if most_common else None

    return stats

# 4. Apply stats to each column
def summarize_dataset(data):
    summary = {}
    for col in data[0].keys():
        col_values = [row[col] for row in data]
        summary[col] = compute_column_stats(col_values)
    return summary

# 5. Group by one or more columns
def group_by(data, keys):
    grouped = defaultdict(list)
    for row in data:
        group_key = tuple(row[k] for k in keys)
        grouped[group_key].append(row)
    return grouped

# 6. Print stats
def print_summary(summary, title="Summary"):
    print(f"\n=== {title} ===")
    for col, stats in summary.items():
        print(f"\nColumn: {col}")
        for stat, val in stats.items():
            print(f"  {stat}: {val}")

def guess_grouping_keys(row):
    keys = []
    for key in row.keys():
        lower_key = key.lower()
        if 'id' in lower_key or 'page' in lower_key or 'state' in lower_key:
            keys.append(key)
    return keys

def main():
    dataset_path = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_posts_president_scored_anon.csv"
    #dataset_path = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_fb_ads_president_scored_anon.csv"
    #dataset_path = "/Users/rijulchaturvedi/Documents/Personal/MASTERS/Documents/Applications/After Admit Procedure and Admit Letters/Syracuse University/Research Assistant iSchool Syracuse University/Research Task July 2025/Task_04_Descriptive_Stats/2024_tw_posts_president_scored_anon.csv"

    data = load_csv(dataset_path)
    print(f"✅ Loaded {len(data)} rows.")

    # Print available columns
    columns = list(data[0].keys())
    print("\n📌 Available columns:", columns)

    # Overall summary
    overall = summarize_dataset(data)
    print_summary(overall, "Overall Dataset Summary")

    # Suggest grouping keys
    suggested_keys = guess_grouping_keys(data[0])
    print(f"\n🔍 Suggested grouping keys: {suggested_keys}")

    # Use first suggested key if any
    if suggested_keys:
        key1 = suggested_keys[0]
        grouped = group_by(data, [key1])
        print(f"\n\n=== Grouped by {key1} (first 3 groups) ===")
        for group_key, group_data in list(grouped.items())[:3]:
            group_summary = summarize_dataset(group_data)
            print_summary(group_summary, f"group: {key1} = {group_key}")

    # Use first two if available for double grouping
    if len(suggested_keys) >= 2:
        key_pair = suggested_keys[:2]
        grouped_2 = group_by(data, key_pair)
        print(f"\n\n=== Grouped by {key_pair} (first 3 groups) ===")
        for group_key, group_data in list(grouped_2.items())[:3]:
            group_summary = summarize_dataset(group_data)
            print_summary(group_summary, f"group: {key_pair} = {group_key}")

if __name__ == "__main__":
    main()