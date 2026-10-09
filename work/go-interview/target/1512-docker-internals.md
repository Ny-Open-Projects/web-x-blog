# 1512 Docker 底层三大基石：namespace 隔离、cgroup 限流、UnionFS 分层

> 分类：容器 / Docker | 难度：L2 | 题型：原理题 | 频率：高 | 关键词：**容器=进程**/**namespace**/**cgroups**/**UnionFS**/**镜像层与容器层**
> 原文锚点：第 1~25 段「容器的本质就是 Linux 操作系统里面的进程…通过 namespace 和 cgroups 这两种机制使它可以拥有自己的根文件系统、网络配置、进程空间…cgroups 用于限制和控制进程对系统资源如 CPU 内存磁盘网络的使用…Docker 使用 UnionFS 实现镜像和容器的分层存储」

## 一句话总述
**容器 = 被「隔离视图 + 资源配额 + 分层文件系统」包装过的 Linux 进程**：**namespace** 给进程一份独立的世界观（自己的 PID/网络/挂载点/主机名，隔离「看得见什么」）；**cgroups** 给进程套上资源配额（CPU/内存/IO 限额，隔离「能用多少」）；**UnionFS** 把只读镜像层与可写容器层叠加（隔离「改了什么」）——再加 Dockerfile 构建镜像、Registry 分发、客户端-守护进程（dockerd）架构，构成 Docker 全貌。

## 面试官视角
- 考察意图：区分「会用 docker run」与「懂容器本质」——面试官要听你说出「容器就是进程」这句话，以及三大基石各自解决什么问题。
- 分档：P5 知道容器比虚拟机轻；P6 报得出 namespace/cgroup/UnionFS 三件套与各自职责；P7 能列 namespace 的六种类型、镜像层只读共享+容器层可写的写时复制机制。
- 红旗答案：「容器是轻量级虚拟机」——没有独立内核，本质是进程；把 namespace 和 cgroup 的职责说反（前者管视图隔离、后者管资源配额）。
- 惊艳点：「**虚拟机隔离的是硬件（Hypervisor 虚拟化指令集），容器隔离的是操作系统资源视图——所以容器启动是毫秒级、密度是每机上百个**」 [经验]。

