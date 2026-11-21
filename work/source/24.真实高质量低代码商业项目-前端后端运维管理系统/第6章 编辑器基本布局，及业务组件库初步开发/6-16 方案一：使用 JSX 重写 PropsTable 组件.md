大家好，上节课呢，我们说到在 Vue 的单文件组件中，template 部分呢，假如直接渲染一个 v-node，那会以字符串的形式直接输出它整个 object 内容，而不会将它转换成对应的虚拟 DOM 节点并且展示。

这节课呢，我们就来解决这个问题。

第一种解决方案，大家肯定能想到，那就使用这个 JSX 直接替换 SFC，就是 Single File Component 的写法。

那么 JSX 天生就是转换成 v-node。

啊，那么直接呢，在 JSX 中写 Vue 的变量，那肯定会被完美转换。

那么我们这节课呢，就来完成这个任务。

现在呢，我们这个 template 大家可以看呢，写的也是比较复杂。

那么 JSX 和 Vue template 写法上有一些差异，正好我们可以做一个对比，来看看它们的差异在哪里。

好，我这里已经新建了一个同名的 props table，不过它的后缀名呢是 TSX。

我们把它写到这个生成 final props。

这个代码的地方，然后呢，我们要想返回一个 JSX，我们可以看到在 setup 中呢，我们可以 return 直接返回一个 function，在这里，然后呢，这个 function 里面再返回你想要返回的对应的 JSX 就好了。

我已经写到这里，好，那么 final props 已经包括了我们这个属性的对应关系。

我们现在第一步是循环它，我们没有了 way for，那么循环一个 object，我们就可以使用 object keys 方法啊。

我们来跟原来相对比一下啊。

大家可以看，我们从这里开始写啊。

那么自然呢是 object keys，那么应该是 final props。

注意呢是 value，因为它是一个 computed props map。

这里面呢我们称之为 key。

好，首先呢我们在这里拿到 value，那就是 value 呢等于 final props 点 value 啊。

那么是上面的 key。

好，拿到以后呢，我们就先 return 最外面这个结构。

我们创建一个 div，它的上面的 key 呢就是 key，class 呢这里有是 prop item。

好，第一个最简单的呢是我们要输出这个 label，这个很简单，这里呢没有为 if，我们可以直接使用这个 JavaScript 表达式来写啊，那就是 value text，那我们就写后面的这个 span 结构啊，我这里直接复制一下就可以了。

好，接下来呢，我们把这个 label 写完以后呢，后面呢是一个我们的这个 class 等于 raw component。

好，我们来看一下界面啊。

大家可以看到，现在 label 呢已经循环的展示出来了。

好，现在呢遇到了我们的这个第一个难题啊。

第一个难题呢，我们在 view template 中呢，假如我们要渲染一个动态的组件名啊，我们使用了 component is 这种写法。

但是在 JSX 中呢，我们是不能这样做的啊。

对于那个动态的名称呢，我们必须拿到它的组件实例，然后把一个变量呢赋值给组件实例。

假如因为你是变化的话，注意呢，这个变量最好是大写的，它的代表它是一个组件。

好，这里呢，由于我们只有组件的名称，大家记得呢，我们的 props map 我们打开看一下。

好，在这里这个组件名称呢，而且它也是这个 string。

所以，我们必须建立一个 string 和它真实组件实例的一个对应关系。

我们来看一下该怎么做。

我们回到这里，首先呢，我把它的实例都拿出来，就是 on design view 这些我们需要的这些组件的一系列的实例。

然后呢，我们建一个 key value 的一个对应关系。

我们这里已经写好了，复制一下。

哎，我们可以看一下，那就是 a tax area 对应的是 input 下面的 tax area，这些都是组件的实例。

啊，我们特别注意呢，有些组件呢，它是在这个主要组件上面的属性上面的啊，比如说 input 点 text area， text area 就是它属性上面的啊，下面也有，比如说 radio group、 radio button、 select option 等等很多。

好，现在呢，我们就可以根据这个字符串呢拿到这个组件实例了。

我们来看一下怎么做。

好，我们回到这里，那么我们就称之为 component name，大写一下。

好，那就是 map to component。

这里面呢，我是使用这个 value .component。

好，这样就拿到它的这个实例，然后我们就可以进行一个渲染了。

这很简单了，我给它复制一下，在这里面。

好啊，这样就完成了一个渲染。

