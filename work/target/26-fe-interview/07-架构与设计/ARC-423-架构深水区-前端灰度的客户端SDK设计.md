---
title: [ARC-423] 前端灰度的客户端 SDK 设计要点有哪些？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-423：前端灰度的客户端 SDK 设计要点
**答**:
- SDK 三职责：分桶判定（输入用户特征，输出版本/开关值）、版本加载（按分桶结果决定加载哪个 bundle）、上报标注（所有数据带桶信息）。
- 分桶稳定性：分桶因子优先 userId（登录稳定）> 设备 ID（未登录稳定）> 随机（仅当次会话）；分桶结果持久化（会话内不变，ARC-390）。
- 版本加载设计：入口 HTML 由服务端按分桶返回对应版本 script 标签（服务端分桶，避免双下载）；端上分桶兜底时接受"先下载默认版再切换"的代价并优化（预取另一版本关键资源）。
- 灰度安全：SDK 加载失败的兜底（默认版本可运行）；分桶服务不可用时走"最后已知配置"而非全量回滚。
- 与实验平台接口统一：灰度、AB、特性开关共用一套分桶 SDK（正交分层：不同实验用不同分层盐，ARC-277）。
```javascript
class GraySDK {
  async resolve(feature) {
    const cfg = this.configs[feature];
    if (!cfg) return 'control';
    const cached = this.local.get(feature);                     // 会话内稳定
    if (cached && cached.cfgVersion === cfg.version) return cached.bucket;
    const bucket = this.hashBucket(this.unitId, cfg.salt, cfg.rollout);
    this.local.set(feature, { bucket, cfgVersion: cfg.version });
    return bucket;
  }
  hashBucket(uid, salt, rollout) {
    return hash(`${salt}:${uid}`) % 100 < rollout ? 'treatment' : 'control';
  }
}
```
