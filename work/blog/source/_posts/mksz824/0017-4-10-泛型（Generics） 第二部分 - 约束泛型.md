---
disableNunjucks: true
title: 4-10 泛型（Generics） 第二部分 - 约束泛型
date: 2026-11-17 15:17:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课介绍了泛型出现的动机、要解决的问题和泛型的简单用法，可以把它看成是一个占位符，使用的时候才动态填入确定的类型值。这节课接着探讨泛型更深入的用法：约束泛型。

## 为什么需要约束

举一个例子。新建一个函数 echoWithArray，接收一个 arg，函数内部 console.log(arg.length)，然后返回 arg。再给泛型添加上：T arg，返回 T。

```ts
function echoWithArray<T>(arg: T): T {
  console.log(arg.length)
  return arg
}
```

这时候出现了一个错误：property length doesn't exist on type T。因为在函数内部使用泛型变量的时候，由于事先不知道它是哪种类型，不能随意操作它的属性或方法。泛型 T 不一定包含 length 属性，我们可以给它传入任意类型，有些类型没有 length 属性，所以编译时报错了。

一个解决方案是决定这个函数只作用于含 length 属性的 T 类型的数组。把 arg 改成 T 的数组（后面加方括号），返回值也改成 T 的数组：

```ts
function echoWithArray<T>(arg: T[]): T[] {
  console.log(arg.length)
  return arg
}
echoWithArray([1, 2, 3])
```

这样 length 属性有了，报错消失，传入数组也能返回正确的 number 数组。

但这个方案还不完美：我们只能传入数组，可是对象甚至简单类型的 string 都可以有 length 属性。假如传入一个 string，它会报错，因为 string 不能赋值给数组类型。

## 用 extends 约束泛型

我们需要一个新的解决方案：对泛型进行约束，只允许函数传入包含 length 属性的变量。这就是约束泛型。

先新建一个 interface，叫 IWithLength，包含一个属性 length，返回 number：

```ts
interface IWithLength {
  length: number
}
```

再创建一个几乎一样的函数，改名为 echoWithLength：T arg，返回 T，内部 console.log(length)，return arg。它同样会在 length 处报错。现在我们不想让它只接受数组，可以用 extends 关键字来约束传入的泛型，告诉它必须有 length 属性，否则报错。

```ts
function echoWithLength<T extends IWithLength>(arg: T): T {
  console.log(arg.length)
  return arg
}
```

extends 加在尖括号里 T 刚初始化的时候，把 IWithLength 放在后面，问题就解决了。

## 验证

试几个例子。传入 string 'str'：没有问题，成功返回一个 string。传入 object `{ length: 10 }`：里面有 length 属性，没有问题，返回的也是一个 object。传入数组 [1, 2, 3]：没问题，返回 array of number。

这就发现了 interface 的奇妙之处，活生生的 duck typing 又出现了：只要叫起来像鸭子，只要你有 length 属性，符合这个约束，就没有问题。不管你是字符串、object 还是数组都可以。甚至可以带更多的属性，比如再加一个 width: 10，也没有报错，而且返回正确的值，只要包括 length 就行。

再来一个错误的例子：传入数字 123。123 里面没有 length 属性，提示 not assignable to parameter of type IWithLength，自然报错了。

## 小结

这节课着重讲了约束泛型，关键是在泛型中使用 extends 关键字，让传入值满足特定的约束条件，而不是想传什么就传什么。
