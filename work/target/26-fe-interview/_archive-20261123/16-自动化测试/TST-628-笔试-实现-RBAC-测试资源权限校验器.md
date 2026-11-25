---
title: [TST-628] 笔试：实现 RBAC 测试资源权限校验器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-628：笔试：实现 RBAC 测试资源权限校验器

**题目**：实现 authorize(subject, policy)。subject={role,team,env,action}；policy={roles:{role:[权限]},grants:[{team,env,actions}]}。权限与 env 支持 '*' 通配，返回 {ok,why?}。

**答**：
- 角色权限支持通配符 *。
- 资源作用域按 team/env 匹配，支持 env='*' 通配。
- 给出明确的拒绝原因，便于排查。

```javascript
function authorize({ role, team, env, action }, { roles, grants }) {
  const rolePerms = roles[role] || [];
  if (!rolePerms.some(p => p === '*' || p === action))
    return { ok: false, why: `角色 ${role} 无 ${action} 权限` };
  const hit = grants.find(g => g.team === team &&
    (g.env === '*' || g.env === env) &&
    (g.actions || []).some(a => a === '*' || a === action));
  return hit ? { ok: true } : { ok: false, why: `${team}/${env} 未授权 ${action}` };
}
const roles = { dev: ['run:test'], admin: ['*'] };
const grants = [{ team: 'pay', env: 'staging', actions: ['run:test'] }];
console.log(authorize({ role: 'dev', team: 'pay', env: 'staging',
  action: 'run:test' }, { roles, grants }).ok); // true
```

**评分点**：
- 角色权限通配符正确
- team/env 作用域匹配准确
- 拒绝原因可读可排查
- 默认拒绝（最小权限）
