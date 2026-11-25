---
title: [RBL-679] 构建器遥测的隐私边界：opt-in 设计与「够用的最小数据」
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-679：构建器遥测的隐私边界：opt-in 设计与「够用的最小数据」

**答**:
- 构建器遥测（RBL-589 提过数据驱动放量）的合规框架：**opt-in 主动开启**（默认关闭——与 Web 产品的匿名遥测不同，开发者工具在 CI/公司环境跑，默认收集涉嫌侵入），遥测声明文件（TELEMETRY.md）列出每个收集项与用途——透明是信任的基础。
- 最小数据原则：收集「决策所需的最少字段」——比如 feature flag 的 fallback 率需要 { flag, enabled, fallback, 工具版本, OS 平台大类 }，不需要路径/代码内容/用户名；「构建时长分布」需要时长区间（分桶）而非精确值。
- CI 环境的特殊性：遥测在 CI 里跑会被记录（公司日志审计）——SDK 设计上 CI 检测（CI env 变量）时默认关闭或要求显式 env 白名单；同时上报聚合 ID 用「仓库级 hash」而非用户身份（可统计「多少仓库用了 X」而不是「谁」）。
- 数据保留与退出：保留期声明（如 90 天聚合保留）、退出机制一键生效（本地 flag + 网络层拒绝）；开源工具还要提供「可完全离线构建」的承诺——遥测失败绝不阻塞构建（fail-open）。
- 追问钩子：为什么构建器遥测比 Web 遥测更敏感？——构建器有源码与配置上下文，任何「顺手多收集」都可能泄露商业信息（内部包名/路径结构）；「最小 + opt-in + fail-open」三原则是开发者工具的合规底线。

```javascript
// 遥测 SDK 的合规实现
class Telemetry {
  constructor({ enabledFile, ciDetect, endpoint }) { ... }
  get enabled() {
    if (this.ciDetected && !process.env.TELEMETRY_CI_OPTIN) return false;  // CI 默认关
    return this.localOptIn === true;                     // 显式 opt-in
  }
  report(event) {
    if (!this.enabled) return;
    const payload = sanitize(event);                     // 白名单字段裁剪
    sendWithTimeout(this.endpoint, payload, { failOpen: true, timeoutMs: 800 })
      .catch(() => {});                                  // 遥测失败绝不阻塞构建
  }
}
const sanitize = (e) => ({
  flag: e.flag,                                          // 白名单字段
  enabled: e.enabled, fallback: e.fallback,
  tool: e.toolVersion, os: platformBucket(e.platform),   // 平台大类不精确
  repo: hash(e.repoName),                                // 仓库级 hash 非身份
  durationBucket: bucketMs(e.duration),                  // 分桶非精确
});
```
