---
title: 沙箱：执行不可信代码的隔离方案
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, 沙箱, 安全]
---

## 沙箱：执行不可信代码的隔离方案

低代码/工作流平台若开放脚本编辑，就必须隔离不可信代码。分级方案：**进程内 vm 软隔离（超时+配额+审计）→ 容器硬隔离 → 失败自动降级**。未做隔离不得对外开放脚本编辑。

**本项目实例**（自研参考实现）：
- vm 软隔离层（`nodes/sandbox.ts`）：Node vm + 严格模式 IIFE，封掉 `Function/globalThis/global`，静默 console；同步 timeout + 异步 watchdog 双保险；输出 256KB 配额；结果如实标注 `isolation:'vm'`。代码注释原文明确"vm 层不是安全边界"。
- 容器硬隔离层（`nodes/container-sandbox.ts`）：dockerode 起一次性容器——CapDrop ALL / no-new-privileges / 非 root / 只读根 / 禁网 / 128MB 内存 / 0.5 核 / pids 64，容器内再套一层 vm；容器不可用自动回退 vm 是 **fail-open 设计**（降级不拒绝执行）——注意 vm 硬化可被 `data.constructor.constructor` 经典链绕过，工程注释原文自认「vm 不是安全边界」，公网裸暴露即 RCE 面。这两点本身就是好素材。
- 配套审计表 `wf_audit`：记录 codeHash、isolation 类型、outputBytes。

沙箱配置全 env 化（WF_SANDBOX_MODE=vm|container、限额、docker socket 路径）。

出处「scan3 §2-A；scan4 §7」
