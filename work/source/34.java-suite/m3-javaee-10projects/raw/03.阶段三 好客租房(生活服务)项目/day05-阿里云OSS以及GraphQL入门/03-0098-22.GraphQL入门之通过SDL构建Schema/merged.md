# 22.GraphQL入门之通过SDL构建Schema

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\22.GraphQL入门之通过SDL构建Schema【海量资源尽在 ubkz.com】.mp4
- 时长 12分30秒（音频 751s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续啊呃前面呢我们通过这种java API的方式呢去做了以这样的一个grepql这样的一个实现啊呃其实我们会发现这种代码呢编写起来还是比较费劲的啊那么尤其是你看像这种我们需要对每个这个对象去做这样的一些这个定义那么大家可以想一下如果说我们以后的对象有很多的话那么这种定义还是非常的麻烦的啊也非常的繁琐的啊那么
[00:29] GraphQL-Java这个工程呢为我们提供了有另外一种构建的方式就是这种方式就通过我们的这个配置文件或者说通过我们这个GraphQL这样的文件的一个构建那么它呢把它称之为叫做SDL这种方式去作为构建这叫一种特殊的一种GraphQL
[00:51] DSL文件那么把它称之为SDL官方呢其实也推荐使用这种SDL的方式去做一个构建啊构建那么下面我们就来来看一下这种方式怎么样去做一个构建那么我们先在我们resource下面创建这样的一个文件啊咱们把这个文件先创建出来在这我们来创建一个文件好那么这个文件呢创建好之后呢我们把这个内容拷过来
[01:23] 这个内容呢其实前面我们也都说过也是比较简单的这样的一个内容就是定义了一个叫做user query然后呢有定义了一个user然后呢我们指定它的参数是id然后它的类型呢是这种long类型ok对象类型呢是user类型就是这样的一个定义那么接下来我们来看一下通过这种sdl这种方式去构建这个scammer应该怎么去玩啊
[01:48] 那么在这建议大家来去安装一个这个GrabQL这样的一个插件那么装完之后它就会有这样的一个提示或者这样的一个显示OK好那么如果你不装这个插件也可以就是我们通过一个文本编辑器对这个文件做一个编辑就可以了好那么我们接着继续往下面看那么下面我们来写一个代码去做这样的一个测试好那么这个类的名字叫GrabQL
[02:16] ql然后呢叫sdl啊demo啊写这样的一个测试的一个用例然后呢下面我们来写一个man方法然后呢我们这个man方法中怎么去写呢我们还是一点一点来分析去写它这个代码啊呃这个代码呃相对于前面可能简单一点啊但是呢第一次初次接触呢还是会觉得有点繁琐好那么我们接着继续往下面去看啊那么我们在这个位置呢写一个webql
[02:46] 依然是通过他去这个对象去做一些相关的操作等于什么呢等于grabql.new一个grabql还是刚才这种方式然后呢我们通过build去得到一个他然后呢我们给他设置先设置为一个none然后呢下面是不是就可以做一些这个查询了那我们把前面这个查询这个拷过来吧把它拷过来这个都一样这个都是一样的把它拷到这
[03:15] 然后我们就不要好保留这两个就可以了好嘞那么接下来我们要解决的是不是这个none的问题那么这个none怎么解决我们给它定义一个叫什么叫webql对吧ql然后叫scammer然后它就等于什么先等于一个none把这个先传递给它传递给它
[03:41] 好通过这个scammer去构造一个ql然后做一个查询那么关键的问题呢我们就要解决是他啊那么在前面我们这个实践中呢我们是通过我们的api的方式去构建了一个这个scammer那么接下来呢我们将通过我们的sdl这种方式去做构建所以在这个位置呢我们就不能去通过啊前面的去啊这样去做构建了而是通过一个叫做new一个啊new一个scammer
[04:11] scammerscammer的一个generatorgenerator然后呢去去做一个构建啊去用一个这个对象去做一个构建那么这个对象呢需要有两个参数啊我们来看一下这两个参数它是什么意思呢我们来点进去来看一下它需要有两个参数啊一个是叫做type definition register另外一个呢叫做这个waiting然后呢我们把它拷过来
[04:41] 那么拷贝到哪里呢拷贝到这那么我们先拷到这然后呢我们做一个简单的一个处理OK把它封号结束然后呢它呢也设置为它吧把两个呢圈给它设置为None设置为None然后呢下面的这个也设置为None好嘞好那么这两个我们搞定之后啊那么我们就可以把这两个参数呢传递给它了然后我们一个一个来做一个解决
[05:09] 那么我们只要把这两个参数的这个none这个问题解决掉那么其实我们这个代码就写完了哎呀ok好的我们先来看一下上面的这个这个呢是对于type的一个定义啊一个注册那么他怎么样去做一个注册呢其实我们在这个位置呢需要去new一个叫做scammer的一个scammer的一个parter一个解析器啊EMA然后呢parter去解析
[05:37] 解析什么呢去解析我们的这个前面所写的这个文件啊那么我们通过一个解析吧那么通过什么解析呢就是我们通过这个文件的内容去做一个解析那我们定一个stream叫做failcontactor就是内容等于什么呢先等于空然后呢我们把这个内容呢去传递过去就是我们要通过这个schema这个parter解析器
[06:05] 去解析我们刚刚所创建的这个文件来得到一个我们这个register就是注册器然后呢我们来看一下这个内容怎么得到呢所以我们接下来就需要解决一个问题就是读取这个文件的一个内容那么我们先把这个文件的名字呢先给它定义出来fail name等于等于它对吧是这个文件那么怎么样去读取这个文件呢那我们是不是需要将来做一个读取
[06:34] 那么我们先导入一个依赖吧什么依赖呢就是我们那个关于IO的一个操作的一个依赖叫commons-io-commons然后呢IO这个依赖把它导入进来这个依赖我相信大家也都用过啊所以呢我们来看一下在这个里面呢我们用看一下这个IO怎么去用啊怎么去用那么我们通过这个IOIO有tools去toostring
[07:03] toString去做一个转化对吧然后呢我们需要拿到一个inputStream和一个encoding那么inputStream怎么拿那么当然encoding比较简单我们先来写UTF-8就可以了那么这个inputStream怎么去拿呢我们是可以通过这么去拿通过这个这个类点这个class拿到它的一个叫做
[07:33] 点什么呢get class loader然后呢再去get resource就去拿到他通过他的一个类的加载器去拿他的一个resource资源那么资源谁呢是不是就是这个fail那么通过这个get resource他就会去查找他的resource下面的一个资源的内容ok
[07:55] 好那么通过他呢是不是就可以去读取到我们的一个文件那么我们把它呢这个他会有一个异常的抛出啊那就抛出这个异常了好那么现在我们是不是其实解决了这个问题对吧通过这个文件然后去得到一个注册器下面我们来看一下他怎么解决呢他是在解决我们的数据的查询的问题啊他呢解决的是解决的是数据的查询啊解决的是数据的查询
[08:22] 是数据的查询我们来看一下这个叫做run time warning那么它是去查询数据那么所以我们在这个里面就需要给它去定义一些数据的查询那么这个怎么写我们来看一下需要通过它的API来做一个来做一个编写那么我们调用它里面有个方法叫一个new一个run time一个warning然后我们在这个里面去build当然了不能直接build对吧里面还去设置一些内容然后点type
[08:53] 那么这个type是谁呢type其实就是我们的在我们这个文件中啊所定义的这个叫做yourquery啊这个啊定义的它然后呢我们再来给它定义一个啊使用的Lamb的表达式去拿到它一个build对象然后呢我们去往这个build对象中啊给它去添加一些data一个fetcher就是去查询这个数据啊那么查询数据
[09:18] 那么查询什么数据呢我们来看一下我们这个文件那么在文件中呢我们查询的是不是这个Url这个数据对吧所以我们写的这个Failed Name就是Url那么第二个参数呢就是我们去如何去查询这个数据那么所以呢我们可以看一下在这个位置是不是就可以拿到我们的这个Argument然后呢就是来一个叫做ID然后我们它的返回值是不是就是可以拿到一个Lung的一个ID对吧
[09:46] 然后呢我们就可以去return一个new一个user然后呢ID就是他这样咱们把前面的那个代码就靠过来吧那就不重复了啊好那么找到前面的这个代码去new的这个代码我们来靠一下那么把它就拿过来哎OK好那么这样的话我们是不是就已经就实现了啊这样的一个查询好把它丢到这个位置来
[10:13] 好那么到这里这个会报错这个bill的这个位置呢我们就不需要去这个大括号了直接去调用就可以了把这个大括号拿掉这个拿掉应该是这样的好这样就对了刚刚是这个括号呢有点问题好嘞那么我们现在是不是就完成了一个数据的一个查找对吧查询那么下面我们来做一个测试来看一下那么它是否能够查询到我们这个数据呢走来看一下那么等待它的一个执行
[10:43] 那么我们现在要查询的呢就是ID和这个NAMEID和NAME那么我们可以看到在这个位置是不是已经查询到了一个ID和一个NAME当然了我们还是可以给它添加一个比如说AGE那么它是不是能查到这个AGE的这样的一个数据呢我们来看一下那么同样是不是AGE这个数据是不是依然是可以查询到那么通过这种方式是不是就已经实现了我们的一个实现了我们的一个这样的一个编写对吧GridQL的一个服务的一个定义
[11:14] 那么这种方式是不是显然要比前面我们的通过我们的存这个java API这种方式定义是不是要简单那么一些对吧要简单一些那我们把这个给大家加一些注释啊那么下面这个完成的一些工作是不是就是读取我们的这个webql文件ql文件然后呢进行什么呢进行解析啊进行解析
[11:41] 那么下面呢是不是解决这个查询这个问题然后呢下面我们是不是就可以去生成我们的一个scammerscammer生成这个scammer之后呢我们就可以根据根据这个scammer对象对象来生成我们的什么GrabQL这样的一个对象然后呢通过这个对象是不是就可以执行下面一个查询了这个呢就是
[12:08] 官方的所推荐的第二种方式通过什么呢通过我们这个呃国家QR文件去构建我们的scam然后呢通过这个scam再去构建我们那个呃对象然后去最后做一个查询哎OK好那么是关于我们通过啊通过这个SDL来构建我们的scam呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Java 项目中通过 GraphQL 的 Schema 定义和 RuntimeWiring 配置来构建并执行 GraphQL 查询。

