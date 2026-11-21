"""重复文件的哈希跳过: 尺寸短路 + 内容摘要 + 台账复用"""
import hashlib

FILES = {
    # 文件名: 内容字节串 与 修改时间(模拟 stat 结果)
    "orders_2026-11-01.csv": [b"dt,amt\n" + b"2026-11-01,10\n" * 50, 1000],
    "orders_2026-11-02.csv": [b"dt,amt\n" + b"2026-11-02,12\n" * 50, 1000],
    "users_2026-11-01.csv": [b"id,name\n" + b"1,zhang\n" * 30, 1000],
    "users_2026-11-02.csv": [b"id,name\n" + b"2,li\n" * 30, 1000],
}


def digest(content):
    return hashlib.sha256(content).hexdigest()


def ingest_run(files, ledger, hash_calls):
    """返回本次真正入库的文件与跳过的文件; 尺寸与修改时间都没变才信任台账"""
    copied, skipped = [], []
    for name, (content, mtime) in sorted(files.items()):
        size = len(content)
        old = ledger.get(name)
        if old and old["size"] == size and old["mtime"] == mtime:
            skipped.append(name)          # 尺寸与 mtime 没变, 复用台账哈希
            continue
        h = digest(content)
        hash_calls.append(name)
        ledger[name] = {"size": size, "mtime": mtime, "sha256": h}
        copied.append(name)
    return copied, skipped


if __name__ == "__main__":
    ledger, hash_calls = {}, []
    copied1, skip1 = ingest_run(FILES, ledger, hash_calls)
    print(f"首次运行: 入库 {len(copied1)} 个, 跳过 {len(skip1)} 个")
    assert len(copied1) == 4 and len(hash_calls) == 4, "首次运行全部要计算哈希"
    # 第二次运行: 内容完全不变
    hash_calls.clear()
    copied2, skip2 = ingest_run(FILES, ledger, hash_calls)
    print(f"重跑不变数据: 入库 {len(copied2)} 个, 跳过 {len(skip2)} 个, 重哈希 {len(hash_calls)} 次")
    assert copied2 == [] and len(hash_calls) == 0 and len(skip2) == 4, "不变数据应零哈希零入库"
    # 第三次运行: 一个文件内容变化但尺寸相同, 一个新增文件
    FILES["orders_2026-11-02.csv"] = [b"dt,amt\n" + b"2026-11-02,15\n" * 50, 1001]
    FILES["orders_2026-11-03.csv"] = [b"dt,amt\n" + b"2026-11-03,9\n" * 50, 1002]
    hash_calls.clear()
    copied3, skip3 = ingest_run(FILES, ledger, hash_calls)
    print(f"增量运行: 入库 {copied3}, 跳过 {len(skip3)} 个, 重哈希 {len(hash_calls)} 次")
    assert sorted(copied3) == ["orders_2026-11-02.csv", "orders_2026-11-03.csv"]
    assert len(hash_calls) == 2, "只有 mtime 或尺寸变化和新文件才付出哈希成本"
    print("要点: 尺寸加 mtime 双短路让'没变就不动'成为默认; 同尺寸且 mtime 也被伪造时要靠周期审计兜底")
