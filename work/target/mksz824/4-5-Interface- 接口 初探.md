# 4-5-Interface- 接口 初探

前面学习了如何定义原始类型和数组的类型，还缺 JavaScript 里用得最多的 Object 类型。帮我们方便定义对象类型的新概念叫 Interface（接口）。TypeScript 的 Interface 非常灵活，这节课讲它第一个也是最基础的功能：对对象的"形状"（shape）进行描述。

## 鸭子类型

Interface 还有一个响亮的称号：duck typing（鸭子类型）。维基百科的定义是：如果一个东西长得像鸭子、像鸭子一样游泳、像鸭子一样嘎嘎叫，那它就可以被看成一只鸭子。鸭子类型是动态编程语言的一种对象推断策略，更关注对象能如何被使用，而不是对象本身的类型。听起来有点费解，后面会一点一点体会到。

Interface 本身像一种抽象的契约，或者说一张图纸，可以描述编程语言中的各种类型。另外要注意，Interface 并不存在于 JavaScript 中，TS 编译后它不会被转换到目标代码，只在编译期做类型的静态检查。

## 定义接口

进入代码，新建文件 Interface Basic，用 interface 关键字定义一个叫 Person 的接口：

```typescript
interface Person {
  name: string;
  age: number;
}
```

有些编程语言建议接口名以大写字母 I 开头，提示别人这是一个 Interface，加不加都只是建议。接着声明一个变量 viking 为 Person 类型，同样用冒号：

```typescript
const viking: Person = {
  name: 'viking',
  age: 20,
};
```

接口会约束变量的形状，赋值时必须和接口保持一致：少了属性（比如删掉 age）会报错，多了属性（比如加一个 id）同样报错。

## 可选属性与只读属性

有时我们不想完全匹配形状，这时可以用可选属性。在属性名后面加问号，表示该属性可以不存在：

```typescript
interface Person {
  name: string;
  age?: number;
}
```

age 加不加都不会报错。

还有只读属性：希望某些字段只能在创建时被赋值，用 readonly 定义：

```typescript
interface Person {
  readonly id: number;
}
```

创建之后再修改 `viking.id = 9527` 就会报错：`cannot assign to 'id' because it is a read only property`。

readonly 看起来和 const 有点类似，区分方法很简单：readonly 用在属性上，const 用在变量上。

## 小结

这节课的 interface 主要是对对象的形状做约束，它还有更多高级用法，可以描述类、函数、数组等世间万物，我们慢慢去挖掘。