2) 按时间顺序列出每张画面的要点：
画面 1：
- 在 IntelliJ IDEA 中，展示 `GraphQlDemo.java` 文件，其中定义了 GraphQL 对象类型 `User`，包含字段 `id`（GraphQlLong）、`name`（GraphQlString）和 `age`（GraphQlInt）。
- 同时定义了查询字段 `user`，并设置了参数 `id` 的数据获取器（dataFetcher）。

画面 2：
- 在 IntelliJ IDEA 中，右键点击项目目录 `src/main/java/itcast/graphq`，弹出菜单，选择“Create New Class”。
- 用于创建新的 Java 类。

画面 3：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件的创建过程。
- 项目结构显示 `src/main/resources/user.graphqls` 文件。

画面 4：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件的初始代码，其中定义了 GraphQL 查询 `user(id:100) {id,name}` 并执行。

画面 5：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中开始使用 `SchemaGenerator` 来生成 Schema。
- 代码中包含 `SchemaGenerator` 的构造函数和 `makeExecutableSchema` 方法。

画面 6：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中使用 `SchemaGenerator` 生成可执行的 Schema。
- 代码中包含 `new SchemaGenerator().makeExecutableSchema()`。

画面 7：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中使用 `SchemaParser` 解析 GraphQL 文件。
- 代码中包含 `new SchemaParser().parse(fileContent)`。

