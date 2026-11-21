# 6-5-LText 使用 hooks 重用逻辑

这节课完成上节课留下的代码升级工作。上节课特别说到，transformToComponentProps 这个转换函数的返回并没有像我们想象的那样：可以推论传入的类型并返回。解决方案大家应该都知道：一个函数想在调用时把类型流入函数体内再流出来，肯定要使用泛型。

看看它的使用位置，在 LText 中调用。我们希望调用这个函数时把类型流入函数体内，再流出到 defaultProps。来到 defaultProps.ts。这是一个箭头函数表达式的泛型：在圆括号的左边加上泛型 `<T>`，参数也就不需要写类型了，直接赋值为 T。这么简单就改完了吗？看一下，发现了一个错误。原因是 mapValues 对第一个参数是有要求的，而现在的 T 没有任何类型限制。这里就可以用之前说的泛型类型约束来解决：我们希望 T 满足参数之前的条件，之前参数是一个 index type，key 是 string，value 是 any。使用 extends 关键字，T 必须满足这个需求才可以当做参数，拷贝过来。错误就消失了。

保存后看 LText 中的最终结果。现在流入的是 textDefaultProps 类型，流出的 defaultProps 都有对应的提示，一一对应。再往里添加属性，text 的错误消失了；点任何属性时，都能联想出 props 上的所有类型，比原来方便了很多。比如点 font，关于 font 的一些值就出现了，这个任务完美完成。

这里得意一下，再强调一遍：我们将泛型传入，然后用 mapValues 处理，它其实也是有类型的，点进去看，它同样以泛型的方式把类型传入再完美地返回，经过了多层的处理。大家有空可以看看 mapValues 的类型定义，写得非常精彩，看看自己能不能看懂。

完成这个任务后，再处理组件重复的逻辑。业务组件中已经写了一些重复的逻辑。第一个是 styleProps，这是一个重复的逻辑。不过它其实很简单，只有一行代码，可以提取也可以不提取。除了它还有一个重复逻辑，看需求文档：业务组件有一个事件功能属性，事件类型可以选择跳转 URL。假如选择跳转 URL，点击以后就跳转到对应的 URL 地址。这是一个重复的逻辑，可以把这两个逻辑都抽象到一个钩子函数中。

我创建了 hooks/useComponentCommon.ts 文件，把两个逻辑抽象在其中。创建函数 useComponentCommon。首先把 props 传进来，这里又想到跟刚才一样，最好使用泛型把 props 的类型流动进来，返回的值就能带上对应的类型，照抄刚才的泛型约束。除了 props 还有第二个参数，就是 pick 哪些 style 的参数，称之为 picks，它是一个 string 数组。

这个函数要返回两个内容。第一个当然是 styleProps，照猫画虎跟那边一样：computed 调用 pick，第一个参数是 props，第二个参数是我们的 picks 数组。第一个功能完成。第二个功能是 handleClick，点击时的一个 handle，因为是点击后的回调，就是一个 function。做一下判断：假如 props.actionType 等于 url，并且 props.url 不为空，就进行跳转：`window.location.href = props.url`。逻辑写完。两个逻辑写完以后，不要忘记把它们都返回：一个是 styleProps，第二个是 handleClick。最后 export default useComponentCommon。

有了它就可以导入使用了：import useComponentCommon from 上一级的 hooks/useComponentCommon。把原来 LText 中的两段逻辑删掉，用这个 hooks 取代：`const { styleProps, handleClick } = useComponentCommon(props, textStylePropsNames)`，第一个参数是属性 props，第二个是要拿掉的 styles 数组。把返回的 styleProps、handleClick 接收下来，再把 click 的逻辑加到模板上，也就是 @click="handleClick"。

保存后看页面的最终结果。特别注意，我在 editor 里给最后一个元素加了一个属性：actionType 是 url，并且有对应的 url 值，点击以后应该能跳转。渲染没什么问题，点击最后的 hello3，就完成了一次跳转。

整个任务完成了。这节课完成了之前两节课留下的两个任务，现在逻辑比原来清晰了很多，逻辑的重用也实现了最初步的实现。今天的课就到这里，谢谢大家。
