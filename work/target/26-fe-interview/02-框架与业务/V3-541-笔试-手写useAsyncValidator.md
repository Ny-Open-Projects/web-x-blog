---
title: [V3-541] 笔试：手写 useAsyncValidator（防抖 + 竞态守卫）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 表单]
type: 笔试题
---

## V3-541：笔试：手写 useAsyncValidator

**答**：实现 `useAsyncValidator(sourceRef, validator, { debounce = 300 })`：① 返回 { status: 'idle'|'pending'|'valid'|'invalid', message, validate }；② 输入变化防抖触发异步校验；③ 竞态守卫：旧校验完成晚于新校验时丢弃（seq 令牌）；④ 组件卸载取消挂起校验；⑤ validate() 手动立即触发（提交前全量校验）。写出实现。

```javascript
export function useAsyncValidator(source, validator, { debounce = 300 } = {}) {
  const status = ref('idle');       // idle | pending | valid | invalid
  const message = ref('');
  let timer = null, seq = 0, unmounted = false;
  onScopeDispose(() => { unmounted = true; clearTimeout(timer); });

  async function run() {
    const mySeq = ++seq;
    status.value = 'pending';
    try {
      const result = await validator(toValue(source));
      if (mySeq !== seq || unmounted) return;      // 旧校验丢弃
      if (result === true) { status.value = 'valid'; message.value = ''; }
      else { status.value = 'invalid'; message.value = result; }
    } catch (e) {
      if (mySeq !== seq) return;
      status.value = 'invalid'; message.value = String(e);
    }
  }
  watch(source, () => {
    clearTimeout(timer);
    status.value = 'pending';                       // 输入中显示校验中
    timer = setTimeout(run, debounce);
  });

  function validate() {                             // 手动立即
    clearTimeout(timer);
    return run();
  }
  return { status, message, validate };
}
// 用法: 用户名可用性校验(服务端)
const uname = ref('');
const { status, message } = useAsyncValidator(uname,
  async (v) => (await api.checkName(v)).available ? true : '该用户名已被占用');
```

**评分点**：
- 防抖 + seq 竞态守卫（双防御）
- 四态状态机（idle/pending/valid/invalid）供 UI
- 卸载取消与旧结果丢弃
- 手动 validate 与自动触发的共存
