---
disableNunjucks: true
title: 7-16 单独测试 Vuex store
date: 2026-11-17 14:36:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

之前我们学习和进行的都是界面上的测试，这是前端工程师的惯有思维：天天打交道的内容就是界面，在界面上一阵点击，然后观察交互后的效果。从架构师课开始我就一直在强调，可以用数据抽象出界面和展示的对应关系。尤其是上一周，我们把文本组件的属性对应到表单组件，用特殊的数据结构进行描述，让它可以渲染和实时更新，正是数据掌控界面的一招妙棋。

现在有一个神奇的存在：Vuex Store。上节课我们把它通过 provide 挂载到组件中进行过测试，但它的实现其实和 App 组件是完全独立开来的。它就是一个特殊的数据结构，只用特定的方法，比如 commit 一个 mutation 来更新其中的数据。所以它的测试根本不需要什么魔法，也不需要任何界面方面的复杂准备环境。这节课就来学习 Vuex Store 的单独测试。

有同学会问：抛开界面单独给 store 写测试，有必要吗？有收益吗？现在的 store 看起来很简单，你可能写一堆用例也感受不到妙处。但当 store 变得非常复杂以后，比如要开发画布的撤回和重做（undo redo）功能，这些测试就是灵丹妙药：可以最大限度保证功能运行正常，还能一次性运行很多复杂的 case，手工去测就非常麻烦了。随着课程推进，你会越来越感受到测试在大型项目中的重要性。

测试流程很简单。一开始先检测初始的 state 是否正常。然后是最重要的部分：怎样修改数据。修改数据需要调用特殊的方法，所以要触发 mutations，或者 actions（后面会学，它也是改变数据的一种方式）。最好给每个 mutation 写一个单独的 case，互相独立。触发 mutation 之后，检查修改后的 state 是否正常，流程就完成了。另外 getters 也可以写单独的用例，跟主流程关系不大，单独验证它是否正常即可。

按照这个原则测试我们现在的 store。这里已经建好了 store.spec.ts 并跑起来。目前有三个模块，我把测试分割成一系列用例：describe 当中可以包裹 describe，把一些用例组织在一起。第一个是 test user model，第二个是 test templates model，这两个比较简单，留给大家自己写。最后我带大家写 test editor model。

第一个用例测默认数据是否正常，叫 should have default components。store 已经导入，写 `expect(store.state.editor.components).toEqual(testComponents)`，其中 testComponents 就是 editor 初始化用的那份数据。第一个测试用例完成。

接下来测第一个 mutation，叫 setActive，它要传入一个 id：`store.commit('setActive', testComponents[0].id)`。首先断言它生效了，state 当中有改变：`store.state.editor.currentElement` 要等于对应的元素。同时这里还能顺带测试 getters，因为有一个 getters 专门用来取当前选定的元素：`expect(store.getters.getCurrentElement.id).toBe(testComponents[0].id)`。没问题，第一个 mutation 测试完毕。

下一个是 addComponent。先创建一个 payload，因为它要传入添加的内容，类型是 Partial<TestComponentProps>，text 写成 text one。然后 `store.commit('addComponent', payload)`，断言 components 添加了一项：`expect(store.state.editor.components).toHaveLength(testComponents.length + 1)`。

跑一下出现失败：期望长度是 5，实际是 4。而且 testComponents 的数量也跟着增加了，为什么？原因是引用传递：testComponents 传进去之后，add 的时候它自己也变了。为了让它不变，需要克隆一份作为初始值。用 lodash 的 clone 方法（从 lodash-es 导入），创建 `const clonedComponents = clone(testComponents)`，这样两边互不影响。把断言里的引用都替换成 clonedComponents 之后，测试就通过了。

除了长度加一，还要测真正添加进去的内容和传入的一致：取出最后一项。可以用 lodash 的 last 方法拿到 `last(store.state.editor.components)`，断言 `expect(lastItem.props.text).toBe('text one')`。通过，没问题。

最后一个用例是 updateComponent，对应的 mutation 是 updateComponent。它要传入一个 key-value 对：创建 newProps，key 是 text，value 是新值 update。`store.commit('updateComponent', newProps)`。这里不用传 id，因为它使用当前已选中的 element 来完成操作，之前 setActive 已经选择过了。用刚才的 getter 拿到当前元素：`const currentElement = store.getters.getCurrentElement as ComponentData`，然后断言 `expect(currentElement.props.text).toBe('update')`。

跑一下，全部都是绿的，漂亮的 pass 出现了，store 的测试就写完了。通过测试我们发现，不需要借助界面就能知道这些 mutation 对 store 的操作是否成功，做到了界面和逻辑的分离。这就是我们要一直坚持的中心思想。这节课的任务到此完成，谢谢大家，再见。
