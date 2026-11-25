---
title: [RBL-036] 笔试：手写一个 Rspack 风格的 markdown 转 JS loader
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-036：笔试：手写一个 Rspack 风格的 markdown 转 JS loader
**答**：实现一个 loader（webpack/Rspack 兼容写法），把 .md 文件转换为 JS 模块。要求：1) 支持异步 loader 写法（用 this.async）；2) 把 markdown 中图片路径改写为 options.base 前缀；3) 输出 `export default html` 形式；4) options.base 为空时跳过改写；5) 出错时通过回调让构建失败。

```javascript
const { marked } = require('marked');

module.exports = function (source) {
  const cb = this.async();               // 异步 loader 必须用回调返回
  const { base = '' } = this.getOptions() || {};
  try {
    let md = source;
    if (base) {
      // 仅改写相对路径图片，跳过 http/data URL
      md = md.replace(/(!\[[^\]]*\]\()((?!https?:|data:)[^)\s]+)\)/g,
        (_m, head, url) => `${head}${base}/${url.replace(/^\//, '')})`);
    }
    const html = marked.parse(md);
    cb(null, `export default ${JSON.stringify(html)};`, Buffer.from(html).byteLength ? undefined : undefined);
  } catch (err) {
    cb(err);                              // 错误必须传给构建，不能吞
  }
};
```
**评分点**：
- 使用 this.async() 获取回调而非直接 return（异步契约正确）。
- 正则改写保留捕获组结构且排除绝对 URL（边界处理）。
- 输出是合法 ESM 模块（字符串 JSON.stringify 防注入）。
- 失败路径 cb(err) 让构建报错，不吞异常。
- getOptions 读取配置并有默认值兜底。