我们来看看界面上它怎么样，产生效果没有？

我们点击一个，哎，大家可以看到呢，现在这些这个内容呢，这些组件呢都已经出现了。

好，我们接下来继续来做。

同时呢，我们要把这个子组件添加一下。

子组件呢很简单，首先呢，我们把这个照猫画虎，我们把这个 sub component 的 name 也添加一下啊。

这里我直接复制就好了，这个没有什么难度。

我们可以看一下啊， sub component 啊，我们先判断 sub component 是否存在，然后就取啊。

然后呢，我们在这里面进行一个循环，那就是当然使用的是 value option 啊。

Value dot option, it, if it exists, ah, it's the same logic as the previous one. You can see it's similar to if. So, if it exists, we use value dot options dot map. Then, each of its items is called option. Okay, here we return, that is sub component. Ah, sub component. Then, its properties are value. Then, it equals.

option点value上面这个字呢，就是option点text，option点text。

好，我们就完成了这个渲染。

我们来看看我们现在这个组件长什么样。

大家可以看到，现在它的选项呢都有了，而且我们点开字体呢，虽然这里有点短啊，但是呢，我们现在这个朝思暮想的这些这个font family呢已经出现了，所以我们这个vno的渲染呢是非常的成功。

好，那么下一步工作呢是添加属性。

我们在 G S X 中添加属性呢，就像在这个 H T M L 标签上添加属性一样。

比如刚才我添加的这个 sub component 上面的这个 value 属性，我们就可以直接写 value 等于花括号包裹的这个值。

但是呢，我们现在在这个主要的这个 component 上面呢，它的属性比较多，不仅有 key 是可变的这个 value prop 啊，还有一系列的 extra props。

为了解决这个问题呢，G S X 还支持在标签上进行一个 spread 写法，就像类似这样的，可以将我们的属性呢全部展开。

所以这时候呢，我来创建一个这个 props，好，在这里 props 好。

首先呢，我们是要拿动态的 value prop，它的值呢是 value 点 value，然后我们还有一系列的 extra props，就是我们给它展开就好了啊。

extra props. 最后呢，我们把这个 props 呢在这上面进行一个动态展开，就是 component name. 好，现在呢，我们来看看我们的这个属性呢是否出现。

大家可以看到呢，现在属性呢已经上来了。

我们再点击这个看一下，我们看一下宋体、黑体、楷体、仿宋。

现在我们定义的这个样式已经成功的出现了，非常开心。

好，现在属性呢已经全部出现了啊。

最后呢，我们要添加事件了啊。

不同于 template 的写法啊，在这里我们可以看到。

原来 template 是 v on，然后是 click。

那么我们在 JSX 中写法呢？

我们可以事件的属性名称呢？

我们这么写，我们是 on 加上一个事件名称，后面这个事件的第一个字母要大写。

所以呢，我们现在需要将它这个命名方式呢转换一下。

我们可以看到这个 event 现在是这么写的，所以我们要在这里进行一个转换。

首先呢，我们需要一个帮助函数啊，帮我们把字符串的第一个字母呢转换成大写。

这里已经建立好了一个，先放在这里。

好，capitalize first letter。

然后呢，我们在这个 events 里面做一个简单的转换，那就是首先呢，我们要 on，然后呢，加上我们的这个新建的函数啊， capitalize first letter 啊，我们把这个给它包裹一下。

好，这样呢，我们就完成了这个事件的改造。

最后呢，我们把这个值呢，因为它也是一个属性，那么也加到这个属性当中去。

那就是 value点儿 advance给它展开放到里面去。

好，我们最终呢来测试一下我们结果是怎么样。

好，现在呢我点击看看它是否会更新。

我们可以看到中间这个字号进行了一个更新，点击中它已经换了位置。

然后呢，我们来试试我们的心爱的字体楷体，没问题；

黑体都会变成这个对应的字体。

好，那么展示更新都没有问题啊。

我们这节课的任务就完成了。

我们使用 JSX 呢，替代了这个 template 的写法。

大家特别要注意呢，刚才我们提出的三点，这两个完全不一样的点，大家觉得怎么样？

你更喜欢哪一种呢？

下节课呢，我们来看看使用 template 怎样来完成这个任务，同时呢，对比一下 JSX 和 template 写法的两种写法的一个优劣。

好，到这里吧，谢谢大家，再见。

