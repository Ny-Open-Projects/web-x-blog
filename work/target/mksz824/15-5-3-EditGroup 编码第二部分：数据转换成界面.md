# 15-5-3-EditGroup 编码第二部分：数据转换成界面

上节课我们完成了组件分组数据的初步计算，把传入的所有属性按需求做了粗略分组：得到一个大的分组，里面有多个分组项，每一项的 items 中包括了所有应该处理的选项。下一步需要把这个数组里的内容转化成对应的 key-value 对象，从数组转成对象，才能把整个对象传入已经写好的 PropsTable 组件，显示出对应的一系列表单。

## 数组转对象

所以需要对 newGroups 重新计算一下。新建一个变量 `editGroups`，它也是计算属性，用 computed 实现。

实现很自然：循环 `newGroups.value.map`，其中每一项是 group。要做计算的是它的 items，把 items 转化成 key-value 对象。一开始准备一个空对象，称为 `propsMap`，类型指定为 `AllComponentProps`，指代所有属性的 key-value 对象类型。然后用 forEach 往里添加：

```ts
const propsMap: AllComponentProps = {} as AllComponentProps
items.forEach((item) => {
  propsMap[item] = props.props[item]
})
```

每一项的值从原始属性中取得。这里会有一个类型错误：因为 props 是 AllComponentProps，它上面的值是一系列固定的 key，所以要做类型断言，把 item 断言成这些 key：`item as keyof AllComponentProps`，之后就没有问题了。

新的 propsMap 计算完毕后返回。整个 map 返回的对象展开原来的 group，再把新的 props（也就是 propsMap）添加上去。把 editGroups 返回出去，原来的 newGroups 模板展示就不需要了，只要展示每个 group 的 props 即可。

看最终结果：计算正确，拿到了对应的 key-value 对象，把数组转换成了对象。

## 接入 PropsTable 与手风琴

有了 props 就可以用老朋友 PropsTable 组件了。把它引入并添加到 components 中，然后替换：把之前的 pre 标签去掉，换成 props-table，传入这个对象。可以看到值都显示出来了，并且成功附上了对应的表单，界面就是想要的。

接着把这些内容替换成 Ant Design Vue 提供的手风琴组件，也就是 Collapse。首先在外层加一个 `a-collapse` 标签，然后把每一项换成里面的 `a-collapse-panel`，并加一些对应属性：

- `key`：不使用 item.text，而是把 index 拿出来，用字符串模板拼成 `item-0`、`item-1` 这样的形式；
- `header`：面板标题，替换成 `item.text`。

去掉调试用的 v-for 输出后，分组效果已经有了，每一项都能点开。还需要默认打开第一项：Collapse 的 v-model 叫 `activeKey`，我们添加一个 `currentKey` 表示当前展示的 key，值就是第一项对应的 key，即 `item-0`（index 从 0 开始）。把 currentKey 返回出去，v-model 添加到最外层的 a-collapse 上。看效果：第一项已经默认展开。

## 让事件继续向上传递

还有一个问题：修改表单没有任何效果，值都不更新了。大家都知道我们的数据流是自上而下的，而 PropsTable 里根本没有发出任何事件，之前它发的是 change 事件，所以需要通过 EditGroup 把这个事件再发送出去。

修改：在 EditGroup 中新建一个 `handleChange`，事件对象设置成 any；在 emits 里添加经典事件 change；内部通过 `context.emit('change', e)` 发送出去，并 return `handleChange`。然后在 PropsTable 上添加 `@change="handleChange"`。

这样 EditGroup 就像一个二道贩子：把 PropsTable 发送出来的事件通过中继转发到 EditorView 中去。EditorView 那边我已经把 change 监听接上了，等于转发了一道。

现在再来感受：点击加粗，文字加粗了；斜体也没问题，能够成功生效。值能够正常更新，分组工作也完成了。

## 小结

这个过程中其实讲了一个数据结构转换的过程。要学会的是先分析、写一些伪代码，再根据伪代码书写对应的逻辑，这样效率会快不少。希望大家以后面对稍微复杂一点的问题时，学会使用这一招。
