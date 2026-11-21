---
title: [R19-294] RSC 架构下文件上传怎么做（Action 直收 FormData 的限制）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-294：RSC 架构下文件上传怎么做？
**答**：
- 小文件：form action 直接收 File（Server Action 支持 File 类型，Next 默认 body 大小限制 1MB，可配 serverActions.bodySizeLimit）。
- 大文件：不要过 action——前端分片直传对象存储（预签名 URL），action 只负责「创建上传会话 + 确认完成 + 入库」。
- 进度：action 上传拿不到进度事件，直传方案（XMLHttpRequest/fetch 流）才能上报进度。
- 安全：服务端校验 MIME/魔数/大小，不信任前端限制。
- 面试表达：「action 管协议与元数据，对象存储管字节流」是上传的标准分工。
