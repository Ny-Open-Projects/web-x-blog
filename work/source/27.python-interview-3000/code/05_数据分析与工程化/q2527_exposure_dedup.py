"""运营曝光去重: 毛曝光 触点去重与独立触达"""

from datetime import datetime, timedelta

IMPS = [
    # 用户, 活动, 素材, 渠道, 时间
    ("u1", "c1", "v1", "push", "09:00"),
    ("u1", "c1", "v1", "push", "09:05"),    # 10 分钟窗口内重复投递
    ("u1", "c1", "v1", "push", "09:20"),    # 窗口外, 计一次
    ("u2", "c1", "v1", "feed", "10:00"),
    ("u3", "c1", "v2", "feed", "10:00"),
    ("u1", "c2", "v1", "search", "11:00"),
    ("u1", "c2", "v1", "search", "11:05"),  # 10 分钟窗口内跨渠道重复投递
    ("u2", "c2", "v1", "search", "12:00"),
    ("u4", "c2", "v1", "search", "12:00"),
]
WINDOW = timedelta(minutes=10)


def dedup(imps):
    """同一 用户x活动x素材 在合并窗口内只计一个触点"""
    kept = []
    last_seen = {}
    for user, camp, creative, channel, ts in sorted(imps, key=lambda x: x[4]):
        key = (user, camp, creative)
        t = datetime.strptime(ts, "%H:%M")
        if key in last_seen and t - last_seen[key] < WINDOW:
            continue
        last_seen[key] = t
        kept.append((user, camp, creative, channel, ts))
    return kept


if __name__ == "__main__":
    kept = dedup(IMPS)
    campaigns = sorted({row[1] for row in IMPS})
    print(f"{'活动':<4} 毛曝光 去重后 独立用户 人均频次")
    for camp in campaigns:
        raw = [r for r in IMPS if r[1] == camp]
        kp = [r for r in kept if r[1] == camp]
        users = {r[0] for r in kp}
        freq = len(kp) / len(users)
        print(f"{camp:<4} {len(raw):4d} {len(kp):6d} {len(users):6d} {freq:8.2f}")
    assert len(IMPS) == 9 and len(kept) == 7, "应剔掉 2 条窗口内重复"
    same_user_multi = len({r[0] for r in kept if r[1] == "c1"} & {r[0] for r in kept if r[1] == "c2"})
    print(f"跨活动独立用户仍按人计: u1 同时出现在 {same_user_multi} 个活动, 汇总去重不许重复算人头")
    print("要点: 毛曝光考核投放执行, 去重触点考核真实到达, 独立触达考核人头, 三个数不可混用")
