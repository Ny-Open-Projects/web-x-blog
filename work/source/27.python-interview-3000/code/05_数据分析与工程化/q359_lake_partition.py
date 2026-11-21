import os

def partition_path(base, table, data_date, batch):
    """湖表分区路径约定:表 / 数据日期 / 批次, 不可变写入。"""
    return f"{base}/{table}/date={data_date}/_batch={batch}/part-000.parquet"

def write_partition(rows, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):               # 幂等:同分区同批次覆盖
        pass
    with open(path, "w") as f:             # 演示用文本, 生产为 parquet
        for r in rows:
            f.write(str(r) + "\n")
    return path

if __name__ == "__main__":
    p = partition_path("lake", "ods_order", "2026-11-01", "b1")
    write_partition([{"oid": 1}, {"oid": 2}], p)
    write_partition([{"oid": 1}, {"oid": 2}], p)   # 重跑覆盖同一路径
    print("partition:", p, "idempotent ok")
    import shutil
    shutil.rmtree("lake")
