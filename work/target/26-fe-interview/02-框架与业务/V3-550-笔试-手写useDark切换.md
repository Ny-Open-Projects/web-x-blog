---
title: [V3-550] 笔试：手写 useDark（主题切换 composable）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## V3-550：笔试：手写 useDark

**答**：实现 `useDark({ storageKey, valueDark, valueLight })`：① 优先级：localStorage 用户选择 > prefers-color-scheme；② 返回 isDark 可写 ref——写入同时更新 html class 与持久化；③ 系统主题变化（未手动选择时）自动跟随（matchMedia change 监听）；④ 手动选择后「跟随」断开（用户覆盖优先），清除选择恢复跟随；⑤ 首帧防闪（SSR 场景说明内联脚本兜底）。写出实现。

```javascript
export function useDark({
  storageKey = 'vueuse-color-scheme',
  valueDark = 'dark', valueLight = 'light',
} = {}) {
  const systemDark = matchMedia('(prefers-color-scheme: dark)');
  const store = useLocalStorageState(storageKey, null);    // null = 跟随系统

  const prefersDark = ref(systemDark.matches);
  useEventListener(systemDark, 'change', (e) => prefersDark.value = e.matches);

  const isDark = computed({
    get() {
      const user = store.value;
      return user ? user === valueDark : prefersDark.value;  // 用户覆盖 > 系统
    },
    set(v) {
      store.value = v === prefersDark.value ? null : (v ? valueDark : valueLight);
      // 与系统一致时清掉存储 → 恢复自动跟随
    },
  });
  // 应用到 DOM
  watchEffect(() => {
    const cls = document.documentElement.classList;
    isDark.value ? cls.add('dark') : cls.remove('dark');
    document.documentElement.style.colorScheme = isDark.value ? 'dark' : 'light';
  });
  return isDark;
}
// 首帧防闪(SSR): head 内联脚本在渲染前设置 class
// <script>document.documentElement.classList.toggle('dark',
//   localStorage.getItem('vueuse-color-scheme')
//     ? localStorage.getItem('vueuse-color-scheme')==='dark'
//     : matchMedia('(prefers-color-scheme: dark)').matches)</script>
```

**评分点**：
- 三级优先级（用户 > 系统 > 默认）与「与系统一致清存储恢复跟随」的设计
- class + colorScheme 双写（原生表单控件跟随）
- 系统变化监听与用户覆盖的交互
- SSR 首帧内联脚本防闪的认知
