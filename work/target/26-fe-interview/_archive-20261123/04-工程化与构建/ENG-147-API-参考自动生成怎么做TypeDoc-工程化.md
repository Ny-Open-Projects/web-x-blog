---
title: [ENG-147] API 参考自动生成怎么做？TypeDoc 工程化要点？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-147：API 参考自动生成怎么做？TypeDoc 工程化要点？
**答**：
- 工具库与 SDK 的 API 文档用 TypeDoc 从代码生成：导出符号、泛型、抛错说明全部来自实现，不存在文档过期。
- typedoc-plugin-markdown 输出 md 可直接挂进 VitePress 或 GitHub Wiki，与手写指南融合。
- 注释规范配套：@param @returns @throws @example，CI 用 typedoc 校验未导出与未注释项阻断。
- 版本归档：每个 npm 版本对应一版 API 文档路径（/api/v2/），保证参考与所用版本一致。

```bash
# TypeDoc 生成 API 参考并集成进文档站
# 1. 生成 markdown 版 API 文档
npx typedoc src/index.ts \
  --plugin typedoc-plugin-markdown \
  --out docs/api \
  --excludePrivate --excludeInternal \
  --readme none

# 2. CI 校验 警告升级为错误 未导出符号阻断
npx typedoc src/index.ts --validation.notExported --treatWarningsAsErrors

# 3. 发版时按版本归档
V=$(node -p "require('./package.json').version")
mkdir -p docs-site/api && mv docs/api "docs-site/api/v${V}"
```

## 第二十九章 依赖治理（ENG-148 ~ ENG-153）
