---
title: [WCN-941] 生产环境 source map 的源码泄露风险：怎么策略化上传与隔离
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-941：生产环境 source map 的源码泄露风险：怎么策略化上传与隔离

**答**：
- 结论先行：把 map 随包发布等于公开源码；生产策略应是「构建产物外网可见、map 仅内网/监控平台可见」——map 上传到私有存储，配 `//# sourceMappingURL` 指向受控地址或干脆去掉 URL。
- 三种策略：① 不上报（仅本地开发）；② hidden（生成 map 但不写 sourceMappingURL，只有手动注入才用）；③ 私有源（通过监控平台如 Sentry 的 auth token 拉取，浏览器无权限拿不到）。
- 敏感信息清洗：即便 map 私有，也要避免把 `.env` 密钥、内网路径编入 sourcesContent；构建时正则过滤或只上传 minified 映射不含 sourcesContent。
- 访问控制：map 存储桶按环境隔离、带鉴权与短时签名 URL，禁止 CDN 缓存 public 可读（大促前安全审计常查此项）。
- 追问钩子：面试官问「监控平台怎么还原堆栈」——答：上传时带 release/version，平台按 sourcemap 归档，用生成文件的版本+行列反查原始栈，浏览器不接触 map。

```javascript
// 构建配置：map 上传到私有平台，产物外网不带 URL
module.exports = {
  productionSourceMap: false, // 不生成公网可访问的 map URL
  configureWebpack: {
    devtool: 'hidden-source-map', // 生成 map 但不写 sourceMappingURL
    plugins: [new SentryPlugin({
      release: process.env.RELEASE, // 带版本，平台按版本取 map
      authToken: process.env.SENTRY_TOKEN,
      // 敏感路径清洗：
      stripPrefix: ['/home/ci/', '/internal/'],
    })],
  },
};
// 结果：浏览器 DevTools 看不到源码，Sentry 能还原堆栈
```
