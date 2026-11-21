---
title: [NODE-549] Node 服务的 UGC 发布链路（评论/帖子）服务端如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-549：UGC 发布链路服务端
**答**:
- 链路：发布请求（校验：频率/资格/内容规范）→ 内容处理（敏感词 NODE-548/机审 NODE-547/格式清洗（XSS 净化 NODE-355））→ 存储（内容表 + 索引（检索 NODE-387））→ 分发（状态流 ARC-608 + 通知订阅者）。
- 频控与防刷：发布频率限制（同用户/同内容——重复内容检测：相似度指纹（防机器人刷贴）NODE-456 风控）、资格校验（等级/实名要求——分级发布权限）。
- 发布协议：幂等（客户端幂等键——双击防重）、分步内容（长文草稿/图片先传后发——发布引用已传媒体 ID ARC-377）、发布结果三态（成功/审核中/失败+原因 ARC-608）。
- 存储设计：内容表（正文 + 元数据）、计数分离（点赞/评论数——计数表防热点行 NODE-520 攒批更新）、大内容（长文——分段存储/对象存储外置）。
- 一致性：发布后立即可见性（自己可见（审核状态流）vs 他人（审核通过后）——可见性规则统一）、删除与索引同步（删除 → 索引删除事件 NODE-507 失效）。
```javascript
async function publishPost(uid, draft) {
  await rate.allow(`post:${uid}`);                               // 频控
  if (await dupCheck(draft.content)) throw new DuplicateContent();
  const clean = sanitize(draft.content);                         // XSS 净化
  const audit = await moderate(clean);                           // 机审
  return savePost({ uid, content: clean, state: audit.state }, audit);
}
```
