# 4-3-原始数据类型和 Any 类型

这节课正式进入 TypeScript 的学习。开始之前先回答一个常见问题：TypeScript 难不难？如果要达到非常熟练的程度，比如自己写各种定义文件，确实需要功力和时间；但只是日常使用，让它帮我们完成类型检查，认真跟完课程很快就能上手。这节课先讲最容易理解的部分，补一点 JavaScript 的基础知识。

## 原始数据类型

JavaScript 的数据类型分为两大类：原始类型（Primitive）和对象类型（Object）。MDN 文档写得很清楚：除 object 以外的所有类型都是不可变的，值本身无法被改变，这些值称为原始值。原始类型总共有七种：boolean、null、undefined、number、bigint、string 和 symbol。其中 symbol 和 bigint 是 ES6 之后加入的，这里暂时不讨论。剩下五种类型在 TypeScript 里都有与之一一对应的类型，下面用代码逐一演示。

新建文件 Basic Types，先看布尔类型。声明类型的方式是在变量名后面加冒号，再写类型名称：

```typescript
const isDone: boolean = false;
```

如果尝试把一个数字赋给 isDone，编辑器会报错：`Type '123' is not assignable to type 'boolean'`，类型校验就完成了。

接下来是 number 和 string，写法相同：

```typescript
let age: number = 10;
let firstName: string = 'viking';
```

字符串里使用模板字符串也没有问题，`hello ${firstName}` 不会报错。

undefined 和 null 这两个类型值得单独说，面试官经常问它们的区别，不清楚的同学可以自己去查一查。更重要的是，undefined 和 null 是所有类型的子类型，也就是说 undefined 类型的变量可以赋值给 number 类型的变量。做个测试：声明一个 num，类型是 number，把 undefined 赋给它，编辑器不会报错。

## Any 类型

现在来一个需求：系统要接入第三方系统，输入可能来自未知的 API 或用户输入，我们无法确定它是什么类型，怎么办？这时 any 类型就来救场了。从单词就能看出，它表示"什么类型都行"，允许赋值为任意值：

```typescript
let notSure: any = 4;
notSure = 'maybe a string';
notSure = true;
```

不仅如此，在任意值上访问任何属性都是允许的，调用任意方法也不会报错，比如 `notSure.myName`、`notSure.getName()` 都能通过检查。

但也正因为如此，当我们有明确的类型时，应该避免使用 any。任意调用属性和方法很容易出错，而且等于放弃了类型检查，这时 TypeScript 和 JavaScript 就没什么区别了。

## 小结

这节课把原始数据类型过了一遍，顺手复习了 JavaScript 的基础知识，还引出了万金油 any。当然 TypeScript 不会一直这么简单，下节课会有更复杂的类型出现。
