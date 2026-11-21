import json
import os

def record_lineage(meta_path, table, inputs, code_version, rows):
    """每次产出追加一条血缘记录:谁、依赖什么、什么代码、产出多少。"""
    records = []
    if os.path.exists(meta_path):
        records = json.load(open(meta_path))
    records.append({"table": table, "inputs": inputs,
                    "code_version": code_version, "rows": rows})
    json.dump(records, open(meta_path, "w"), indent=2)
    return records

def downstream(records, table):
    """反向追踪:哪些表直接依赖了 table。"""
    return [r["table"] for r in records if table in r["inputs"]]

if __name__ == "__main__":
    meta = "lineage.json"
    record_lineage(meta, "dws_user_day", ["ods_order", "ods_user"], "git#abc123", 1000)
    record_lineage(meta, "ads_rpt", ["dws_user_day"], "git#abc123", 30)
    records = json.load(open(meta))
    print("downstream of dws_user_day:", downstream(records, "dws_user_day"))
    os.remove(meta)
