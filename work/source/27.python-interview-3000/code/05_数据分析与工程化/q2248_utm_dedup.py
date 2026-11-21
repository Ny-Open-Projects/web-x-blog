"""UTM 归一化与重复投递去重: 归因前先清洗触点"""

from collections import Counter
from datetime import datetime, timedelta

CLICKS = [
    # 用户, 时间, utm_source, utm_campaign, 是否转化
    ("u1", "2026-03-01 09:00", "WeChat ", "spring_sale", False),
    ("u1", "2026-03-01 09:40", "wechat", "Spring_Sale", False),       # 窗口内重复投递
    ("u1", "2026-03-01 18:00", "wechat", "spring_sale", True),        # 超出窗口, 有效新触点
    ("u2", "2026-03-02 10:00", "douyin", "brand_x", False),
    ("u2", "2026-03-02 10:05", "douyin", "brand_x&gclid=abc", False),  # 带跟踪垃圾参数
    ("u3", "2026-03-02 11:00", " DouYin", "brand_x", True),
]
ALIAS = {"wx": "wechat", "weixin": "wechat", "dy": "douyin"}
FMT = "%Y-%m-%d %H:%M"


def normalize(source, campaign):
    s = source.strip().lower()
    s = ALIAS.get(s, s)
    c = campaign.split("&")[0].strip().lower()
    return s, c


def dedup_touches(clicks, window_min=60):
    """同一用户同一 campaign 在窗口内只保留首个触点"""
    out, last_seen = [], {}
    for user, ts, src, camp, conv in clicks:
        s, c = normalize(src, camp)
        key = (user, s, c)
        t = datetime.strptime(ts, FMT)
        prev = last_seen.get(key)
        if prev is not None and t - prev <= timedelta(minutes=window_min):
            continue
        last_seen[key] = t
        out.append((user, t, s, c, conv))
    return out


if __name__ == "__main__":
    clean = dedup_touches(CLICKS)
    for user, t, s, c, conv in clean:
        print(f"{user} {t:%m-%d %H:%M} {s}/{c} 转化={conv}")
    print(f"原始触点 {len(CLICKS)} 条, 清洗去重后 {len(clean)} 条, 剔除 {len(CLICKS) - len(clean)} 条")
    conv_src = Counter(s for _, _, s, _, conv in clean if conv)
    print("去重后转化来源分布:", dict(conv_src))
    print("要点: 归一化别名表与去重窗口都进公共清洗函数, 埋点端报表端共用一套")
