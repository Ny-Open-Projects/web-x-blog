---
title: [ENG-140] 包的弃用与迁移怎么做？deprecate 与 codemod 怎么联动？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-140：包的弃用与迁移怎么做？deprecate 与 codemod 怎么联动？
**答**：
- 弃用不是删除：npm deprecate 给旧版本打消息，用户 install 时即可看到迁移指引。
- 弃用消息要可执行：写明替代 API 与迁移文档链接，配合 ESLint deprecated 规则在 IDE 直接标出调用点。
- 大规模调用点迁移配 codemod：jscodeshift 一次性改写，比人工 grep 可靠，可进 CI 全仓执行。
- 节奏：deprecate → 观察调用量下降 → 主版本真正移除，中间至少留两个版本周期缓冲。

```bash
# 1. 弃用旧版本并给出可执行指引
npm deprecate @corp/legacy-cache@^1.0.0 "已废弃 请迁移到 @corp/http-cache v3 迁移文档 https://docs.corp.com/migrate-cache"

# 2. codemod 全仓迁移调用点 转换器见 codemods/legacy-cache-to-v3.ts
npx jscodeshift -t ./codemods/legacy-cache-to-v3.ts src/ --extensions=ts,tsx

# 3. 验证无残留引用
grep -rn "legacy-cache" src/ && echo "存在残留引用" || echo "import 迁移完成"
grep -rn "legacyGet" src/ | wc -l        # 旧 API 调用点应为 0
```
