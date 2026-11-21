"""守恒差额的分块定位: 累计差额首次非零的块就是事故现场"""

LEDGER = [
    # 块号, 读入行数, 支出行数(落表+去重+隔离)
    ("c1", 1000, 1000),
    ("c2", 1000, 1000),
    ("c3", 1000, 980),      # 这一块丢了 20 行
    ("c4", 1000, 1000),
]


def locate(ledger):
    """累计差额首次变非零的块即肇事块"""
    cum = 0
    for chunk_id, read, out in ledger:
        prev = cum
        cum += read - out
        if cum != 0:
            return chunk_id, cum - prev, cum
    return None, 0, cum


if __name__ == "__main__":
    chunk_id, delta, cum = locate(LEDGER)
    print(f"定位: 肇事块 {chunk_id}, 该块未落账 {delta} 行, 此后累计差额 {cum}")
    assert chunk_id == "c3" and delta == 20
    fixed = [(c, r, o if c != "c3" else r) for c, r, o in LEDGER]
    chunk_id2, _, cum2 = locate(fixed)
    print(f"修复后重跑: 首个异常块 {chunk_id2}, 期末累计差额 {cum2}")
    assert chunk_id2 is None and cum2 == 0, "修复后必须全零"
    print("要点: 逐块台账让'总数对不上'收缩到具体分片; 块级差额等价于一次线性扫描, 大表可再二分")
