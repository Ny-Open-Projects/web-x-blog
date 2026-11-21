# 6-3-LText 组件初步实现

上节课我们循环输出了 editor store 中的内容，但它现在还是一个非常蠢的 div，需要用业务组件库的组件来代替它了。那现在是否要创建一个单独的库进行开发呢？分析下来它最终肯定会有一个单独的 repository，但对于这种情况，我觉得现在没有必要。项目初期，这种特性的开发可以先按照方便的原则进行，等基本功能和验证都开发完毕，再将它统一移动。

这一周我希望把渐进式开发的思路放在大家脑子里：有了技术方案的总体指导方针，实施过程中可以采用小步快跑的方式，将一个特性慢慢丰富，而不是一下想吃成胖子。把所有特性罗列起来，先从简单的出发，在开发过程中善于对现在的解决方案提出问题并加以改善。

第一个业务组件可以称之为 LText 文本组件。暂定它有两个属性，但它们非常有代表性。看技术方案：我们希望业务组件把属性分成两大部分，一个是样式属性，一个是其他属性。样式属性选择 fontSize，其他属性选择它里面的内容 text。所以先修改假数据：在 store 的测试数据中，text 已经有了，多加一个 fontSize 当作样式属性。

现在创建组件。我已经写好了 LText.vue 的架子，它在 components 下面，现在写它的逻辑。逻辑很简单，首先要确定 props：text 的 type 是 string；fontSize 的 type 也是 string；再多加一个属性叫 tag，让用户可以自定义传入标签，默认是 div。假如你想更语义化，可以传入 h2 二级标题或者 p 标签等等。tag 的 type 是 string，加一个 default 默认值，默认值就是 div。属性加完了。

接下来在 setup 中完成功能。从技术文档可以知道，我们需要从所有属性中找到其中的样式属性（也就是 CSS 属性），并作用到模板的 style 属性上。从一个对象中找对应的 keys，相信大家都会做，但这里我不自己写，而是用一个工具，大家都熟悉，就是 lodash。它提供了非常多的函数，在对象、数组和函数上做扩展功能，非常方便。用 `npm install lodash-es --save` 安装。特别注意它还需要定义文件：`@types/lodash-es --save-dev`。

有同学也许分不清 lodash 和 lodash-es 这两个模块的区别。lodash-es 是 lodash 的姊妹版本，关键在于后面的 -es 代表 ES Modules：整个模块都采用标准的 ES 模块书写。对于使用支持 tree shaking 的打包工具（比如我们用的 Webpack 或 Rollup）来说，打包会非常友好，能大量减少代码体积，所以这里使用 lodash-es。

现在需要从一个对象中找出特定属性并返回一个对象，可以用 pick 方法。看它的例子：传入 object 和一个数组，返回选中的键，跟我们的需求非常类似。回到代码，首先引入 lodash-es 的 pick：用 pick 从 props 中挑出 style，得到 styleProps。特别注意要使用 computed，让它返回响应式对象，因为传入的 style 有可能改变，我们希望组件跟着一起改变。pick 第一个参数传入 props，第二个参数是数组，我们目前只有一个样式属性 fontSize，把它 pick 出来，然后 return styleProps。看一下它的类型：styleProps.value 点，可以看到它已经能找出 pick 出来的 fontSize，类型非常完备。

有了它就可以在界面中展示了。由于标签不是固定的，可以使用 component is 的写法：写 `<component :is="tag">`，is 对应 props 上的 tag 属性（默认 div），再把 style 传进去，也就是 styleProps；再传一个 class，称为 l-text-component；最后把 text 放在里面，LText 的初步开发就完成了。

现在把它循环展示在界面中，自然要回到 editor.vue。因为 LText 不是全局组件，需要 import 进来：from 上一级的 components/LText.vue，注册到 components 里。然后在模板上替换原来直接放的 div。要动态展示一个组件，所以也使用 component 标签，加上 v-for：component in components，key 写 component.id，is 是它的 componentName，最后用 v-bind 把所有属性都绑定上去，也就是 v-bind="component.props"。循环输出组件的任务就完成了。

到界面上看看能否完美出现。刷新一下，它已经出现了，而且 style 属性开始作用：每个元素的 fontSize 都不一样，样式属性已经生效，字体大小都变化了，text 也正常展示。

但现在这个 LText 组件肯定是有问题的。课程开始时说过，现阶段就是用最简单的例子开发，在开发中发现问题并完善。现在有什么问题呢？第一，业务组件的样式属性很多，不只是这一个 fontSize。假如要一个一个写，比如有十个属性，无疑要累死；同样 styleProps 的第二个参数也是写死的。我们需要想办法完成重用并且简化。第二，多个业务组件（我们有 LText，至少还有 LImage、LShade 等等，可以扩展出很多）有可能都需要把 style 从所有属性中摘取出来的功能，这是技术文档分析的基本做法，我们自然希望找一个通用的方法将它抽离出来，做成一个独特的函数，抽离并获得 styleProps 的逻辑。

通过开发我们发现了这两个问题。今天第一步就开发到这里，大家可以在课下思考一下怎样完成这个任务，下节课一起来解决这个难题。这节课就到这里，谢谢大家。
