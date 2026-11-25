---
title: [H5-386] 笔试：手写容器检测与能力注册表
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 笔试题, Hybrid]
type: 笔试题
---

## H5-386：笔试：手写容器检测与能力注册表

**答**：实现 `Container`：① 检测运行容器：'app-ios' / 'app-android'（UA + 桥对象存在）/ 'weixin' / 'browser'；② 能力注册表：每能力（pay/share/push/camera）在各容器下的可用性与实现函数（桥调用或 Web API 或不支持）；③ `can(cap)` 查询与 `do(cap, ...args)` 调用（不支持抛错并列出降级建议）；④ 能力版本协商：App 桥带版本号，能力有 minBridgeVer；⑤ 输出能力清单用于页面初始化决策。写出核心实现。

```javascript
const REG = {
  pay: {
    'app-ios': { ver: 2, run: (o) => bridge.call('pay', o) },
    'app-android': { ver: 2, run: (o) => bridge.call('pay', o) },
    'weixin': { run: (o) => wxJsapiPay(o) },
    browser: null, // 不支持
  },
  share: {
    'app-ios': { run: (d) => bridge.call('share', d) },
    'app-android': { run: (d) => bridge.call('share', d) },
    weixin: { run: (d) => wxShare(d) },
    browser: { run: (d) => navigator.share(d) },
  },
  camera: {
    'app-ios': { ver: 3, run: () => bridge.call('camera') },
    'app-android': { ver: 3, run: () => bridge.call('camera') },
    weixin: null,
    browser: { run: () => navigator.mediaDevices.getUserMedia({ video: true }) },
  },
};

class Container {
  constructor(bridgeVer = 0) {
    const ua = navigator.userAgent;
    this.bridgeVer = bridgeVer;
    this.type = /MyApp\/.*iOS/.test(ua) ? 'app-ios'
      : /MyApp\/.*Android/.test(ua) ? 'app-android'
      : /MicroMessenger/.test(ua) ? 'weixin' : 'browser';
  }
  can(cap) {
    const impl = REG[cap]?.[this.type];
    if (!impl) return false;
    return impl.ver == null || this.bridgeVer >= impl.ver; // 版本协商
  }
  async do(cap, ...args) {
    if (!this.can(cap)) throw new Error(`cap ${cap} unsupported in ${this.type}`);
    return REG[cap][this.type].run(...args);
  }
  caps() { return Object.keys(REG).filter(c => this.can(c)); } // 能力清单
}
```

**评分点**：
- 容器判定顺序（自有 UA 优先于微信特征）
- 能力表按容器分支 + null 表示不支持
- 桥版本协商（minBridgeVer）决定能力可用
- caps() 清单输出支撑页面初始化降级决策
