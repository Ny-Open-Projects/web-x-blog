---
title: [AIC-281] AI 门禁如何检测「异常行为」——比如测试突然全绿但断言被削弱？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-281：AI 门禁如何检测「异常行为」——比如测试突然全绿但断言被削弱？
**答**：
- diff 级监控：对测试文件的修改做强度校验——删除断言、放宽期望值、跳过用例需人工确认。
- 趋势监控：断言密度（断言数/用例数）、覆盖率、变异分数周环比，骤降即告警。
- 行为指纹：关键路径的 golden test（黄金用例）不可被 AI 修改，只能人改。
- 告警分级：疑似规避行为先评论提醒，反复出现升级为阻塞 + 通知 owner。

```javascript
function testStrengthDiff(oldT: string, newT: string) {
  const cnt = (s: string) => (s.match(/expect\(/g) || []).length;
  const removed = cnt(oldT) - cnt(newT);
  if (removed > 0 || /it\.skip|test\.skip/.test(newT) && !/it\.skip|test\.skip/.test(oldT))
    return { suspect: 'weakened-tests', removed, humanConfirm: true };
  return { suspect: null };
}
r
```
