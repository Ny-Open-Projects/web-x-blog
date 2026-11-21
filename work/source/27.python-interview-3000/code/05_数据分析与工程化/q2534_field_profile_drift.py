"""字段级 diff 的分布画像: 行数守恒也要查分布漂移"""

try:
    import pandas as pd
except ImportError:
    pd = None

N = 100
TOLERANCE = 0.05      # 空值率漂移容忍 5 个百分点


def make_rows(null_rule):
    rows = []
    for i in range(N):
        rows.append({
            "uid": f"u{i:03d}",
            "city": ["北京", "上海", "广州", "深圳", "杭州"][i % 5],
            "amount": None if null_rule(i) else 100.0 + i,
        })
    return rows


def profile(rows):
    cols = {}
    for f in rows[0]:
        vals = [r[f] for r in rows]
        nulls = sum(1 for v in vals if v is None)
        numeric = [v for v in vals if isinstance(v, (int, float))]
        cols[f] = {
            "null_rate": nulls / len(vals),
            "distinct": len({v for v in vals if v is not None}),
            "mean": sum(numeric) / len(numeric) if numeric else None,
        }
    return cols


if __name__ == "__main__":
    p1 = profile(make_rows(lambda i: i % 50 == 0))     # 昨日: amount 空值率 2%
    p2 = profile(make_rows(lambda i: (i % 5) < 2))     # 今日: amount 空值率 40%
    print(f"两日行数一致: {N} == {N}, 守恒断言无感知")
    for f in p1:
        d_null = abs(p2[f]["null_rate"] - p1[f]["null_rate"])
        verdict = "DRIFT" if d_null > TOLERANCE else "OK"
        print(f"  [{verdict}] {f}: 空值率 {p1[f]['null_rate']:.0%} -> {p2[f]['null_rate']:.0%}, "
              f"基数 {p1[f]['distinct']} -> {p2[f]['distinct']}, 均值 {p1[f]['mean'] and round(p1[f]['mean'], 1)}"
              f" -> {p2[f]['mean'] and round(p2[f]['mean'], 1)}")
    assert p2["amount"]["null_rate"] - p1["amount"]["null_rate"] > TOLERANCE
    if pd is not None:
        df2 = pd.DataFrame(make_rows(lambda i: (i % 5) < 2))
        print("pandas 视角: 空值率", df2.isna().mean().round(2).to_dict())
    print("要点: 行数 diff 抓不到'字段悄悄变空', 列画像把空值率 基数 均值三件套纳入门禁")
