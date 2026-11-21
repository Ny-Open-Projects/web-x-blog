
DEBTS = [
    {"name": "三处复制的口径 SQL", "fix_cost": 8, "monthly_leak": 2},
    {"name": "核心模块无类型标注", "fix_cost": 20, "monthly_leak": 3},
    {"name": "手工发布的报表", "fix_cost": 6, "monthly_leak": 4},
]

def rank(items):
    return sorted(items, key=lambda d: -d["monthly_leak"] / d["fix_cost"])

for d in rank(DEBTS):
    ratio = d["monthly_leak"] / d["fix_cost"]
    print(f"{d['name']}:修复 {d['fix_cost']}h 月漏损 {d['monthly_leak']}h 性价比 {ratio:.2f}")
print("按性价比排序,优先偿还回本最快的债,漏损数据来自工时与事故记录")
