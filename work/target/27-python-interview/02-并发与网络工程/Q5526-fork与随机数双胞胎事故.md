---
title: [Q5526] fork 与随机数：双胞胎序列事故
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5526 · fork 与随机数：双胞胎序列事故

> 难度:★★★★ | 标签:fork, 随机数, 事故复盘

**问**：fork 出的子进程为什么会拿到和父进程（或兄弟进程）完全相同的随机序列？现代 CPython 已经堵了哪个洞、还有哪些洞没堵？这类事故的指纹和修复清单是什么？

**答**：原理：`fork()` 复制整个进程内存，PRNG 的内部状态一并继承——父子/兄弟共享同一条随机序列的"时间线"。现代 CPython 堵了最常见的洞：`random` 模块通过 `os.register_at_fork(after_in_child=_inst.seed)` 在 fork 后的子进程里**自动重播种默认实例**（用 urandom），所以"直接 `import random` 后 fork"在新版是安全的。没堵的洞：1) **自建实例** `random.Random(42)`——对象状态随 fork 复制，两个子进程产出逐字节相同的序列（可复现演示）；2) **第三方/自研 PRNG**（numpy 的 `RandomState` 实例、C 扩展内部状态、业务自实现 LCG）——同样不会被钩子覆盖；3) **用时间做种子**（`seed(int(time.time()))`）——同秒内 fork 的多个子进程种子相同，配合"复制状态"双重翻车。事故指纹：**日志/trace 里多个 worker 生成完全相同的"随机"id/采样集**，且按 worker 启动顺序呈同一序列——采样器、验证码、幂等键、灰度分流全被"同一支骰子"支配。修复清单：子进程入口显式 `seed()`（从 `os.urandom`/`secrets` 取熵）；随机 id 一律 `secrets.token_hex/os.urandom`（OS 熵，fork 无状态问题）；spawn 启动方式天然无此问题（全新解释器，Q574）；单测里用固定种子做确定性，但要按"每进程一种子"约定。

```python
# file: code/02_并发与网络工程/q5526_fork_random.py
import os, random, time

rng = random.Random(42)              # 自建实例:fork 后不会被重播种
parent_first = rng.random()          # 父进程先消耗一步,子进程从这里分叉

for name in ("c1", "c2"):
    pid = os.fork()
    if pid == 0:
        # 两个子进程继承同一实例状态 -> "双胞胎"序列
        print(name, "instance:", round(rng.random(), 6), flush=True)
        # 默认实例已被 random 模块的 register_at_fork(after_in_child=seed) 重播种
        print(name, "module :", round(random.random(), 6), flush=True)
        os._exit(0)

time.sleep(0.2)
for _ in range(2):
    os.waitpid(-1, 0)
print("父进程 fork 前消耗值:", round(parent_first, 6),
      "(子进程继承该状态,两个子进程的 instance 值必然相同)")
print("结论: 默认 random 实例 fork 安全(register_at_fork 重播种);")
print("      自建 Random 实例/第三方 PRNG/numpy RandomState 必须在子进程入口显式重播种")
```

**追问**：1) 为什么 `multiprocessing` 的 fork 启动没这问题？——`BaseProcess._bootstrap` 在子进程入口会重播种（实测 fork 两个 worker 得到不同序列），但第三方 PRNG/扩展状态仍不归它管，混用场景照样翻车。2) `os.urandom`/`secrets` 为什么免疫？——它们直读 OS 熵池，没有用户态状态可被复制；唯一要防的是 fork 后 fd 层面的怪异（与随机无关）。3) 怎么在压测/巡检里把这类事故挖出来？（提示：对"随机"产物的全域分布做卡方/唯一率检查（Q2934 采样思路），同批次内重复率异常即告警，再按 worker 维度对齐序列指纹定位）

## 背诵要点
1. fork 复制 PRNG 状态：父子/兄弟共享同一条随机时间线，产物可能逐字节相同。
2. CPython 用 `register_at_fork(after_in_child=seed)` 重播种**默认 random 实例**；自建实例、numpy RandomState、C 扩展状态不在覆盖内。
3. 修复：子进程入口显式重播种；"随机 id"用 secrets/os.urandom；或改 spawn 启动方式。

## 复盘追问
1. 灰度分流用了 `random.Random` 实例 + fork 预派发（gunicorn 类模型），为什么不同 worker 总把同一批用户分进实验组？（提示：worker 间序列相同 + 分流按请求序消耗随机数，同序号请求落同桶；改 hash 分流（Q1340）或每 worker 重播种）
2. 怎么给"fork 安全"写回归测试？（提示：fork N 个子进程收集各自动产物断言互不相同；CI 里对 PRNG 实例的创建点做 lint，要求"实例随进程创建而非模块级"）
