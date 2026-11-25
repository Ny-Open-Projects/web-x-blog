---
title: [WEB-257] 线上报错监控方案：window.onerror 到 SourceMap 还原
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 监控]
type: 面试题
---

## WEB-257：线上报错监控方案：window.onerror 到 SourceMap 还原

**答**：
- 三类捕获：window.onerror（同步运行时错误，含行列号）、window.addEventListener('unhandledrejection')（未处理的 Promise 拒绝）、资源 onerror（script/img 加载失败，无堆栈）。
- 跨域脚本报 Script error：script 标签加 crossorigin + 服务端 CORS 响应头，否则堆栈被抹掉。
- 上报内容：错误消息/堆栈/行号列号 + 释放环境信息（版本号、UA、路由、用户 ID）+ 面包屑（最近 N 次操作与请求）。
- SourceMap 还原：构建产出版本上传到监控平台（不入 CDN），错误按版本号 + 行列号反解回源码；或 Sentry 的 release+artifact 方案。
- 避免风暴：同一错误聚合去重（指纹）、限流采样、白名单忽略噪声。

```javascript
function reportError(err, extra = {}) {
  navigator.sendBeacon('/monitor/error', JSON.stringify({
    message: err.message,
    stack: err.stack,
    release: __APP_VERSION__,       // 构建注入
    ...extra,
  }));
}
window.addEventListener('error', (e) => {
  if (e.target && e.target.src) return reportError(new Error(`资源加载失败:${e.target.src}`));
  reportError(e.error || e, { type: 'runtime', lineno: e.lineno, colno: e.colno, file: e.filename });
}, true);
window.addEventListener('unhandledrejection', (e) => reportError(e.reason, { type: 'promise' }));
```

**追问**：

1. 为什么上报用 `sendBeacon` 而不是 fetch？ → 页面卸载时 fetch 会被中断，sendBeacon 由浏览器排队发送且不阻塞卸载；但它有体积上限（约 64KB），大 payload 得分片或走正常请求。
2. SourceMap 上传到监控平台，怎么防止源码泄露？ → 只传私有制品库并做访问控制，绝不部署到 CDN；构建用 hidden-source-map，确认上传成功后可删除本地 map。
3. 资源加载失败没有堆栈和行列号，靠什么定位？ → 只能靠资源 URL、页面路由、面包屑和发布版本号；可给 script 绑 onerror 上报 chunk 名，再用构建清单反查源码模块。
