# 20.GraphQL入门之编写代码实现查询用户的GraphQL服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\20.GraphQL入门之编写代码实现查询用户的GraphQL服务【海量资源尽在 ubkz.com】.mp4
- 时长 16分55秒（音频 1016s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就正式的来去写一下这个代码就是我们使用GrabQI-Java这个工程呢我们来去编写一下GrabQI这样的一个接口的服务那么下面呢我们要编写的是查询User对象这样的一个服务那么我们来看一下它的一个服务结构的一个定义那么这个结构的定义呢我们只是先做一个参考OK好那我们来看一下
[00:27] 那么在这个位置我们定义一个scammer然后下面有一个query是吧有一个UqueryUquery是不是就是这种类型的定义了个type这种类型的Uquery
[00:36] 那么Udo快捷呢又去定义了一个user对象user的一个这个字段然后呢下面的对象呢是不是这个user对象然后呢继续往下面去定义那么user对象呢又会有一些IDName还有Age这样的一些这个字段OK那么大概呢就是有这样的一个定义那么其实我们可以看到下面这个user对象的一个定义是不是就是跟我们刚刚所创建的一个user对象其实是一致的OK好那么下面我们就来编写这个代码我们来去做一个实现
[01:05] 那么进入我们这个刚刚创建的工程然后在这工程里面呢去创建一个包呃叫什么包呢就叫demo吧啊叫个demo包点demo然后呢在这个里面呢我们去写一个demo这个代码那么就写一个叫做什么呢graper ql啊ql然后呢demo啊就写这样的一个呃demo然后呢我们在这个里面呢去写一些这写一个我们的一个
[01:36] 慢方法啊然后在这个慢方法里面呢去写一些相关的代码大家要注意了写这个GrabQL杠加吧这个他的一些这个APL不是特别好写啊所以呢我们需要一点一点去去写他这个代码啊那么我边写呢边去讲解啊来帮助大家对这个代码的一个理解那么我们首先呢去需要定义一个GrabQL然后这样的一个对象啊通过这个对象呢我们要去做一个查找
[02:06] 那么这个对象怎么来的呢它需要通过这个GrabQL这个对象中有一个这个new这个GrabQL看到了吗然后呢需要传递一个参数这个参数是什么呢我们先不管把它设置为一个num然后呢我们来一个build那么其实可以看到GrabQL-java这个工程它的一个构造对象的方式是通过什么什么结构呢是不是这个构建器的方式去做一个构建啊OK
[02:31] 那么当我们去有了这个GrabQL这样的对象的话我们就可以去对他做一个查询的操作以是Q的去做一个查询OK那么我们先可以把这个查询是不是写出来比如说我们叫一个query等于什么呢给他个字符号那么就叫注意查询的是以这个以这个大括号开头的其实就是我们那个json的一个字符号对吧然后呢我们要查询这个Ura这个对象
[02:55] 那么查询优对象的什么样的属性呢查询他的UID和Name我们先写这样的一个小的一个案例然后我们把这query对象query这幅创是不是传递给他好那么到这儿我们是不是就已经把这个基本的一个结构是不是打好了那么关键是我们解决的问题是不是解决这个none的问题对吧那我们来看一下他的需要接收的是一个grabql schema这样的一个对象那么他需要什么我们是不是给他定义什么对不对那么就点grab
[03:22] QL什么呢Scammer这个对象那么定义个他那我们来看一下这个Scammer这个对象那么这个对象怎么去写呢我们先给他设置为空先把它给他丢过来OK这个大家应该能看懂吧好那么我们来看一下这个None怎么处理那么这个None呢我们显然呢是需要去做这样的一个定义是不是要定义定义定义个他呀对吧所以呢我们需要
[03:47] 给他定义一个这个query怎么定义呢通过一个grabql scammer然后呢他也是通过一个点点一个new一个scammer定义一个新的scammer然后呢定义一个什么呢query定义一个query这个query呢他要设置的是一个type那么我们先给他设置为none吧然后呢做一个build这样的话我们是不是就得到了一个我们先给他设置为none然后呢
[04:19] 先得到一个这个build然后得到一个scammer对象那么接下来其实我们要解决的问题就把这个num给它解决掉就可以了对吧那么这个num怎么解决呢来看一下那么在这个query中它所接收的有两个是build一个就是grabql object type我们选用下面这种方式我们来给它定义一个叫做grabqlql然后就有一个object type
[04:46] 那么这个定义的是什么呢我们来看一下那么在前面呢我们其实只是定义了一个scanner对吧那么他所定义的是这个queryquery是谁呢query其实是他是不是就是userquery啊所以我们接下来要定这个userquery那么我们就需要一个叫userqueryquery什么呢叫一个object type然后呢给他设置为呢那么我们把它传递过来是不是就
[05:12] 这样的话是不是就OK了好那么下面我们要解决的是不是就这个none的这个问题把它解决掉是不是就OK了那我们来看一下这个怎么样去解决呢那么我们还是要回到我们前面的这个定义在这个定义上面我们来看一下那么在这个位置呢我们可以看到它是不是在前面定义一个scanner然后下面定义一个这个url query而我们现在只定义需要定义这个url query对不对需要定义它那么我们来定义一下这个url query
[05:39] 那么他这个num怎么样去定义一个对象呢通过这个object type的静态方法有一个叫new一个object然后呢给他去设置一个什么的name这个name是谁呢其实是他啊上面的这个就是yellowquery跟他要保持一致
[05:56] 然后呢我们给他去做这样的一个设置最后呢点来一个build当然这个还没有结束这个没有结束因为在他的内部呢其实是需要一些我们的一些这个对象的一些定义的所以呢我们自断的定义不是对象自断的定义那我们需要给他设置一个什么呢设置一个这个failed设置一个failed那么这个failed呢我们选用的是第二个这个参数类型叫做
[06:24] grabql field definition就是一个定义啊一个定义那么它是什么呢其实我们要解决的是不是就是变成这个none的问题了哎ok好那么我们继续往下面看而这个它所定义的是不是就是一个Ura这个类型啊或者说就是这样的一个定义那么ok那么我们来先把它这个定义给它先创建出来那么就叫什么呢grab什么呢呃ql叫什么呢叫object
[06:53] 叫什么呢Failed,叫Failed definition是它别搞错了那么就叫User就叫UserFailed definition就叫它
[07:04] 然后呢把它设置为一个浪然后呢我们把这个对象的传递给他好这样的话呢他这个就搞定了那么接下来我们要解决的问题呢其实是这个浪的问题对吧那么到这里呢我们其实就开始要定义的是不是这一项内容对吧这一行第七行这个代码那么他怎么玩呢其实还是这个他的一个套路啊就是去通过一个new一个
[07:27] definition然后呢去最后呢去做一个build当然了这个中间呢还需要给他设置一些点一个什么的name这个name要注意他取决意的就是我们里面的这个name是他啊他这个name哎name哎写一个这不错然后呢他的一个type是什么类型呢要注意他的一个type就是说这个属性
[07:50] 这个字段它所对应的这个后面的这个对象的类型是谁呢我们要给它设置一个type而这个type呢我们是不是又要去做一个定义啊所以我们要再去给它定义一个groupqlobject type它就叫什么呢叫做urlurlobject typeurlobject type等于什么呢先设置为呢我们把这个urlobject type呢给它也传递过来
[08:15] 然后呢这个none这个我们来看这个none怎么去解决呢还是一个相同套路通过它的一个静态的一个方法然后呢再去做一个build当然了这个里面不能直接做build对吧还需要去给它设置一些内容那么这个应该怎么样去做一个设置呢其实就是说你这个url应该怎么设置那么我们就需要给它设置它的一个name其实就是谁呢要注意这个时候就变成什么大写的这个url大写的这个url
[08:43] 好然后呢我们继续往下面看那么他呢是不是又有一些其他的字段比如说有ID,Name这样的字段那么我们同样通过这个Field要给他进行做一个设置那么我们通过这个还是通过这个Definition给他去New一个Definition然后呢去设置一个Name叫谁呢ID
[09:04] 然后呢继续给他设置一个type这个时候type呢我们就给他设置一种这种类型啊那么type就设置他了那么我们使用的是你看那么我们后面使用的这种lang呢虽然是不是他的一个标令啊所以呢我们使用他的scannerscanners然后呢设置他的一个叫做lang啊这样的一个类型啊那么我们往下面拷贝那么下面呢我们还有name和age那么name是什么类型呢
[09:33] Name是它的叫做字符号类型对吧就叫String然后下面的Age是Int类型那我们来看一下它有没有对应的Int类型不是get点那么找到IntOK好到这里我们这个User这个是不是就搞定了把它是不是就传递给它对吧OK那么我们来梳理一下那么在前面我们可以看到我们所定义的是这样一个定义那么我们刚刚所写的这个代码
[10:03] 对吧这个代码其实它所完成的一个所完成的一个这个功能或者说完成了一个内容的其实就是完成了这样的一个定义对吧定义了这样的一个实现OK好那么下面的这个定义呢它是定义了什么这个的定义它其实定义的是不是就是上面的这个内容对吧定义的是它OK定义的是这一句话然后呢下面这个url query它的一个实现呢其实实现的是上面的这个内容
[10:34] 就是这个内容我们把这个就这样拷拷贝他他实现这样的一个定义然后呢继续往下面看这个scanner他呢是不是就完成了上面的这个定义完成了上面的这个定义所以我们通过这种代码的这种形式呢去实现了他的一个这种结构的一个定义
[10:58] 好那么接下来我们是不是就可以尝试去查询一下呢对不对那么我们来看一下isq的做一个执行查询那么它的返回值呢它其实返回的是一个叫做reout这样的一个对象啊reout的对象那么我们通过这个reout其实可以去把它的两个信息打印出来对吧一个呢是打印它的打印它的reout打印它的errors错误还有一个打印它的一个叫做date或它的一个数据啊它的一个数据
[11:28] 他的一个数据OK好那么这两个内容呢可以去把它打印出来当然了我们也可以把这个他的一个什么呢查询叫query吧queryquery冒号加一个谁呢加一个上面这个query对象就我们把这个查询支付刹也打印出来好那么接下来呢我们去做一个执行查询走看他是否能够查到数据呢能不能查到数据那么OK我们可以看到显然现在是不是
[12:02] 查不到数据啊对吧那么为什么查不到数据呢我们来看一下啊他的提示是说这个url query没有fail在就是我们这个对象啊在这个url query中呢没有定义什么意思呢就是说你在url query的定义是不是在这个里面我们做了一个定义定义的是不是这个url这个小写的url啊而你查询的时候你通过这个大写的url查询那么显然是不对的啊所以我们通过这个小写的去做一个查询我们再去执行走
[12:35] 看一下他这回能不能查到数据那么OK现在我是不是可以正常的去做执行但是是不是没有数据啊各位想一想没有数据为什么没有数据呢那么在我们前面所有这个呢都是做了一些定义并没有去真正的去查询数据是不是所以呢我们是缺少一个查询数据的一个动作啊那么这个查询数据的动作在哪里呢
[13:02] 那么我们是不是需要找到它的一个位置那么其实我们可以看到在这个位置是不是我们定义了这个Ur这个对象那么所以在这个位置我们要指定它的一个这个数据你是从哪里去做一个查询点一个data一个factor去做一个获取获取这个数据
[13:21] 那么这个里面呢我们就为了简单做一个实现呢我们先给他去实现一个什么呢去定义一个new一个static就静态的数据就是说无论你怎么样去查询那么我返回的都是这个数据做这样的也先做一个简单的一个实现啊那么我们去定义一个user那么user呢我们可以设置一个他的一些参数啊一些数据那比方说他的ID呢就是1然后他的名字呢对应的就张三然后呢他的年龄呢对应的就是
[13:50] 20哎呀OK好那么我们是不是添加了这样的一个数据啊那么接下来呢我们再次做一个运行来看一下效果那么有没有查到数据呢那么你可以看到在这个位置是不是就已经查询到我们这个数据了对不对那么我们来看一下在这个位置我们查询的时候是不是指定了他的ID和Name如果我再给他添加一个指定叫什么呢叫age那么看他是否能够返回我们的三个字段呢就我们前面所说他这种效果
[14:20] 就是按需查找可以发现是不是依然可以去返回的这三个字段那么如果我只需要一个字段那么是不是我只需要来一个ID那么它是不是就会只返回一个字段OK那么这样的话是不是就实现前面所做的那个什么按需返回对不对OK好那么这样的话我们就把它的第一个代码我们就给大家演示完成了通过我们那种Java API的方式我们去实现了这样的一个定义以及一个查询
[14:49] 那么要注意的是在我们讲义中所实现的这个呢是将每一个这个步骤去拆分成了一个一个的这个方法那么其实在这个位置跟我们的这样的实现啊其实是没有任何区别的只是我们在实现的过程中啊没有去拆分这个方法而已啊那么其实是一样的啊效果是一样的OK好那么打印的一个结果就是这样的一个结果啊好
[15:13] 那么接下来呢我们再讲一个小的一个点呢就是我们在打印这个error和data的时候啊那么其实还有另外一种输出的方式就是这样的输出来看一下那么在在GrabQL中呢它有一个规范中有一个这样的一个定义就是要求语道中呢要有一个标准的一个这样的一个输出那么我们通过这个方法来获取它的一个标准的一个输出那我们来看一下它会有什么样的一个输出的一个结果
[15:42] 那么在这个结果中呢他会以这样的一个结果去做一个输出就是外面的会有一个大括号中间有个date等于什么什么OK那么如果当我们的这个查询出错的话或者说我们的这个查询失败的话那么他会把我们的error做一个返回我们来看一下那么他的返回的结构就会变成这个样子就error等于什么什么OK这样的话是一个标准的一个返回那么我们的以后呢会使用这种标准的一个输出去这样做
[16:12] 这样的一个数据的一个响应和数据的一个返回OK而不是采用这样的一种方式啊这个点大家一定要注意哎OK这个是规范中所这样做了这样的一个规范啊
[16:23] 好那么关于我们的第一个这个小案例呢我们就讲到这里这个代码啊大家可能第一次接触的话会觉得有点呃有点怪或者说有点难去理解或者难去记忆啊那么我们需要去对照着啊这样的一个他的一个结构的一个定义然后呢去编写这样的代码然后呢再去做这样的一个理解那么我相信大家呢呃多敲几遍那么就能够去理解这样的一个代码好那么关于第一个
[16:50] 这个查询的这个用户的一个实现呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 中使用 GraphQL 框架定义查询对象类型、构建 Schema 并执行查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中 GraphQL Schema 的定义片段，包含 `type User { id:Long! name:String }`。
画面2：IDE 中显示 `GraphQlDemo.java` 的 `main` 方法，创建 `GraphQL` 实例。
画面3：在 `main` 方法中调用 `GraphQLSchema.newBuilder().query(...)` 构建 Schema。
画面4：PDF 文档中展示 `User` 类型的定义和 Java 实现的导入语句。
画面5：IDE 中 `GraphQlDemo.java` 的 `main` 方法，使用 `GraphQL` 类的静态方法。
画面6：IDE 中 `GraphQlDemo.java` 的 `main` 方法，定义 `GraphQLObjectType` 和 `GraphQLFieldDefinition`。
画面7：IDE 中 `GraphQlDemo.java` 的 `main` 方法，为 `userFieldDefinition` 设置 `type` 为 `userObjectTy`。
画面8：IDE 中 `GraphQlDemo.java` 的 `main` 方法，为 `userFieldDefinition` 设置 `name` 为 `"user"`。
画面9：IDE 中 `GraphQlDemo.java` 的 `main` 方法，定义 `userQueryObjectType` 并设置 `field`。
画面10：IDE 中 `GraphQlDemo.java` 的 `main` 方法，定义 `query` 字符串并执行。
画面11：IDE 中 `GraphQlDemo.java` 的 `main` 方法，为 `userFieldDefinition` 设置 `.dataFetcher(...)`。
画面12：PDF 文档中展示 `createGraphqlSchema` 方法的定义和 `createUserDefinition` 方法。
画面13：IDE 中 `GraphQlDemo.java` 的 `main` 方法，执行查询并打印结果。
画面14：IDE 中 `GraphQlDemo.java` 的 `main` 方法，打印 `result.toSpecification()`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```GraphQL
#对应的User定义如下
schema {
  query: UserQuery
}
type UserQuery {
  #定义查询的类型
  User: User #指定对象以及参数类型
}
type User {
  #定义对象
  id:Long! # !表示该属性是非空项
  name:String
}
```

