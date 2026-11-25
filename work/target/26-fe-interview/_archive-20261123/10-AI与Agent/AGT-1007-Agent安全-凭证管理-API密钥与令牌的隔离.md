---
title: [1007] Agent 系统里的 API 密钥怎么管理才不会泄露
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 凭证]
type: 面试题
---

## 1007：Agent 系统里的 API 密钥怎么管理才不会泄露

**答**：
- 密钥不进模型上下文：Agent 代码持有密钥，模型只产生「动作意图」，由宿主代码注入密钥执行——prompt 里出现密钥 = 迟早泄露（日志、缓存、trace 都会带出去）。
- 最小权限令牌：每个 Agent 会话签发短期 scoped token（限定工具范围 + TTL），而不是共享长期 master key；会话结束令牌作废。
- 出口审查：外发请求网关统一检查目标域名白名单 + 请求体不含凭证模式（正则扫 AK/SK 格式），防止「密钥随答案外流」。
- 追问钩子：第三方工具需要凭证怎么办？——凭证代理模式：工具拿到的是「代执行凭证」只能调指定 API，拿不到原始密钥。

```ts
// 动作意图与凭证分离
const intent = await llm('生成调用意图(JSON)：{ api, params }');   // 模型不接触密钥
const token = await issueToken({ agent: ctx.agentId, scope: intent.api, ttl: 300 });
return gateway.exec(intent, { token });   // 宿主注入凭证执行
// 出口审查：请求体出现 AK/SK 模式直接拦截
if (AK_PATTERN.test(JSON.stringify(intent))) return block('credential leak');
```

