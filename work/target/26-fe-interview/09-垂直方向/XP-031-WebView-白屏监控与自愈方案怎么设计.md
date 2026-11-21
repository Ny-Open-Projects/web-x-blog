---
title: [XP-031] WebView 白屏监控与自愈方案怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-031：WebView 白屏监控与自愈方案怎么设计？
**答**：
- 白屏根因分类：资源加载失败（CDN/离线包损坏）、JS 报错中断渲染、内存回收（iOS 杀 WKWebView 进程）、内核崩溃。
- **检测手段**：① 渲染检测——`document.elementFromPoint` 采样视口多点判断是否全空白，或比较 DOM 树节点量；② 信号量——首字节时间/FCP 超阈值；③ 原生侧检测进程存活与 `didTerminate` 回调。
- **自愈策略分级**：重载页面（换非离线包 URL）→ 重建 WebView 实例 → 清缓存后重载 → 兜底静态页；同一会话限次数（防循环白屏）。
- 上报闭环：白屏率按版本/机型/离线包版本聚合，白率超阈值自动停用对应离线包（联动 XP-030 灰度）。

```javascript
// H5 侧检测脚本（Native 注入，采样视口渲染内容）
export function startWhiteScreenMonitor({ points = 5, thresholdMs = 3000, onWhite } = {}) {
  const start = performance.now();
  const timer = setInterval(() => {
    if (performance.now() - start > thresholdMs) return finish(true);
    const blanks = samplePoints(points).every(
      (el) => !el || el.tagName === 'HTML' || el.tagName === 'BODY' || isBlankStyle(el),
    );
    const hasContent = document.body && document.body.children.length > 0;
    if (!blanks && hasContent) return finish(false);   // 有内容即视为正常
  }, 500);

  function finish(white) {
    clearInterval(timer);
    if (white) {
      reportWhiteScreen({ url: location.href, dpr: devicePixelRatio, ua: navigator.userAgent });
      onWhite?.();                                     // 通知 Native 执行自愈
      bridge.call('webview.selfHeal', { level: 'reload', cacheBust: true });
    }
  }
}
// Native 侧分级自愈（伪码）：
// level reload → loadUrl(url + ts)（绕过离线包）
// level recreate → pool.recycle + 新建实例（对应 iOS didTerminate / 内存回收场景）
// level purge → 清 WebView 缓存与离线包 current 指针后重载，单会话最多 2 次，超出落兜底页
```
