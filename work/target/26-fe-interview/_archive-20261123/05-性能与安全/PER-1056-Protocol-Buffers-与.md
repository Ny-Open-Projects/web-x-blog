---
title: [PER-1056] Protocol Buffers 与 JSON 在前端的工程化对比
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1056：Protocol Buffers 与 JSON 在前端的工程化对比

**答**：
- 体积：pb 比 JSON 小 30%~60%；解析速度 pb 快数倍（二进制直读 vs 字符串解析）。
- 工程成本：pb 需要 schema 管理与代码生成（proto→TS 类型），双端版本对齐（schema 兼容性规则）。
- 前端接入：pbjs/pbts 生成代码 + fetch 层按 content-type 自动解码；调试成本高（需工具转 JSON）。
- 选型建议：高频大流量接口（IM 消息/行情推送）上 pb，普通管理后台保持 JSON 简单性。

```javascript
// pb 动态解码（配合 .proto 编译产物）
import { Root } from 'protobufjs';
const root = await Root.load('/proto/msg.proto');
const Msg = root.lookupType('im.Message');
function decodeMessage(buf) {
  const msg = Msg.decode(new Uint8Array(buf));
  return Msg.toObject(msg, { longs: String, defaults: true });  // long 精度安全
}
// 版本兼容铁律：只加字段不改编号；前端容忍未知字段（proto3 默认保留）
```
