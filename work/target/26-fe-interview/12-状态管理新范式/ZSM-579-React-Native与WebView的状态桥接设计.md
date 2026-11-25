---
title: [ZSM-579] React Native 与 WebView 的状态桥接设计怎么避免回环
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-579：React Native 与 WebView 的状态桥接设计怎么避免回环

**答**：
- 回环死锁是头号坑：RN 把状态推给 WebView → WebView 更新自己状态 → WebView 又把变化推回 RN → RN 更新 → 再推……无限循环。根源是**双向通道没有方向语义**。
- 解法：协议上区分「指令」和「回执」。RN→WebView 的消息带 `origin: 'native'`；WebView 状态机收到 native 推送后应用变更但**不再广播**（打标记 `applyingRemote: true`）；只有 WebView 内部用户操作产生的变更才回传（`origin: 'web'`）。RN 侧同样对称处理。
- 通道选型：RN 用 `postMessage`/`injectJavaScript`（onMessage + evaluateJS），一次通信是异步跨进程序列化——大状态、高频更新（每帧）不要走 bridge，把高频数据放 WebView 内部，只同步「结果状态」（如提交完成、坐标终值）。
- 版本与信任：桥消息要带 `schemaVersion`，两端版本不一致时降级（WebView 重载或提示升级）；WebView 内内容不可信，native 收到的指令必须白名单校验，禁止直接 `eval`。
- 追问钩子：初始化时序——WebView 加载完成前 native 的推送会丢，协议要带「ready 握手」：WebView ready 后发 hello，native 重放当前状态。

```javascript
// RN 侧
const [state, setState] = useState(initial)
const webRef = useRef(null)

function pushToWeb(payload) {
  webRef.current?.injectJavaScript(
    `window.__onNativeMessage(${JSON.stringify({ origin: 'native', ...payload })}); true;`
  )
}

function onWebMessage(e) {
  const msg = JSON.parse(e.nativeEvent.data)
  if (msg.origin !== 'web') return       // 只处理 web 侧主动变更
  if (!ALLOWED_ACTIONS.has(msg.action)) return   // 白名单
  setState(merge(state, msg.patch))
}

// WebView 内部（H5 侧）
let applyingRemote = false

window.__onNativeMessage = (msg) => {
  applyingRemote = true                    // 标记：这次变更来自 native
  store.setState(msg.patch)
  applyingRemote = false                   // 应用但不回传
}

// store 订阅：只有本地变更才回传
store.subscribe((s, patch, meta) => {
  if (meta.fromRemote || applyingRemote) return   // 回环剪断
  window.ReactNativeWebView.postMessage(
    JSON.stringify({ origin: 'web', action: 'sync', patch, schemaVersion: 2 })
  )
})

// ready 握手：WebView ready 后请求状态重放
window.onload = () => window.ReactNativeWebView.postMessage(
  JSON.stringify({ origin: 'web', action: 'hello' })
)
```
