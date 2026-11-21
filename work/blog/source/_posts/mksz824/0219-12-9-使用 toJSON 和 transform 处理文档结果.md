---
disableNunjucks: true
title: 12-9 使用 toJSON 和 transform 处理文档结果
date: 2026-11-17 17:39:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课说到，现在返回给用户的信息里带着所有数据，其中有些信息不该暴露。比如 password，无论如何都不想让用户知道数据库里存的是什么；还有 `__v`，这是 mongoose 自带的一个版本字段，对用户没有用，也不希望返回。

## 直接 delete 行不行

最直观的想法：user 是一个查询出来的对象，在返回之前 `delete user.password` 应该就可以。试试看。先不管 TS 报错（因为 UserProps 里 password 是必填字段，TS 不允许直接删除），实际运行一下：点击 Send，password 还在，没有任何效果。

原因要回到 user 的具体类型上。它不是一个普通的 UserProps 类型，而是 `UserProps & Document<...>` 这样的交叉类型。Document 是 model 的实例。再次强调：Document 不是普通的 object，它除了数据库对应的属性，还有非常多的作用和方法。官方文档里对 documents 的描述是：上面有很多方法可以完成数据操作，比如 save 方法进行 updating，还可以做 validating 验证等等，功能很多，大家可以自行了解。总之记住：Document 不是普通对象，不能直接对它 delete 属性。

## toJSON / toObject

不过可以把 Document 转换成普通的 JSON 对象。有两个方法可以完成，功能一样，只是别名不同：`user.toJSON()` 和 `user.toObject()`。转换之后拿到的是普通 JSON 对象，就可以删除了：

```ts
const userObj = user.toJSON();
delete userObj.password;
return userObj;
```

保存后再点击 Send，password 就被隐藏掉了，说明转换过程成功了。但问题是：每次处理都要重复这套流程，先转 object 再 delete 不想要的字段，尤其 password 这种完全不想暴露的字段，肯定每次都要删。有没有一劳永逸、自动删除不需要字段的方法？答案是肯定的。

## schema 的 toJSON.transform

回到 user model。记得 schema 有第二个参数，可以添加一系列选项。这里添加一个叫 toJSON 的选项（toObject 也有同样的能力）。toJSON 里可以配置一个 transform 函数，它有两个参数：第一个是 document，第二个是 ret（plain object，也就是转换后的 JSON）。

这样就可以在每次调用 toJSON 时对转换过程做处理，写在这个函数里：`delete ret.password`，同时把 mongoose 自带的 `__v` 也删掉。这就完成了转换的劫持。

现在 controller 里不需要手动转换和 delete 了，全部删掉，只保留在 user 上调用 toJSON，调用时 transform 就会自动运作，把 password 和 `__v` 都删掉。保存后点击 Send，password 和 `__v` 两个属性都消失了。

这就是 transform 的妙用，之后还会用它做一些类型转换，大家记住这种写法。

## 小结

这节课有两个知识点。第一，query 返回的内容不是普通的 JavaScript object，而是 model 的实例（Document），上面有很多方法和属性，点出来时 TS 会提示出来，但不能在上面随便 delete 属性。第二，可以通过 toJSON 或 toObject 把它转换成普通 JavaScript 对象，并且在 schema 第二个参数的 toJSON 配置里用 transform 函数劫持转换过程、自动完成处理。
