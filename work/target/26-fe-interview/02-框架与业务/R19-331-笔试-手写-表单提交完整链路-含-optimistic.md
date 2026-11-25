---
title: [R19-331] 笔试：手写「评论提交」完整链路（校验/乐观/回滚/重试）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-331：笔试：手写「评论提交」完整链路
**答**：实现 CommentForm：客户端校验（非空/长度 ≤500）不通过不发请求；乐观插入评论（status: sending）；提交失败回滚并保留输入；成功替换为服务端数据；提交中禁用按钮。

```javascript
function CommentForm({ postId, comments, addCommentAction }) {
  const [optimistic, addOptimistic] = useOptimistic(
    comments,
    (list, op) => [...list, { ...op, id: `tmp-${Date.now()}`, status: 'sending' }]
  )
  const [text, setText] = useState('')
  const [pending, startTransition] = useTransition()
  const [error, setError] = useState('')
  function submit(e) {
    e.preventDefault()
    const t = text.trim()
    if (!t) return setError('评论不能为空')
    if (t.length > 500) return setError('最多 500 字')
    setError('')
    startTransition(async () => {
      addOptimistic({ body: t })
      setText('') // 乐观清空输入
      try {
        const res = await addCommentAction(postId, t)
        if (!res.ok) { setText(t); setError(res.msg || '发布失败') } // 保留输入
      } catch { setText(t); setError('网络异常，请重试') }
    })
  }
  return (
    <form onSubmit={submit}>
      <textarea value={text} onChange={e => setText(e.target.value)} />
      {error && <p role="alert">{error}</p>}
      <button disabled={pending || !text.trim()}>{pending ? '发布中…' : '发布'}</button>
      <ul>{optimistic.map(c => <li key={c.id}>{c.body}{c.status === 'sending' && ' ⏳'}</li>)}</ul>
    </form>
  )
}
```
**评分点**：
- 客户端校验前置（不发注定失败的请求）。
- 乐观插入 + sending 标记；失败回滚自动 + 输入恢复（手动 setText）。
- pending 禁用按钮防重复。
- addOptimistic 在 transition 内调用。
