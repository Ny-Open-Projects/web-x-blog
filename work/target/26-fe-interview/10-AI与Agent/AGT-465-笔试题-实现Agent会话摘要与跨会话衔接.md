---
title: [AGT-465] 笔试题——实现跨会话衔接（上次会话摘要+未结事项提醒）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-465：手写跨会话衔接：上会话摘要、未结任务、用户可跳过

**需求与边界**：
- 输入：上一会话记录、本次开场；输出：衔接上下文块。
- 边界要求：① 摘要含（做了什么/结论/未结事项）三段；② 未结事项仅提醒不自动接续（用户主导）；③ "新话题"声明则跳过衔接；④ 摘要生成离线异步（不阻塞开场）。

**答**：
```javascript
async function sessionHandoff(prevSession, { summarize, taskBook }) {
  // 1. 离线摘要（上会话结束时已生成，缓存）
  const cached = await cache.get(`summary:${prevSession.id}`);
  const summary = cached ?? await summarize(prevSession, {
    rule: `输出三段：完成事项/关键结论/未结事项。
      未结事项引用任务簿条目 id` });
  if (!cached) await cache.set(`summary:${prevSession.id}`, summary);
  // 2. 未结事项
  const open = summary.openTasks
    ?.map(id => taskBook.get(id)).filter(t => t?.status === 'open') ?? [];
  // 3. 构造衔接块（用户可跳过）
  return {
    inject: {
      type: 'handoff',
      content: `上次会话（${dateOf(prevSession)}）：
        ${summary.done}\n关键结论：${summary.conclusions}`,
      openItems: open.map(t => `${t.what}（${t.who ?? '待定'}）`),
    },
    behavior: {
      mention: `开场提示："上次我们完成了 __，还有 __ 未结，
        要继续吗？"——仅提醒一次`,
      skipIf: (firstMsg) =>            // 新话题声明跳过
        /^(新话题|换个事|另外)/.test(firstMsg),
      rule: '仅提醒不自动接续——用户主导',
    },
  };
}
```

**评分点**:
- 三段摘要（完成/结论/未结）且离线缓存生成（不阻塞开场）。
- 未结事项仅提醒不自动接续（用户主导边界）。
- 新话题声明跳过衔接（不打扰合法切换）。
- 摘要引用任务簿 id 可回溯原文。
