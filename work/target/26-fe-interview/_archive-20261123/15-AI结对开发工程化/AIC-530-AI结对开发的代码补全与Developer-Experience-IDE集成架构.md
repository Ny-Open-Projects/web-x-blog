---
title: [AIC-530] AI 补全的 IDE 集成架构
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-530：AI 补全的 IDE 集成架构

**答**:
- AI 补全的 IDE 架构：1) **Language Server Protocol (LSP)** 扩展（AI 补全作为 LSP 的补充——LSP 管类型/跳转，AI 管"下一行写什么"；2) **ghost text 渲染**（AI 建议以灰色文本显示在光标后——Tab 接受、Esc 拒绝——inline suggestion 的 UI 协议；3) **上下文收集**（LSP 的 document Symbol（当前文件的函数/类/导入——RBL-502 上下文裁剪的 IDE 集成）；4) **debounce 与取消**（用户停止打字 200ms 后才触发 AI 补全——打字中的补全会被取消（防抖 RBL-874）；5) **多模型路由**（RBL-526 的 IDE 版：inline → 快模型；chat → 慢模型）。
- IDE 集成的性能约束：1) **延迟要求**（补全延迟 < 300ms（用户感知阈值——超过 300ms 用户开始自己写——AI 补全失去意义）；2) **上下文收集的成本**（LSP 符号查询 = 10ms + AI 调用 = 200ms——总延迟 = 210ms < 300ms 阈值）；3) **取消机制**（用户继续打字 → 取消进行中的 AI 请求（AbortController RBL-640）——取消的成本 = 已发 tokens 的浪费（计费但不使用）。
- 追问钩子：为什么「AI 补全的延迟要求 <300ms」是硬约束？——用户打字速度 ≈ 3 字/秒 = 每字 333ms——AI 补全延迟 > 300ms = 用户已经打了下一个字（补全过时了——不匹配当前光标位置）；「300ms 是补全的生死线」：超过 = 用户放弃等待自己写（AI 从 helper 变成 burden）；延迟优化：上下文裁剪（RBL-502 减少 input tokens）+ 便宜快模型（RBL-526 降低推理时间）+ debounce（避免不必要的调用）。

```typescript
// AI 补全的 IDE 集成（VSCode extension 概念）
import * as vscode from 'vscode';
export function registerAICompletion(context: vscode.ExtensionContext) {
  const provider = vscode.languages.registerInlineCompletionItemProvider(
    [{ scheme: 'file', language: 'typescript' }],
    {
      async provideInlineCompletionItems(document, position, context, token) {
        // 1) 防抖：检查是否打字中
        if (isTyping()) return;                            // 打字中取消
        // 2) 上下文收集（LSP + 文件）
        const symbols = await getDocumentSymbols(document);
        const imports = extractImports(document.getText());
        // 3) AI 调用（带取消）
        const result = await callAI({
          code: document.getText(),
          position: document.offsetAt(position),
          symbols, imports,
          signal: token,                                    // VSCode 取消信号
        });
        if (token.isCancellationRequested) return;          // 取消检查
        // 4) 返回建议
        return [new vscode.InlineCompletionItem(
          result.completion,
          new vscode.Range(position, position),
        )];
      },
    }
  );
  context.subscriptions.push(provider);
}
// 防抖实现
let typingTimer: NodeJS.Timeout;
function isTyping() {
  // 200ms 内有输入 → typing
  return Date.now() - lastInputTime < 200;
}
```
