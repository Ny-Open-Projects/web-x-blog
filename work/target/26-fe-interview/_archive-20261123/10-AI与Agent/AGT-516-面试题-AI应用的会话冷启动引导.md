---
title: [AGT-516] 新用户首次进入 AI 对话页，冷启动引导怎么设计才能降低空页面流失？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-516：新用户首次进入 AI 对话页，冷启动引导怎么设计才能降低空页面流失

**答**：
- 空会话是最大流失点：用「场景化示例卡」代替空白输入框，示例按用户角色/来源动态推荐（来自运营配置+行为画像），点击即填充输入框并可修改。
- 引导要教「能力边界」：一句话告诉用户能做什么、不能做什么，用可点击的示例表达，不用长文字说明。
- 首轮回复质量决定留存：首轮请求走保底策略（更强模型/更全系统提示），并可配欢迎语模板。

```javascript
function getSuggestionCards(user) {
  const pool = config.cardsByRole[user.role] ?? config.defaultCards;
  return rankByProfile(pool, user.profile)  // 按画像排序
    .slice(0, 3).map(c => ({ ...c, onClick: () => {
      input.setParts(c.draftParts);          // 点击填充而非直接发送，保留修改权
      input.focus();
    } }));
}
```

