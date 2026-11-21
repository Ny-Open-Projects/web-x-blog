---
title: [PER-639] canvas 指纹与浏览器隐私的攻防边界：指纹采集的原理、隐私合规约束与业务方的正确姿势
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-639：canvas 指纹与浏览器隐私的攻防边界：指纹采集的原理、隐私合规约束与业务方的正确姿势

**答**：
- 原理：canvas 绘制相同内容在不同设备（GPU/字体/抗锯齿）产出像素级不同结果，hash 后作为高熵指纹；同类还有 WebGL 参数、AudioContext、字体枚举——组合熵足以唯一定位设备。
- 合规约束：指纹属于个人标识信息，GDPR/个保法下用于非必要追踪需告知同意；主流浏览器已做对抗（RFP 模式加噪、用户代理收敛、存储分区）——依赖指纹做风控的业务要接受熵值持续下降的现实。
- 业务正确姿势：反欺诈场景用指纹+行为+设备多信号融合而非单点指纹；普通业务绝不做静默指纹采集（合规风险 + 浏览器对抗导致不可靠）；对内做指纹熵体检知道自己暴露多少。
- 对抗现状：`navigator.webdriver`、Canvas 加噪（Brave/Safari）、IP+指纹联合——指纹的可靠性随浏览器版本衰减，架构上不要把核心功能绑死在指纹上。

```javascript

// 指纹熵体检（内部审计用，不做对外采集）
async function fingerprintEntropyAudit() {
  const signals = {};
  signals.ua = navigator.userAgent.length;                   // 熵近似：长度差异
  signals.canvas = await probeCanvas();                      // 绘制 hash 是否跨设备稳定
  signals.webgl = (() => { const gl = document.createElement('canvas').getContext('webgl');
    const dbg = gl.getExtension('WEBGL_debug_renderer_info');
    return dbg ? gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL) : 'blocked'; })();
  signals.fonts = (() => { try { return document.fonts.size; } catch { return 0; } })();
  signals.webdriver = navigator.webdriver;                   // 无头标记
  return {
    signals, rfp: signals.canvas === 'noised',
    advice: signals.webdriver ? '自动化环境' : '普通环境',
    note: '仅用于熵评估与自动化检测，禁止用于用户追踪（合规红线）',
  };
}
function probeCanvas() {
  const c = document.createElement('canvas'); c.width = 200; c.height = 40;
  const ctx = c.getContext('2d');
  ctx.font = '16px Arial'; ctx.fillText('指纹熵检测', 5, 20);
  ctx.strokeStyle = '#f60'; ctx.arc(50, 20, 10, 0, 7); ctx.stroke();
  let h = 0; const d = c.toDataURL();
  for (const ch of d) h = (h * 31 + ch.charCodeAt(0)) | 0;
  return String(h);
}
```
