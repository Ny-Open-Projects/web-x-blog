# 017 资源组（CPU 资源管理）

> 分类：MySQL 8.0 新特性/运维 | 难度：L3 | 题型：概念主问 | 频率：低 | 关键词：**RESOURCE GROUP** / **CPU 亲和** / **线程优先级**
> 原文锚点：第 240~267 段「8.0 引入资源组，可管理线程使用的 CPU 资源」

## 一句话总述
MySQL 8.0 引入**资源组（Resource Group）**：把线程绑定到指定 **CPU 核**并设置**线程优先级**，用于隔离重要/次要业务的 CPU 争抢；目前仅支持 CPU 维度。

## 面试官视角
- **考察意图**：是否知道 8.0 的资源隔离能力及其平台限制。
- **P5** 知道 8.0 有资源组。
- **P6** 能说清 CPU 绑定 + 优先级两类参数与语法。
- **P7** 能指出平台差异（Linux 有效）与权限要求。
- **红旗**：说「资源组能限制内存/IO」。
- **惊艳点**：点出 CPU 亲和在 **Linux 才真正生效**，macOS/Windows 上线程优先级会被忽略 `[经验]`。

## 主问答
**Q：MySQL 8.0 的资源组有什么用？**
**A：**
1. **结论**：资源组把线程绑定到指定 **vCPU 核**并设**线程优先级**（用户组 0~19、系统组 -20~0），隔离 CPU 争抢；**目前只支持 CPU**。
2. **机制**：`CREATE RESOURCE GROUP` 定义组（SYSTEM/USER 两类 + vcpu 列表 + 优先级），再用 `SET RESOURCE GROUP ... FOR <thread_id>` 把线程挂上去；可从 `information_schema.resource_groups` 与 `performance_schema.threads` 查线程号。
3. **边界**：仅 CPU 维度，**不能限内存/IO**；CPU 亲和需 Linux（且进程有 CAP_SYS_NICE），macOS/Windows 上优先级无效。
**加分层**：资源组是"隔离"手段，不能替代容量规划；误绑核反而制造热点。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 资源组管啥 | 概念 | CPU 资源 | 换题 |
| L2 | 怎么建/绑定 | 基础 | CREATE/SET 语法 | 判 P5 |
| L3 | 优先级范围 | 原理 | 用户 0~19/系统 -20~0 | 判 P6 |
| L4 | 平台限制 | 判断 | Linux 生效 | 判 P6+ |
| L5 | 生产用过吗 | 实战 | 讲隔离案例 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| MySQL 8.0+ | 资源组自 8.0 引入；8.0.28 起部分行为收敛 | 按「仅 CPU + Linux 生效」答 |

## 关键代码
```sql
-- 建用户资源组：绑定第 0 核、优先级 10
CREATE RESOURCE GROUP rg_report TYPE = USER VCPU = 0 THREAD_PRIORITY = 10;
-- 查线程号后绑定（performance_schema.threads 取 PROCESSLIST_ID）
SET RESOURCE GROUP rg_report FOR 84;
```

## ⚠️ 原文纠错
原视频演示把资源组命名为「爱慕课」并在单核虚拟机上绑定第 0 核——仅为教学演示。生产环境核心不足时绑核会加剧争抢；且 macOS/Windows 上 THREAD_PRIORITY 不生效，答题须说明平台限制 `[经验]`。

## 总结与追问预判
- 资源组 = 8.0 的 CPU 隔离能力，仅 CPU、Linux 有效，别当内存/IO 限制用。
- 下一题：见 010（数据字典）、018（原子 DDL）。
