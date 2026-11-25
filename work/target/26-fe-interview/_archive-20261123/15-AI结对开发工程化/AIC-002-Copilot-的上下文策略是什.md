---
title: [AIC-002] GitHub Copilot 补全的上下文策略是什么？为什么它有时「不知道」同仓库其他文件的代码？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-002：GitHub Copilot 补全的上下文策略是什么？为什么它有时「不知道」同仓库其他文件的代码？
**答**：
- Copilot 补全主要依赖当前文件 + 邻近打开的 tab（Neighboring Tabs）+ 路径相关文件，窗口有限，不是全仓库检索。
- 「不知道」的根因：目标文件与被引用文件不在上下文窗口内，模型只能按 import 名猜测签名，导致参数错、导出不存在等幻觉。
- 补救手段：先打开并聚焦相关文件（让它们进入 tab 上下文）、在注释或 Chat 里 `#file` 显式引用、把关键类型定义放近处。
- Copilot Chat 场景有额外检索（workspace 搜索），但补全（inline completion）基本只有局部窗口，两者上下文策略不同。
- 追问钩子：上下文越小越要「先声明后使用」，比如让 AI 先生成 types 文件再生成实现。

```typescript
// 反面：utils/format.ts 未打开，Copilot 只能猜签名
import { formatPrice } from '@/utils/format'; // 可能猜错参数顺序

// 正面：把关键签名以注释「喂」给模型，或先让 AI 生成该文件
/**
 * formatPrice(cents: number, currency: 'CNY' | 'USD'): string
 * 输入 19900、'CNY' → '¥199.00'
 */
export function priceCell(cents: number, currency: 'CNY' | 'USD') {
  return formatPrice(cents, currency);
}
```
