---
title: [ZSM-432] 笔试：手写撤销操作的服务端协调（撤销也要提交）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-432：手写撤销操作的服务端协调
**需求**：实现 `createServerBackedUndo(api)`：1) `apply(patch)`：本地应用 + 服务端提交，服务端返回 opId 与版本；2) `undo()`：取最后 op 生成逆 patch，本地应用 + 服务端提交 `api.undo(opId, baseVersion)`；3) 撤销与在途 apply 竞态：apply 未确认前 undo 排队等待（串行化）；4) 服务端拒绝撤销（该 op 已被他人依赖）→ 本地回滚撤销并提示；5) 全程幂等（opId 复用）。

```javascript
export function createServerBackedUndo(api, store) {
  const history = []               // { opId, patch }
  let chain = Promise.resolve()    // 串行化链

  function apply(patch) {
    chain = chain.then(async () => {
      const r = await api.commit({ patch, opId: crypto.randomUUID(), baseVersion: store.version })
      store.apply(patch); store.version = r.version
      history.push({ opId: r.opId, patch })
    })
    return chain
  }

  async function undo() {
    return (chain = chain.then(async () => {
      const last = history[history.length - 1]
      if (!last) return { changed: false }
      try {
        const inverse = invertPatch(store.getState(), last.patch)
        const r = await api.undo({ opId: last.opId, baseVersion: store.version })   // 幂等：同 opId 重放安全
        store.apply(inverse); store.version = r.version
        history.pop()
        return { changed: true }
      } catch (e) {
        if (e.code === 'DEPENDENT') return { changed: false, reason: '已被他人依赖' }   // 拒绝：不回滚本地
        throw e
      }
    }))
  }

  return { apply, undo }
}
```
**评分点**：
- 串行化链（apply/undo 排队，竞态消除）——核心考点
- 撤销也走服务端提交（撤销是数据事件），幂等 opId 复用
- 服务端拒绝分支（依赖检查）清晰：不回滚本地已应用的逆 patch（本地已生效才提示）
- history 与版本号同步维护（baseVersion 冲突检测）
