# 4-21-响应式基础 - Ref 和 Reactive

这节课正式进入 Vue 3 结合 TypeScript 基础知识的学习。事先声明一点：假如你已经比较熟悉 Vue 3 的基础知识，也看过我之前课程的基础内容，可以选择跳过。但如果你用过 Vue 3 却没有和 TypeScript 结合过，我还是建议你看一下，两者结合会有挺多新知识，而且这些基础课程都是 2023 年最新录制的，根据最新文档新增了不少内容。

## 什么是响应式

Vue 3 最重要的就是响应式。响应式对象是一种神奇的数据结构：当你修改它的值的时候，对应的页面（视图）会自动更新到对应的状态。这里抛弃大家在 Vue 2 中已经了解的一些知识，采用全新的 Composition API（组合式 API）来感受它的新用法。

来到源代码，用 App.vue 作为试验场。第一步把默认的内容都删除掉（包括 setup 语法），为了理解简单先删掉，之后会慢慢讲默认代码的奥妙。

## ref：第一个响应式对象

从最简单的 count 开始：显示一个数，并新增一个数，了解响应式的基础。

第一步导入一个 function，from 'vue'，这个 function 叫 defineComponent。它是一个完全为类型服务的函数：不加也可以，但加上以后会有非常多的类型推断，TS 会帮我们完成一些工作。正常情况下我们直接导出一个 Object 就可以；使用 defineComponent 包裹以后，再输入时这些对应的属性都有自动提示了，比如 name，我们称之为 app。

然后是最重要的 key：setup。setup 是 Composition API 特殊的钩子函数，关于组件的逻辑都可以写在其中。

在这里创建第一个响应式对象，需要的函数叫 ref。创建变量 count，初始化为 0；再创建一个函数 increase，调用时把这个值加一。怎样修改响应式对象的值呢？count 上有一个特殊的属性叫 value，必须修改这个 value 的值才可以，特别注意。TS 也会提示，自动帮我们补全对应的属性。

要注意的是：你要在模板中使用的所有属性和函数，都要进行返回，然后才能在模板中使用。把 count 和 increase 返回出去，模板中新增一个 h1 展示 count。这时零就出现了，展示成功。

这里有一个小问题：在 script 中访问值需要写 count.value，但在模板中被访问时不需要写 value。这是 Vue 帮我们做的一个简单优化，叫 ref 的自动解包：当 ref 在模板中作为顶层属性被访问时，它会被自动解包，直接使用就可以。

下一步添加一个 button，type 设为 button，点击时调用 increase 更新值。点击按钮，可以看到值被更新了，整个流程成功。

小结：使用 ref 声明一个响应式对象，它上面有一个属性 value，改变 value 的值，视图就会更新。

## reactive：第二个响应式对象

第二个响应式对象叫 reactive，和 ref 类似但有些区别。它的参数必须是一个 object：给它写入 0 会报错，Number is not assignable to object。传入一个对象 { userName: 'viking', age: 30 }，就用 reactive 新建了一个响应式对象。

更新的时候可以把它完全当一个对象使用，不需要点 value 访问属性。比如要把它的 age 加一，直接 user.age++ 就可以。所以 reactive 比 ref 的一个优势是它不需要使用点 value 来访问其中的属性。把 user 返回出去，模板中调用 user.age，一开始显示 30，点击 Increase，功能也正常。

响应式对象其实是 JavaScript 的 Proxy，它的行为表现和一般对象相似，不同之处在于 Vue 能够跟踪响应式对象属性的访问以及更改操作，所以能实现对应的功能。

## 和 TS 结合

现在看看怎样把这两个响应式对象和 TS 结合起来。

**ref 的类型标注。** 传入的类型 0 是 number，那么 count 返回的就是 Ref<number>，它上面的 value 就是 number 类型。也就是说 ref 支持自动推断类型：传入 0，点 value 就是 number 类型。假如传入一个 string，count.value 自然就变成 string 类型，在 string 上做 ++ 操作会报错；直接把它赋值为 string 也会报错。

怎样手动设定类型？ref 函数支持一个泛型，在泛型中传入对应的类型即可。比如现在这个 count 可能是 string 也可能是 number，就传入联合类型：

```ts
const count = ref<string | number>(0)
```

现在 count.value 就是 string 或 number 类型，做 ++ 操作报错，因为只有当它是 number 时才可以。修正代码：使用 type guard 把类型缩小。可以用 typeof 判断，当 count.value 是 number 的时候再进行加一操作，错误就消失了，也能成功实现功能。这就是 ref 进行 TS 标注的方式。

**reactive 的类型标注。** 先创建一个 interface 作为想要的类型：

```ts
interface Person {
  name: string
  age: number
}
```

把 user 直接设定为这个类型，就完成了类型标注。好处是可以获得自动的补全：object 中 name 是 string 类型，要传入字符串；age 是 number 类型，要传入 number。如果什么都不加，它也和 ref 一样，根据传入的参数做类型推论：现在 user 就是传入 object 的类型，name 是 string，age 是 number。

## ref 和 reactive 的区别与选择

最后讲讲两者的区别，挺重要的。

第一，reactive 的参数只能是 object，传其他类型会报错；ref 都可以，包括 reactive 不可以的原始数据类型，比如 string、布尔值、number 等。第二，ref 需要使用 value 来访问其中的值，reactive 不需要。

讲一点原理：ref 在 Vue 源代码内部其实是一种特殊的 reactive，是 reactive 的变种。可以假设一个简单模型：ref 是用 reactive 创建了一个 object，object 上有一个 value，所以它可以实现这样的操作，就是这么简单。

针对 ref 和 reactive 应该怎样选择？官方文档没有讲具体规则，没有特殊规则，可以按个人喜好选择。我个人更喜欢：原始类型使用 ref，object 使用 reactive。其实就是和一段简单的 JavaScript 代码做类比：要声明一个原始类型就用 ref，user 是一个 object 就用 reactive。这是我遵循的简单规则，大家也可以按照自己的喜好发明自己的规则。

## 小结

这节课讲了 defineComponent（帮你进行类型推论的 function 包裹），ref 和 reactive 的用法，ref 的自动解包，ref 和 reactive 怎样进行类型标注，最后讲了它们的区别和选择。
