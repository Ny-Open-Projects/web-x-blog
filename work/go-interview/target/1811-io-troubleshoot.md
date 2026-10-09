# 1811 IO 问题排查：iostat 定位设备瓶颈 + pidstat 锁定进程

> 分类：Linux 基础 / 性能排查 | 难度：L2 | 题型：排查题 | 频率：高 | 关键词：**iostat -xz**/**%util**/**await**/**aqu-sz**/**pidstat**/**%iowait**

> 原文锚点：第 1~14 段「iostat 发现瓶颈 → 指标族判读 → pidstat 定位进程」

## 一句话总述
IO 排查两步走：**iostat -xz 1** 在设备层发现瓶颈（看 r/s、w/s、rkB/s、wkB/s 量化负载，r_await、w_await 看应用感受的等待毫秒，aqu-sz 看平均并发请求，%util 看设备忙碌占比），**pidstat** 在进程层锁定是哪个进程在吃 IO（重点 %iowait 列）——设备层确认有病，进程层找到病人。

## 面试官视角
排查题考的是**指标判读的准确度**，不是工具名。三个判读点分档：① await 与 %util 谁更能说明「应用受影响」——await 是应用视角的等待毫秒、%util 只是设备忙碌时间比；② **RAID/多路径逻辑设备的 %util=100% 是假饱和**——它只说明「100% 的时间都有 IO 在处理」，后端物理盘远未到极限；③ **磁盘忙 ≠ 应用有问题**——异步 IO/预读/page cache 让应用根本感受不到延迟。三处都答对，就是真排查过。

## 主问答
**Q（面试官原话）：** 如何排查 IO 问题？

1. **第一步：iostat -xz 1 扫设备层**（sysstat 包）。`-x` 扩展统计、`-z` 跳过无活动的设备、`1` 每秒刷新。
2. **负载量化四指标**：r/s、w/s（每秒读/写次数）、rkB/s、wkB/s（每秒读/写字节数）——回答「这台盘在扛多少活」。
3. **等待两指标**：r_await、w_await（读/写请求的平均等待毫秒）——**应用视角的感受值，含排队时间**。超过该设备的正常预期（机械盘几 ms、SSD 亚 ms）即设备饱和或故障。
4. **并发与忙碌**：aqu-sz（平均请求队列深度，持续 >1 说明请求在排队）；%util（设备处理 IO 的时间占比，接近 100% 说明设备持续忙碌——**RAID 逻辑设备例外**，见深卡）。
5. **第二步：pidstat -d 锁进程**：输出按进程统计（PID/UID、%usr/%system/%guest CPU、**%wait 等 IO 导致的 CPU 空闲占比**、命令名）。与 top 不同，pidstat 是**滚动输出不清屏**——能看变化趋势、也方便把排查过程留档。
6. **[实测] 方法演示**（macOS 本机，iostat -d）：基线 disk0 tps=132、3.09MB/s；发起 512MB 顺序写（dd，237MB/s 完成于 2.26s）期间 tps 冲到 **7788、264MB/s**——「先测基线、再造负载、对照观测」是 IO 排查的标准动作，Linux 上用 iostat -xz 同理。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 用什么工具扫 IO？ | 说不清 iostat（-x 扩展 -z 去静默） |
| L2 | 哪些指标量化负载？ | 说不清 r/s w/s rkB/s wkB/s |
| L3 | await 和 %util 各说明什么？ | 混淆应用感受与设备忙碌 |
| L4 | RAID 盘 %util=100% 是饱和吗？ | 说不清逻辑设备的假饱和 |
| L5 | 设备忙但应用正常，为什么？ | 说不清异步 IO/预读/page cache 的屏蔽 |

## 版本与兼容性
| 工具 | 作用 | 关键点 |
|------|------|--------|
| iostat -xz 1 | 设备层扫描 | sysstat 包；await 单位 ms；aqu-sz 队列深度 |
| pidstat -d 1 | 进程层定位 | %wait≈等 IO 的空闲占比；滚动输出不清屏 |
| 判读阈值 | 经验值 | %util>60% 关注、~100% 持续=饱和（依设备型号而异） |
| 注意 | 异步屏蔽 | 磁盘忙不一定应用卡，以应用延迟为最终判据 |

## 关键代码
```python
#!/usr/bin/env python3
"""iostat 采样对照: 提取每个采样行的 tps 与 MB/s, 用于基线/负载对照"""
import subprocess

out = subprocess.run(["iostat", "-d", "-c", "3", "-w", "1", "disk0"],
                     capture_output=True, text=True).stdout
lines = out.splitlines()
start = next(i for i, l in enumerate(lines) if "KB/t" in l)
for l in lines[start + 1:]:
    parts = l.split()
    if len(parts) == 3:  # macOS iostat 数据行: KB/t tps MB/s
        kb_per_t, tps, mbs = parts
        print(f"tps={tps:>6}  MB/s={mbs:>7}  KB/t={kb_per_t}")
print("判读: tps 高且 KB/t 大=顺序大块IO; tps 高 KB/t 小=随机小IO")
```

[实测] 输出（第三次采样恰逢后台小 IO，特征可读）：

```text
tps=   133  MB/s=   3.11  KB/t=24.02
tps=    88  MB/s=   4.82  KB/t=56.32
tps=  1118  MB/s=  10.76  KB/t=9.86
判读: tps 高且 KB/t 大=顺序大块IO; tps 高 KB/t 小=随机小IO
```

IO 排查两步链（Linux 语义）：
```text
IO 排查两步链 (排查题标准回答顺序)
├─ 设备层: iostat -xz 1
│   ├─ 负载: r/s, w/s, rkB/s, wkB/s
│   ├─ 等待: r_await, w_await (应用感受, 含排队)
│   ├─ 并发: aqu-sz (持续>1 = 排队)
│   └─ 忙碌: %util (RAID 逻辑设备慎判)
└─ 进程层: pidstat -d 1
    ├─ 按 PID 列出读写量与 %wait
    ├─ 锁定吃 IO 的进程 -> 结合业务归因
    └─ 滚动输出便于记录排查过程
```

[实测] 基线 vs 负载对照：tps 132 → 7788，带宽 3.09 → 264 MB/s（dd 512MB 顺序写期间）。

## 总结与追问预判
核心：**iostat 定设备（await 看感受、aqu-sz 看排队、%util 看忙碌、RAID 例外）、pidstat 定进程（%iowait）；磁盘忙 ≠ 应用卡，最终以应用延迟为准**。追问常拐向「定位到进程后怎么归因」——结合业务（日志狂写/刷盘策略/大文件扫描）与 IO 模型差异见 `1833-sync-vs-async-io.md`、零拷贝减负见 `1836-zero-copy-path.md`、负载体征见 `188-load-diagnosis.deep.md`、RAID 基础见 `1818-raid-basics.md`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文「IOstate/CSstate」均为 **iostat** 的音转；「suffer 机制」应为 **buffer/cache**（写缓冲与预读）；「RID」应为 **RAID**；「SHELL」等零散音转已归一。
2. 事实核校： [经验] 原文「%util 大于 60% 说明设备性能降低」表述过死——60%/100% 是经验参考线，**不同型号/厂商差异大**，且 RAID 逻辑设备 %util=100% 仅表示「时间上一直有 IO」，不代表物理盘极限；判读应结合 await 与应用延迟，原文后段自述了这点，前段表述易误导。
