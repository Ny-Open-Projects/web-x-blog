---
disableNunjucks: true
title: 4-28 创建 useURLLoader
date: 2026-11-17 14:36:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

组合式函数是 Vue3 组合式 API 的重中之重，这节课再讲一个例子加深了解。这次的函数和之前不同：需要传入参数，功能也更复杂。异步请求最常见的需求就是 loading 状态的显示和隐藏：发送请求时显示 loading 图标，加载完毕后隐藏。如果每个请求都要重复写这套逻辑，会让人非常恼火，所以要把公共逻辑提取出来。

## 安装 Axios

发送异步请求需要一个趁手的工具，不想手写 XHR 或用 fetch，那就用大名鼎鼎的 Axios。直接安装最简单的 API，之后会深入它的用法：

```bash
npm install axios --save
```

注意它自带 type 文件，不需要另外安装 TypeScript 的定义文件。

## 编写组合式函数

函数叫 useURLLoader，参数是要加载的 URL，String 类型。首先要声明状态：数据是什么、是否在 loading、是否有 error。这明显是一个 object，用 reactive 声明最合适（用 ref 也可以）：

```typescript
import axios from 'axios';
import { reactive } from 'vue';

export function useURLLoader(url: string) {
  const data = reactive({
    result: null,
    loading: true,
    error: null,
  });

  axios
    .get(url)
    .then((rawData) => {
      data.result = rawData.data;
    })
    .catch((e) => {
      data.error = e;
    })
    .finally(() => {
      data.loading = false;
    });

  return data;
}
```

result 存放异步请求返回的结果，loading 在调用函数时一开始为 true，error 一开始没有任何错误所以是 null。

Axios 是 promise based 的，get 方法发送请求后，在 then 里拿到原始数据，取 rawData.data 就是真正返回的数据；catch 里把错误赋给 error。这里有个细节：出错时 loading 也要置为 false，因为不管成败加载都已经结束。与其在 then 和 catch 里重复写，不如放到 finally，成功失败都会触发，代码更简约。

最后返回 data，函数就写完了。

## 用 Dog API 验证

隆重推荐一个有趣的接口：Dog API，发送请求就随机返回一张狗狗图片的 JSON，图片地址在 message 字段上。用刚写的组合式函数完成任务：

```typescript
import { useURLLoader } from './hooks/useURLLoader';

const dogUrl = 'https://dog.ceo/api/breeds/image/random';
const data = useURLLoader(dogUrl);
```

模板里先加一个 h1，用 v-if 在 data.loading 时显示"我在加载"；loading 结束后 v-else 显示一张 image，src 取 data.result.message。这时 TS 报错了：reactive 没有声明类型，result 被自动推断成初始值 null，没法在 null 上取 message 属性。

这里先简单解决：创建一个 interface，把 result 和 error 用 any 类型 hack 一下：

```typescript
interface IResult {
  result: any;
  loading: boolean;
  error: any;
}
```

这是一个不好的方案，下节课会用精确的类型代替它。现在让功能先可用。运行 npm run dev：一开始显示 loading，随后出现一张可爱的狗狗图片；再试一次，loading 很快结束又出现一张新图片，完美。

## 一个坑：解构丢失响应性

大家稍作修改就可能发现问题：每次写 data.loading、data.result 比较麻烦，能不能直接解构展开？把 loading 和 result 解构出来直接返回，代码确实舒服了。但刷新页面会发现页面根本不更新，永远停在 loading。虽然在 loader 里改变了状态，视图却没有跟着更新。

原因在文档里写得很清楚：Vue 的响应式系统是通过属性访问进行跟踪的，必须始终保持对响应式对象的相同引用。如果把响应式对象的属性赋值或解构到本地变量，就会失去响应性。比如 state 里有个 count，把 `const n = state.count` 取出来，n 就是一个普通的 number 局部变量，对 n 加加并不影响原始的 state。

刚才正是犯了同样的错误：返回的是整个 reactive 对象 data，但解构成 loading 和 result 两个本地变量后，它们已经丢失了响应性。

## toRefs 解决

解决工具是新函数 toRefs：将一个响应式对象转换为一个普通对象，但其中的每个属性都变成了对应的 ref：

```typescript
import { toRefs } from 'vue';

const { loading, result } = toRefs(data);
return { loading, result };
```

转换后 loading 和 result 都被 ref 包装，响应性保留。注意在代码中访问值时要使用 .value 属性。保存刷新，页面正常更新，图片成功出现。

## 小结

通过这个例子应该能体会自定义组合式函数的妙处：把逻辑上重复的代码提取到函数中，像调用函数一样使用它返回的结果。useURLLoader 可以完美胜任各组件里的异步读取工作，和展示完全解绑，想展示文字或图标都行。

不过到目前为止 TypeScript 还没真正上阵，我们获得的红利只有类型推论。网络请求千奇百怪，返回结构大相径庭，下节课就用泛型完成第一次改装，让每次请求的返回对象都按传入的类型获得精确类型和自动补全。
