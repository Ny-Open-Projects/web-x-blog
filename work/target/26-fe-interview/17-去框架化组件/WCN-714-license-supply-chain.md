---
title: [WCN-714] 企业内使用第三方 WC 组件，如何做许可证合规与供应链安全扫描？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-714：企业内使用第三方 WC 组件，如何做许可证合规与供应链安全扫描？

**答**：
- 结论：建立组件准入流水线——自动扫描 license（拒绝 GPL 等传染性协议进入闭源产品）、SBOM 清单生成、依赖漏洞扫描（npm audit / osv-scanner）。
- 对 WC 资源做 SRI（subintegrity）校验与来源白名单；锁定版本并订阅 CVE 通报，定期重扫。
- 追问钩子：发现已上线组件含高危漏洞且无补丁怎么办？考察「下线开关 + 临时补丁 + 替代方案」的应急链路。

```javascript
// 准入检查流水线（伪代码）
async function admit(pkg) {
  const report = {
    license: await scanLicense(pkg),       // 识别协议
    vulns: await scanVuln(pkg),            // 漏洞扫描
    bom: await genSBOM(pkg),               // 软件物料清单
  };
  const BANNED = ['GPL-3.0', 'AGPL-3.0'];
  if (BANNED.includes(report.license)) throw new Error('传染性协议，禁止引入');
  if (report.vulns.some(v => v.severity === 'critical')) throw new Error('存在严重漏洞');
  return report;
}
console.log('组件准入需过 license / 漏洞 / SBOM 三关');
```
