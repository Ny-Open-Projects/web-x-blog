---
title: [XP-077] RN 启动性能优化？Hermes 与懒加载 bundle 怎么落地？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-077：RN 启动性能优化？Hermes 与懒加载 bundle 怎么落地？
**答**：
- 先拆阶段再优化：进程创建 → 原生壳初始化 → JS Runtime 创建 → **bundle 加载与执行** → 首帧渲染，各端用 trace 拆解耗时（口径对齐 XP-113）。
- **Hermes**：发布构建产出预编译字节码 .hbc，免去运行时解析 JS 的 CPU 与内存开销；懒编译 + 压缩 GC 让 TTI 与内存双降；开启 `enableHermes` 并用 `hermes-engine --exec-statistics` 验证。
- **懒加载**：`babel-plugin-transform-inline-requires` + 首屏外路由 lazy require；大型三方 SDK（统计/推送/崩溃）延后到 `InteractionManager.runAfterInteractions`；长列表首屏用骨架屏先出帧。
- 拆 bundle（多业务线场景）：metro 自定义 `processModuleFilter` 拆 base + business bundle，按业务域按需加载，基座预下载。
- 治理量化：T3i（首帧）P50/P90 看板 + bundle 执行耗时单独打点；每次发版跑启动 benchmark，防止"启动刺客"依赖混入。

```javascript
// index.js —— 启动关键路径最小化：首屏之外全部延迟
import { AppRegistry, InteractionManager } from 'react-native';
import { mark } from './src/perf/trace';             // 启动各阶段打点，口径同 XP-113

mark('bundle_exec_start');

// 首屏链路同步 require（配合 babel-plugin-transform-inline-requires 就近执行）
const { HomeScreen } = require('./src/screens/Home');

// 二级页面懒加载：进入路由时才 require，首屏 bundle 只保留关键路径
const lazyScreen = (loader) => (props) => {
  const Screen = loader();                            // 首次进入时同步加载并缓存
  return <Screen {...props} />;
};
const OrderScreen = lazyScreen(() => require('./src/screens/Order').default);
const MineScreen = lazyScreen(() => require('./src/screens/Mine').default);

// 非必需 SDK 延后初始化：不与首帧抢 JS 线程
InteractionManager.runAfterInteractions(() => {
  require('./src/sdk/analytics').init();
  require('./src/sdk/push').init();
  require('./src/sdk/crash').init();
  mark('deferred_sdk_done');
});

AppRegistry.registerComponent('MainApp', () => HomeScreen);

// metro.config.js 拆 bundle（多业务线）：base bundle 预置，业务 bundle 按需
// module.exports = { transformer: { ... }, serializer: {
//   processModuleFilter: (m) => !m.path.includes('business-b'),  // 拆出 business-b
// } };
// release 构建开启 Hermes：gradle.properties -> enableHermes=true，产物为 .hbc 字节码
```
