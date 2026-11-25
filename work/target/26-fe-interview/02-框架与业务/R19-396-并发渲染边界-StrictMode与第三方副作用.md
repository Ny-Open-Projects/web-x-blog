---
title: [R19-396] 并发渲染边界：StrictMode 与第三方 SDK 副作用
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## R19-396：并发渲染边界：StrictMode 与第三方 SDK 副作用

**答**：
- 第三方 SDK 的双执行问题：地图/编辑器 SDK 在 useEffect init——StrictMode 双执行导致「实例双份/事件双绑定」——SDK 不可改时用「模块级单例 + 挂载守卫」
- 单例守卫模式：init 只一次（模块级 flag），组件只「attach/detach」到 DOM——init 与挂载分离是适配第三方 SDK 的通用解
- 全局副作用的注册表：SDK 实例放模块级 Map（key=容器 id）——StrictMode 双 mount 共享同一实例
- 生产环境的并发影响：并发渲染的「丢弃渲染」——SDK 回调里读「React 管理的 DOM」会读到中间态——SDK 的 DOM 隔离（独立容器）是底线
- 清理语义：detach 时 SDK 的 destroy 要幂等——SDK destroy 内部再 destroy 崩溃是常见集成坑

```javascript
let mapInstance = null;                          // 模块级单例
function MapView() {
  const ref = useRef(null);
  useEffect(() => {
    if (!mapInstance) mapInstance = initSDK();    // init 一次
    mapInstance.attach(ref.current);              // 挂载可重复
    return () => mapInstance.detach();            // StrictMode 双执行安全
  }, []);
  return <div ref={ref} />;
}
```
