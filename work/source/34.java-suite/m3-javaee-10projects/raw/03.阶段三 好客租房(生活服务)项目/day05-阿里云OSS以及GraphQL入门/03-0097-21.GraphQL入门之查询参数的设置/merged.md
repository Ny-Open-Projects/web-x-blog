# 21.GraphQL入门之查询参数的设置

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\21.GraphQL入门之查询参数的设置【海量资源尽在 ubkz.com】.mp4
- 时长 5分56秒（音频 357s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们为我们这个查询的设置参数啊通过参数呢来做一个查询那么下面我们来看一下它的一个实现那么在前面我们实现的过程中啊就是我们无论如何去查询那么它返回的数据那么都是一个数据对吧那么我们已经把这个数据是不写死了
[00:18] 那这个位置呢有个叫static data fetcher就是一个静态的数据那么显然这样肯定是不合理的所以我们需要给他去做一些调整那么这样我们来先给他添加一个参数叫什么呢叫argument那么argument呢我们就去去得到一个argument吧就是grep ql argumentargument然后呢点name设置一个名字那么什么名字呢就叫id对吧参数名叫id然后呢
[00:47] 参数的这个类型呢就是我们的这个Scarl下面的一个Lung类型啊这种类型OK那么我们继续往下面看那么这个DataFetcher是不是我们之前设置这个静态数据现在显然是不是不能这么设置了那怎么办呢我们给它去做这样的一个重新是给它设置一个DataFetcher然后呢这个里面呢我们采用一个Lambda表达式来去给它去返回一个这个数据
[01:14] 那么在这个里面呢我们拿到这个env啊就是我们的一个argument参数啊拿到这个参数我们通过它里面去get argument然后呢得到一个id然后它的一个这个返回值显然就会拿到一个谁呢是不是拿到一个楞形的id好拿到这个id之后那么我们是不是就可以去在这个位置是不是就可以去查询数据库了
[01:42] 对不对但是呢我们现在呢仅仅做一个模拟的实现那么咱们就这么来玩直接return来一个new一个把这个call过来吧new一个这个user把它call过来然后呢这个usr id呢就是你传给我的这个id然后呢这个名字呢我们就写一个张三然后呢来一个冒号吧然后加一个这个id那age呢我们就用这个什么呢就int点
[02:11] 就是20去加一个你传入的这个ID的值大概做这样的一个模拟那么写个todo先模拟实现这个大家能够理解这个意思就是我们先做一个简单模拟的实现那么不做一个数据库的查询OK那么然后在这个点需要大家注意的是我们在这个位置使用Lambda表达式其实它就是一个匿名类的一个实现
[02:39] 那么这个我使用Lambda表达设你需要给他设置一下设置成我们的工程的编译的一个版本是设置为8这个一定要注意如果你不设置8的话那么这个Lambda表达设是不能使用的OK好那么下面我们就可以来做一个查询然后走那么猜一下会怎么样我们等待他之前来看一个结果那么其实可以看到现在
[03:09] 这个Date显然等于Null对吧Errors那么有这个Error那么代表什么呢来看一下他说这个不能去获取这个数据对不对由于什么呢由于其实我们现在没有给他设置参数没有设置参数那我们来给他设置一个参数怎么设置呢其实在这个位置来设置一个参数叫什么呢ID冒号是1冒号1就是ID等于1的这个用户去做一个查询来看一下他的一个执行
[03:36] 那么我们其实可以看到是不是已经查到数据了ID等于1然后呢内幕等于张三1然后呢年龄21那么如果传一个100ID等于100的话那么它的返回值那么一定是会跟着发生一个变化对吧来看一下效果OK是不是没有问题啊好那么在这种情况下面我们能不能去只查询ID和名字呢不需要年龄这个字段能不能可不可以呢
[04:05] 当然他也是可以的啊也是可以的你看是不是只返回了ID和内幕好那么这样的话呢我们是不是就已经完成了一个参数的一个添加哎对不对好这就是他的一个这个结果啊当然了对于我们这个代码呢我们可以对他做一些编码层面的一个优化比如说像这个什么呢像这种的一些这个引用啊那么我们是不是可以把它设置为是一个静态的一个引用来看一下静态引用是不是就可以这样去写
[04:35] 这样去写的话那么我们这个代码是不是看起来就会精简一些包括像这种定义是不是也可以把它设置为是一个静态的引用哎呦ok然后呢像这个定义是不是也可以把它设置为是一些静态的一个引用那么这个就不需要了把它拿掉嗯这个还是让它去导一下应该是把那个新导入进来这个不需要了拿掉然后呢上面这个我们就来一个新吧那就来个新
[05:04] 然后这个就不需要了好下面都可以这样去写然后这个这个这个是不是也可以设置为静态的一个导入设置为静态的导入那OK好没有问题然后继续往下面看这个你有一个object没有问题那么这个就不需要设置静态了好那么这样的话我们代码是不是就得到一定程度的一个经典其实大家呢去再去看一些这个文档
[05:27] 是做一些学习的时候呢会发现那么他们呢都是这样的一种编写的方式那么这样的编写方式呢就会比较精简一些啊那么官方的这个文档中呢它也是这样的一种编写的方式那么希望大家能够看到这样的编写方式的时候呢也知道它为什么要是这样去写那么前面呢我们并不是这样去写对吧只是为了精简我们这个代码而去把它做一个静态的一个引入哎OK好那么关于我们这个查询参数的一个设置呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Java 中使用 GraphQL 框架定义对象类型、查询类型、字段和参数，并通过代码执行查询。

