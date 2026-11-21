---
title: [OPT-142] 接口返回 JSON 过大，如何从字段与压缩两端瘦身？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-142：接口返回 JSON 过大，如何从字段与压缩两端瘦身？

**答**：
- 传输体积 = 字段数 × 记录数，治理顺序：①字段裁剪（列表接口只返回列表页展示所需字段，详情字段懒取）②短字段名/枚举值数字化（高频大列表收益明显）③压缩升级 gzip → brotli（文本再省 15~25%）。
- BFF 层做字段白名单是性价比最高的方案：按"调用方页面"定义 DTO，而不是后端一张表吐全字段。
- 压缩服务端配置：brotli 静态预压缩 + 动态请求 gzip 兜底；注意压缩在 CDN/网关做，业务服务不做。
- 验证闭环：上报 `transferSize` 与 `decodedBodySize`，压缩率与裁剪率都进性能看板。

```javascript
// 一一对应：BFF 字段白名单裁剪 + brotli 压缩配置（Express）
const express = require('express');
const compression = require('compression');
const app = express();

// brotli 优先、gzip 兜底
app.use(compression({
  filter: (req, res) => !req.headers['x-no-compression'] && compression.filter(req, res),
  br: { params: { [require('zlib').constants.BROTLI_PARAM_QUALITY]: 5 } }, // 动态请求用 5，平衡 CPU
}));

const DTO = {
  // 按调用方页面定义字段白名单：列表页不需要 remark/createdAt 等 8 个字段
  list:   ['id', 'title', 'status', 'cover'],
  detail: ['id', 'title', 'status', 'cover', 'remark', 'createdAt', 'owner', 'tags'],
};

app.get('/api/records', async (req, res) => {
  const raw = await db.records.find({ /* ... */ });
  const fields = DTO[req.query.view === 'detail' ? 'detail' : 'list'];
  // 白名单裁剪：列表接口体积通常从 480KB 降到 90KB
  const slim = raw.map(r => Object.fromEntries(fields.map(f => [f, r[f]])));
  // 枚举数字化：status 0=待处理 1=进行中 2=完成，比字符串省 60%+
  const enumStatus = { pending: 0, running: 1, done: 2 };
  const packed = slim.map(r => ({ ...r, status: enumStatus[r.status] ?? r.status }));
  res.json({ code: 0, data: packed });
});
app.listen(3000);
```

## 二十二、构建侧性能
