---
title: [TST-734] 平台如何管理安全测试用例的敏感 payload 库（版本与隔离）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-734：平台如何管理安全测试用例的敏感 payload 库（版本与隔离）

**答**：
- 结论：payload 库含真实攻击载荷，必须「版本化 + 分级隔离 + 审计」，不能直接散落在用例代码里。
- 按敏感度分级：公开 payload（低危）全员可用，高危 payload 仅授权团队可见，运行时从密钥服务动态拉取。
- 全库版本化，用例引用固定版本，避免库升级导致用例行为漂移；每次取用留审计日志。
- 追问钩子：高危 payload 泄露到公开代码仓库，平台如何做应急与溯源？

```javascript
// payload 库版本化按级取用
function getPayload(lib, name, level, acl) {
  const item = lib[name];
  if (!item) throw new Error('payload 不存在');
  if (item.level === 'high' && !acl.includes('security-team')) {
    return { ok: false, reason: '无高危 payload 权限' };
  }
  return { ok: true, value: item.versions[item.pinned], version: item.pinned };
}
console.log(getPayload(
  { xss: { level: 'low', pinned: 'v2', versions: { v1: '<img>', v2: '<svg>' } } },
  'xss', 'low', ['dev']
));
```
