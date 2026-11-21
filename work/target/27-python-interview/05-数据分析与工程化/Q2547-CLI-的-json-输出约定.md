---
title: [Q2547] CLI 的 --json 输出约定
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2547 · CLI 的 --json 输出约定

> 难度:★★☆☆ | 标签:CLI, 输出契约

**问**:你的工具要被调度系统和同事两种人用,输出怎么设计?

**答**:双模式加一条铁律:stdout 只出数据,日志一律走 stderr。默认人读模式打印对齐表格和警告摘要给人看;--json 模式往 stdout 打一个纯 JSON 对象,直接可管道给 jq,实测日志 [log] 行出现在 stderr,JSON 单行干净输出。JSON 结构带 schema_version 字段(1.0),消费者据此协商升级——未来加字段不破坏老消费者,改语义必须升版本。这套约定让同一个工具同时喂两个世界:人肉运维看表格,自动化管线解析 JSON 拿退出码和结构化数据,互不迁就。反面教材是 print 调试信息和数据混在 stdout,下游解析全靠正则猜,版本一升全炸。JSON 输出还要保证确定性:键序固定、时间戳带时区,自动化对账才有得比。

```python
# file: code/05_数据分析与工程化/q2547_cli_json.py
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
```

**追问**:
- 追问 1:错误怎么输出?—— 出错时 stdout 保持干净,错误结构化打到 stderr 并配非零退出码,JSON 模式可输出 {"error": {"code": ..., "message": ...}} 到 stderr。
- 追问 2:大结果集怎么避免 JSON 撑爆内存?—— 支持 NDJSON 逐行流式输出,配合 --limit 分页,消费者流式解析不必全量载入。
