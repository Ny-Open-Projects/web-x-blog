# 11-19-什么是 mongoose 以及 ORM ODM 的概念

前面花了大量时间讲 MongoDB Node.js Driver，它是 MongoDB 为 Node.js 推出的类似 SDK 的库，现在我们已经能在 Node.js 中对数据做 CRUD 操作了。是时候把后端框架 egg.js 和 MongoDB 结合起来，让 egg.js 在对应的接口里完成数据的增删改查。

结合时当然可以用一直使用的原生 MongoDB Driver。但编码过程中会发现，它对数据的操作非常灵活：往 collection 里插入数据没有任何限制，想插入任何属性的对象都可以，属性是什么类型也没有验证。灵活是好事，但从另一方面看，对数据结构一点约束都没有，可能造成意想不到的问题和错误。于是就有了 mongoose。特别注意它是建立在 MongoDB Node.js Driver 之上的，不是新写的一套工具。

mongoose 提出了 model（数据模型）的概念：把一个特定的 collection 规定特定属性，抽象成一个 model，用来约束集合中的数据结构。最简单的例子：cat 的 name 是 string，说明 cat 这个对象希望 name 是字符串。在这之上还有很多扩展，比如 getter、setter、plugin 等等，能提供更多功能。而且它的很多方法、传入参数和返回参数都和之前学的 Node.js MongoDB Driver 非常类似，故意做成一模一样，所以上手非常快。业界称之为 ODM 工具，Object Document Mapping。它有 23K Star，是使用 MongoDB 时业界最流行的 ODM，不二之选。

对 ODM 概念如果觉得陌生，它还有个兄弟：如果你之前用编程语言操作过关系型数据库，MySQL、SQLite 等，肯定多少接触过 ORM。ORM 指 Object Relational Mapping。简单来说，ORM 是通过实例对象的语法完成关系型数据库操作的一种特殊技术。这样做有什么优点？第一，不用在程序中写晦涩难懂的 SQL 语句了。第二，它用面向对象的方式操作数据，代码量少、语义性好、容易理解。所谓面向对象，就是把数据库中的一系列概念和面向对象做了 mapping：tables 映射成 class（抽象成类）；records，表中的一行数据，被抽象成 object；records 中的值抽象成实例下的 attributes 属性。除此之外 ORM 还内置了很多功能，数据验证、清洗、预处理等都可以实践。

看个简单例子：不用 ORM 时会直接写 SQL，写法晦涩，对程序不友好；用 ORM 后非常符合代码逻辑：先定义 User Model，然后 User.create() 直接调用方法、传入属性，就完成了插入。对比两种写法，ORM 更容易理解、语义性更好。

ODM 和 ORM 异曲同工，只不过 ODM 针对的是 NoSQL 数据库，也就是 MongoDB。看一个简单的 MongoDB 代码示例：它也有类似的 Model 定义，可以用 mongoose.model 新建一个文档模型，任何属性的类型都可以定义。定义完后用 new User() 实例化一个新 user，在上面调用各种方法。从这个例子会发现，使用 mongoose 更关心对象模型的结构、里面有什么属性，把数据操作面向对象化，和我们最早的数据库设计结构能很好地对应起来。而且它在操作中自带验证，插入错误的字段或类型时会直接报错。

最后想说，是否选用 ODM 没有标准答案。非关系型数据库相比关系型数据库的益处之前说过：完全的自由，no rules。如果你认为数据操作应该简单直接、自由自在、毫无限制，也可以完全不用 ODM 工具（不用 mongoose），直接用原生 Node.js driver 编码。

这节课简单介绍了 mongoose，以及两个重要概念：ORM 和 ODM。
