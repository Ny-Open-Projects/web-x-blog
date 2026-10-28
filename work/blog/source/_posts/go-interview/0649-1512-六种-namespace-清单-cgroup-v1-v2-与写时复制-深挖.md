---
disableNunjucks: true
title: "1512 六种 namespace 清单、cgroup v1/v2 与写时复制 深挖"
date: 2026-10-10 08:53:52
categories: [Go面试题集]
tags: [Go面试题集]
---

> 覆盖源 15-12 全文：namespace 六类型的逐个拆解与「容器里看到的世界」、cgroup v1/v2 的结构差异与 K8s 的配额换算、UnionFS 写时复制的完整链路（镜像层→容器层→删除文件的白屏文件）、与 LXC/libcontainer 的关系定位。主卡已给三大基石与配额实测代码，本附录做机制细节四层深挖。

## 思路与架构

```text
一个容器进程被包装的全过程
├─ clone(CLONE_NEWPID|CLONE_NEWNET|CLONE_NEWNS|...)
│   ├─ PID ns: 自己的 1 号进程
│   ├─ NET ns: 独立网卡/veth/iptables
│   ├─ MNT ns: pivot_root 切换根 -> UnionFS 挂载视图
│   ├─ UTS ns: 自己的 hostname
│   ├─ IPC ns: 独立 System V/POSIX IPC
│   └─ USER ns: 容器内 root ≠ 宿主 root (uid 映射)
├─ cgroup 移动: echo $pid > /sys/fs/cgroup/.../cgroup.procs
│   └─ v2: cpu.max / memory.max / io.max 统一层级
└─ UnionFS 挂载: 镜像只读层(叠) + 容器可写层
    └─ CoW: 改只读层文件 = 先复制到容器层再改; 删除 = 白屏文件遮蔽
```

## 方案取舍
- **六种 namespace 的分工表**：**PID**（进程号空间——容器内 PID 从 1 重新计数，看不到宿主进程）、**NET**（独立网络栈——网卡、路由表、iptables、端口空间全独立，veth 成对网卡把容器接入宿主网桥）、**MNT**（挂载点——配合 pivot_root 切根文件系统，是「独立根文件系统」的实现者）、**UTS**（主机名/域名）、**IPC**（System V IPC 与 POSIX 消息队列隔离）、**USER**（UID/GID 映射——容器内 root 映射为宿主普通用户，安全边界增强）。**「自己的用户 ID 空间」这句原文对应 USER ns，不是 cgroup**——概念易混点 [源码]。
- **cgroup v1 → v2 的结构变化**：v1 每个资源控制器（cpu/memory/io/pids…）**独立层级树**，一个容器要在多棵树各挂一次，控制器间约束易冲突；v2 **统一单层级**，所有控制器挂同一棵树，接口统一成 `cpu.max`（"$quota $period"）、`memory.max`、`io.max` 等——**K8s 的 limits.cpu=2 的换算**即 cpu.max 写 "200000 100000"（2 核）。运行时行为差异要记：CPU 超配额是**被节流（throttle，进程还在但被限速）**，内存超配额是 **OOM kill（直接杀）**——排查容器「变慢 vs 被杀」先分清是 cpu.max 还是 memory.max 触发 [经验]。
- **UnionFS 写时复制的完整链路**：读文件——从上往下找层（容器层→镜像层），找到即返回；**写文件**——若在只读镜像层，先把该文件**整份复制到容器层**再修改（CoW），之后读写都落容器层；**删文件**——在容器层放一个 **whiteout 白屏文件**遮蔽镜像层同名文件（镜像层本身永不被改）；新建文件——直接落容器层。推论：① 同一镜像起 N 个容器共享全部只读层，存储省 N-1 倍；② **高频写大文件是 CoW 恶劣场景**（首次写触发整份复制），数据库类应用把数据目录挂 volume 就是这个原因 [经验]。
- **与 LXC/libcontainer 的关系一句话**：容器机制（ns+cgroup+UnionFS）是**内核能力**，LXC 是早期把内核能力包成用户工具的实现；Docker 初期借道 LXC，0.9.0 起自研 **libcontainer**（后捐为 runC）直接操作 clone/cgroup——从「借壳」到「直连内核」，这正是 `1513-docker-vs-lxc` 差异对比中「抽象层次与管理方式」两条的技术根源 [边界]。
- **安全边界的清醒认知**：namespace 隔离的是**视图**，不是硬件——所有容器**共享宿主内核**：内核漏洞（如脏管道 CVE-2022-0847）对所有容器一视同仁；USER ns + seccomp + capabilities 收紧后风险可控，但与 VM 的硬件级隔离不是一个安全等级。面试里「容器和虚拟机谁更安全」的标准答案：**VM 隔离更强，容器更轻更快，安全敏感混部需补 seccomp/根less/用户 ns 加固** [经验]。

## 答题技巧
- 开口先立「容器=进程」再拆三基石，最后补「vs 虚拟机」——从本质到机制到对比的三段式 [源码]。
- 分工别说反：**namespace 管「看得见什么」，cgroup 管「能用多少」**——一错一档 [经验]。
- 被问「容器里 ps 为什么看不到宿主进程」→ PID namespace：进程号空间独立，容器内自己是 1 号 [经验]。
- 被问「容器变慢和被杀分别查什么」→ cpu.max 节流 vs memory.max OOM，配 cgroup v2 路径 [经验]。
- 主动边界到 `1513-docker-vs-lxc`（LXC 对比）、`188-load-diagnosis.deep`（宿主机视图误判）、`187-process-states`（进程本质），构成容器与进程专题 [边界]。

## 细节与核心 API

**六种 namespace（容器=进程，clone 包装）：**

```text
PID  进程号空间(容器内 PID 从 1 起，看不到宿主进程)
NET  独立网络栈(网卡/路由/iptables/端口，veth 接入宿主网桥)
MNT  pivot_root 切根，独立挂载视图
UTS  独立 hostname
IPC  独立 System V/POSIX IPC
USER UID/GID 映射(容器内 root 映射宿主普通用户)
```

**容器变慢 vs 被杀（cgroup v2 排查）：**

```bash
cat /sys/fs/cgroup/kubepods/.../cpu.max      # "200000 100000" = limits.cpu=2，超则 throttle
cat /sys/fs/cgroup/kubepods/.../memory.max  # 超则 OOM kill（直接杀）
```

**UnionFS 写时复制：读从上往下找层；写=复制到容器层再改（CoW，高频写大文件恶劣）；删=whiteout 白屏遮蔽；新建落容器层。同镜像 N 容器共享只读层省 N-1 倍存储。**