画面2：
```java
package cn.itcast.GraphQL.demo;
import GraphQL.GraphQL;
public class GraphQlDemo {
    public static void main(String[] args) {
        GraphQL graphQL = GraphQL.newGraphQL(...
    }
}
```

画面3：
```java
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema().q
    .query(Builder builder)
    .query(GraphQLObjectType queryType)
    .equals(Object obj)
    graphQL.execute(query);
```

画面4：
```java
package cn.itcast.GraphQL.demo;
import cn.itcast.GraphQL.vo.User;
import GraphQL.ExecutionResult;
import GraphQL.GraphQL;
```

画面5：
```java
GraphQL GraphQL = GraphQL.newGraphQL(graphqlSchema).build();
```

画面6：
```java
GraphQLObjectType userObjectType = GraphQLObjectType.newObject()
    .name("User")
    .field(userFieldDefinition)
    .build();

GraphQLObjectType userQueryObjectType = GraphQLObjectType.newObject()
    .name("UserQuery")
    .field(userFieldDefinition)
    .build();

GraphQLSchema graphQLSchema = GraphQLSchema.newSchema()
    .query(userQueryObjectType)
    .build();

GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema)
    .build();
```

画面7：
```java
.type(Builder builder)
.type(GraphQLObjectType type)
.toString()
.type(GraphQLObjectType type)
```

