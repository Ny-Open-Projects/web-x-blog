---
title: [WEB-249] 浏览器 HTTP 缓存存内存还是磁盘？判断规则
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-249：浏览器 HTTP 缓存存内存还是磁盘？判断规则

**答**：
- 两级存储：memory cache（当前渲染进程内存，关标签页即清，命中极快）与 disk cache（磁盘，重启浏览器仍在）。
- 经验规则（Chrome）：小文件（几 KB~几十 KB 的 CSS/JS/图片）倾向 memory，大文件走 disk；从地址栏/前进后退重复访问当前会话的页面资源更易 memory 命中；普通点击导航重新加载多走 disk。
- memory cache 是非规范化的：各浏览器实现不同、不响应缓存指令的细节（如 no-store 的当前会话表现），不能依赖它做业务。
- 注意：DevTools 开着时禁用缓存选项会让 disk cache 失效但 memory cache 仍可能命中，调试缓存问题要开无痕窗口。

```text
验证方法（无痕窗口外）：
1. 打开页面加载 img → Network: 200 (disk cache)
2. 同一标签刷新 → 200 (memory cache)   小图片走了内存
3. 关标签页重开 → 又是 disk cache
```