2) 按时间顺序列出每张画面的要点：
画面1:
- 代码：在 GraphQlFieldDefinition 中定义了三个字段：id（GraphQlLong）、name（GraphQlString）、age（GraphQlInt），并为 user 字段设置了 StaticDataFetcher，返回一个预设的 User 对象。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面2:
- 代码：在定义 user 字段时，使用 .argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build()) 添加了 id 参数。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面3:
- 代码：在定义 user 字段时，使用 .argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build()) 添加了 id 参数。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面4:
- 代码：在定义 user 字段时，使用 .dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20))) 设置了数据获取器。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面5:
- 代码：在定义 user 字段时，使用 .dataFetcher(environment -> { ... }) 设置了数据获取器。
- 代码：定义了 UserQuery 类型，包含 user 字段。
- 代码：定义了 schema，但未完成。

画面6:
- 画面显示了 IntelliJ IDEA 的 Project Structure 设置界面。
- 语言级别设置为 8 - Lambda, type annotations etc.
- 项目结构中包含 src 和 target 文件夹。

画面7:
- 代码：定义了 GraphQLSchema，创建了 GraphQL 对象，并执行了查询。
- 代码：查询字符串为 "user{id,name,age}"。
- 代码：打印了查询结果和错误信息。

画面8:
- 代码：查询字符串为 "user(id:1){id,name}"。
- 代码：执行查询并打印结果和错误信息。
- 代码：打印了查询结果和错误信息。

画面9:
- 代码：查询字符串为 "user(id:100){id,name}"。
- 代码：执行查询并打印结果和错误信息。
- 代码：打印了查询结果和错误信息。

画面10:
- PDF 页面显示了 GraphQL 的 Schema 和类型规范。
- 代码：展示了如何定义字段和参数。
- 代码：展示了如何执行查询。

画面11:
- 代码：导入了 GraphQL 相关的包。
- 代码：定义了 GraphQLDemo 类。
- 代码：定义了 User 类型。

画面12:
- 代码：定义了 GraphQLSchema，创建了 GraphQL 对象，并执行了查询。
- 代码：查询字符串为 "user(id:100){id,name}"。
- 代码：打印了查询结果和错误信息。

画面13:
- 代码：定义了 GraphQLDemo 类。
- 代码：定义了 User 类型。
- 代码：定义了 UserQuery 类型。

画面14:
- PDF 页面显示了 GraphQL 的 Schema 和类型规范。
- 代码：展示了如何定义字段和参数。
- 代码：展示了如何执行查询。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1:
```java
.field(GraphQLFieldDefinition.newFieldDefinition().name("id").type(Scalars.GraphQLLong)
.field(GraphQLFieldDefinition.newFieldDefinition().name("name").type(Scalars.GraphQLString)
.field(GraphQLFieldDefinition.newFieldDefinition().name("age").type(Scalars.GraphQLInt)
.build();

/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20)))
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面2:
```java
/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build())
.dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20)))
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面3:
```java
/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build())
.dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20)))
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面4:
```java
/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.argument(GraphQLArgument.newArgument().name("id").type(Scalars.GraphQLLong).build())
.dataFetcher(new StaticDataFetcher(new User(id:1L, name: "张三", age: 20)))
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面5:
```java
/**
 * user : User #指定对象以及参数类型
 */
GraphQLFieldDefinition userFieldDefinition = GraphQLFieldDefinition.newFieldDefinition()
.name("user")
.type(userObjectType)
.dataFetcher(environment -> {
    return new User(id:1L, name: "张三", age: 20);
})
.build();

/**
 * type UserQuery { #定义查询的类型}
 */
GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
.name("UserQuery")
.field(userFieldDefinition)
.build();
```

画面6:
```java
Language level: 8 - Lambda, type annotations etc.
```

画面7:
```java
/**
 * schema { #定义查询 }
 */
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().query(userQueryObjectType).build();
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user{id,name,age}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
System.out.println(result.toSpecification());
```

画面8:
```java
/**
 * schema { #定义查询 }
 */
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().query(userQueryObjectType).build();
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user(id:1){id,name}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
System.out.println(result.toSpecification());
```

画面9:
```java
/**
 * schema { #定义查询 }
 */
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().query(userQueryObjectType).build();
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user(id:100){id,name}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
System.out.println(result.toSpecification());
```

画面10:
```java
// 代码：展示了如何定义字段和参数。
// 代码：展示了如何执行查询。
```

画面11:
```java
import cn.itcast.GraphQL.vo.User;
import GraphQL.ExecutionResult;
import GraphQL.GraphQL;
import GraphQL.Scalars;
import GraphQL.schema.GraphQLLong;
import GraphQL.schema.GraphQLString;
import GraphQL.schema.GraphQLInt;
import GraphQL.schema.GraphQLFieldDefinition;
import GraphQL.schema.GraphQLObjectType;
import GraphQL.schema.GraphQLObjectType.newObject;
```

画面12:
```java
/**
 * schema { #定义查询 }
 */
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().query(userQueryObjectType).build();
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();

String query = "{user(id:100){id,name}}";
ExecutionResult result = graphQL.execute(query);

System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
System.out.println(result.toSpecification());
```

画面13:
```java
import static GraphQL.schema.GraphQLObjectType.newObject;
import static GraphQL.schema.GraphQLFieldDefinition.newFieldDefinition;

public class GraphQLDemo {

