---
title: [PER-121] 移动端 H5 与 App 容器（WebView）的安全边界如何划分？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-121：移动端 H5 与 App 容器（WebView）的安全边界如何划分？

**答**：
- 边界模型：H5 跑在容器里，**信任等级 H5 < JSBridge < Native**——任何 Bridge 能力（支付/定位/通讯录）必须由 Native 校验调用方与用户授权，不能 H5 说什么就做什么。
- Bridge 设计三原则：**白名单域名**（只有自家 H5 能调敏感 API）、**最小能力**（按页面下发可用 API 列表）、**参数校验在 Native**（H5 参数一律不可信）。
- WebView 加固：禁用 file 域访问、关闭不用的 WebContents 权限、URL scheme 跳转白名单（防深链劫持）。
- H5 侧自觉：不存储敏感数据到 WebView 可持久化目录、退出登录清理容器缓存。

```javascript
// JSBridge：白名单 + 最小能力 + Native 侧校验
// Native 侧（示意，Android/iOS 同理）必须执行这四步
const BRIDGE_WHITELIST = {
  'https://h5.example.com': ['getUserProfile', 'pay', 'share'],
  'https://partner.example.com': ['share'],            // 第三方页面只有分享能力
};

function handleBridgeCall(h5Url, api, params, callback) {
  const origin = new URL(h5Url).origin;
  const allowed = BRIDGE_WHITELIST[origin] ?? [];
  // 1) 域名白名单 + 2) 该域名可用 API 白名单
  if (!allowed.includes(api)) return callback({ code: 403, msg: 'api not allowed' });
  // 3) Native 侧参数校验，不信任 H5 传入
  if (api === 'pay' && !isValidPayParams(params)) return callback({ code: 400 });
  // 4) 敏感 API 触发 Native 自己的用户授权弹窗（指纹/密码），与 H5 无关
  nativeCall(api, params, callback);
}

// H5 侧：统一封装，只声明需要的能力，不做任何本地持久化
export function callBridge(api, params) {
  return new Promise((resolve, reject) => {
    window.__nativeBridge?.postMessage({ api, params }, (res) =>
      res.code === 0 ? resolve(res.data) : reject(res));
  });
}
callBridge('share', { title: '活动', url: 'https://h5.example.com/act' });
```
