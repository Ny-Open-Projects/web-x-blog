上一节课呢，完成了一个非常初级的 LText 组件，同时我们留下了两个问题。

第一个问题呢，我们就是这个整合 LText Props，让这个业务组件呢可以快速的添加各种属性。

让我们先来完成这个任务。

我们的组件呢有怎样的属性呢？

让我们看看之前写的文档。

我们发现呢，业务组件需求这个文档中呢有这个组件的分类，下面有组件的属性。

我们可以看到 LText 呢属于这个文本。

也就是这个基础的组件，基础组件分为两部分。

第一个呢叫做这个通用的属性，这个通用属性呢对每个基础组件来说呢它都是存在的，而且呢是要有默认值的。

除了通用组件呢，我们还有这个特有属性。

那我们的文本呢有这些特有属性，这两个方面加在一起呢就组成了我们 L text 的整体属性。

所以呢，首先呢我们自然能想到一个通用属性的这么一个数据结构。

这里我创建了一个文件。

在这根目录 s2c 下面，称之为 default props。

我们在这里面放置所有的这个通用的属性。

我们来创建一个 common default props，在这里复制一下。

这里面就是所有的通用的属性和它们这个的默认值啊。

我们可以看到，我是按这个进行分类的。

我们按这个文档中尺寸呀、边框呀、什么阴影啊、透明度，按这个进行一个分类。

这个注释都已经写了。

除了通用属性，刚才我们说的呢，每个组件还有这个特殊的属性。

文本组件的属性呢，就是这个通用属性混合上它的特殊属性，我们就能得到这个 text font props 它的这么一个数据结构。

我们来看一下，除了通用属性，那么我们还有这些文本的特有属性，这里已经创建好了，给大家复制过来。

text font props，我们可以看到这里是它独特的属性。

这个呢，直接把 common default props 使用三个点儿 spread 来给它混入，就完成了整个的属性。

其实呢，这些呢就是组件的所有属性了。

我们要添加到 props 这里当中去，所以我们需要把这个结构呢做一个动态的转换，转换成什么呢？

其实呢，就是把这个结构那么转换成类似一个这样的结构。

Text 啊，我们就拿那个 Text 举例啊，我们把它转换成一个另外的 object，这里面有这个 type。

它是一个 constructor 类型的，那还有一个 default 值，自然呢直接拿到这个值就可以了。

进行这个转换以后呢，我们就可以拿到 components 对应的 props 属性。

这里其实是类似 map 数组的 map 一样的 object 转换，只不过它是作用在 object 上面去。

这时候呢，大家记得这些功能的 low dash 都是有的，我们不用自己写，我们求助一下 low dash。

我们可以看一下这个呢，属性称之为 map values。

我们可以看到 object 下面有一个 map values 这么一个方法，可以看一下它的例子。

它有一个 user 这样的这个 object，然后呢，你使用 map values 以后呢，它会可以把它转换成啊 key 还是一样的，那么 value 转换成另外的一个格式，这正是我们想要的。

来做这个转换吧。

创建一个函数呢，我们 export 我们称之为长一点啊，transform to component props。

注意这个命名呢，我们也要写清楚我们这个函数是干什么的，所以长一点呢其实是有必要的。

props，那么它是个什么类型呢？

它是个index type，key是个string类型，any类型。

我们的props可能有这个多种的类型，这里面我们就给它设置成any吧。

返回什么呢？

我们这里直接return values拿出来，那就是import。

From lodash ES, 我们需要这个 mapValues. Return mapValues. 我们把这个 props 给它传入，然后呢，就能拿到每一项。

每一项我们可以称之为 item. 这时候呢，我们 return. 刚才我们都说了，第一项呢是 type.

假如我们要拿到这个类型上面的一个它的构造函数是什么呀？

我们实际上可以直接调用它的 constructor 这个属性。

我们来看一下啊，item 点 constructor 就拿到了这个它的这个构造函数，类似这样的一个构造函数。

