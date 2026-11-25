---
title: [946] 一个 Agent 被间接提示注入后，污染会沿协作链传播吗
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 安全]
type: 面试题
---

## 946：一个 Agent 被间接提示注入后，污染会沿协作链传播吗

**答**：
- 会，而且是多 Agent 特有的放大器：检索 Agent 把投毒网页摘要传给写作 Agent，写作 Agent 的产出又被评审 Agent 当「待审材料」——污染逐级洗白，每级看起来都正常。
- 防传播三条：产物「来源标注」强制透传（外部内容及其衍生物永远带 untrusted 标记）；高危 Agent（执行类）只接受带可信来源的输入；跨信任边界传递必须过过滤器。
- 实践：编排器维护信任等级（internal > user > external），Agent 产物的信任等级取「输入最低值」，只降不升。
- 追问钩子：怎么检测已经发生的传播？——对最终产物做「内容溯源」，发现结论性语句的最早来源是 external 且绕过了过滤链，即为疑似注入路径。

```ts
const trust = { internal: 3, user: 2, external: 1 };
function propagate(msg, inputs) {
  const minTrust = Math.min(msg.trust, ...inputs.map(i => i.trust));
  // 信任等级只降不升：外部内容衍生的产物永远是 external
  return { ...msg, trust: minTrust, derivedFrom: inputs.map(i => i.id) };
}
if (nextAgent.minTrustRequired > msg.trust) {
  return sanitize(msg);     // 跨信任边界必须过滤
}
```

