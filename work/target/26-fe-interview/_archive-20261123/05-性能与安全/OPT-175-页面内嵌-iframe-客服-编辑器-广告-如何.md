---
title: [OPT-175] 页面内嵌 iframe（客服/编辑器/广告）如何控制性能影响？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-175：页面内嵌 iframe（客服/编辑器/广告）如何控制性能影响？

**答**：
- iframe 的成本：独立文档完整加载流程（DNS/TCP/解析/渲染），同域共享主线程之外的进程但仍有通信开销；跨域 iframe 无法直接优化其内部。
- 控制手段：①非关键 iframe（广告/客服）`loading="lazy"` 推迟到视口附近加载；②`fetchpriority="low"` 降低其资源竞争；③不可见时干脆卸载（v-if + IntersectionObserver）。
- 通信节流：postMessage 高频数据（滚动位置/光标）合并节流，用 Transferable/结构化克隆避免字符串序列化大对象。
- 隔离方案：重计算型第三方内容放 Worker/Partytown（见 OPT-125），iframe 只用于必须独立文档的场景。

```html
<!-- 一一对应：iframe 懒加载 + 可见性卸载 + 节流通信 -->
<div id="ad-slot" style="aspect-ratio: 300/250;"> <!-- 预留尺寸防 CLS -->
  <iframe
    id="ad-frame"
    data-src="https://ads.example.com/unit/123"
    loading="lazy"            <!-- 视口附近才加载，首屏不付出加载成本 -->
    fetchpriority="low"       <!-- 资源竞争让路给首屏 -->
    referrerpolicy="no-referrer"
    title="advertisement" width="300" height="250"></iframe>
</div>
<script>
  // 不可见超过 5s 卸载 iframe：编辑器/广告类可显著省内存
  const frame = document.getElementById('ad-frame');
  const slot = document.getElementById('ad-slot');
  let hideTimer;
  new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      clearTimeout(hideTimer);
      if (!frame.src) frame.src = frame.dataset.src;   // 首次进入才真正加载
      if (!frame.src) frame.src = frame.dataset.src;
    } else {
      hideTimer = setTimeout(() => { frame.src = 'about:blank'; }, 5000); // 离开视口 5s 释放
    }
  }, { rootMargin: '200px' }).observe(slot);

  // 通信节流：滚动位置 100ms 合并一次，且用数字数组而非 JSON 大字符串
  let pendingPos = null, sendTimer = null;
  window.addEventListener('message', e => {
    if (e.data?.type === 'pos-request') {
      pendingPos = [scrollX, scrollY];
      if (!sendTimer) sendTimer = setTimeout(() => {
        frame.contentWindow.postMessage({ type: 'pos', data: pendingPos }, 'https://ads.example.com'); // 限定 targetOrigin
        sendTimer = null;
      }, 100);
    }
  });
</script>
```
