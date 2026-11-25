---
title: [AGT-513] 模型/网络/审核/配额等十几种错误，前端如何建立统一的错误文案与恢复动作映射？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-513：模型/网络/审核/配额等十几种错误，前端如何建立统一的错误文案与恢复动作映射

**答**：
- 建立错误码→（用户文案、是否可重试、恢复动作、埋点分类）的映射表，UI 层只查表不写 if-else，新增错误只改表。
- 文案说人话并给下一步：不说 "500 Internal Error"，说"服务繁忙，已为你保留草稿，点击重试"；可重试的按钮直接内联在错误卡片上。
- 重试要带策略（指数退避、最多 N 次），并把已生成内容保留为"半成品"可查看，避免重试后前功尽弃。

```javascript
const ERROR_MAP = {
  RATE_LIMITED:  { text: '请求太频繁了，{s}秒后可重试', retry: true },
  MODERATION:    { text: '该内容未通过安全审核，换个表述试试', retry: false },
  CTX_OVERFLOW:  { text: '对话太长啦，压缩历史后再试', action: 'compact' },
  MODEL_TIMEOUT: { text: '生成超时，可重试或切换到更快的模型', retry: true, alt: 'switchFast' },
};
function renderError(err) {
  const cfg = ERROR_MAP[err.code] ?? { text: '出错了，请重试', retry: true };
  ui.errorCard({ ...cfg, text: cfg.text.replace('{s}', err.retryAfter),
    keepPartial: err.partial });   // 保留半成品
}
```

