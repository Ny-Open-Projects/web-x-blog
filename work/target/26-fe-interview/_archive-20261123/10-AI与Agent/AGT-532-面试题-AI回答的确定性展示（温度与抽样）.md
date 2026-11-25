---
title: [AGT-532] 产品要求同一问题「重试时给出不同答案」（创意场景）与「完全一致」（计算场景），前端如何呈现与控制？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-532：产品要求同一问题「重试时给出不同答案」（创意场景）与「完全一致」（计算场景），前端如何呈现与控制

**答**：
- 确定性由参数控制：计算/查询类 temperature≈0 且可缓存；创意类给"换一个"按钮（新采样），两套参数模板随任务类型走。
- UI 呈现差异：确定性回答显示"已校验"标识并允许缓存秒答；创意回答显示版本对比（v1/v2 可切换），用户采纳哪版要记录。
- 重试语义分开：确定性场景重试=重新计算（结果应一致，不一致说明上游变了要提示），创意场景重试=重新生成。

```javascript
const TEMPLATES = {
  factual:  { temperature: 0, cacheable: true, retryLabel: '重新计算' },
  creative: { temperature: 0.9, cacheable: false, retryLabel: '换一个' },
};
function RetryButton({ msg, tpl }) {
  const versions = msg.versions;   // 创意场景保留版本
  return <button onClick={async () => {
    const next = await regen(msg, TEMPLATES[msg.kind]);
    if (tpl === TEMPLATES.creative) msg.addVersion(next);  // 版本可切换
    else msg.replace(next);                                // 结果应一致
  }}>{tpl.retryLabel}</button>;
}
```

