---
title: [NODE-781] 笔试题——实现上传与出站双重安全校验（magic bytes + SSRF）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-781：手写双重安全

**需求与边界**：
- 需求：上传与出站安全（SCN-NODE-666/719）——① 上传 magic bytes 校验（伪造扩展防御）+ 大小流式限制；② 出站 SSRF 防御（SCN-NODE-772 复用——URL 预览场景双风险）；③ 文件存储 key 穿越防御（../ 归一化）；④ 上传后病毒扫描异步（隔离区语义）。
- 边界：① magic bytes 表驱动（PNG/JPEG/PDF 头——内容特征）；② 流式大小限制（content-length 预检 + 流中途计数超限断开）；③ 上传文件名不可信（服务端生成 key——原始名只做展示）。

**答**：
```javascript
const MAGIC = { png: [0x89, 0x50], jpg: [0xFF, 0xD8, 0xFF], pdf: [0x25, 0x50, 0x44, 0x46] };
app.post('/upload', auth(), (req, res) => {
  if (+req.headers['content-length'] > 10e6) return req.destroy();   // 预检
  let bytes = 0, header = [];
  req.on('data', (c) => {
    bytes += c.length;
    if (bytes > 10e6) return req.destroy();            // 流中途超限断开
    if (header.length < 8) header.push(...c.subarray(0, 8 - header.length));
  });
  req.on('end', () => {
    const ok = Object.values(MAGIC).some(m => header.slice(0, m.length).every((b, i) => b === m[i]));
    if (!ok) return res.status(415).json({ code: 'BAD_MAGIC' });   // magic bytes（SCN-NODE-666）
    const key = `u/${req.user.id}/${crypto.randomUUID()}`;   // 服务端 key（穿越防御——原始名只展示）
    if (key.includes('..')) throw new Error('TRAVERSAL');
    store.put(key, tmpFile);
    quarantine(key);                                   // 病毒扫描隔离区（异步）
    res.json({ key });
  });
});
// URL 预览（上传+出站双风险）：safeFetch（SCN-NODE-772）包装
app.post('/preview', auth(), async (req, res) => res.json(await safeFetch(req.body.url, ctx)));
```

**评分点**:
- magic bytes 表驱动 + 流式大小限制（双检——SCN-NODE-666）。
- 服务端生成 key（穿越防御——客户端名不可信）。
- 隔离区病毒扫描（上传后异步）。
- URL 预览双风险（上传面 + 出站面——SCN-NODE-772 组合）。
