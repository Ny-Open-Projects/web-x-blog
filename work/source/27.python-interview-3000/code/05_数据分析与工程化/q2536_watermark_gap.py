"""水位空洞检测: 应跑窗口与实跑窗口对账, 补上静默丢失的窗口"""

STEP = 60
EXPECTED = [h * 60 for h in range(8, 13)]          # 08:00..12:00 每小时一个窗口
PROCESSED = [480, 540, 660, 720]                   # 08 09 11 12 点的窗口, 10 点那次失败后没人补


def fmt(minute):
    return f"{minute // 60:02d}:{minute % 60:02d}"


def find_gaps(expected, processed):
    processed_set = set(processed)
    holes = [w for w in expected if w not in processed_set]
    orphans = sorted(processed_set - set(expected))
    dup = len(processed) - len(processed_set)
    return holes, orphans, dup


if __name__ == "__main__":
    holes, orphans, dup = find_gaps(EXPECTED, PROCESSED)
    print(f"应跑 {len(EXPECTED)} 个窗口, 实跑 {len(set(PROCESSED))} 个")
    print("空洞(静默丢数): " + (", ".join(fmt(h) for h in holes) or "无"))
    assert [fmt(h) for h in holes] == ["10:00"], "10 点窗口应被检出"
    print(f"孤儿窗口(计划外): {orphans or '无'}, 重复执行 {dup} 次")
    fixed = sorted(set(PROCESSED) | set(holes))       # 空洞回填重跑
    holes2, _, _ = find_gaps(EXPECTED, fixed)
    assert not holes2, "回填后不应再有空洞"
    print(f"回填重跑后: {len(fixed)} 个窗口全部连续, 水位覆盖无缝")
    print("要点: 调度只保证'触发过', 空洞检测保证'连续覆盖', 失败窗口必须显式回填而不是跳过")
