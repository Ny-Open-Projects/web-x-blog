---
title: [V3-533] 笔试：手写 useLocalStorageState（持久化 + 跨 tab 同步）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 存储]
type: 笔试题
---

## V3-533：笔试：手写 useLocalStorageState

**答**：实现 `useLocalStorageState(key, initial, { serializer })`：① 读：localStorage 初始化（解析失败回退 initial）；② 写：ref 同步持久化（JSON 序列化，Date/Map 支持 custom serializer）；③ 跨 tab 同步：storage 事件监听（其他 tab 修改自动更新本 ref）；④ 值删除（设为 null 清 key）；⑤ 卸载移除监听。写出实现。

```javascript
import { ref, onScopeDispose } from 'vue';

export function useLocalStorageState(key, initial, { serializer = JSON } = {}) {
  function read() {
    try {
      const raw = localStorage.getItem(key);
      return raw == null ? initial : serializer.parse(raw);
    } catch { return initial; }               // 脏数据/隐私模式回退
  }
  const data = ref(read());

  const onStorage = (e) => {
    if (e.key !== key || e.storageArea !== localStorage) return;
    try {
      data.value = e.newValue == null ? null : serializer.parse(e.newValue);
    } catch {}
  };
  window.addEventListener('storage', onStorage);
  onScopeDispose(() => window.removeEventListener('storage', onStorage));

  watchEffect(() => {
    const v = data.value;
    try {
      v == null ? localStorage.removeItem(key) : localStorage.setItem(key, serializer.stringify(v));
    } catch (e) { /* QuotaExceeded: 静默或告警 */ }
  });
  return data;
}
// 用法: 主题/草稿/筛选器持久化
const theme = useLocalStorageState('theme', 'light');
const draft = useLocalStorageState('draft', '', { serializer: {
  parse: (s) => JSON.parse(s),
  stringify: (v) => JSON.stringify({ ...v, savedAt: Date.now() }),
} });
```

**评分点**：
- 初始化解析失败回退（脏数据/隐私模式）
- storage 事件跨 tab 同步（只响应其他 tab 的变更）
- 自定义 serializer 扩展（Date/元数据注入）
- 卸载移除监听 + Quota 异常兜底
