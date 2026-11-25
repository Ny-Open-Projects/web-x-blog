---
title: [TST-921] 快照在 A 机器通过、B 机器失败，如何消除环境噪声保证「可重现」？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-921：快照在 A 机器通过、B 机器失败，如何消除环境噪声保证「可重现」？
**答**：
- 结论：快照必须「与运行环境无关」——统一时区、语言、随机数种子、字体与像素比，任何环境相关值都要归一化或剔除。
- 常见噪声源：时间戳、随机 ID、locale 格式（日期/千分位）、绝对路径、端口、字体渲染差异。
- 做法：序列化前用 normalize 钩子（replace 时间戳为 <TIME>、ID 为 <ID>），并把语言/时区固定进测试配置。
- 追问钩子：同一份组件快照在 CI（Linux）和本地（macOS）因字体不同产生 diff，你怎么在不换字体的前提下消除它？

```javascript
// jest/vitest 配置固定环境
export default { test: { environmentOptions: { locale: 'zh-CN', timezone: 'Asia/Shanghai' } } };

// 序列化前归一化：抹掉环境相关值
function normalizeForSnapshot(value) {
  return JSON.parse(JSON.stringify(value, (k, v) => {
    if (typeof v === 'string') {
      if (/^\d{4}-\d{2}-\d{2}T/.test(v)) return '<ISO_TIME>';
      if (/^[a-f0-9]{8}-[a-f0-9]{4}/i.test(v)) return '<UUID>';
      if (v.includes('/Users/') || v.includes('/home/')) return '<ABS_PATH>';
    }
    return v;
  }));
}
expect(normalizeForSnapshot(order)).toMatchSnapshot();
```
