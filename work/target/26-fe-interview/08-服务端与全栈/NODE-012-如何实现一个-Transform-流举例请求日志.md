---
title: [NODE-012] 如何实现一个 Transform 流？举例：请求日志加解密管道？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-012：如何实现一个 Transform 流？举例：请求日志加解密管道？
**答**：
- 继承 `Transform` 并实现 `_transform(chunk, encoding, callback)`，处理完调用 `cb(err, data)`；可选 `_flush(cb)` 在流结束时输出尾部数据（如最后的 padding、统计信息）。
- 典型管道：`readStream → gunzip → decipher → 处理 → cipher → gzip → writeStream`。
- 注意点：`_transform` 内不要做超长同步 CPU 计算（阻塞事件循环），大计算分片或丢给 worker；`objectMode: true` 可以在流里传 JS 对象而不是 Buffer。

```javascript
const { Transform } = require('node:stream');
const crypto = require('node:crypto');

// Transform 1：日志脱敏（替换手机号）
class SensitiveFilter extends Transform {
  _transform(chunk, _enc, cb) {
    const text = chunk.toString()
      .replace(/1[3-9]\d{9}/g, (m) => m.slice(0, 3) + '****' + m.slice(7));
    cb(null, Buffer.from(text));
  }
}

// Transform 2：AES 加密
class AesEncryptor extends Transform {
  constructor(key, opts = {}) {
    super(opts);
    this.cipher = crypto.createCipheriv('aes-256-cbc', key, key.subarray(0, 16));
  }
  _transform(chunk, _enc, cb) {
    cb(null, this.cipher.update(chunk));
  }
  _flush(cb) { cb(null, this.cipher.final()); } // 输出尾部 padding
}

// 组合：明文日志 → 脱敏 → 加密 → 落盘
function secureLogPipeline(readStream, writeStream, key) {
  return new Promise((resolve, reject) => {
    const { pipeline } = require('node:stream');
    pipeline(readStream, new SensitiveFilter(), new AesEncryptor(key), writeStream,
      (err) => (err ? reject(err) : resolve()));
  });
}
module.exports = { SensitiveFilter, AesEncryptor };
```
