---
title: [MFW-344→MFW-344] SSR 应用的依赖审计自动化（双端图分域）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-344：依赖审计分域

**答**:
- 分域审计更有意义：client bundle 依赖（体积/许可证/浏览器兼容）与 server 依赖（CVE/CPU 攻击面/native 兼容）风险模型完全不同——一锅审计漏掉各自重点
- 自动化管线：构建产物 → 解析 module graph → 按 server/client 标注 → 三个门禁（client：体积榜+license；server：CVE+已知恶意包名单+native 白名单；共同：维护活跃度——2 年未更新的传递依赖标黄）
- 晋升门：新依赖引入 PR 自动附审计卡（体积增量/传递依赖数/最近发布/替代品对比——reviewer 三秒决策材料）
- 豁免治理：与门禁豁免同构（MFW-464：issue+until+owner 分离审批——audit 例会清理过期豁免）

```text
分域三门禁：client(体积/license) / server(CVE/恶意名单/native) / 共同(活跃度)
流程：新依赖 PR 自动审计卡 → reviewer 快决；豁免走 issue+until
```
