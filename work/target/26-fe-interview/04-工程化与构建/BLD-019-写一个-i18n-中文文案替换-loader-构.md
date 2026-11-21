---
title: [BLD-019] 写一个 i18n 中文文案替换 loader（构建期把中文替换成 i18n 调用）。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-019：写一个 i18n 中文文案替换 loader（构建期把中文替换成 i18n 调用）。
**答**：
- 方案：匹配源码中的中文字符串字面量，替换为 `t('key')`，key 用"文件名 + 序号 + 内容 hash"生成，词条写入 this.emitAsset 或 JSON 文件供翻译平台消费。
- 只处理字符串字面量（用正则定位引号内中文）避免误伤注释和标签名；模板字符串单独处理。
- 用 getOptions（webpack 5 的 this.getOptions）接收词条映射，支持已有人工翻译则复用。

```javascript
// i18n-loader.js
module.exports = function (source) {
  const options = this.getOptions(); // { dict: { 你好: 'home.greet' } }
  const dict = options.dict || {};
  const fileKey = this.resourcePath.split(/[\\/]/).pop().replace(/\.\w+$/, '');
  let index = 0;
  const collected = this.__i18nCollected || {}; // 也可用 WeakMap 与 plugin 通信

  // 匹配单引号 双引号 字符串中的中文
  const regex = /(['"`])((?:(?!\1).)*[\u4e00-\u9fa5]+(?:(?!\1).)*)\1/g;

  const out = source.replace(regex, (match, quote, text) => {
    if (dict[text]) return `t('${dict[text]}')`;
    const key = `${fileKey}_${index++}_${Buffer.from(text).toString('base64url').slice(0, 8)}`;
    collected[key] = text;
    return `t('${key}')`; // 由 babel 插件注入 t 或约定全局 t
  });

  this.emitFile('i18n/zh.json', JSON.stringify({ [fileKey]: collected }, null, 2));
  return out;
};

// webpack.config.js
// module.exports = { module: { rules: [
//   { test: /\.(js|vue)$/, exclude: /node_modules/, use: [{
//     loader: './i18n-loader',
//     options: { dict: { 你好: 'common.hello' } },
//   }] },
// ] } };
```
