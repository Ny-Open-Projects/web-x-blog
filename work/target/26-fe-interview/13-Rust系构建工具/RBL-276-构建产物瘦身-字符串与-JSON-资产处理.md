---
title: [RBL-276] 构建产物瘦身：字符串/JSON/资产的处理策略
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-276：构建产物瘦身：字符串/JSON/资产的处理策略

**答**:
- JSON 数据：大 JSON 进 bundle 是体积黑洞——改 fetch 按需加载或 asset 拆出（URL 引用），构建期做「JSON 瘦身」插件（只保留用到的字段）
- 字符串常量：i18n 语言包按语言分包懒加载；超长正则/模板字符串外置
- 图片资产：构建期按需压缩（sharp/squoosh 插件）+ 大图转 CDN 引用；inline 阈值（<4KB base64）平衡请求数
- 深度手段：产物内重复字符串提取（长重复串入字典）、死字符串清除（ unreachable 文案）——收益小放最后

```javascript
// JSON 瘦身插件（processAssets）
const slim = (json) => pickFields(json, ['id', 'name', 'price'])   // 只留渲染字段
// 资产
{ test: /\.(png)$/, type: 'asset', parser: { dataUrlCondition: { maxSize: 4 * 1024 } } }
```
