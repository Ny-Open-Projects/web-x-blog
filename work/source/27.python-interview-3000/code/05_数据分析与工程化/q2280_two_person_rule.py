"""配置变更的双人复核: 制单复核分离与高危升级"""

from collections import namedtuple

Change = namedtuple("Change", "id maker checker action")


def review(change, is_senior=False):
    if change.checker == change.maker:
        return "拒绝", "制单人与复核人相同, 双人规则被破坏, 记录违规"
    if change.checker is None:
        return "挂起", "等待独立复核人认领, 超时自动升级"
    if "大版本" in change.action and not is_senior:
        return "升级", "高危变更需高级复核人批准"
    return "通过", f"复核人 {change.checker} 批准并归档"


if __name__ == "__main__":
    cases = [
        Change("CHG-1", "alice", "alice", "下调连接池到 5"),
        Change("CHG-2", "alice", None, "调整分区保留 30 天"),
        Change("CHG-3", "alice", "bob", "切换数仓大版本"),
    ]
    for c in cases:
        state, why = review(c)
        print(f"{c.id} [{c.action}] 制单 {c.maker} 复核 {c.checker} -> {state}: {why}")
    state, why = review(cases[2], is_senior=True)
    print(f"CHG-3 高级复核 -> {state}: {why}")
    print("要点: 制单复核分离; 高危变更按内容分级要求更高权限; 超时升级不许挂到过期; 归档可审计")
