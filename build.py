import csv
import json

events = []

# 讀 CSV
with open("events.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        row["lat"] = float(row["lat"])   # 座標轉成數字
        row["lng"] = float(row["lng"])
        events.append(row)

# 依開始日期排序
events.sort(key=lambda e: e["date_start"])

# 寫成 JSON
with open("events.json", "w", encoding="utf-8") as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

print(f"完成：{len(events)} 筆")