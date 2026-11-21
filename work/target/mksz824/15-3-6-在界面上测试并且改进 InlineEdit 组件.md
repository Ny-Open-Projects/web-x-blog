# 15-3-6-在界面上测试并且改进 InlineEdit 组件

之前写完了 InlineEdit 的测试和代码，现在需要在界面上验证结果，看看它是否像测试中对应的那样好用。

## 接入图层列表

首先来到 LayerList，将原来的 span 文本替换成 InlineEdit：属性传入正确的值，也就是 `item.layerName`；事件处理绑定 `@change`，处理逻辑和之前的 handleChange 完全相同，发送到外面的 mutation 去处理。这里处理的是 layerName，按这个键名写即可。

替换完毕后逐个测试，和测试用例完全一致：点击图层一，能成功切换到 input；输入新值后按回车，事件带着新的值发送出去，值更新并回到文本界面，Enter 没有问题；再测 Esc：输入一个新值 sdf，点击 Esc，退回到之前的值，也没问题。

## input 自动 focus

UI 上有一点可以改进：点击进入编辑后，input 并没有获得焦点，还需要再点一次。希望点击后 input 自动 focus。实现很简单：在代码中拿到 input 这个 DOM 节点，调用 focus。

来到 InlineEdit，另外获取一个节点，称为 `inputRef`，类型具体化为 `Ref<HTMLInputElement | null>`，把它返回出去；在 input 上添加 ref 属性，就能拿到 DOM 节点。focus 应该加在 watch `isEditing` 的地方：当 `isEditing` 转换为 true 时执行 focus。加一段逻辑：`if (inputRef.value)` 就调用 `inputRef.value.focus()`。

这么写可以吗？实际点击一下，发现没有任何效果，还是没 focus，需要重新点击。debug 一下：在 watch 里 console，发现这时候 `inputRef.value` 还是 null，也就是说 DOM 还没有生成。

还记得 watch 选项里的 flush 参数吗？它有 pre、post 和 sync 三个选项，默认是 pre，也就是在 DOM 生成之前运行。这里 watch 运行时 DOM 还没生成，所以拿不到节点。当然可以把 flush 改成 post 让它在 DOM 生成后运行，但更常用的方式是使用 Vue 提供的 `nextTick` 等待 DOM 生成完毕后再运行：把回调改成 async，在里面 `await nextTick()` 之后再运行 focus 逻辑。

再点击测试，input 会自动 focus（可以看到蓝色的边框），反复试几次都正常。

## 调试 click outside 失效

前面几个用例看起来没问题，但发现点击外侧不太好使：它并没有返回之前的文本节点。这就需要调试。这里有个经验之谈：调试没有特殊技巧，一个是断点，在你觉得可能出问题的代码处加断点，看触发时的具体值；第二个最原始也最常用，console.log 大法。但注意 console.log 是异步的，打印结果有可能不是代码运行那一刻的值。

经过调试，问题出在这里：InlineEdit 的最外层 click 事件加了 `.stop` 修饰符，也就是停止冒泡。点击事件不会冒泡到 document 上去，所以点击 InlineEdit 内部时，useClickOutside 根本没有被触发，`isClickedOutside` 的值没有任何改变。

用一个最原始的调试方法验证：把 `isClickedOutside` 直接显示到界面上。第一次点击图层设置切换到编辑时，它变成了 true；但点击图层一（InlineEdit 内部）时，由于 stop 阻止了冒泡，它没有任何变化；再点击外侧，它还是 true。watch 监控不到对应的改变，watch 中的逻辑自然不会触发。

如果把图层设置默认切换到展示区（第一次不经过那个点击），就能看出端倪：初始是 false，点击 InlineEdit 内部还是 false（依旧感知不到），点击外侧时才变成 true。但这样做还是有个问题：第一次点击变成 true 之后，再点击进来不会切换回 false，所以再次编辑时就会出问题。

## 修复方案

最简单的修正思路是：既然 InlineEdit 现在是一块"黑洞区域"，它感知不到 document 上绑定的任何点击，那么对于它而言，document 上能触发的点击都是点击到外侧的。所以在 `isOutside` 的 watch 中，每次点击处理完以后，把 `isOutside` 复原到最初的 false 即可。这样每次点击都会重新走一遍判断逻辑：如果值变为 true，就把 `isEditing` 设置成 false，然后立刻复原。

最终实现的效果：初始是 false；点击 InlineEdit 内部时它感知不到任何变化；点击外侧时它变成 true，触发 watch 里的逻辑，退出编辑状态，随后把值复原成 false，完成整个过程。

当然这是一种投机取巧的方法。另一种方法是把 click 的 `.stop` 去掉，这是大家认为很自然的想法。但这么做会有一个新的坑，很有意思，大家可以自己试一试，用你的调试知识看看能否找到这个 bug 的原因。

## 小结

到这里 InlineEdit 的开发就完成了。图层列表一共实现了四个功能：隐藏、锁定、选中，以及修改图层名称；另外还有 InlineEdit 里的验证功能，很简单，大家可以自己完成。

注意：单元测试中我们没能成功模拟"点击外侧"这个功能，因为测试用例没有模拟多次交互，而这个问题正是在多次交互中出现的。所以测试驱动开发完成编码后，再在界面上测试、推动测试升级，是一个很好的实践。

下一节课要接触一个很有意思的 UI 交互：列表的拖动排序。
