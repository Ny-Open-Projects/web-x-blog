---
title: [AGT-228] 子 Agent 的上下文隔离——并行子任务怎么互不污染？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-228：主 Agent 派发并行子任务时，上下文怎么隔离与汇总？

**答**:
- 隔离原则：子 Agent 各自拥有独立上下文，只接收"任务说明书"（目标+必要背景+产出格式），不带主对话全程历史——上下文泄漏会让子任务被无关信息干扰且成本翻倍。
- 汇总协议：子 Agent 返回结构化结果（结论/依据/置信度/未解决项），主 Agent 只把汇总结果写进自己的上下文——子过程的噪声（工具原始输出）不回传。
- 共享事实的传递：多个子任务需要的公共背景，由主 Agent 在派发时显式注入（拷贝进任务书），而不是让子 Agent 自己去查——一次注入换来 N 次重复检索的节省。
- 冲突处理：并行子 Agent 对同一问题给出不同结论时，主 Agent 按置信度+依据质量仲裁（AGT-155 的冲突仲裁），必要时追加一个验证子任务。

```javascript
async function fanOut(main, tasks) {
  const brief = extractBrief(main.context);   // 公共背景一次提取
  const results = await Promise.all(tasks.map(t =>
    runSubAgent({                             // 独立上下文
      system: SUB_ROLE[t.type],
      messages: [{ role: 'user',
        content: `${t.goal}\n背景：${brief}\n
          输出格式：{conclusion, evidence,
          confidence, openIssues}` }],
      tools: t.tools, maxSteps: t.maxSteps })),
  );
  return merge(results);   // 主上下文只进结构化汇总
}
```
