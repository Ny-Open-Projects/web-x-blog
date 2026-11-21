---
title: [ENG-030] source map 的原理和生产环境怎么配置？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-030：source map 的原理和生产环境怎么配置？
**答**：
- source map 是"编译产物位置 -> 源码位置"的映射文件（.map），基于 VLQ 编码的 mappings 字段。
- dev 追求速度：eval-cheap-module-source-map 折中最好；trace 精确映射用 source-map。
- 生产环境给监控平台还原错误堆栈：生成 hidden-source-map，只上传 .map 到内部平台，不发布到 CDN。
- 绝不把完整 source map 公网暴露，否则源码等于开源。

```javascript
// webpack.config.js
module.exports = {
  // 开发环境：速度快，行级映射够用
  devtool: 'eval-cheap-module-source-map',

  // 生产环境如需错误还原：
  // devtool: 'hidden-source-map'  // 生成 .map 但产物不引用
  // 构建后把 .map 上传到监控平台，报错时自动还原堆栈
};
```

---

## 第六章 代码规范工具链（ENG-031 ~ ENG-034）
