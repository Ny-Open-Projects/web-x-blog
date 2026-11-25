---
title: [XP-152] 跨端容器 JSI 设计：同步直调与宿主对象
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-152：跨端容器 JSI 设计：同步直调与宿主对象

**答**：
- 题目：实现类 JSI 的同步桥——JS 侧持有 Native 对象代理（HostObject），方法调用同步返回（无 JSON 序列化）。
- 思路：Native 注册 HostObject（方法表）→ JS 侧 Proxy 拦截调用 → 直调 Native（跳过序列化）；大数据用共享内存（ArrayBuffer 传递）。
- 评分点：同步语义；Proxy 拦截；共享内存传输。

```javascript
// JS 侧：Native 模块代理
function createHostObject(name, methods) {
  return new Proxy({}, {
    get(target, method) {
      if (methods.includes(method)) {
        return (...args) => nativeCallSync(name, method, args);   // 同步直调
      }
      throw new Error(`method ${method} not found on ${name}`);
    },
  });
}
const NativeStorage = createHostObject('Storage', ['get', 'set', 'remove']);
NativeStorage.set('key', 'value');                         // 同步返回（无回调延迟）
// 大数据：ArrayBuffer 共享
const buf = new SharedArrayBuffer(1024);
nativeWrite(buf, data);                                    // Native 直接读内存——零拷贝
// 对比旧 Bridge：JSON.stringify(10MB) 耗 200ms+；JSI 直调 < 5ms
```
