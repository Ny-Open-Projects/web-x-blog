#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pick.py — 按主题缺口选题（替代"随手抓最厚的"）

背景：2026-10-03 盘点发现全库 107 张卡严重失衡 ——
调度器 GMP 占 30 张（28%），而 GC/性能/接口/标准库加起来只有 9 张。
继续"按体量抓最厚的"会让失衡加剧，因此改为**按缺口选题**。

用法：
  python3 pick.py            # 每个主题列 2 个候选
  python3 pick.py 3          # 每个主题列 3 个
  python3 pick.py 2 --xl     # 只看 XL（≥12KB）
"""

import argparse
import json
import os
import re
from pathlib import Path

ROOT = Path(os.environ.get("MT_ROOT", Path(__file__).resolve().parent.parent)).resolve()
PIPE = Path(os.environ.get("MT_PIPE", Path(__file__).resolve().parent))
STATE = Path(os.environ.get("MT_STATE", PIPE / "state.json"))

# 与 SELECT.md 的缺口表保持一致；顺序 = 优先级
# ⚠️ 正则要「窄而准」，宁可少推也不要推错 —— 2026-10-03 被 worker 指出两个 bug：
#    ① 「错误处理」含 `返回` → 把「浏览器输入URL到返回页面」误判（正文其实是 DNS/TCP/HTTP）
#    ② 「接口/抽象」含 `设计` → 把「Java 设计模式有哪些」捞进来（Go 语境无关，属 R2 降级）
#    修法：去掉过宽的通用词，改用该主题**特有**的术语。
GAPS = [
    ("GC/内存",   r"GC|垃圾回收|内存泄漏|逃逸|堆|栈|分配器|指针|数值|类型转换"),
    ("性能/基准", r"性能|基准|优化|调优|压测|耗时|限流|剖析|profil"),
    # ⚠️ 2026-10-03 第三次修正：原正则含 `算法`，把 7 篇**纯算法/通识**捞进标准库栏
    #    （LRU/LFU、一致性哈希、页置换、进程调度、磁盘调度、复杂度、算法100题）——
    #    这些是算法/OS 通识题，不是 Go 专项。已从正则里去掉 `算法`，并把 8 篇标为 skipped。
    ("标准库",    r"strings|strconv|time\.|sync\.|fmt\.|sort\.|json\.|bufio|regexp|标准库|编码|io/ioutil|os\.File|text/template|unicode"),
    ("并发模式",  r"并发|锁|原子|单例|channel|协程|通道|select|竞态|race|死锁|Once|WaitGroup|原子操作"),
    ("网络/IO",   r"http|net/http|网络|IO|timer|context|文件|读写|socket|客户端|服务端|epoll|表单|连接池|域名"),
    # 错误处理：去掉「返回」「异常」等通用词，只留 Go 侧特有表述
    ("错误处理",  r"错误|error|panic|recover|defer|fatal|闭包"),
    # ── 以下两栏是 2026-10-03 14:50 按用户裁定新增 ──
    # 起因：我曾把 8 篇「非 Go 专项」标为 skipped（OS 页置换/进程调度/磁盘调度、
    # LRU/LFU、一致性哈希、复杂度、算法100题、面试准备）。**用户裁定「全收，重排任务」**。
    # 复核原文后确认：这些**不是废料，是另一类** —— OS 理论在 Go 里有对应实现
    # （页置换↔Go 堆管理、调度↔GMP、磁盘调度↔文件 IO），算法通识是性能分析前置。
    # 关键是**单独归栏**，不能塞进 Go 专项栏，也不能当 R2/R3 剔除。
    ("OS↔Go 对照", r"页置换|页面置换|进程调度|磁盘调度|页面分配|时钟页面"),
    ("算法通识",   r"复杂度|大o|算法必备|LRU|LFU|一致性哈希|缓存淘汰"),
    ("面试方法论", r"如何回答|怎么回答|回答.*面试官|准备数据结构和算法|面试准备|自我介绍|反问"),
    # 接口/抽象：去掉「设计」（会捞到 Java 设计模式），只留 Go 侧术语
    ("接口/抽象", r"interface|接口|泛型|反射|reflect|继承|内嵌|嵌入|抽象类|方法集|装饰器|工厂"),
    ("map/slice", r"map|slice|切片|映射|append|range"),
]

# 已超配、停止产出的主题（命中则直接排除）
BLOCKLIST = r"调度|GMP|调度器|sysmon|proc\b|work-stealing|findrunnable|goroutine-profile|goid"


def load():
    if not STATE.exists():
        raise SystemExit(f"找不到 {STATE}，请先 `python3 queue.py init`")
    return json.loads(STATE.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int, nargs="?", default=2, help="每个主题列几个")
    ap.add_argument("--xl", action="store_true", help="只看 XL（≥12KB）")
    a = ap.parse_args()

    st = load()
    pend = [t for t in st["tasks"].values() if t["status"] == "pending"]
    if a.xl:
        pend = [t for t in pend if t["bytes"] >= 12000]

    print(f"待处理 {len(pend)} 篇"
          f"{'（仅 XL）' if a.xl else ''}，按缺口优先级列出：\n")

    picked = set()
    for name, pat in GAPS:
        hits = [t for t in pend
                if re.search(pat, t["title"])
                and t["id"] not in picked
                and not re.search(BLOCKLIST, t["title"], re.I)]
        hits.sort(key=lambda t: -t["bytes"])
        if not hits:
            continue
        for t in hits[:a.n]:
            picked.add(t["id"])
            print(f"  [{name:<8}] {t['id']:>7} {t['bytes']:>6}B  {t['tier']:>2}  {t['title'][:40]}")
            print(f"{'':>16}{t['source']}")
        if len(hits) > a.n:
            print(f"{'':>10}… 该主题还有 {len(hits) - a.n} 个候选")

    print(f"\n共 {len(picked)} 个候选。已排除超配主题（调度器/GMP）。")
    print("开工前照例：checkdup.py --allocate N 申请编号")


if __name__ == "__main__":
    main()
