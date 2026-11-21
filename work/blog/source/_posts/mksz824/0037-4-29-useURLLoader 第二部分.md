---
disableNunjucks: true
title: 4-29 useURLLoader 第二部分
date: 2026-11-17 15:37:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课成功显示了狗狗图片，useURLLoader 已经可用，但从类型上来说还不完美：result 现在是 any。我们希望 result 能获得传入的类型，也就是在运行时才确定的类型。这是我们第一次真正需要 TS 来解决的问题。

## 泛型改造

第一个想到的方法就是泛型。useURLLoader 是一个函数，完全可以加泛型。特别注意泛型要添加的位置：箭头函数形式的函数，T 加在函数名后面。现在的目标是把 T 一路传递到最终的 result 上。

data 的类型是 IResult，而 IResult 是一个 interface，interface 也可以接受泛型，所以可以做二层传递：函数上的泛型 T 传给 IResult，IResult 再传给 result：

```typescript
interface IResult<T> {
  result: null | T;
  loading: boolean;
  error: any;
}

export const useURLLoader = <T = any>(url: string) => {
  const data = reactive<IResult<T>>({
    result: null,
    loading: true,
    error: null,
  });
  // ...
};
```

这里会报一个错，原因是我们一开始的 result 初始值是 null，所以它的类型是 null 和 T 的联合类型，补上联合声明即可。理解一下这个双层传递：先把 T 传到函数里，再通过 interface 上的泛型传给 result。

result 是 `null | T` 也很合理：一开始没有数据，加载完毕后才获得真正的 T。使用时要先判断 result.value 是否存在，不存在不能取值，TS 借此帮我们实现了 type guard，规避错误。最后给 T 一个默认值 any，这样不传泛型也能用。

## Dog API 加持类型

Dog API 返回 status 和 message 两个字段，都是 string。创建对应 interface 并传入泛型：

```typescript
interface DogResult {
  status: string;
  message: string;
}

const { result, loading } = useURLLoader<DogResult>(dogUrl);
```

传入一瞬间，result 就变成了 DogResult 和 null 的联合类型。使用时先判断 result.value 存在，之后访问 message、status 都有自动补全和正确的类型。

更巧妙的是 Volar 在模板上也能做判断：模板里直接取 result.message 会报错，因为 result 可能是 null。这就是 TS 提前帮我们发现问题。修改模板：不用 v-else，改用 v-if，判断条件是 loading 为 false 且 result 存在，这时再访问 src 就没问题了。type guard 类型收窄在 Vue 标签上同样运作，v-if 把联合类型中的 null 去掉后，result 就变成了 DogResult。

## 第二个请求

如果觉得没啥稀奇，再发另一个请求看看。JSONPlaceholder 这个 API 的 `/todos/1` 会返回一个简单的 todo 数据结构。定义新 interface（简化只写 title）：

```typescript
interface TodoResult {
  title: string;
}

const { result, loading } = useURLLoader<TodoResult>(todoUrl);
```

传进去的一瞬间 TS 就报错了：message 不在 result 上，因为 TodoResult 只有 title。这正是类型系统在帮我们找错误。展示也相应调整：图片用不了了，用 h1 显示 result.title 即可。注意别忘把 URL 也替换成 todo 的地址。保存运行，文字成功显示。

## 小结

用泛型改造之后，这个函数更强大了：发任何种类的异步请求，只需要引入 function、传入 URL、定义返回数据的类型，TS 就能帮你做一大堆事情；不想传类型也可以，会退化为 any。后面的课程我们会越来越多地用 TS 特性改造程序，让它更健壮、写起来更方便。
