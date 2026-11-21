# 12-4-改进 Model 的ts 类型支持

上节课完成了用户的创建，但发现一个很不爽的问题：应用里对 model 的 TS 支持不完善。第一个问题，`ctx.model.` 后无法联想出模型名称，比如 user 必须手动打出来；第二个问题，模型完成查询等操作后，返回的数据没法自动联想出 model 上定义的一系列字段。

## 手动方案：类型断言

先看手动解决第二个问题的做法。现在 user 是 `mongoose.Model<any>` 类型，第一个泛型是 any。可以做类型断言把类型丰富起来：

```ts
const currentUserModel = this.ctx.model.user as mongoose.Model<UserProps>;
```

用 mongoose 的 Model 类型做断言，把第一个泛型定义为 UserProps。定义完成后做一次查询：`currentUserModel.findById(id)`，观察 result 的类型，可以看到它是 `UserProps & Document` 或者 null 的联合类型，因为查询条件不符合时拿不到结果。所以先用 type guard 把 null 排除掉，之后 result 里就能看到 id、username、password 等所有定义的属性。

这种方式可行，但不想每次使用都写类型断言，太麻烦。怎样让它自动获得类型？

## 原理：egg-mongoose 的类型扩展

看一下 egg-mongoose 对 Egg 的类型扩展。之前分析过，它扩展在 Application 和 Context 两个对象上，属性名都叫 model，类型是 MongooseModels。看 MongooseModels 的定义：它是一个 type，本身是个 indexable type，第一个 key 是任意字符串，所以没法联想出具体的模型名；而且它传入的第一个泛型是 any，所以也联想不出数据结构。

我们的目的就是修改它，用类型重载：根据文件名添加对应的 key，根据每个 model 定义的 props 补上泛型。

## 自动方案：利用自动生成的类型文件

 typings 文件夹根目录下有一个 index.d.ts，可以在里面编写自定义类型。特别注意：这个文件不是自动生成的，不会在每次启动应用时被覆盖，所以自定义类型都写在这里。

先手写一个 interface 来覆盖 MongooseModels 类型：

```ts
interface MongooseModels {
  User: mongoose.Model<UserProps>;
}
```

写完感受一下效果：`this.ctx.model.` 后面 user 名称出现了，findById 之后 result 的类型也完全正确，phone、picture、password、username、id 以及内置的方法和属性都能点出来。这说明这种方式可行。

但不舒服的地方是：每次在 model 目录新建一个模型文件，都要来这里新建对应的类型，忘了就会报错。有没有办法自动处理所有文件？人工显然没法遍历 models 文件夹下的文件并生成类型。这时想到 app.helper 可以自动生成类型文件，看看它有没有生成 models 的类型。

观察 typings 目录：我们手写的 index.d.ts 不会被自动生成；application.d.ts 和 context.d.ts（app config 下面）都会自动生成。其中 app 里根据文件夹自动生成了对应的类型文件，models 文件夹也生成了对应的 model/index.d.ts。看看里面的门道：

它会循环文件夹，把 models 目录里的文件 import 进来。我们只有一个 user.ts，所以只 import 了一个，有多少个文件就会自动 import 多少个。然后定义了一个 interface 叫 IModel：key 是文件的名称（首字母改成大写），对应的类型是函数的返回类型。

这里有两个 TS 知识点。第一，想拿到一个函数的返回类型，有特定的写法：import 进来的是一个 function，要拿到函数的具体类型用 `typeof` 加函数名；第二，拿到函数类型后，用内置类型工具 `ReturnType<T>` 获取返回类型。记住，我们要的是类型，而不是函数本身。

还有一个特别注意点：之前写 model 的时候，自定义 model 传入了 UserProps 泛型，这一步非常必要。它保证 `ReturnType` 拿到的是带着实体属性的对应模型类型。回头看自动生成的 User 类型：它就是 `mongoose.Model<UserProps>`，和我们需要的手写类型完全一致，而且可以根据文件数量自动扩展。

## 收尾：让 MongooseModels 继承 IModel

有了 IModel 这个完美的类型，只需简单修改手写的 interface：

```ts
interface MongooseModels extends IModel {
  [key: string]: mongoose.Model<any>;
}
```

让 MongooseModels extends IModel，同时保留原来的 indexable type 作为兜底：找不到的 key 仍然可以随便写，类型是 `Model<any>`。这样就不用一行行手写了。

保存后测试：`this.ctx.model.user` 正常，写 post 也不报错（类型是 `Model<any>`）。换回 user，findById 传入 id，result 返回的类型和刚才一样，是 UserProps 与 null 的联合类型，属性都能正常点出。

这节课完成了 Model 类型的 TS 演化，现在可以轻松访问 model 上对应的文件名称、查询实体上的各种属性，上节课留下的任务完成。
