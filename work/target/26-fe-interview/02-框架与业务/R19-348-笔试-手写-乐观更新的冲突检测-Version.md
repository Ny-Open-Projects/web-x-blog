---
title: [R19-348] 笔试：手写带版本冲突检测的乐观编辑（文档标题）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-348：笔试：手写带版本冲突检测的乐观编辑
**答**：编辑文档标题：乐观显示新标题；action 携带 baseVersion；服务端发现 version 不一致返回 CONFLICT + 服务端最新值；前端弹「覆盖 or 查看最新」选择。

```javascript
function TitleEditor({ doc }) {
  const [optimistic, addOptimistic, clear] = useMyOptimistic(doc.title, (_cur, op) => op.value)
  const [conflict, setConflict] = useState(null)
  function save(title) {
    addOptimistic({ value: title })
    startTransition(async () => {
      const res = await renameAction(doc.id, title, doc.version)
      if (res.code === 'CONFLICT') {
        setConflict(res.serverTitle)      // 服务端最新值
        clear()                           // 回滚乐观显示
      } else if (!res.ok) {
        toast(res.msg)
      }
    })
  }
  return (
    <div>
      <input defaultValue={optimistic} onBlur={e => e.target.value !== doc.title && save(e.target.value)} />
      {conflict && (
        <dialog open>
          <p>该文档已被修改为「{conflict}」，你的修改：{optimistic}</p>
          <button onClick={() => { setConflict(null); save(optimistic) }}>覆盖</button>
          <button onClick={() => setConflict(null)}>保留服务端版本</button>
        </dialog>
      )}
    </div>
  )
}
// 服务端：update where version = baseVersion（乐观锁），失败返回 CONFLICT + 当前值
```
**评分点**：
- 乐观锁（version 条件更新）是冲突检测核心。
- CONFLICT 分支：回滚乐观 + 展示双值让用户决策。
- 覆盖路径重新发起 action（带上新 version 由服务端返回）。
- 说明乐观锁 vs 最后写入胜出的取舍。
