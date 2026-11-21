# 15-3-5-添加 useClickOutside

上节课完成了快捷键的需求，这节课继续完成下一个功能：点击外侧时完成编辑并更新值。看到这个功能，自然想到抽象出一个 hook 函数来完成。判断是否点击到了某个 DOM 节点外侧的需求还是很常见的，比如下拉菜单的关闭，打开下拉菜单后，点击外面希望它被关闭，用的就是同一个思想。

## 测试用例

测试我已完全补全。唯一要注意的是：这里创建的是 `MouseEvent`，之前是 `KeyboardEvent`。同样用 document 来 dispatch 这个 event，就等于在外侧发送了一次点击事件。接下来断言组件还原成 h2 的原始标签形态，并且值被更新，一开始设的是 `test updated`，点击外侧后也要变成 `test updated`，同时 change 事件要被发送。

## 实现 useClickOutside

先抛开具体需求，创建一个通用功能：判断是否点击到某个 DOM 节点的外侧。

参数我没有直接传 DOM，而是传了一个 element ref，类型是 `Ref<HTMLElement | null>`，里面是 DOM 节点。因为在 Vue 中获取元素一般用 ref 并且它会变化，所以参数用 ref 类型。

函数内部：

- 首先定义最终使用的变量 `isClickedOutside`，代表是否点击到了外侧，初始为 false。
- 和 useKeyPress 一样，在 document 上添加 click 事件并让它触发响应，所以创建一个 `handler`，参数 `e` 的类型是 `MouseEvent`（之前键盘那里是 `KeyboardEvent`）。

在 handler 里首先要判断 element ref 也就是 DOM 节点是否存在，因为它一开始是 null 和 HTMLElement 的联合类型：

```ts
const handler = (e: MouseEvent) => {
  if (elementRef.value) {
    // 检查当前点击元素是否在目标 DOM 区域内
  }
}
```

检查的方式：当前点击元素是 `e.target`，可以使用 DOM 上的 `contains` 方法判断一个元素是否包含另一个元素。包含时 `isClickedOutside` 为 false，不包含时为 true。

这里出现了两个类型问题。第一个：`event.target` 是联合类型，可能是 null 或 EventTarget，所以要先判断 `e.target` 存在再取值。type guard 生效后 null 被排除了，但还有问题：`e.target` 是 EventTarget 类型，而 `contains` 需要的是 Node 类型，两个类型对不上。

为什么 `e.target` 不是 Node？在 DOM 的世界里我们一直以为 target 就是 DOM 元素。这是使用 TypeScript 的工程师经常被问到的问题。回顾之前复习过的 HTMLImageElement 继承关系图：EventTarget 是所有元素的基类，而这里需要的 Node 是它的子类，所以不合拍。为什么 EventTarget 不是普通的 Node 或 Element？因为文档中介绍过，它不仅是 element，还可能是 document、window，甚至是 XHR 这样的对象，所以两者并不相等。

之前总结的知识在这里完美呼应了。这种情况下可以使用类型断言，类型断言可以把父类断言成具体的子类。我们知道现在是在 DOM 上操作，所以断言成一个 HTMLElement：

```ts
if ((e.target as HTMLElement) && elementRef.value) {
  isClickedOutside.value = !elementRef.value.contains(e.target as HTMLElement)
}
```

类型错误就消失了，`isClickedOutside` 在内部点击时为 false，点击外侧时为 true。

接下来和 useKeyPress 一样：在 `onMounted` 里执行 `document.addEventListener('click', handler)`，在 `onUnmounted` 里把它移除。最后把需要的值 `isClickedOutside` 返回出去。

## 在 InlineEdit 中使用

把 `useClickOutside` 添加到 InlineEdit 里。它需要一个 ref 类型的参数，里面是节点，所以创建一个 `wrapper`，类型同样是 `Ref<HTMLElement | null>`，初始为 null，并把它返回出去，在模板上赋一个相同的 ref 名称，我们要拿到 InlineEdit 的根节点来做判断。

拿到节点后就可以使用自定义函数了，返回值称为 `isOutside`：`const isOutside = useClickOutside(wrapper)`。返回值是响应式对象，要判断它是否变成 true，可以用 watch（和上面 isEditing 的处理一样）：

```ts
watch(isOutside, (newValue) => {
  if (newValue && isEditing.value) {
    isEditing.value = false
    context.emit('change', innerValue.value)
  }
})
```

newValue 等于 true（点击到了外面）并且处于编辑状态时，处理和 Enter 一样：把 `isEditing.value` 设置成 false，发送 change 事件出去。

运行测试，全部通过。这节课对应的编码工作就完成了，单元测试完全通过。但我们还没有在界面上做任何测试，下节课在界面上测试这些代码，看看 InlineEdit 是否像单元测试中写的那样准确无误地工作。
