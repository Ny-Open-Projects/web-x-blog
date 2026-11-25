---
title: [1092] 「用户让 Agent 做的事」和「Agent 有权做的事」怎么绑定
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 越权]
type: 面试题
---

## 1092：「用户让 Agent 做的事」和「Agent 有权做的事」怎么绑定

**答**：
- 核心原则：Agent 动作权限 ≤ 用户权限。Agent 以「用户身份的代理令牌」执行（代执行模式），令牌的 scope 由用户实际权限推导，用户无权看的资源 Agent 也无权碰。
- 反模式警示：「Agent 用自己的超级账号干活」——用户 A 让 Agent 读用户 B 的数据就是越权事故；正确做法是每会话签发「用户限定令牌」。
- 间接越权：Agent A 的输出被 Agent B 消费时，B 获得的信息不能超过「A 服务的用户」的权限——输出标注权限上下文，跨用户传递即拒绝。
- 追问钩子：管理员委托 Agent 批量操作怎么办？——显式授权提升流程：管理员动作走「临时提升令牌 + 事后审计」，不改变默认最小权限。

```ts
async function agentAct(user, action) {
  const scope = deriveFrom(user.permissions, action.required);  // ≤ 用户权限
  if (!scope.ok) return refuse('insufficient user permission');
  const token = await issue({ subject: user.id, scope, ttl: 300 });
  return executor.run(action, { token });                        // 代执行
}
```
