---
title: [MP-066] Taro 3.0 为什么重构为运行时方案？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-066：Taro 3.0 为什么重构为运行时方案？
**答**：
- Taro 3 改为**运行时**方案：在小程序逻辑层实现一套轻量 DOM/BOM（taro-runtime），React/Vue 操作的是这套**假 DOM**，再由 taro-dom 的 diff 把变化通过 setData 同步到渲染层的模板结构。
- 渲染层是固定的模板（base template：view/text/image 全量枚举），通过模板递归 + 绑定数据渲染任意树。
- 优点：完整支持 React/Vue 动态特性、JSX 写法无限制；缺点：多一层虚拟 DOM 与 setData 同步，性能依赖优化（diff 粒度、setData 频率）。

```javascript
// Taro 3 运行时：React 操作 taro-runtime 的假 DOM，diff 后 setData
import { View, Text } from '@tarojs/components'
import { useShareAppMessage } from '@tarojs/taro'

export default function Index() {
  useShareAppMessage(() => ({ title: 'Taro 3 运行时' }))
  return (
    <View className='index'>
      <Text>hello taro</Text>
    </View>
  )
}
```
