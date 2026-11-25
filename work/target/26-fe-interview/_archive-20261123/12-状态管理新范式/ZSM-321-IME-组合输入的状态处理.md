---
title: [ZSM-321] 输入法组合输入（拼音候选）下状态更新怎么处理
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-321：输入法组合输入（拼音候选）下状态更新怎么处理

**答**:
- IME 组合期间 input 事件携带的是「拼音过程值」，直接受控更新会打断候选——必须区分 compositionstart/update/end 与普通 change
- 受控组件模式：composition 期间不把 value 写回状态（用非受控/本地 ref 缓冲），compositionend 才 commit 进 store 触发搜索/校验
- 中文搜索框经典 bug：输入拼音每敲一键都触发请求——debounce 只能缓解，组合期抑制才是根治
- 提交语义：Enter 在组合期间是「确认候选」不是「提交表单」，keydown 里要判 `e.isComposing`

```javascript
function useIMEInput(onCommit) {
  const composing = useRef(false)
  return {
    onCompositionStart: () => (composing.current = true),
    onCompositionEnd: (e) => { composing.current = false; onCommit(e.target.value) },
    onChange: (e) => { if (!composing.current) onCommit(e.target.value) },   // 组合期不 commit
    onKeyDown: (e) => { if (e.key === 'Enter' && !e.nativeEvent.isComposing) submit() },
  }
}
```
