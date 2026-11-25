---
title: [ZSM-121] 笔试：实现 SWR 的离线写队列（断网暂存 mutation，联网后重放）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-121：实现 SWR 的离线写队列（断网暂存 mutation，联网后重放）
**答**：实现 `queueMutation(task)` 与自动重放：1) 网络正常直接执行 task（一个返回 Promise 的函数）；2) 断网时把 task 存入 localStorage 队列；3) 监听 online 事件按序重放，成功一条删一条；4) 某条连续失败 3 次则跳过该条继续后续；5) 提供清空接口。边界：页面刷新后队列仍在；重放时保持提交顺序。

```javascript
const KEY = 'offline-mutation-queue'

function read() { return JSON.parse(localStorage.getItem(KEY) ?? '[]') }
function write(q) { localStorage.setItem(KEY, JSON.stringify(q)) }

export function queueMutation(task) {
  const q = read()
  const item = { id: Date.now() + Math.random(), tries: 0,
                 payload: task.toString() }        // 序列化任务
  q.push(item); write(q)
  return navigator.onLine ? replay() : Promise.resolve()
}

export async function replay() {
  for (const item of read()) {
    try {
      await eval(`(${item.payload})()`)            // 恢复任务并执行
      write(read().filter(t => t.id !== item.id))  // 成功即移除
    } catch (e) {
      item.tries++
      if (item.tries >= 3) write(read().filter(t => t.id !== item.id))
      else write(read().map(t => t.id === item.id ? item : t))
      break                                        // 保序：失败即停，下次重放
    }
  }
}

window.addEventListener('online', replay)
export const clearQueue = () => write([])

// 评分点：
// 1. 队列持久化到 localStorage，刷新不丢
// 2. online 事件触发重放，按提交顺序执行
// 3. 失败保序：遇到失败停止，避免后续任务依赖丢失
// 4. 重试上限 3 次，死任务不阻塞队列
// 5. 说出「task 需可序列化」的真实约束（加分）
```
