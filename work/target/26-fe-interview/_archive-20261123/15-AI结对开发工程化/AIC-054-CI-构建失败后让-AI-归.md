---
title: [AIC-054] CI 构建失败后让 AI「归因」的做法是什么？归因机器人的输出应该长什么样？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-054：CI 构建失败后让 AI「归因」的做法是什么？归因机器人的输出应该长什么样？
**答**：
- 做法：把失败日志（截取关键段）+ 本次 PR diff + 相关提交信息喂给模型，让它输出「失败类型、最可疑的改动、修复建议」。
- 输出结构固定：分类（编译错/测试挂/lint/环境问题）+ 可疑点（file:line + 理由）+ 建议动作（一行命令或一段代码）。
- 预处理很重要：日志要裁剪——只保留首个错误堆栈 + 少量上下文，完整万行日志既贵又稀释注意力。
- 模型常犯的错：把环境性失败（网络超时、flaky test）归因给代码改动，要在 prompt 里教它「先判断是否 flaky」。
- 追问钩子：归因评论末尾加「是否帮你重试」按钮自动化掉 flaky 场景，避免人肉 rerun。

```javascript
// 日志归因：裁剪 → 归因 → 结构化输出
function trimLog(log, maxLines = 80) {
  const lines = log.split('\n');
  const firstErr = lines.findIndex(l => /error|fail/i.test(l));
  const start = Math.max(0, firstErr - 10);
  return lines.slice(start, start + maxLines).join('\n');
}
const prompt = `
失败日志：\n${trimLog(log)}\n
PR 改动摘要：${diffStat}
请输出 JSON：{category: "compile|test|lint|env|flaky", suspect: {file, line, why}, fix, isFlaky: boolean}
优先判断是否 flaky/环境问题，再归因代码改动。`;
```
