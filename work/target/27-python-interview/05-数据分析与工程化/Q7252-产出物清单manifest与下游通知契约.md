---
title: "[Q7252] 下游只知道「跑完了」：产出物清单与完成通知的契约"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7252 · 下游只知道「跑完了」：产出物清单与完成通知的契约

难度：P6 ｜ 标签：产出物清单、下游通知、分区就绪、数据就绪探测

基线：Python 3.12；模拟任务完成通知携带 manifest（分区/行数/校验和），下游先验签再消费。

**问**：数据管道的任务完成后只在群里发一句"taskX 跑完了"。下游任务要么死等调度依赖（依赖配置错了就白等），要么轮询目标表（读到半截数据）。完成的"通知"到底该带什么信息？没有 manifest 的完成通知和有 manifest 的，对下游的消费方式差别在哪？

**答**：
- **结论**：完成通知的核心不是"喊一声"，而是**交付一份可验证的产出清单（manifest）**：分区标识、输出表/文件清单、行数、校验和、生成时间、管道版本。下游拿到 manifest 可以：① **验签消费**——核对行数/校验和与实际一致才读数，防止读到半截或被污染的产出；② **精确依赖**——只依赖 manifest 里声明的分区，而不是"上游任务结束"这种过程性事件；③ **可追溯**——manifest 落库后，"这份数是哪次运行、哪个版本产出的"有据可查（Q2537 运行清单、Q2978 依赖健康检查的底座）。没有 manifest，下游只能轮询探测（Q7032 的就绪探测），既慢又可能读到中间态。
- **取舍**：① manifest 的生成成本：行数/校验和要扫输出，大表可以只做"分区级行数 + 抽样校验和"，全量校验留给对账任务；② 通知通道：回调（下游注册）比广播可靠，消息丢失时下游还有轮询兜底——两条腿都要有；③ manifest 要**不可变**：产出物一旦发布，manifest 冻结，重跑产出新版本新 manifest，别原地改。
- **实战**：① 平台把 manifest 生成做成任务框架的收尾钩子，任务作者只声明输出分区，不手写清单；② 下游消费入口统一"先验 manifest 再读数"，验签失败拒绝消费并告警；③ manifest 落库成为元数据的一部分，血缘与影响面分析（Q1742）直接受益。

```python
"""产出物 manifest：生成 -> 验签 -> 下游消费的完整契约。"""
import hashlib
import json


def compute_checksum(rows: list[dict]) -> str:
    payload = json.dumps(rows, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode()).hexdigest()[:16]


def build_manifest(task: str, partition: str, rows: list[dict],
                   pipeline_version: str) -> dict:
    return {"task": task, "partition": partition,
            "pipeline_version": pipeline_version,
            "row_count": len(rows),
            "checksum": compute_checksum(rows),
            "status": "final",                      # 冻结不可变
            }


def verify_and_consume(manifest: dict, actual_rows: list[dict]) -> tuple[bool, str]:
    """下游消费入口：先验 manifest 再读数。"""
    if manifest["status"] != "final":
        return False, "manifest 未冻结, 拒绝消费"
    if manifest["row_count"] != len(actual_rows):
        return False, (f"行数不符: manifest={manifest['row_count']} "
                       f"实际={len(actual_rows)}")
    if compute_checksum(actual_rows) != manifest["checksum"]:
        return False, "校验和不符: 产出疑似被改写或写了一半"
    return True, "验签通过, 消费"


def poll_without_manifest(rows_getter, want: int, tries: int = 10) -> str:
    """反例：无 manifest 只能轮询，可能读到半截。"""
    for i in range(tries):
        rows = rows_getter(i)
        if len(rows) >= want:
            return f"第{i+1}次轮询拿到 {len(rows)} 行 (可能是半截, 无法自证完整)"
    return "超时未就绪"


if __name__ == "__main__":
    rows = [{"order_no": f"A{i}", "amount": 50} for i in range(100)]
    mf = build_manifest("taskX", "ds=2026-11-24", rows, "v2.3.1")
    print("manifest:", {k: mf[k] for k in ("task", "partition", "row_count")})
    print("验签:", verify_and_consume(mf, rows))

    half = rows[:60]                                # 模拟读到半截产出
    ok, msg = verify_and_consume(mf, half)
    print("半截数据验签:", ok, "->", msg)

    print("\n无 manifest 对照:", poll_without_manifest(
        lambda i: rows if i >= 3 else rows[:20], want=100))
    print("结论：完成通知=可验证的 manifest；下游先验签再消费, 半截/污染数据进不来")
```

**追问一**：行数和校验和要扫全量输出，大表扛不住怎么办？

→ 解析：分级验证：分区级做"行数 + 元数据（文件大小/文件数）"轻校验，校验和只对抽样行（比如按主键取模 1% 的行）计算，行级精确校验交给日间对账任务兜底。manifest 里诚实声明校验等级（`checksum: sampled@1%`），下游据此决定信任程度。另一个技巧是让**写入方在写时就累计**：逐批写入时顺带更新行数与滚动校验和，完成时零额外扫描——这与 Q2961 ETL 最小实现里的对账钩子同思路，把验证成本摊进正常写入路径。

**追问二**：manifest 通知消息丢了，下游怎么办？

→ 解析：这就是为什么通知要"回调 + 轮询"双通道：回调丢消息时，下游的就绪探测（Q7032）会查 manifest 注册表——manifest 本身落库，通知只是"催一下"的加速器，不是唯一事实源。下游消费入口统一以"注册表里存在 status=final 的 manifest 且验签通过"为准绳，通知丢了最多晚几个探测周期，不会漏消费或读半截。反过来的教训是：如果只做群消息这种"人读的广播"，没有机器可验证的事实源，下游永远只能轮询裸表。
