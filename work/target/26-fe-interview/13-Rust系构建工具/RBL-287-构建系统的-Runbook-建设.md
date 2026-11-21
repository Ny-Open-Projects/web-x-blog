---
title: [RBL-287] 构建系统的 Runbook 怎么建设
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-287：构建系统的 Runbook 怎么建设

**答**:
- 条目结构：症状（用户看到什么）→ 快速诊断命令（copy-paste 可用）→ 处置步骤（分「止血」与「根治」）→ 升级路径（谁来看）——值班同学 3 分钟内能行动
- 高频条目：缓存异常（命中率骤降排查）、构建挂死（超时杀进程+重跑）、磁盘满（runner 清理）、工具升级回滚、平台二进制缺包
- 维护机制：每次事故复盘更新对应条目（Runbook 是活的）；季度审计（过期条目清理，链接失效检测）——失效 Runbook 比没有更糟
- 自动化嵌入：Runbook 步骤脚本化（`./scripts/diagnose-cache.sh`），人只做判断不做复制粘贴

```markdown
## 症状：CI 缓存命中率 < 30%
诊断：./scripts/diagnose-cache.sh --last-50
  → 输出 miss 原因分布（fingerprint/version/first）
止血：fingerprint 占比高 → 检查最近合并的配置变更
根治：修复后重放 10 次构建验证命中率回升
升级：>2h 未恢复 → @构建平台值班
```
