---
title: [WEB-083] 什么是站点隔离 Site Isolation？它防的是什么攻击？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-083：什么是站点隔离 Site Isolation？它防的是什么攻击？
**答**：
- 早期 Chrome 按标签页分配渲染进程，恶意页面里的跨站 iframe 与宿主同进程，能通过 Spectre 等侧信道偷读同进程内存。
- 站点隔离后，不同站点的文档（含跨站 iframe）强制运行在不同渲染进程，进程边界成为物理隔离，侧信道只能读到本进程数据。
- 触发条件：桌面 Chrome 默认对"会渲染跨站 iframe 的页面"启用；进程数随之膨胀，移动端曾因内存考虑降级。
- 前端关联：CORS/CORB 管数据可读性，Site Isolation 管内存可读性，两层防御互补。

```html
<!-- 跨站 iframe：站点隔离下运行在独立渲染进程 -->
<!-- 验证方式：打开 chrome://process-internals 可看到 frame 与 process 的对应关系 -->
<iframe src="https://third-party.example.com/ad"></iframe>
<script>
  // 即便同进程都做不到的事在隔离后更不可能：
  // 跨进程无法直接读取 iframe 内 DOM，跨源 DOM 访问再被同源策略拦一道
  try {
    console.log(frames[0].document.body.innerText);
  } catch (e) {
    console.log('跨源 iframe 的 DOM 不可访问', e.name); // SecurityError
  }
</script>
```
