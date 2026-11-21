"""上游心跳检测: 进程活着不等于数据在流, 心跳与水位双查"""

INTERVAL = 10          # 上游正常 10 分钟一跳
WINDOW = 60            # 批窗口 60 分钟
# 心跳记录: 跳动时刻(分钟), 已完成批次窗口末端, 批行数
RECORDS = [
    (600, 540, 1200),   # 10:00 跳, 完成到 09:00 批
    (610, 540, 1200),   # 10:10 还在跳, 但批次没再推进
    (620, 540, 1200),
    (690, 540, 1200),   # 11:30 仍在跳, 已空转一小时
]


def check(records, now):
    last_t, last_batch, _ = records[-1]
    hb_age = now - last_t                       # 心跳年龄
    batch_lag = now - last_batch                # 批次水位滞后
    if hb_age >= INTERVAL * 2:
        return "stale", f"心跳停跳 {hb_age} 分钟"
    if batch_lag >= WINDOW * 2:
        return "stale", f"心跳在跳但批次水位滞后 {batch_lag} 分钟"
    return "fresh", "正常"


if __name__ == "__main__":
    status, reason = check(RECORDS, 605)
    print(f"10:05 检查: {status} ({reason})")
    assert status == "fresh"
    status, reason = check(RECORDS, 700)
    print(f"11:40 检查: {status} ({reason})")
    assert status == "stale" and "滞后" in reason, "应检出'活着但没出货'"
    status, reason = check(RECORDS[:-1], 700)
    print(f"若心跳也停了: {status} ({reason})")
    assert "停跳" in reason
    print("要点: 心跳表要带批次水位, 只查进程心跳会漏掉'空转'型断流, 双指标才抓得住两种死法")
