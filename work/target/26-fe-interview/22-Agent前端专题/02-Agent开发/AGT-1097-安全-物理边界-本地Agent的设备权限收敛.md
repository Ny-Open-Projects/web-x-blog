---
title: [1097] 跑在用户设备上的本地 Agent，权限怎么收敛
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 端侧]
type: 面试题
---

## 1097：跑在用户设备上的本地 Agent，权限怎么收敛

**答**：
- 本地 Agent 危险点：文件系统全盘可读、剪贴板、屏幕内容、浏览器会话——比服务端 Agent 多了「物理级」敏感面。
- 权限框架：按「目录/能力」逐项授权（首次访问弹授权框，权限面板可撤销），敏感能力（读下载目录、截屏）默认关闭。
- 数据出界控制：本地 Agent 上云推理时，出界内容过脱敏（本地文件路径、账号名），并提供「离线模式」（敏感数据本地小模型处理，不出设备）。
- 追问钩子：用户授权疲劳怎么办？——按「操作族」授权（一次授权「读笔记目录」覆盖该类操作）+ 权限使用记录可视化（用户看得见 Agent 用过什么权限），授权有据可依。

```ts
const caps = {
  fs: { '/Documents/notes': 'prompt-then-grant' },  // 逐目录授权
  clipboard: 'off',                                  // 默认关
  screen: 'off',
};
async function readFile(p) {
  if (!granted(caps.fs, p)) return askUser(p);       // 首次授权
  audit.push({ cap: 'fs', path: p });                // 使用记录可视
  return sanitizeBeforeUpload(await fs.readFile(p)); // 出界脱敏
}
```
