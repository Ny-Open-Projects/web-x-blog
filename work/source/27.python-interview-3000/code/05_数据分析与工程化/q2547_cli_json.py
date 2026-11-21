"""CLI 的 --json 输出约定: stdout 只出数据, 日志走 stderr"""

import argparse
import json
import sys

SUMMARY = {
    "date": "2026-03-01",
    "orders": 120,
    "gmv": 9800.5,
}
WARNINGS = ["3 笔小额订单待人工核验"]


def build_result():
    return {"schema_version": "1.0", "data": SUMMARY, "warnings": WARNINGS}


def log(msg):
    print(f"[log] {msg}", file=sys.stderr)


def main(argv):
    parser = argparse.ArgumentParser(description="订单日报工具")
    parser.add_argument("--json", action="store_true", help="输出机器可读 JSON")
    args = parser.parse_args(argv)
    log("读取汇总数据完成")            # 日志永远走 stderr, 不污染管道
    if args.json:
        print(json.dumps(build_result(), ensure_ascii=False))
        return 0
    print("日期       订单数   GMV")
    print(f"{SUMMARY['date']}  {SUMMARY['orders']:6d}  {SUMMARY['gmv']:8.1f}")
    print("警告: " + "; ".join(WARNINGS))
    return 0


if __name__ == "__main__":
    print("== 人读模式(日志可见于 stderr) ==")
    main([])
    print("== JSON 模式 ==")
    main(["--json"])
    payload = json.loads(json.dumps(build_result()))
    assert payload["schema_version"] == "1.0" and payload["data"]["orders"] == 120
    print("约定: stdout 可直接管道给 jq, schema_version 保证消费者可协商升级")