## 主问答
**Q（面试官原话）：** 讲讲 Docker 的底层原理。
**A：**
1. **先立本质：容器是 Linux 进程**。类比集装箱——封装的是**软件运行环境**（应用+依赖），使货物（应用）在任何环境流转都无需重新装配。容器与普通进程的差别在于被三套机制包装，**不是另一种虚拟机** [源码]。
2. **基石①：cgroups（资源配额）**——内核特性，**限制与控制进程组对 CPU、内存、磁盘 IO、网络**等资源的使用量。Docker 通过 cgroups 为容器分配并限制资源上限，保证容器之间**不相互抢资源**——解决「能用多少」 [源码]。
3. **基石②：namespaces（视图隔离）**——内核特性，**隔离进程的视图**：PID（进程号空间）、NET（网络栈）、MNT（文件系统挂载）、UTS（主机名）等，使容器拥有「自己的」根文件系统、网络配置、进程空间甚至用户 ID 空间——容器内 `ps` 看不到宿主机其他进程。解决「看得见什么」 [源码]。
4. **基石③：UnionFS（分层文件系统）**——把多个独立文件系统**叠加**成完整容器文件系统：**镜像由多个只读镜像层组成**（每层对应 Dockerfile 的一条指令）、**镜像层可被多容器共享**（省存储）、容器启动时在镜像层上叠加一个**独占的可写容器层**，运行期文件变化都写在这里——镜像层保持不变，这是「同一镜像起 N 个容器」与「镜像可分发」的基础 [源码]。
5. **架构与配套**：镜像可由 **Dockerfile** 构建或从 **Registry**（Docker Hub/私有仓库）拉取，仓库提供集中存储与分发；Docker 采用**客户端-服务端架构**——`docker` CLI 是客户端，`dockerd` 守护进程负责容器生命周期管理（创建/启动/停止）。四层技术组合（隔离+配额+分层+架构）实现应用的封装、部署与管理 [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 容器的本质是什么？ | 本质 | 被隔离包装的 Linux 进程，不是虚拟机 | P5 停 |
| L2 | namespace 和 cgroup 各管什么？ | 分工 | namespace 管视图隔离，cgroup 管资源配额 | P5 停 |
| L3 | 镜像层和容器层什么关系？ | 分层 | 镜像层只读可共享，容器层可写独占，写时复制 | P6 停 |
| L4 | 为什么容器启动是毫秒级？ | 对比 | 无内核引导，只是 fork 一个带隔离的进程 | P6 停 |
| L5 | 容器里 CPU 超配额会怎样？ | 深挖 | cgroup 限流 throttle 而非杀进程；内存超限则 OOM kill | P7 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Docker 0.9.0 前 | 依赖 LXC；之后自研 libcontainer | 历史演进见 1513-docker-vs-lxc [边界] |
| cgroup v1 | 每控制器独立层级，挂载分散 | 老系统可见多目录 |
| cgroup v2 (现代默认) | 统一层级，cpu.max/memory.max 接口清爽 | 新内核按 v2 答配额路径 |
| Linux only | Docker 依赖内核特性，macOS/Windows 跑在 VM 里 | 「容器是 Linux 进程」的前提 |
| 安全边界 | namespace+cgroup ≠ 强安全隔离 | 共享内核，逃逸风险与 VM 不同级 |

## 关键代码
```go
// 容器内读取自身 cgroup 配额 (K8s 场景判断「有效核数」的正确姿势 [经验])
package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func cpuQuota() (float64, bool) {
	// cgroup v2: /sys/fs/cgroup/cpu.max 形如 "200000 100000" (quota period)
	b, err := os.ReadFile("/sys/fs/cgroup/cpu.max")
	if err != nil {
		return 0, false
	}
	parts := strings.Fields(string(b))
	if parts[0] == "max" {
		return 0, false // 未限额
	}
	quota, _ := strconv.ParseFloat(parts[0], 64)
	period, _ := strconv.ParseFloat(parts[1], 64)
	return quota / period, true // 有效核数 = quota / period
}

func main() {
	if cores, ok := cpuQuota(); ok {
		fmt.Printf("cgroup 有效核数: %.2f\n", cores) // 如 200000/100000 = 2.0
	} else {
		fmt.Println("未设置 CPU 配额")
	}
}
// [经验] 容器内 runtime.NumCPU() 读的是宿主机核数; 配额判断要用 cgroup
```

## 总结与追问预判
一句话记忆：**「容器 = 进程 + namespace（看得见什么）+ cgroup（能用多少）+ UnionFS（改了什么），dockerd 管生命周期」**。Docker 与 LXC 的对比（生命周期/抽象层次/管理/生态）见 `1513-docker-vs-lxc` [边界]；负载诊断中「容器内核数不可信」的教训见 `188-load-diagnosis.deep`。常追问「容器怎么实现根文件系统」——答 mount namespace + pivot_root 切换视图 + UnionFS 提供层叠内容；再追问「镜像层共享怎么做到只读」——答 UnionFS 写时复制（CoW）：修改只读层文件时先复制到容器层再改。

## ⚠️ 原文纠错
1. 术语归一：[经验] 源为语音转写，「saygroups」应为 cgroups，「lemonspace/lemespspace」应为 namespaces，「uniFS/UIFS」应为 UnionFS，「dockdockdockfile」应为 Dockerfile，统一为规范术语。
2. 结构纠错：源口述「第二个就是文件系统」「第三个就是镜像与仓库」编号错乱（实为四大块：隔离性含 cgroup+namespace / 文件系统 / 镜像与仓库 / 客户端-守护进程），本卡已重组为三大基石+架构四层。
3. 补充：源未列 namespace 的具体类型（PID/NET/MNT/UTS/IPC/USER）与写时复制机制，均为高频追问点，本卡深挖卡已补。