画面 8：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中使用 `IOUtils.toString` 方法读取 `user.graphqls` 文件内容。
- 代码中包含 `IOUtils.toString(GraphQLSDLDemo.class.getClassLoader().getResource(fileName))`。

画面 9：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中使用 `SchemaParser` 解析文件内容并创建 `TypeDefinitionRegistry`。
- 代码中包含 `new SchemaParser().parse(fileContent)`。

画面 10：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中创建 `RuntimeWiring` 对象并设置查询类型。
- 代码中包含 `RuntimeWiring.newRuntimeWiring().type(typeName: "UserQuery", builder -> ...).build()`。

画面 11：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中定义了 `UserQuery` 类型的数据获取器。
- 代码中包含 `builder.dataFetcher(fieldName: "user", environment -> { Long id = environment.getArgument(name: "id"); return new User(id, name: "张三:" + id, age: 20 + id.intValue()); })`。

画面 12：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中执行 GraphQL 查询并打印结果。
- 代码中包含 `System.out.println("query:" + query); System.out.println(result.toSpecification());`。

画面 13：
- 在 IntelliJ IDEA 中，展示 `GraphQlSDLDemo.java` 文件，其中修改了 GraphQL 查询，增加了 `age` 字段。
- 代码中包含 `String query = "{user(id:100) {id,name,age}}";`。

