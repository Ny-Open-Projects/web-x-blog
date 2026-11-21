# 6-4-LText 添加通用属性

上一节课完成了非常初级的 LText 组件，同时留下了两个问题。这一节先完成第一个：整合 LText 的 props，让业务组件可以快速添加各种属性。

我们的组件有怎样的属性呢？看看之前写的文档。业务组件需求文档中有组件的分类，下面是组件的属性。LText 属于文本类的基础组件，基础组件的属性分为两部分。第一部分叫通用属性，它对每个基础组件都存在，而且要有默认值；除此之外还有特有属性，文本组件有这些特有属性。两方面加在一起，就组成了 LText 的整体属性。

自然可以想到需要一个通用属性的数据结构。我在 src 下面创建了一个文件，叫 defaultProps.ts，在里面放置所有的通用属性。创建一个 commonDefaultProps，把文档中的属性复制进来，里面就是所有通用属性和它们的默认值。可以看到我是按文档中的尺寸、边框、阴影、透明度这样分类的，注释都已经写好。除了通用属性，每个组件还有特殊属性：文本组件的属性就是通用属性混合上它的特殊属性，得到 textFontProps 这个数据结构。textFontProps 里是文本独特的属性，直接用三个点 spread 把 commonDefaultProps 混入，就完成了整个属性。

其实这些就是组件的所有属性了，要添加到 props 当中去。所以需要把这个结构做一个动态转换，转换成什么样的呢？拿 text 举例，把它转换成另一个 object，里面有 type，是 constructor 类型，还有一个 default 值，直接拿到值就可以了。转换以后就能拿到组件对应的 props 属性。这类似于数组的 map，只不过作用在 object 上。lodash 有这个功能，不用自己写。

这个方法叫 mapValues。看它的例子：有一个 user 这样的 object，使用 mapValues 后 key 还是一样的，value 转换成另外的格式，正是我们想要的。来做这个转换。创建一个函数 export，名字长一点，叫 transformToComponentProps，命名要写清楚函数是干什么的，长一点其实有必要。参数 props 的类型呢？它可能有多种类型，就用 index type：key 是 string，value 是 any。

返回什么呢？从 lodash-es import mapValues，return mapValues(props, ...)，把 props 传入后能拿到每一项，每项称之为 value。第一项是 type：要拿到类型上的构造函数，可以直接调用它的 constructor 属性，value.constructor 就拿到了它的构造函数；default 值就是 value 本身。这样就完成了转换。

现在导入使用。上一层目录就是 defaultProps，需要函数本身 transformToComponentProps，还需要 textDefaultProps。然后进行转换：`const props = transformToComponentProps(textDefaultProps)`，这样就获得了对应的类型。接着替换原来手写的 props：tag 我要留下，因为它不属于这些通用属性，属于另类的属性；把原来手写的 text 和 fontSize 删掉，把转换结果 spread 展开，就完成了修改。

第一个问题解决了，继续修改 styles 的获取。现在需要拿到所有样式属性的名称。所有属性由两部分组成：样式属性和其他属性。我们要拿到所有样式属性的 key 组成的数组，因为 pick 的第二个参数是一个数组，所以要把其他几个属性剔出去。怎么剔除？lodash 又来帮我们了：without 是数组上的方法，前面提供数组，后面提供想要剔除的值，最后返回剔除完的数组，很合我们的口味。

来弄一下。继续 export 一个 const，称之为 textStylePropsNames。使用 without，先把 without 导进来。第一个参数是所有的键，可以用 Object.keys(textDefaultProps)；要剔除的属性就手打了，因为知道有哪些通用的要剔出去：actionType、url、tag 和 text 这几个不是样式属性，属于其他属性，把它们剔出去。复制进来（不手打了），就获得了 textStylePropsNames，它也是一个数组。把它导进来，在 pick 那里做替换，保存。

看看最终结果。页面刷新一下，发现内容都挤在一起了，因为默认属性里有 component 的 top、left 值（可以看到 left、top），而且 position 是 absolute。现在暂时禁用一下，看得更清楚一点：我们还不到做定位的时候。在样式里加一个 position: relative 先暂时覆盖，保存。现在样式都出现了。为了体现其他样式，我在 editor.ts 中又多加了几个属于我们属性中的 CSS 样式，比如 color 和 fontSize。现在 color 和 fontSize 都成功应用了，上一节课提出的问题之一就完成了。

不过再看我们的 text，现在有一个问题：模板报错了。因为现在我们的 text props 没有被成功推断，变成了这种宽泛的类型，所以找不到 text 属性。实际上除了 tag，其他一系列属性都找不到，这不是我们想要的。我们希望在模板中也能推断出正确的属性，并且享受自动补全，这需要做一点小小的进化。

下节课一起来解决。想一想：一个函数想获得它传入的属性的类型并且对应地返回，相信大家眼前一亮，知道该用什么特性了。这里先卖个关子，下节课再讨论。这节课就到这里，谢谢大家。
