"""表格数据的异常单元格检测: 字段规则 + 分布离群双通道"""
import statistics
from datetime import datetime

TODAY = datetime(2026, 11, 1)
CITY_WHITELIST = {"北京", "上海", "广州", "深圳", "杭州"}

ROWS = [
    {"name": "张三", "age": 34, "city": "北京", "signup": "2026-01-15", "spend": 120.0},
    {"name": "李四", "age": "三十五", "city": "上海", "signup": "2026-02-20", "spend": 98.0},
    {"name": "王五", "age": 260, "city": "北京", "signup": "2026-03-01", "spend": 350.0},
    {"name": "赵六", "age": 28, "city": "魔都", "signup": "2026-03-05", "spend": 210.0},
    {"name": "钱七", "age": 31, "city": "广州", "signup": "2026/13/01", "spend": -5.0},
    {"name": "孙八", "age": 29, "city": "深圳", "signup": "2026-04-11", "spend": 88.0},
    {"name": "周九", "age": 45, "city": "杭州", "signup": "2026-05-02", "spend": 99999.0},
    {"name": "吴十", "age": 38, "city": "上海", "signup": "2026-05-20", "spend": 150.0},
]


def check_age(v):
    if not isinstance(v, int):
        return "age 不是整数"
    if not 0 <= v <= 120:
        return "age 越出人类范围"
    return None


def check_city(v):
    if v not in CITY_WHITELIST:
        return "city 不在白名单, 疑似别名或脏值"
    return None


def check_signup(v):
    try:
        dt = datetime.strptime(v, "%Y-%m-%d")
    except ValueError:
        return "signup 不是合法的 YYYY-MM-DD"
    if dt > TODAY:
        return "signup 晚于当前日期"
    return None


def check_spend(v):
    if not isinstance(v, (int, float)) or v < 0:
        return "spend 为负或类型错误"
    return None


def mad_outliers(values, key, thresh=3.5):
    """修正 z 分数: 0.6745 * (x - 中位数) / MAD"""
    med = statistics.median(values)
    mad = statistics.median([abs(v - med) for v in values])
    out = []
    if mad == 0:
        return out
    for i, v in enumerate(values):
        mz = 0.6745 * (v - med) / mad
        if abs(mz) > thresh:
            out.append((i, key, mz))
    return out


if __name__ == "__main__":
    anomalies = []
    for i, row in enumerate(ROWS):
        for col, checker in [("age", check_age), ("city", check_city),
                             ("signup", check_signup), ("spend", check_spend)]:
            reason = checker(row[col])
            if reason:
                anomalies.append((i, row["name"], col, row[col], reason))
    for i, col, mz in mad_outliers([r["spend"] for r in ROWS], "spend"):
        anomalies.append((i, ROWS[i]["name"], col, ROWS[i][col],
                          f"spend 修正 z 分数 {mz:.1f} 远超 3.5"))
    print(f"共检出 {len(anomalies)} 个异常单元格:")
    for i, name, col, val, reason in anomalies:
        print(f"  行{i} {name}.{col} = {val!r}  ->  {reason}")
    reasons = {a[4].split()[0] for a in anomalies}
    assert len(anomalies) >= 6, "六类埋点问题都应被检出"
    assert any("age" == a[2] and a[3] == "三十五" for a in anomalies)
    assert any(a[2] == "signup" for a in anomalies), "非法日期应被检出"
    assert any(a[2] == "spend" and a[3] == 99999.0 for a in anomalies), "MAD 离群应被检出"
    assert any(a[3] == -5.0 for a in anomalies), "负金额应被域规则检出"
    print("要点: 域规则抓'一定错', 分布离群抓'数字合法但离谱', 双通道结果都落到单元格级清单才可修复")
