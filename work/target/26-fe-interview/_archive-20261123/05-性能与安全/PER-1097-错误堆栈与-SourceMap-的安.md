---
title: [PER-1097] 错误堆栈与 SourceMap 的安全发布策略
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1097：错误堆栈与 SourceMap 的安全发布策略

**答**：
- 问题：公开 sourcemap 暴露源码逻辑（密钥/内网地址/注释）；不发布则线上堆栈无法定位。
- 策略：sourcemap 不随静态资源发布，上传到私有错误平台（Sentry 等支持）；或发到鉴权域名。
- 清理：构建期剥离注释与硬编码密钥（env 注入而非源码常量）；日志采集侧对堆栈中的内网域名脱敏。
- 验证：生产环境直接访问 *.map 应 404；错误平台还原率监控（map 版本覆盖度）。

```javascript
// 构建后上传 sourcemap 并本地删除
async function publishMaps(dir) {
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.map'));
  await sentryUpload(dir, { release: BUILD_ID, files });   // 上传私有平台
  files.forEach(f => fs.unlinkSync(`${dir}/${f}`));        // 删除不发布
  // 服务器同时拦截 *.map 请求返回 404（Nginx 规则）
}
// Sentry 还原率检查：processedEvents / capturedEvents > 0.9
```
