---
title: [TST-526] 笔试：笔试：flaky 用例自动隔离与复活机制
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-526：笔试：笔试：flaky 用例自动隔离与复活机制

**题目**：实现 FlakyManager，管理用例的隔离状态。接口：record(name, passed) 记录一次执行结果；isQuarantined(name) 查询是否隔离；revive(name) 手动复活；autoReview(now) 自动处理。规则：① 最近 10 次记录中失败率 > 0.3 则自动隔离；② 被隔离用例若手动 revive 后连续 5 次通过则稳定复活；③ 隔离超过 7 天未修复则升级告警（返回需告警列表）。要求给出完整可运行实现。

**答**：
- 结论：用滑动窗口记录结果，按失败率判定隔离；复活用「连续通过计数」；告警用「隔离时长」。
- 实现要点：每个用例维护 recent 数组（限长 10）与 quarantinedAt、streak；record 更新窗口并重算隔离/复活；autoReview 扫描超时项。
- 追问钩子：为什么用滑动窗口而非全历史？——近期行为更能反映当前稳定性，旧失败不应永久拖累已修复的用例。

```javascript
class FlakyManager {
  constructor() { this.cases = new Map(); this.WIN = 10; this.TH = 0.3; }
  #state(name) {
    if (!this.cases.has(name)) this.cases.set(name,
      { recent: [], quarantined: false, quarantinedAt: 0, streak: 0 });
    return this.cases.get(name);
  }
  record(name, passed) {
    const s = this.#state(name);
    s.recent.push(passed); if (s.recent.length > this.WIN) s.recent.shift();
    const failRate = s.recent.filter(x => !x).length / s.recent.length;
    if (failRate > this.TH && !s.quarantined) {
      s.quarantined = true; s.quarantinedAt = Date.now(); s.streak = 0;
    }
    if (s.recent.length >= 5 && s.recent.slice(-5).every(Boolean)) s.streak = 5;
    if (s.streak >= 5 && s.quarantined) { s.quarantined = false; s.streak = 0; }
    return s.quarantined;
  }
  isQuarantined(name) { return this.#state(name).quarantined; }
  revive(name) { const s = this.#state(name); s.quarantined = false; s.streak = 0; }
  autoReview(now = Date.now(), ttl = 7 * 86400000) {
    return [...this.cases.entries()]
      .filter(([, s]) => s.quarantined && now - s.quarantinedAt > ttl)
      .map(([name]) => name);
  }
}
```

**评分点**：
- 滑动窗口 WIN=10 与失败率阈值 TH=0.3 判定隔离正确。
- 复活需连续 5 次通过（streak），逻辑清晰。
- 隔离超过 7 天进入告警列表（autoReview）。
- 状态封装完整、边界（首次记录、窗口未满）不出错。
