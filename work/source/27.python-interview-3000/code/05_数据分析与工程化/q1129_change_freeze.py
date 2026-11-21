from datetime import date

FREEZES = [(date(2026, 11, 5), date(2026, 11, 13), "大促核心链路冻结")]
FASTLANE = {"config", "copy", "docs"}

def can_release(change_date, change_type, urgent=False):
    for start, end, _ in FREEZES:
        if start <= change_date <= end:
            if urgent:
                return True, "紧急修复走审批例外"
            if change_type in FASTLANE:
                return True, "低风险快速通道"
            return False, "冻结期内,核心变更暂停"
    return True, "正常发布"

for d, t in ((date(2026, 11, 8), "api"), (date(2026, 11, 8), "config"), (date(2026, 11, 20), "api")):
    ok, why = can_release(d, t)
    print(f"{d} {t}: {'允许' if ok else '拒绝'} - {why}")
