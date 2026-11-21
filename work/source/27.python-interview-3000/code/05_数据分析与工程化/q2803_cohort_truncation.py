"""成熟龄未对齐的截断偏差: 未满窗用户把留存率人为拖低"""

OCT_D7_RATE = 0.45          # 10月群等成熟龄第 7 日留存
NOV_N = 1100                # 11月群规模
NOV_MATURE_N = 430          # 已满 7 天观察窗的用户
NOV_MATURE_RETAINED = 194   # 其中第 7 日仍活跃的
NOV_IMMATURE_N = NOV_N - NOV_MATURE_N
# 未满窗用户在各自的截断窗口内已回访的(不是真流失, 只是还没到第 7 天)
NOV_IMMATURE_SO_FAR = 134


def naive_retained():
    """错误口径: 把未满窗用户全算进分母, 他们'尚未回访'被当成流失"""
    return NOV_MATURE_RETAINED + NOV_IMMATURE_SO_FAR


def mature_retained_rate():
    """正确口径: 只统计满窗用户, 未满窗的遮罩后单独披露"""
    return NOV_MATURE_RETAINED / NOV_MATURE_N


if __name__ == "__main__":
    naive = naive_retained() / NOV_N
    mature = mature_retained_rate()
    print(f"11月群 {NOV_N} 人, 其中满 7 天窗的仅 {NOV_MATURE_N} 人")
    print(f"错误口径(未满窗算流失): {naive_retained()}/{NOV_N} = {naive:.1%}")
    print(f"正确口径(仅满窗用户): {NOV_MATURE_RETAINED}/{NOV_MATURE_N} = {mature:.1%}")
    print(f"对照 10月群等成熟龄第 7 日留存 {OCT_D7_RATE:.1%}")
    drop_naive = OCT_D7_RATE - naive
    drop_mature = OCT_D7_RATE - mature
    print(f"错误口径结论: 暴跌 {drop_naive:.1%} 个百分点 -> 触发流失告警")
    print(f"正确口径结论: 差 {drop_mature:+.1%} 个百分点 -> 基本持平")
    assert naive < mature - 0.1, "截断偏差应把留存显著拖低"
    assert drop_mature > -0.02, "满窗口径下两群应基本持平"
    assert drop_naive > 0.1, "截断口径会给出暴跌假象"
    immature_rate = NOV_IMMATURE_SO_FAR / NOV_IMMATURE_N
    print(f"附注: 未满窗用户当前临时回访率 {immature_rate:.1%}, 会随窗口补满而上升, 不能与满窗率混合")
    print("要点: 新同期群的留存天然随成熟度爬升, 报表要么遮罩未满窗, 要么标注'部分成熟', 别拿半成品比满月")