画面 14：
- 在 Adobe Reader 中，展示 PDF 文档的第 7.2.2 节“构建schema”，其中包含 Java 代码示例。
- 代码中包含 `import cn.itcast.GraphQL.vo.User;` 和 `import orgaql.schema.idl.TypeDefinitionRegistry;`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```java
public class GraphQLDemo {
    public static void main(String[] args) {
        /* type User {#定义对象}
        GraphQLObjectType userObjectType = newObject()
            .name("User")
            .field(newFieldDefinition().name("id").type(GraphQLLong))
            .field(newFieldDefinition().name("name").type(GraphQLString))
            .field(newFieldDefinition().name("age").type(GraphQLInt))
            .build();
        /* user : User #指定对象以及参数类型
        GraphQLFieldDefinition userFieldDefinition = newFieldDefinition()
            .name("user")
            .type(userObjectType)
            .argument(newArgument().name("id").type(GraphQLLong).build())
            .dataFetcher(environment -> {
                Long id = environment.getArgument(name: "id");
            });
    }
}
```

画面 3：
```java
package cn.itcast.GraphQL.demo;
public class GraphQLSDLDemo {
}
```

画面 4：
```java
import GraphQL.ExecutionResult;
import GraphQL.GraphQL;
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema: null).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 5：
```java
import GraphQL.schema.GraphQLSchema;
import GraphQL.schema.idl.SchemaGenerator;
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema();
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 6：
```java
import GraphQL.schema.idl.SchemaGenerator;
import GraphQL.schema.idl.TypeDefinitionRegistry;
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        TypeDefinitionRegistry typeRegistry = null;
        RuntimeWiring wiring = null;
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema();
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 7：
```java
import GraphQL.schema.idl.SchemaParser;
import GraphQL.schema.idl.TypeDefinitionRegistry;
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        String fileContent = null;
        TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(fileContent);
        RuntimeWiring wiring = null;
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 8：
```java
public class GraphQLSDLDemo {
    public static void main(String[] args) {
        String fileName = "user.graphqls";
        String fileContent = IOUtils.toString(Reader input);
        TypeDefinitionRegistry typeRegistry = null;
        RuntimeWiring wiring = null;
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 9：
```java
public class GraphQLSDLDemo {
    public static void main(String[] args) throws IOException {
        String fileName = "user.graphqls";
        String fileContent = IOUtils.toString(GraphQLSDLDemo.class.getClassLoader().getResource(fileName));
        TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(fileContent);
        RuntimeWiring wiring = null;
        GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);
        GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
        String query = "{user(id:100) {id,name}}";
        ExecutionResult result = graphQL.execute(query);
        System.out.println("query:" + query);
        System.out.println(result.toSpecification());
    }
}
```

画面 10：
```java
public class GraphQLSDLDemo {
    public static void main(String[] args) throws IOException {
        String fileName = "user.graphqls";
        String fileContent = IOUtils.toString(GraphQLSDLDemo.class.getClassLoader().getResource(fileName));
        TypeDefinitionRegistry typeRegistry = new SchemaParser().parse(fileContent);
        RuntimeWiring wiring = RuntimeWiring.newRuntimeWiring()
            .type(typeName: "UserQuery", builder -> {

