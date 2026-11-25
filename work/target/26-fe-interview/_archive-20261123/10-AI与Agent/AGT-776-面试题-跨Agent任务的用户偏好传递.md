---
title: [AGT-776] 主 Agent 派任务给子 Agent 时，用户偏好如何传递（全量画像还是按需摘要）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-776：主 Agent 派任务给子 Agent 时，用户偏好如何传递（全量画像还是按需摘要）

**答**：
- 传递「任务相关偏好摘要」而非全量画像：主 Agent 根据任务类型筛画像字段（编码任务带技术栈+风格，写文档任务带语气+格式），压缩成偏好前缀注入子 Agent——全量画像既贵又稀释注意力。
- 偏好传递带优先级标记：用户显式配置 > 蒸馏偏好，子 Agent 收到冲突字段时采信显式配置并在结果里说明取舍。
- 回写通道：子 Agent 执行中发现新偏好信号（用户对产出反复修改），不直接写全局画像，回传主 Agent 由统一蒸馏管线处理（单一写入原则）。

```javascript
async function dispatchTask(task) {
  const pref = filterProfile(profile, task.kind);   // 按任务筛字段
  const sub = await spawnAgent(task, {
    prefix: `用户偏好（显式配置优先）：${render(pref)}`,
  });
  sub.on('preference-signal', (sig) =>
    distillQueue.add(sig));                          // 回传统一蒸馏
  return sub.result;
}
```

