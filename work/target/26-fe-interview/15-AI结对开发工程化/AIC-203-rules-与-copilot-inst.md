---
title: [AIC-203] Cursor rules 与 GitHub Copilot 的 .github/copilot-instructions.md 有什么差异？团队要双 IDE 支持怎么办？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-203：Cursor rules 与 GitHub Copilot 的 .github/copilot-instructions.md 有什么差异？团队要双 IDE 支持怎么办？
**答**：
- Cursor 支持三级匹配（always/glob/agent），copilot-instructions 是单一全局文件，粒度更粗。
- Copilot 新版也支持 .github/instructions/*.instructions.md 的 applyTo glob 模式，粒度接近 Cursor 的 globs。
- 双 IDE 策略：规范写成「单一事实源」（如 docs/standards/*.md），再用脚本生成两家的规则文件，避免双写漂移。
- 差异点还要注意注入时机：Copilot 按文件打开注入，Cursor 支持任务级语义注入。

```javascript
# 单一事实源 → 双 IDE 产物（构建脚本思路）
# docs/standards/*.md → .cursor/rules/*.mdc（front-matter 注入）
#                     → .github/instructions/*.instructions.md（applyTo 注入）
node scripts/sync-rules.js && git diff --exit-code .cursor .github/instructions \
  || echo "规则产物过期：请重新执行 sync-rules（CI 中作为门禁）"
r
```
