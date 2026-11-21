"""哈希台账的损坏审计: 同尺寸改内容与截断文件都要抓出来"""
import hashlib

LEDGER = {
    # 文件名: 台账里的尺寸与摘要(采集入库时的状态)
    "events_2026-11-01.csv": {"size": 400, "sha256": "a" * 64},
    "events_2026-11-02.csv": {"size": 380, "sha256": "b" * 64},
    "events_2026-11-03.csv": {"size": 360, "sha256": "c" * 64},
}

DISK = {
    # 实际磁盘内容: 02 号同尺寸被改写, 03 号被截断, 01 号完好
    "events_2026-11-01.csv": {"size": 400, "sha256": "a" * 64},
    "events_2026-11-02.csv": {"size": 380, "sha256": "d" * 64},
    "events_2026-11-03.csv": {"size": 210, "sha256": "e" * 64},
}


def audit(ledger, disk):
    """全量再哈希审计, 返回问题清单"""
    findings = []
    for name in sorted(ledger):
        rec = ledger[name]
        cur = disk.get(name)
        if cur is None:
            findings.append((name, "丢失", "台账有档, 磁盘无文件"))
        elif cur["size"] != rec["size"]:
            findings.append((name, "尺寸漂移", f"台账 {rec['size']}B, 磁盘 {cur['size']}B"))
        elif cur["sha256"] != rec["sha256"]:
            findings.append((name, "内容篡改", "尺寸一致但摘要不同, 同尺寸改写"))
    for name in disk:
        if name not in ledger:
            findings.append((name, "台账外文件", "未登记, 需要补录或清理"))
    return findings


def repair(ledger, disk, findings):
    """修复: 尺寸漂移与篡改文件以磁盘现值为准重建台账并标记重采"""
    repaired, reingest = [], []
    for name, kind, _ in findings:
        if kind in ("尺寸漂移", "内容篡改") and name in disk:
            ledger[name] = dict(disk[name])
            repaired.append(name)
            reingest.append(name)
    return repaired, reingest


if __name__ == "__main__":
    findings = audit(LEDGER, DISK)
    print("审计发现:")
    for name, kind, detail in findings:
        print(f"  {name}  [{kind}]  {detail}")
    kinds = {kind for _, kind, _ in findings}
    assert "内容篡改" in kinds, "同尺寸改写必须靠摘要抓出来"
    assert "尺寸漂移" in kinds, "截断文件应表现为尺寸漂移"
    repaired, reingest = repair(LEDGER, DISK, findings)
    print(f"修复 {repaired}, 标记重新采集 {reingest}")
    assert sorted(reingest) == ["events_2026-11-02.csv", "events_2026-11-03.csv"]
    assert audit(LEDGER, DISK) == [], "修复后审计应零发现"
    print("要点: 台账不是免检金牌, 周期性全量再哈希是唯一能抓'同尺寸改内容'的手段; 修复必须连带重采")