它的 default 值就是 item 本身。

这样呢，我们就完成了这样的一个转换。

现在呢，我们把这个来给它进行一个导入。

你的上一层就是 default props。

我们需要这个函数本身 transform to component props。

我们呢还需要这个 text default props。

这时候呢，我们就可以进行一个转换了。

ask default props 就等于 transform component props，然后把这个 text default props 给它传进去，这样我们就获得了对应的这个类型了。

我们这时候呢，把这个进行一个替换。

这个 tag 我是要留下的，因为它是不属于这些通用属性上面的一个另类的属性，所以说我们把这两个给它删掉，把它 spread 展开，这样就完成了这么一个修改。

现在我们解决了第一个问题啊，我们继续来把这个 styles 做一个修改。

现在我们需要拿到所有的 styles 属性名称。

我们知道呢，我们所有属性呢是由两部分组成的。

这里其实我们就拿到所有的属性名称，但是呢是由两部分组成的。

我们可以看一下啊，样式属性除了这部分呢，还有其他属性。

我们现在要做的呢就是拿到所有样式属性的 key 组成的数组，因为它第二个参数呢是一个数组，所以呢我们需要把其他几个属性给剔出去。

怎么样剔出呢？

剔出一个属性里面特定的一些 key 呢？

可以看一下 lodash 啊，它又来帮我们了。

所以我们可以使用一个 without，它是 array 上面的一个方法。

来看一下，我们首先前面提供一个数组，然后呢后面我们提供我们想要剔除的一些值，最后返回的就是剔除完的一个值。

看起来很合我们的口味，我们来弄一下。

好，我们在这里呢 default class 你继续进行一个修改， export class 我们称之为 tax style。

props names. 然后我们使用 without，先把 without 给它导进来。

without 第一个呢是我们这个 key 的这个所有的键可以使用 object keys。

以及 text default props。

我们要剔除的属性，这个我们就手打了，因为我们知道呢，它会有哪些通用的要剔出去。

首先这几个它明显不是这个 action，它这两个明显不是我们需要的。

接下来呢，还有一个 text，这三个呢不是我们这个样式的属性，而是属于其他的属性，所以呢我们把它给剔出出去。

我们来复制一下吧，我们不手打了。

这时候我们就获得了这个 text style props names，它也是个数组。

如果我们把它导进来，这里那就是在这里。

把这个进行一个替换，保存。

现在呢，我们来看一下我们最终的这个结果是什么样的。

那页面我们刷新一下，现在发现我们的这个都挤在一起了，因为我们这个默认属性呢有这个 component 的这个 top left 值啊，我们可以看一下 left top，而且它的 position 呢是 absolute。

我们现在呢，暂时给它禁用一下，这样我们看的就更清楚一点。

因为现在呢，我们还不到做定位的时候。

那我就在这个样式这里加一点，这里加一个position的relative，先把它暂时覆盖一下，保存一下。

我们可以看到呢，现在我们的样式呢都已经出现了。

这里呢，为了体现其他的样式呢，我在这个editor T S中呢又多加了几个这个我们已经属于我们这些属性中的这个CSS样式，比如说color。

Font size. We can see that now color and font size have both been successfully applied. Now we have completed one of the questions raised in the previous lesson. However, let's look at our text. Now it has a problem. We find that there is an error in the template. Because now our text props have not been successfully inferred, but have become this type. Therefore, we cannot find the text property. In fact, except for the tag property,

我们其他的一系列的这个属性呢，都是找不到，这不是我们想要的。

我们希望呢，在模板中也能推断出正确的属性呢，并且可以享受自动补全。

那么这里呢，需要做一点小小的进化。

下节课让我们一起来解决一下。

我们想一想，一个函数想获得它传入的属性的类型，并且对应的返回，相信大家都会眼前一亮啊，知道我们应该用什么特性了。

这里先卖个关子，我们下节课再来讨论。

这节课呢就到这里，谢谢大家，再见。

