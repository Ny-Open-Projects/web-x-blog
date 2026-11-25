---
title: [MP-392] 笔试：手写 wx API mock 测试基建
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 测试]
type: 笔试题
---

## MP-392：笔试：手写 wx mock

**答**：实现组件单元测试的 wx mock 基建：① 全局 wx 对象 mock：分层实现——request（按 url 规则返回 mock 数据/可编程队列）、storage（内存 Map 模拟）、toast/modal（记录调用断言）；② 可编程响应：`wxMock.request.when('/api/user').reply(200, {...})`——按 url 注册响应；③ 调用断言：`expect(wx.toast).toHaveBeenCalledWith(...)`（jest spy 语义）；④ 时间控制：wx.nextTick/setInterval mock（fake timers 配合）；⑤ 与 miniprogram-simulate 的集成（global.wx 注入）。写出实现。

```javascript
// wx-mock.js
export function createWxMock() {
  const storage = new Map();
  const routes = new Map();
  const calls = { toast: [], modal: [] };

  const wxMock = {
    request(opts) {
      const key = Object.keys(routes).find((p) => opts.url.includes(p));
      const rule = routes.get(key);
      setTimeout(() => rule
        ? rule.status < 400 ? opts.success({ statusCode: rule.status, data: rule.data }) : opts.fail({ errMsg: 'request:fail ' + rule.status })
        : opts.fail({ errMsg: 'request:fail no mock' }), 0);
    },
    setStorageSync: (k, v) => storage.set(k, v),
    getStorageSync: (k) => storage.get(k) ?? '',
    removeStorageSync: (k) => storage.delete(k),
    getStorageInfoSync: () => ({ keys: [...storage.keys()], currentSize: 100, limitSize: 10240 }),
    showToast: (o) => calls.toast.push(o),
    showModal: (o) => { calls.modal.push(o); o.success?.({ confirm: true }); },
    createSelectorQuery: () => ({ select: () => ({ boundingClientRect: (cb) => cb(null) }).exec?.() ?? ({ exec: (cb) => cb?.([null]) }) }),
    requestWhen: (urlPattern) => {
      let rule;
      routes.set(urlPattern, rule = { status: 200, data: null });
      return { reply: (status, data) => { Object.assign(rule, { status, data }); return rule; } };
    },
    __calls: calls,
  };
  global.wx = wxMock;
  return wxMock;
}
// 测试用例
it('登录失败提示', () => {
  const wx = createWxMock();
  wx.requestWhen('/code2session').reply(401, {});
  renderLogin();
  tapSubmit();
  expect(wx.__calls.toast[0].title).toBe('登录失败');
});
```

**评分点**：
- 分层 mock（request 可编程/storage 内存/交互记录）
- when().reply 的可编程注册语义
- 调用断言（spy 语义）供 UI 反馈验证
- 与 simulate/global.wx 注入的集成
