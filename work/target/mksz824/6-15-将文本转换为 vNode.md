# 6-15-将文本转换为 vNode

上节课我们简介了虚拟 DOM 和组件的关系，还使用 h 函数创建了 VNode 节点。这节课把普通的 text 形式转换成一个丰富的 VNode 类型。

首先修改类型。要展示的下拉菜单 option 中的 text，现在还是一个简单的 string 类型，这里给它加一个 VNode 类型。VNode 是 Vue3 内置的类型，我们把它导进来。text 可以是 string 也可以是 VNode。

做完类型修改就来转换。先把字体相关的数据单独拿出来复制一下，放在这里，称之为 fontFamilyArray，里面有 text 和 value。接下来要把 text 从原来的普通 string 转换成一个 span 的 VNode 节点。首先需要把 value 中的值赋到这个 span 上面去，想到用 map 方法做转换：创建一个 fontFamilyOptions，等于 fontFamilyArray.map，拿到想要的字体，return 一个对象，value 是一模一样的，直接返回 font.value。

text 这里就要使用 h 函数来创建了。把 h 引过来。h 有三个参数，之前说过：第一个是节点名称，这里称之为 span；第二个是各种属性，可以有 props、class 和 style，这里需要的是 style，style 中需要 fontFamily，等于 font.value；最后一个是 children，也就是它里面的值。我们这里只有一个文本节点，所以自然是 font.text。这样就完成了对应的转换，把原来的 text 转换成了一个丰富的 VNode 节点。

然后把这个替换一下：原来的数据不需要了，删掉，使用三个点展开式把它添加到选项中。第一个是"无字体"那一项，它原来没有字体，所以不用转换。

除了使用 h 的方法，当然还有另一个方法。上节课说过，TSX 其实就是 createVNode 的语法糖，而且我们项目直接支持这种写法，比写 h 函数方便一点。换一种写法看看是不是节省时间。首先把后缀名改一下：原来叫 ts，改成 tsx，点 Rename 替换成 tsx。现在用 TSX 写法替换这段：先删掉，直接写类似 HTML 的结构。创建一个 span，它的属性直接写 style，里面是 fontFamily，值应该是 font.value，最终里面是 children，值是 font.text。这样语法糖就写完了，是不是比原来快捷很多？

但是发现这里报了一个错误。因为现在 text 返回的是一个 JSX，JSX element 是一个通用的全局类型，在不同的库里需要自定义它的具体样式，而我们是 VNode。所以这里要做一个类型断言，把它断言成一个 VNode：`as JSX.Element as VNode`（或者直接 as VNode）。这样就不会有错误了，错误消失。

做完这步工作，把它展示到 PropsTable 上看一看。首先修改一下类型：OptionText 要做同样的修改，它也可以是 VNode，要不然会报错。现在没有错误了。到界面上看看会不会展示出最终的内容：刷新，点击选择字体。可以看到，它没有展示出 HTML 结构，而是直接把 VNode 对应的 object 展示出来了。虽然这里看不全，但知道它就是 VNode 最后生成的一系列 object，并没有转换成我们想要的 HTML 或者 DOM 结构。

这该怎么办呢？留一个问题，下节课一起来解决。这节课到这里，谢谢大家。
