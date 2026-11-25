---
title: [V3-542] 笔试：手写 useClipboard 与 useFullscreen（能力降级组合）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 设备能力]
type: 笔试题
---

## V3-542：笔试：手写 useClipboard 与 useFullscreen

**答**：实现：① `useClipboard({ source, copiedTimeout = 1500 })`：copy() 走 navigator.clipboard，失败降级 execCommand；copied 响应式状态（1.5s 后复位）；② `useFullscreen(targetRef)`：isFullscreen 响应式（监听 fullscreenchange）、enter/exit/toggle、iOS 降级提示（无 API 返回 unsupported）；③ 两者都做权限/异常分类处理；④ 卸载清理。写出实现。

```javascript
export function useClipboard({ copiedTimeout = 1500 } = {}) {
  const copied = ref(false);
  const text = ref('');
  async function copy(value = text.value) {
    try {
      await navigator.clipboard.writeText(value);       // 异步 API 优先
    } catch {
      const ta = document.createElement('textarea');    // execCommand 降级
      ta.value = value;
      ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      const ok = document.execCommand('copy');
      ta.remove();
      if (!ok) throw new Error('clipboard unavailable');
    }
    text.value = value;
    copied.value = true;
    setTimeout(() => copied.value = false, copiedTimeout);
  }
  return { text, copied, copy };
}

export function useFullscreen(targetRef) {
  const isFullscreen = ref(false);
  const supported = 'fullscreenElement' in document;
  function sync() { isFullscreen.value = document.fullscreenElement === (targetRef.value ?? document.documentElement); }
  sync();
  useEventListener(document, 'fullscreenchange', sync);
  async function enter() {
    if (!supported) throw new Error('fullscreen unsupported (iOS Safari)');
    await (targetRef.value ?? document.documentElement).requestFullscreen();
  }
  async function exit() { await document.exitFullscreen(); }
  const toggle = () => isFullscreen.value ? exit() : enter();
  return { isFullscreen, supported, enter, exit, toggle };
}
```

**评分点**：
- 剪贴板两级降级（async API → execCommand）+ 异常分类
- copied 状态超时复位（UI 反馈语义）
- fullscreenchange 事件同步（外部触发如 Esc 也能感知）
- iOS 无 API 的 supported 探测
