---
title: [PER-272] SPA 用户一天不刷新页面，内存治理有哪些系统性策略？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-272：SPA 用户一天不刷新页面，内存治理有哪些系统性策略？

**答**：
- 路由级释放：离开路由时真正卸载（组件销毁、监听解绑、定时器清理、全局 store 里的页面级数据清空）。常见漏点：全局状态库（Redux/Zustand）里塞页面数据不清理——加"路由离开自动清理该页面 slice"的机制。
- 缓存全量审计：全局缓存必须有上限（LRU）与 TTL（见 PER-268）；埋点去重集合改用容量受限的结构；日志缓冲滚动上限。
- 大数据降级：商品长列表数据分页拉取不囤积；历史消息虚拟化 + 只保留可视区 ± 缓冲；图片位图用后即弃（URL.revokeObjectURL）。
- 主动降级与"软刷新"：内存水位超阈值（如 300MB）时提示用户刷新或自动导航到关键页（丢失可接受状态）；兜底一切残余泄漏。
- 度量闭环：heap baseline 监控（PER-271）+ detached 检测（PER-266）+ 堆快照回归（实验室），版本对比追责。

```javascript
// 路由离开自动清理（以 Zustand 风格示意）
const useStore = create((set) => ({
  pageData: null, pageCache: new Map(),
  setPageData: (d) => set({ pageData: d }),
}));
// 路由守卫统一清理：
router.afterEach((to, from) => {
  if (from.meta.ownState) {
    for (const key of from.meta.ownState) useStore.setState({ [key]: null });
    from.meta.cleanup?.();            // 页面级缓存/监听由 meta 注册，统一回收
  }
});
// 图片位图用后即弃：
const url = URL.createObjectURL(blob);
img.src = url;
img.onload = () => URL.revokeObjectURL(url);   // 解码完成后释放底层存储
```
