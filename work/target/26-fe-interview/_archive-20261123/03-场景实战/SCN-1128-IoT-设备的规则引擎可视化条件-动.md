---
title: [SCN-1128] IoT 设备的规则引擎可视化（条件-动作流）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1128：IoT 设备的规则引擎可视化（条件-动作流）

**答**：
- 可视化：规则流（条件节点/动作节点/分支），拖拽编辑（简化为表单+预览优先）。
- 校验：规则循环检测（A 触发 B，B 触发 A 死循环）。
- 灰度：规则启用灰度（先影响部分设备验证）。

```javascript
// 规则循环检测
function detectRuleLoop(rules) {
  const graph = new Map(rules.map(r => [r.trigger.deviceId, r.action.deviceId]));
  for (const start of graph.keys()) {
    let cur = start;
    for (let i = 0; i < rules.length; i++) {
      cur = graph.get(cur);
      if (!cur) break;
      if (cur === start) return { loop: true, at: start };
    }
  }
  return { loop: false };
}
```
