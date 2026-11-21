# 12-2-定义 UserModel

上一周学完了基础知识，这一周进入第一个也是非常重要的数据类型：用户（user）的一系列功能开发。导学里说过，这一章会围绕用户的操作和鉴权机制做比较广泛的讲解，并在部分内容上做深入了解。但一切的前提是先把数据库里用户这个数据结构的模型建立起来，也就是创建对应的 model。

第一步是确保上周的任务已经完成：安装并启用官方的 egg-mongoose 插件。我已经安装了 egg-mongoose（版本 3.3.1），在 plugin 里 enable 了它，package 里 add 了 mongoose，数据库配置上添加了对应的 URL。特别注意：这里创建了一个新的数据库，名称就叫 OpsFlow。另外 test.ts 有一行变红了，是一个 TS 错误，因为当前 mongoose 的版本上没有 id 这个属性，把这行测试代码删掉即可。`npm run dev` 启动，一切正常。

## 定义 interface 和字段

接下来正式创建 user model。在 `app/model` 下新建 user.ts，先导入需要的两个依赖。

为了让 model 更好地和 TS 配合，先创建一个 interface 来约束模型，命名为 UserProps 并 export 出去。官方文档的 TypeScript support 一节也提到了这种做法，编码过程中会逐一看它如何发挥作用。字段包括：

- `username`：string，用户名。它和 id 一样是唯一的，不能重复；
- `password`：string；
- 一些数据库设计阶段预留的可选字段：nickname（昵称）、pictures（头像图片地址）、phoneNumber（手机号码）等。随着应用发展这些字段可能发生变化，这正是 MongoDB 的灵活性所在；
- `createdAt` 和 `updatedAt`：两个 Date 类型的时间字段。在数据库设计中非常常见，方便观测数据的时间节点。

## 创建 schema

然后创建函数体 `initUserModel`，参数 app，类型 Application。函数里创建对应的 schema，称为 userSchema，即 `new Schema<UserProps>(...)`，把 UserProps 作为泛型传进去。

这里要说明一个遗憾：如果你用的是最新的 Mongoose 6，泛型可以自动联想出 interface 上定义的所有属性；但 egg-mongoose 的更新停留在一年前，依赖的还是 Mongoose 5，定义文件没更新到最新，没有自动提示。希望同学们学习时可以把库更新到 Mongoose 6，感受泛型的魅力。不过没关系，定义的 interface 后面还有用武之地。

由于没有自动提示，schema 里的约束只能手写，这正好能体会有没有 TS 的区别：类型属性在 TS 下不容易写错，没有就可能出错。username 的约束写成 `{ type: String, unique: true, required: true }`，unique 表示它独一无二，required 表示创建时必传。其余字段我直接复制过来了。

createdAt 和 updatedAt 这两个属性我们没有手动定义约束，而是交给 mongoose 的一个特性：通过 schema 的第二个参数启用。添加 `{ timestamps: true }`，官方文档的描述是：让 mongoose 为 schema 自动创建 created_at 和 updated_at 字段，并在创建和更新的时候自动赋值，非常方便。

## 注册 model

schema 定义完毕后 return。注意 return 时要用 app 上的 mongoose 调用 `mongoose.model`，model 名称传 'User'，schema 传我们定义的 userSchema。最后在 model 上再添加一个泛型，把 UserProps 传进去。这个泛型现在的作用还体会不到，后面会发现它大有来头。文档 create a model 一节就是这么规定的，把 interface 传进去即可。

最后 `export default initUserModel`，model 就建立好了。第一步任务完成后，下节课就可以使用这个 model 做进一步的数据操作，简单实现增加和查找两个功能。
