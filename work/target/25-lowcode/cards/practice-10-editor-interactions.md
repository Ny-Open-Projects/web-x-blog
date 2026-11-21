---
title: 编辑器高级交互：工具栏定位与滚动显隐
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 实战, 编辑器, IntersectionObserver]
---

## 编辑器高级交互：工具栏定位与滚动显隐

**工具栏定位**（IntersectionObserver + getBoundingClientRect）：
- `IntersectionObserver`（threshold:0.9）监听画布内组件：露出 <90% 就隐藏工具栏；root 设为 canvas 容器；useEffect 的 return 里 `disconnect()` 清理。
- 选中组件用 `data-id` 匹配 DOM → `getBoundingClientRect()` 取相对视口坐标（right 是到视口零点不是到右边缘，易错）→ 工具栏绝对定位 `left=rect.right、top=rect.bottom-工具栏高度`。
- 首次挂载 DOM 未就绪拿不到坐标：setTimeout 延迟 500ms 再 resizeComponent。
- 强制刷新技巧：布尔 state `ifReach` 作 useEffect 依赖，点击置 true 触发重算、非首次分支改回 false 借第二次执行完成刷新；拖拽结束 setIfRefresh(true) 重算坐标。

**滚动显隐**：策略 = 滚动即隐藏、停止 200ms 再显示、滚出超 10% 保持隐藏；`useRef` 绑画布父容器 + addEventListener('scroll')，handleScroll 反复 clearTimeout 实现防抖；父调子方法用 `useImperativeHandle` + ref；显隐双来源（父 showToolBar + 子 localHidden）用 classnames 拼合。

出处「课程25 · 18-6~18-8」
