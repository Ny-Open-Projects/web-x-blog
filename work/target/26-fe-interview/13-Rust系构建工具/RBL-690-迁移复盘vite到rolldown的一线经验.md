---
title: [RBL-690] 迁移复盘：Vite→Rolldown 一线迁移的五个坑与解法
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-690：迁移复盘：Vite→Rolldown 一线迁移的五个坑与解法

**答**:
- 坑 1「插件的 rollup 钩子语义微差」：transform 的 this.getCombinedSourcemap 等 rollup 专有 API 在 rolldown 兼容层缺失——症状是老插件静默不生效；解法：迁移前跑「插件兼容扫描」（列举用到的 rollup API，逐个对照兼容表）。
- 坑 2「CSS 行为差异」：postcss 配置的消费顺序/async css 插件的时序差异导致样式顺序错乱——解法：迁移验证清单里把「样式级联顺序」列为专项（RBL-628 的顺序序号机制校验）。
- 坑 3「缓存语义变化」：rolldown 的增量缓存键更细，旧的 CI 缓存目录结构不兼容——解法：升级 CI 缓存 key 前缀（版本化），避免脏缓存复用。
- 坑 4「resolve 边界」：exports 字段的严格性（vite 宽松、rolldown 按规范拒绝未列子路径）——症状是深层 import 报错；解法：诊断驱动（错误码直达文档），迁移期临时开 `strictExports: false` 过渡。
- 坑 5「团队肌肉记忆」：vite 的 HMR 语义（client 端 overlay/reload 策略）与 rolldown dev 有差异——解法：迁移期统一 dev 体验文档 + 内部 FAQ；「构建器迁移的隐性成本一半在人的习惯上」。
- 追问钩子：这五个坑的共同预防是什么？——「兼容扫描 + 语义 diff 验证 + 专项清单」都在 RBL-648 的升级兼容矩阵里；复盘的价值是把这些坑沉淀为迁移工具的自动检查项，而不是口头经验。

```javascript
// 迁移前兼容扫描（插件 API 使用面）
const ROLLUP_ONLY = [
  'this.getCombinedSourcemap', 'this.moduleIds', 'this.addWatchFile',
  'this.setAssetSource', 'this.getAssetFileName',
];
async function scanPlugins(pluginDirs) {
  const risks = [];
  for (const file of collectJs(pluginDirs)) {
    const code = fs.readFileSync(file, 'utf8');
    for (const api of ROLLUP_ONLY)
      if (code.includes(api))
        risks.push({ file, api, severity: /getCombinedSourcemap|moduleIds/.test(api) ? 'high' : 'medium' });
  }
  return risks;                                          // high: 必改；medium: 查兼容表
}
// 迁移验证清单（专项）
const CHECKLIST = [
  '样式级联顺序一致（dump 计算样式对比 3 个关键页面）',
  'chunk 划分语义 diff 为空或全部声明',
  'CI 缓存 key 前缀已版本化',
  'exports 严格性诊断全部处理或开过渡 flag',
  'HMR 行为清单（overlay/reload/状态保持）通过',
];
```
