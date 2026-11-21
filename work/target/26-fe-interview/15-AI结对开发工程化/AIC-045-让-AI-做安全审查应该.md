---
title: [AIC-045] 让 AI 做安全审查，应该检查哪些前端特有的安全问题？它的盲区在哪？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-045：让 AI 做安全审查，应该检查哪些前端特有的安全问题？它的盲区在哪？
**答**：
- 前端特有清单：XSS（dangerouslySetInnerHTML/v-html 的数据来源）、敏感信息硬编码（密钥、内网 URL、测试账号）、越权渲染（仅靠前端隐藏的权限控制）、不安全的 postMessage、开放重定向、依赖的 prototype 污染。
- AI 擅长的：模式匹配类问题（「这里把用户输入塞进了 innerHTML」），因为特征明显且在 diff 附近。
- 盲区一：跨文件的数据流——污染源在 A 文件、汇聚点在 B 文件，AI 若只见单文件就漏报，必须喂调用链。
- 盲区二：运行时/配置层——CSP 头、CORS 配置、构建产物的 sourcemap 泄漏、CI 变量注入，这些不在代码 diff 里。
- 追问钩子：AI 安审定位是「人力放大器」，不能替代 SAST/依赖扫描等确定性工具，正确关系是互补而非替代。

```javascript
// 前端安审清单 prompt（模式匹配部分）
const secChecklist = [
  'dangerouslySetInnerHTML / v-html 的内容是否含用户可控数据',
  '硬编码的密钥、token、内网域名',
  '前端隐藏实现权限（应后端校验的接口级权限）',
  'window.postMessage 未校验 origin',
  '重定向目标来自 URL 参数且未白名单',
].map((s, i) => `${i + 1}. ${s}`).join('\n');
```
