# 4-9-泛型（Generics） 第一部分

这节课接触 TypeScript 中最难的部分：泛型（Generics）。有一张很形象的网络图：一个滑梯的前半段写着 adding simple type annotations，给变量加简单的类型声明，比如 string、number、boolean、array，一路平滑；但一到 generics 这一段，坡度直接变成地狱级。所以只要掌握好泛型，就算攻克了 TypeScript 最难的点。

## 动机

不讲概念，先谈动机：泛型要解决什么问题？考虑一个只做一件事的函数 echo，传入参数原样返回：

```typescript
function echo(arg: any): any {
  return arg;
}
```

如果参数不写类型，调用 `echo(123)` 时返回值是 any，变量丧失了类型信息，这不是好现象。

第一个思路是给参数和返回值都标成 number，这样 result 确实是 number 类型了。但函数可能接收 string、布尔甚至复杂类型，一个 number 满足不了所有需求。

第二个思路是 any，把参数和返回值都换成 any。但这也不对：传入和返回之间没法保持统一，类型照样丢失，甚至还会出 bug。比如把 result 声明为 string 类型，检查依然通过，因为 any 返回值可以赋给任何类型；但理论上传数字就该返回 number。怎么解决？

## 第一个泛型

泛型是指在定义函数、接口或类的时候，不预先指定具体类型，而是在使用时再指定类型的特征。改造 echo：在函数名后面加一对尖括号，里面写泛型的名称 T（名字随意，T 只是习惯写法）。T 相当于创建了一个占位符，一个神秘的变量，它可以是任意类型，在使用的时候再指定：

```typescript
function echo<T>(arg: T): T {
  return arg;
}
```

参数和返回值都定义为 T，类型就一一对应起来了。调用时显式传入类型：

```typescript
const str = echo<string>('str');
```

传入 string，返回也是 string，泛型立了第一功。当然也可以完全不指定，类型推论会帮我们完成：`echo(123)` 推断 T 为 number，返回 number；`echo(true)` 返回 boolean。这时如果把结果声明为 string，就会报错 `type 'true' is not assignable to type 'string'`，之前 any 的问题彻底解决。

## 两个泛型参数

函数还可以传多个值。新需求：传入一个元组，两个元素类型随意，返回一个交换了位置的新元组：

```typescript
function swap<T, U>(tuple: [T, U]): [U, T] {
  return [tuple[1], tuple[0]];
}
```

用两个泛型参数 T 和 U 约束元组的两项，返回值类型相应写成 `[U, T]`。调用 `swap(['str', 123])`，返回的类型是第一项 number、第二项 string，于是第 0 项可以当 number 使用，调用 number 上的方法；第 1 项可以当 string 使用，调用 string 上的任何方法。

## 小结

这节课介绍了泛型的动机和最简单的用法。泛型就像一个占位符或变量，使用时把类型像参数一样传入，它可以原封不动地把类型带出来。
