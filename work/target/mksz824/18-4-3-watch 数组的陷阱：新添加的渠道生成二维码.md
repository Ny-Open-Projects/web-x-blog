# 18-4-3-watch 数组的陷阱：新添加的渠道生成二维码

上节课我们初步完成了生成二维码的任务，这节课针对代码做优化，重点是修复一个现存的问题，并借此引出 watch 使用中非常有意思的话题。

先说优化。我把代码做了一个提取，在 helper.ts 中创建了新的函数 generateQRCode，把渲染逻辑放进去：传两个参数，第一个是要渲染的 DOM 节点的 ID，第二个是要渲染的数据 URL，内部调用 QRCode.toCanvas 生成二维码，返回一个 Promise。然后用这个函数替代之前的逻辑，直接 `await generateQRCode(id, url)` 就可以了。第一步优化很简单。

重头戏是问题的修复。现在新建一个渠道，输入你好、点击创建新渠道，二维码不会出现。原因很明显：generateQRCode 不会随着 channels 数组的递增而调用。所以必须监控 channels 的变化，拿到新添加的一项，手动调用一次 generateQRCode。这自然想到 watch。

添加 watch：source 是 channels，回调接收两个参数，newChannels 和 oldChannels。先打印 changes 看它有没有被调用。回到页面创建一个渠道，发现 watch 并没有执行，但数组确实添加成功了。

为什么回调没有被触发？在文档中找答案。Vue3 文档里有一节 Watch on Arrays，标注为 breaking change，大意是：watching array 时，回调只会在数组被替换时触发；如果需要在数组被 mutation 时触发，必须指定 deep 选项。watch 除了 source 和回调，还有第三个参数 options，其中就有 deep，把它设置为 true。再测试：创建新渠道，changes 能被成功触发了。

第一步完成之后，再看 newChannels 和 oldChannels 的区别。只打印它们的 length，再创建一个渠道，结果是 newChannels 是 4，oldChannels 也是 4，两个数组完全相同，根本无法比较长度、拿到最后一项。

这又是为什么？另一份 V3 文档里，reactive computed watchers 下的 Watching reactive objects 一节是这么描述的：对于 reactive 对象里包裹的数组或对象，如果想比较前后的值，需要在 watch 时创建一份拷贝。因为我们原来的做法等于是在传递引用，两个对象当然完全一样。文档的示例就是创建拷贝，对比较深的对象还使用了 lodash 的 cloneDeep，这样前后就是两个完全不一样的值了。

除了拷贝，还有一种做法：在 mutation 中用 immutable 的方式修改 channels。来到 editor.ts，之前我们是 `state.channels.push(data)`，这是 mutable 的方式，直接修改了 state.channels 这个数组。现在改为返回一个新数组：`state.channels = [...state.channels, data]`，把前面的展开，data 填在后面，这就是 immutable 的修改。再测试：创建新渠道，newChannels 等于 2，oldChannels 等于 1，成功拿到了不一样的两项。

既然用了 immutable 的方式，deep 选项也不需要了，把它删掉。接着对比两个数组的长度：如果 newChannels 的 length 大于 oldChannels，说明新添加了一项。这时要拿到新数组的最后一项，可以用 lodash 的 last 方法，引出来之后 `const createdChannel = last(newChannels)`。因为返回值可能是 undefined 或 ChannelProps，所以要判断它存在，存在才调用 generateQRCode 生成二维码。回调需要改成 async 才能用 await。

现在来测试：添加一个 test、一个微信，点击创建新渠道，二维码还是没有出现。我打了一个 console，发现 generateQRCode 内部拿到的 ele 节点是 null。这里我一下就明白了：之前讲 watchEffect 时提到过运行顺序。watch 的第三个参数（就是刚才放 deep 的地方）有一个 flush 选项，默认是 pre，也就是在 DOM 节点更新之前运行，此时新渠道的 DOM 节点根本还没有生成，自然拿不到。把 flush 调成 post，意思是在 DOM 更新之后再运行里面的操作。再测试：点击创建新渠道，节点能拿到，二维码出现了。

经过这一系列努力，现在可以对新创建的渠道生成二维码了。这节课掌握的关键是针对 reactive 对象使用 watch 的一系列处理方法，现在你对 watch 的应用应该更清晰了。
