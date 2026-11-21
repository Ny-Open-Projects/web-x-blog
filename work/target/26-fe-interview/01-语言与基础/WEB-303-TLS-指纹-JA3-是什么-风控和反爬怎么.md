---
title: [WEB-303] TLS 指纹（JA3）是什么？风控和反爬怎么用它？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 笔试题
---

## WEB-303：TLS 指纹（JA3）是什么？风控和反爬怎么用它？
**答**：
- JA3 把 ClientHello 里的 TLS 版本、密码套件、扩展、椭圆曲线、压缩方法顺序拼接后取 MD5，生成客户端指纹。
- 不同浏览器/库/版本组合的指纹高度可区分：真实浏览器指纹 vs Python requests/Go http 默认指纹差异明显。
- 风控场景：脚本工具指纹命中黑名单 → 触发验证码/拦截；防御方要注意"指纹可伪造"，只作为信号之一。

```javascript
// JA3 指纹生成（简化）
function ja3(hello) {
  const s = [
    hello.version,
    hello.ciphers.join('-'),
    hello.extensions.join('-'),
    hello.curves.join('-'),
    hello.formats.join('-'),
  ].join(',');
  return hash(s);
}
const chromeHello = { version: 771, ciphers: [4865, 4866], extensions: [0, 43, 51], curves: [29, 23], formats: [0] };
console.log('JA3:', ja3(chromeHello).slice(0, 8));
// Python-requests 的默认套件列表与浏览器差异大 → 风控一眼识别
```

**评分点**：
- 结论先行，能一句话说清核心机制
- 要点覆盖主流程与关键分支（异常/并发/边界）
- 代码可运行且体现安全或性能意识
- 能主动说出"工程上怎么选"与常见坑
