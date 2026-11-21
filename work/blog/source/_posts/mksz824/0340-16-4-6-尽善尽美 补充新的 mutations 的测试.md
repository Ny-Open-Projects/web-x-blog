---
disableNunjucks: true
title: 16-4-6 尽善尽美 补充新的 mutations 的测试
date: 2026-11-17 08:40:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课修完了 bug。到目前为止我们添加了很多新交互，store 里也多了不少 mutation。对 store 的操作和交互、界面是可以完全分开的，所以这节课给 store 补充测试，也为下一个需求，历史记录的回滚和重做，做一个预热。那两个功能比较复杂，写测试是很好的辅助手段。

打开 store 的测试文件，关注点在 editor 这一块，所以加了 `only`。已有的 case 是 `should have default`（默认能拿到当前 currentComponent），接下来补充 `copy and paste component`、`moveComponent`、`deleteComponent` 几组测试，另外 `add and update` 也要做一些更新。先跑一遍，目前全部通过。

## 完善 add 的测试

现有的 `add component works fine` 里，对 `lastItem` 只判断了 `text` 是否等于 `text1`。现在组件添加时已经带上全部属性了，所以第一步把断言补完整：从 OpsFlow 组件库引入 `textDefaultProps`，在期望值里做一次混入。另外新添加的组件应该有新的 `layerName`，画布上已有一个图层，新加的应该是「图层2」，所以多加一条 `expect(lastItem.layerName).toBe('图层2')`。

## copy 与 paste 的测试

新 case `copy and paste component should works fine`。前面已经调用过 `setActive`，有选中的元素，直接提交 mutation：

```ts
store.commit('copyComponent')
```

copy 成功后，`store.state.editor.copiedComponent` 默认是没有值的，现在应该有值了，断言 `toBeDefined`。这里有个细节：copy 成功后 mutation 里会调用 Ant Design Vue 的 `message.success`，需要用 `jest.mock` 做全局模拟。我们不判断它是否被调用过，直接 mock 掉就行。

copy 之后继续 commit `pasteCopiedComponent`（名称比较长，从 mutation 定义里复制）。粘贴后 components 应该多一项：原来加一，现在多了一项所以加二。然后验证粘贴出来的组件和最初复制的完全一样：取 `lastItem`，断言它的 `props` 用 `toEqual` 等于 `cloneComponents[0]`（第一项是被选中的）。这个 case 通过，说明拷贝加粘贴功能没问题。

## moveComponent 的测试

`moveComponent` 是独立的 mutation，测试稍微复杂一点。先拿旧值，通过 getter 拿 `getCurrentElement`。getters 没有类型信息，返回 `any`，所以要手动指定为 `ComponentData` 类型。缓存旧值叫 `oldValue`，取它的 `left`，用 `parseInt` 转成数字，可能为空所以给默认值 0。

接着向左移动：

```ts
store.commit('moveComponent', {
  direction: 'left',
  amount: 5,
  id: currentElement.id,
})
```

成功的话 `left` 应该减小：`expect(...).toBe(oldValue - 5 + 'px')`。趁热再向右移动，`direction` 为 `right`、`amount` 为 3，期望值就是 `oldValue - 5 + 3` 再拼上 px。都通过了，移动逻辑没问题。

还有 up 和 down 两个方向，大家可以自行补充。这种多分支的情形最好把所有分支都覆盖到，代码覆盖率才高，测试也更准确，top 和 bottom 毕竟是另一个维度的计算。

## update 的 isRoot 测试

`updateComponent` 新增了一个 `isRoot` 参数，可以直接修改组件根级属性而不是 props，需要针对它加一个 case。找一个存在的 key，比如 `layerName`，value 改成 `newLayer`，`isRoot` 设为 `true`，再次 commit。断言 `currentElement.layerName` 变成了 `newLayer`。测试全部通过。

## delete 的测试

delete 很简单，大家可以自己写：触发 `deleteComponent` 之后，components 总数应该少一项。

测试补充到这里。从结果看，目前的 mutations 逻辑都能按需求正常运作，这节课的目的就达到了。
