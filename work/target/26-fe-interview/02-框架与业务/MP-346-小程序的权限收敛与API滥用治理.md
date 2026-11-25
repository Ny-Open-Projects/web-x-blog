---
title: [MP-346] 小程序权限收敛与 API 滥用治理
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-346：小程序权限收敛与 API 滥用治理

**答**：
- API 收敛的动机：wx.* 直接散落业务代码——「能力不可测（隐私合规审计难）+ 行为不一致（授权引导各写各的）」——统一能力层封装
- 能力层设计：Capabilities 模块（getLocation/requestSubscribe/saveImage 等封装——含授权引导闭环 + 埋点）——业务只调语义方法
- 合规审计面：隐私协议声明与实际调用对齐（requirePrivacyAuthorize 的接口清单 vs 代码扫描的 wx.* 调用清单）——CI 静态扫描（AST 扫 wx.* 调用 + 白名单比对）
- 弃用 API 治理：官方弃用 API（getSystemInfoSync）的存量扫描与替换排期——lint 规则禁用弃用 API
- 深水点：能力层的降级策略统一（不支持/未授权/失败的分级返回）——业务层拿到统一的 { ok, data, reason } 结构

```javascript
// 能力层
export const CAP = {
  async getLocation(opts) {
    await ensurePrivacy();                           // 隐私协议前置
    try { return { ok: true, data: await wx.getLocation(opts) }; }
    catch (e) {
      if (e.errMsg?.includes('auth')) return guideSetting('scope.userLocation');
      return { ok: false, reason: 'fail' };
    }
  },
};
// CI 扫描: AST 扫 wx.getLocation 直调 → 强制走 CAP.getLocation (lint rule)
```
