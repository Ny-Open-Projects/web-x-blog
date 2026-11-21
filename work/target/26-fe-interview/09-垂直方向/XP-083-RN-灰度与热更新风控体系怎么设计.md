---
title: [XP-083] RN 灰度与热更新风控体系怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-083：RN 灰度与热更新风控体系怎么设计？
**答**：
- 发布节奏：dev → staging（内部包）→ production **百分比放量**（1/5/20/50/100），每档观察窗口（≥2h）内看核心风控指标再进下一档。
- 风控指标：JS 异常率、启动崩溃率、启动耗时 P90、热更成功率；阈值触发**自动熔断回滚**（CodePush `rollback` 指令回退到上一稳定 bundle 槽位）。
- 兼容矩阵：bundle 与原生壳版本强关联——热更包声明 `minNativeVersion/maxNativeVersion`，服务端按客户端原生版本下发匹配 bundle，杜绝"新 bundle + 旧壳"错配。
- 完整性：热更包公钥签名校验（code-push-sgn），防传输链路篡改；bundle 内 checksum 二次校验，失败走内置 bundle 兜底。
- 合规与体验：iOS 遵守审核条款（默认静默修复受限，需用户可感知策略合规执行）；强更/弱更分级，弱更允许本次跳过；全链路埋点（下载/安装/激活/回滚）进 XP-069 看板。

```javascript
// src/hotupdate/index.js —— 热更新客户端执行器：灰度遵循 + 签名校验 + 失败兜底
import codePush, { InstallMode } from 'react-native-code-push';

const RISK = { crashRate: 0.005, jsErrorRate: 0.02 };  // 熔断阈值（口径同 XP-068）

export async function checkAndSync() {
  try {
    await codePush.sync({
      deploymentKey: pickDeployment(),                  // 服务端按 灰度桶+原生版本 下发
      installMode: InstallMode.ON_NEXT_RESTART,         // 弱更：下次启动生效，不打断用户
      mandatoryInstallMode: InstallMode.IMMEDIATE,      // 强更：立即安装
      rollbackRetryOptions: { enableInAppRestart: true },
    });
  } catch (e) {
    track('hotupdate.failed', { stage: 'sync', msg: String(e) });
    // 失败兜底：继续使用内置 bundle，业务全量可用（功能可能旧一版）
  }
}

function pickDeployment() {
  // 服务端策略：客户端上报 原生版本 + 灰度桶 id，返回命中桶的 deploymentKey
  // bundle manifest 声明 minNativeVersion，原生版本不满足则不下发（兼容矩阵）
  return grayConfig.hotUpdate?.deploymentKey ?? Staging;
}

// 服务端熔断（伪代码）：滑动窗口内 crashRate/jsErrorRate 超 RISK 阈值
//   → 自动执行 code-push rollback <app> Production → 客户端下次 sync 拉回旧包
// 全链路埋点：download/install/activate/rollback 四事件 + 版本号，进 XP-069 看板
```

---

## 十、Flutter 深度实战（084-091）
