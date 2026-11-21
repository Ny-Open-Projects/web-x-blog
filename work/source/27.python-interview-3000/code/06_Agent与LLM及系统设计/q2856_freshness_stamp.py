"""Q2856 答案的数据截止标注:从证据日期推导可信窗口。

用户问「现在政策是什么」,答案里不写「依据截至哪天」,用户就会把
两年前的旧规当现行政策。给答案盖时间戳:取全部证据的最新日期,
按距今天数分档附上新鲜度提示,过期严重时明确提示人工核实。
"""

from datetime import date

FRESH_DAYS = 30
STALE_DAYS = 180


def stamp(evidence_dates, today):
    """evidence_dates: 该答案引用的证据发布日期列表。"""
    newest = max(evidence_dates)
    oldest = min(evidence_dates)
    age = (today - newest).days
    if age <= FRESH_DAYS:
        note = None
    elif age <= STALE_DAYS:
        note = "证据已超过 %d 天未更新,注意时效" % FRESH_DAYS
    else:
        note = "证据严重过期,建议人工核实"
    text = "依据截至 " + newest.isoformat()
    return {"stamp": text, "newest": newest, "oldest": oldest,
            "age_days": age, "note": note}


def main():
    today = date(2026, 11, 5)
    s1 = stamp([date(2026, 10, 20), date(2026, 9, 1)], today)
    assert s1["stamp"] == "依据截至 2026-10-20" and s1["note"] is None, s1
    s2 = stamp([date(2026, 5, 1)], today)
    assert s2["age_days"] == 188, s2   # 超过 180 天,严重过期
    assert "人工核实" in s2["note"], s2
    s3 = stamp([date(2026, 8, 15)], today)
    assert s3["age_days"] == 82 and "30 天" in s3["note"], s3
    # 旧证据会拉低整体可信度:标注必须用最新证据日期
    s4 = stamp([date(2026, 11, 1), date(2025, 1, 1)], today)
    assert s4["newest"] == date(2026, 11, 1) and s4["note"] is None, s4
    assert s4["oldest"] == date(2025, 1, 1)
    for s in (s1, s2, s3):
        print(s["stamp"], "|", s["note"])


if __name__ == "__main__":
    main()
