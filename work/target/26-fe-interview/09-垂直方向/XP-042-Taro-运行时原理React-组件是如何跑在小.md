---
title: [XP-042] Taro 运行时原理？React 组件是如何跑在小程序上的？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-042：Taro 运行时原理？React 组件是如何跑在小程序上的？
**答**：
- 三步本质：**编译期**把 JSX 编译成模板（WXML）并抽离静态结构；**运行时**实现一套"小程序版 react-dom"（taro-runtime），把 React 的 DOM 操作**代理**为 setData 数据更新。
- 核心机制：运行时构造一个 **伪 DOM 树**（TaroElement），React 对它的 createAppend/remove 操作不触发真实渲染，而是 diff 出**数据补丁**（模板绑定的 data 字段），再 setData 给渲染层。
- 渲染层 WXML 是一份**通用模板**（递归 view/text/image 组件树，按节点类型动态渲染），配合 data 里的树形数据驱动显示。
- 事件：WXML 上绑定统一入口（`eh`），运行时找到对应 TaroElement，触发 React 合成事件体系。
- Hooks 与 React 生态（Redux 等）可直接用，因为它们只依赖 react 运行时，不依赖真实 DOM——这就是适配层的价值。

```jsx
// Taro 运行时核心链路示意（简化源码模型）
import { createReactApp, TaroElement, TaroText } from '@tarojs/runtime';
import { createPageConfig } from '@tarojs/taro';

// 1) 自定义 renderer：把 react-dom 的宿主操作换成 TaroElement 操作
// ReactDOM.createRoot → taroRoot，commitUpdate 不写 DOM 而是标脏节点
class FakeElement extends TaroElement {
  enqueueUpdate(payload) {                    // React 改动 → 收集数据补丁
    this.pendingUpdates.push(payload);        // { path: 'a.b.c', value } 形式
  }
  flush() {
    const patch = diff(this.pendingUpdates);
    this.getPageInstance().setData(patch);    // 2) 经 native 中转到渲染层（同 setData 心智）
  }
}

// 3) 模板侧：编译期生成通用递归模板（WXML 片段）
// <template name="tmpl_0_view"><view id="{{i.uid}}" bindtap="eh">{{i.cn}}</view></template>
// <template is="tmpl_0_view" data="{{ i: root.cn[0] }}" /> —— 树形 data 驱动，无 DOM 操作

// 业务代码完全标准 React，感知不到上述机制
function Cart() {
  const [count, setCount] = useState(0);
  useEffect(() => { Taro.setStorageSync('cart', count); }, [count]);
  return <Button onClick={() => setCount(count + 1)}>加购 {count}</Button>;
}
export default createPageConfig(Cart, 'pages/cart/index');
```
