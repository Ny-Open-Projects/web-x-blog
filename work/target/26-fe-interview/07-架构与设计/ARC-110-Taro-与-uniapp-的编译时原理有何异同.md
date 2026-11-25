---
title: [ARC-110] Taro 与 uni-app 的编译时原理有何异同（AST 转换 + 运行时适配）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-110：Taro 与 uni-app 的编译时原理有何异同（AST 转换 + 运行时适配）？
**答**：
- 共同架构：编译时把一份代码（React/Vue 写法）转成各端能跑的产物（小程序 wxml/wxss/js），运行时把框架的视图层操作映射到对应平台（小程序 setData 或原生渲染）。
- Taro 1/2 重编译时（Babel AST 转换模板，受限多）；Taro 3 转向运行时方案：在小程序里模拟 DOM/BOM，让 React/Vue 正常跑，再由渲染层 diff 后 setData，兼容性好但内存与性能开销更高。uni-app 以 Vue 模板编译时转换为主，语法限定更紧但产物更轻。
- 架构启示：选编译时轻量产物还是运行时强兼容，是跨端框架的根本权衡；业务跨端差异越多，越应该选运行时方案。

```javascript
// 简化的编译时转换示意：JSX/模板 → 小程序模板（Taro 编译时思路）
// 源码：
//   <View onClick={handleClick}>{title}</View>
// 编译时：Babel AST 提取标签、事件、表达式，生成两端产物
//   1. 生成 wxml（事件改为绑定方式，表达式改为数据绑定）
//      <view bindtap="handleClick">{{title}}</view>
//   2. 生成 js：提取模板依赖的数据字段，注入 setData 逻辑
const compiledTemplate = '<view bindtap="handleClick">{{title}}</view>';
// Taro 3 运行时方案示意：宿主环境模拟 DOM
const doc = createMiniProgramDocument();          // 模拟 document/tree
const root = doc.createElement('root');
// React 按 web 方式执行，操作的是模拟节点树
// 渲染层对模拟树做 diff，只把变化部分序列化后 setData 到真实 wxml
root.diffAndFlush((patch) => {
  miniApi.setData(patch);                         // 小程序端
  // 同一套模拟树也可对接 RN（渲染原生组件）或 H5（真 DOM）
});
// 权衡：编译时产物轻、语法受限；运行时兼容全语法、内存开销大
```

**追问**：

1. 运行时方案在小程序里模拟 DOM，setData 数据量怎么控住才不卡？ → 只 diff 出变化的节点路径做增量 setData，限制单次数据体积，长列表配分页或虚拟列表，别整棵树往视图层灌。
2. 编译时方案碰到小程序不支持的语法（动态组件、ref 直接操作节点）怎么办？ → 编译期直接报错或降级为运行时组件，Taro 3 靠模拟 DOM 撑住，uni-app 则要写条件编译分支，不要指望静默兼容。
3. 一套代码多端，rpx/vh 与 flex 兼容差异怎么体系化治理？ → 单位统一走设计稿换算层，平台差异集中在条件编译的样式补丁里，配合按端截图的视觉回归守住。