画面8：
```java
.type(Scalars.GraphQLLong)
.type(Scalars.GraphQLString)
.type(Scalars.GraphQLInt)
```

画面9：
```java
GraphQLSchema graphQLSchema = GraphQLSchema.newSchema()
    .query(userQueryObjectType)
    .build();

GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema)
    .build();

String query = "{User{id,name}}";
graphQL.execute(query);
```

画面10：
```java
String query = "{User{id,name}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
```

画面11：
```java
.dataFetcher(new StaticDataFetcher(new User()))
```

画面12：
```java
public static GraphQLSchema createGraphqlSchema(GraphQLFieldDefinition userDefinition) {
    GraphQLObjectType userQuery = newObject().name("UserQuery")
        .field(userDefinition).build();
    return GraphQLSchema.newSchema().query(userQuery).build();
}

// 定义查询的类型
public static GraphQLFieldDefinition createUserDefinition(GraphQLObjectType userObjectType) {
    return GraphQLFieldDefinition.newFieldDefinition()
        .name("user")
        .type(userObjectType)
        .build();
}
```

画面13：
```java
String query = "{user{id,name,age}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.getErrors());
System.out.println(result.getData());
```

画面14：
```java
System.out.println(result.toSpecification());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PDF 文档标题为“7.1.3、编写查询User对象实现”，左侧目录显示“7.1.3、编写查询User对象实现”。
画面4：PDF 文档标题为“黑马程序员”，下方有“改变中国IT教育，我们正在行动”。
画面12：PDF 文档标题为“7.1.3、编写查询User对象实现”，左侧目录显示“7.1.3、编写查询User对象实现”。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

