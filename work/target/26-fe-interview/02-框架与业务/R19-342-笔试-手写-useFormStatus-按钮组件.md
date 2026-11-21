---
title: [R19-342] 笔试：手写通用 SubmitButton（useFormStatus + 确认态）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-342：笔试：手写通用 SubmitButton
**题**：实现 SubmitButton：form 提交中自动禁用并显示 spinner（useFormStatus）；支持 pendingText；提交成功后 2s 内显示成功态再恢复（通过 useActionState 外部信号传入 done 标志）；在无 form 包裹时正常渲染。

```javascript
'use client'
function SubmitButton({ children, pendingText = '提交中…', done = false, ...rest }) {
  const { pending } = useFormStatus()
  const doneTimer = useRef(false)
  const showDone = done || doneTimer.current
  useEffect(() => { if (done) { doneTimer.current = true; const t = setTimeout(() => doneTimer.current = false, 2000); return () => clearTimeout(t) } }, [done])
  return (
    <button type="submit" disabled={pending || showDone} {...rest}>
      {pending ? pendingText : showDone ? '✓ 已提交' : children}
    </button>
  )
}
// 使用：<form action={formAction}><SubmitButton pendingText="保存中…" done={state.ok}>保存</SubmitButton></form>
```
**评分点**：
- useFormStatus 必须在 form 内（说明机制）。
- pending 禁用防双击。
- done 成功态 2s 恢复（外部信号 + 内部 timer 结合）。
- 无 form 时降级正常渲染（不抛错）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-37dd35aa-c730-49eb-b85d-f12a5a3747cc-cwd'; fi
exit "$__zcode_status"
