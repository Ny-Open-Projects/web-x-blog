# 8-22-扩展知识：Element 类型家族之间的关系

这节课要完成图片上传以后的一个需求：根据图片的真实大小设置它的 CSS 宽度。

## 需求背景

有的同学也许会说，设置一个 max-width 属性不就可以了吗？但请记得，我们的设置选项里 props 中有 width 属性，所以必须在开始时给它设置一个比较恰当的宽度值。能直接设置成编辑器的宽度 375px 吗？可以，但肯定不是完美的解决方案。比如这张图的真实大小是 184px，强行设置成 375px 就会发生图片模糊。我们希望获得上传图片的真实宽高：真实宽度小于编辑器就用原来的值，大于最大宽度就用最大宽度。

现在的问题来了：我们只有一个图片的 URL，怎样通过 URL 获得图片的真实宽高？这是一个很好的可以扩展知识面的问题。

## HTMLImageElement 与类型定义文件

首先来到一个大家平常经常使用的标签：img。也许有人会说这有什么稀奇，所有人都在用，平平无奇。但它的 DOM 节点有一个神奇的类型，称为 HTMLImageElement，是标准 Web API 的一部分。在 TS 中看一下这个内置类型：const 一个 HTMLImageElement，点过去可以看到它有两个定义。看 interface 的定义，它属于内置的 lib.dom.d.ts 的一部分，有一系列属性和方法。

其实大部分 HTML 标签都有一个对应的类型。之前我们多次遇到 HTMLInputElement，获取 input 的 element 时就是那个类型，它和 HTMLImageElement 是平行的类型。翻阅 TS 定义会发现大多数标签都能在这里找到对应的类型：HTMLIFrameElement、HTMLHyperlinkElementUtils，还有 HTMLElement 等一系列定义。看这个定义文件能学习很多 API 的用法。

## 家族溯源

从 ImageElement 网上溯源，看它继承了什么：它继承了一个称为 HTMLElement 的类型。找它的 interface：这是一个 HTML 通用的类型，上面有一大堆通用属性，很多我们都很熟悉，hidden、innerText、offsetHeight、offsetLeft，click、addEventListener 等方法。

还能继续往上吗？HTMLElement 还继承了 Element。Element 是文档对象 Document 中的一个基础对象，里面也有一些熟悉的属性，比如非常常用的 classList。它还有很多不同元素类型的子类：比如 HTMLElement 继承了 Element，SVGElement 也是 Element 的子类型。

有点停不下来，继续往上。Element 继承自 Node。Node 有点意思：它是一个基本的抽象类，没有一个真正的 Node 对象，现实浏览器中没有一个跟 Node 完全相同的对象，所有实现都是基于它的子类。它包括了 document、刚才说的 element，还有 document fragment。

最终还可以继续往上：Node 继承自 EventTarget。EventTarget 是一个 DOM 接口，可以接收事件，并且可以创建监听器。element、document、window 都是最常见的 event target，其他对象也可以作为 event target，比如我们很熟悉的 XMLHttpRequest。

## 类型断言的应用

所以在 uploader 中的 handleFileChange，大家想起来没有？它的参数 e 是一个 event 对象，e.target 的类型是 EventTarget 或者 null 的联合类型。EventTarget 是所有元素最大的祖先。所以我们可以把它断言成一个更具体的类型 HTMLInputElement，这就是类型断言的一个应用：将一个父类断言为一个更具体的子类。

通过这张图，我们搞清了 element 之间的来龙去脉，它们的家族是怎样延续的。从一个获取图片大小的需求衍生出这么多知识点，是不是很有意思？

## Event 家族与 MDN

我又发现另一个有意思的类型：event。除了定义 event，我们还定义了 DragEvent，它们看起来也是紧密联系在一起的。它们的关系是怎样的？大家可以带着这个问题看看 event 家族之间的关系，可以参考 MDN 的网站，这张图就是从 MDN 上拿来的。从 MouseEvent 点进去，写得非常清楚，并且有类似的图帮你描述，大家可以自己去了解。

最后强烈推荐 MDN 文档网站：它是我开发这么多年以来的良师益友，是我见过最丰富、最准确的文档网站，请大家善于利用。

下节课回到正题，看看怎样通过 HTMLImageElement 这种类型的元素获取图片的实际大小。这节课先到这里，大家再回顾一下这张继承关系图，很有意思。谢谢大家。
