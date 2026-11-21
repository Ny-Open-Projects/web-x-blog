# 23.GraphQL入门之对象嵌套

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\23.GraphQL入门之对象嵌套【海量资源尽在 ubkz.com】.mp4
- 时长 7分15秒（音频 435s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么我们接着继续前面呢,我们通过两种方式呢去
[00:04] 实现了我们的GraphQL的一个这样的一个服务的一个编写那么第一种方式是通过我们的Java API的方式对吧第二种方式第一种方式看一下是不是在这个位置通过这种Java存的这种Java API的方式去实现第二种方式是通过我们去定义一个我们这个GraphQL的一个文件然后通过去解析这个文件然后得到我们的一个对象然后去做
[00:30] 得到我们scam的一个对象然后再去做我们的一个查询那么是这样的两种实现那么官方的更推荐的使用的是第二种是吧通过这种sdl这种方式那么大家其实我们在编写完成之后呢也会发现这种方式呢就更加的方便和简单一点啊
[00:49] 那么接下来我们要看到内容的是在前面我们写的这两个demo中他们的使用这个U的对象都是一个单一的U对象它并没有一些这种对象之间的关系对吧所以接下来我们就来解决一个问题就是一个对象的一个欠套那么比如说我们现在还有另外一个对象叫card对象那么用户和这card对象是一对一的关系
[01:14] 那么这card对象呢是代表着他的一个身份证身份证的一个对象那么一个用户是不是只能有一个身份证号所以他们之间关系呢是一对一的关系那么下面呢我们就来去展现一下这种关系的一种这种有了这种关系之后啊那么去实现我们的GradeQL这样的一个服务的话那么应该怎么去做啊那么我们下面来创建一个card对象把这个对象呢我们创建出来那么拷贝这个代码把这个代码我们Ctrl C拷一下
[01:43] 然后呢进入到我们的这个VO这个包然后呢把它贴过来好来看一下这样的话呢我们这个代码呢是不是就已经贴进来了那么下面呢我们就需要给这个U2对象是不是添加一个属性对吧叫什么呢就叫Card对吧Card然后呢Card好然后呢我们下面再给他添加一个什么呢是不是Get和Set的方法好那么添加一个Get和Set
[02:14] 然后我们选错了应该选的是这个选择它然后到get和set的方法那么这个全参数的构造方法是不是也需要重新生成一下那么去找到全参数的构造的方法那么全选OK好这样的话就编写完成了那么这个是不是仅仅是在我们代码级别对吧我们去对象这个级别去设置他们的关系那么接下来我们来看一下在grabql这个文件中
[02:42] 如何去表现它的关系呢其实它也是跟我们这个类似啊那我们就需要在下面给他写一个type然后呢写一个这个card对象那么card对象中有哪些字段呢我们来看一下是不是有一个叫card number还有一个叫user id那我们来看一下这个card number那么它是什么类型呢叫string类型对吧然后呢下面一个叫user id那么user id它的类型呢是long这个类型哎ok
[03:09] 好 那么这个是不是我们就定义好一个card的一个对象那么如何去给他们两个去创去建立一个关系呢就一对一的关系那么你需要在这个位置来一个什么呢card冒号然后来一个card好 这样的话呢就实现他们的一个关系了实现关系了ok好 那么实现了这个关系之后那么可能就会有同学就会去猜了那么我们是不是在这个位置去做执行的时候呢他就可以把我们的card对象是不是查询到对吧
[03:38] 那么是不是怎么查询呢是不是有一个card然后呢这个里面显示什么呢哎是不是多没有多吧啊没有多没有多没有多就对了啊没有多一个那个括号card然后呢来一个这个括号然后呢这个里面我们要显示的就是card number然后呢还有个叫usid那么把它这两个呢显示出来查询我们走一下看一下效果嗯报错
[04:08] 这个是报什么错呢这个缺少构造函数对不对那么这样我们再给它设置一个none我们来看一下它会怎么样走这个是这个是前面也是由于我们刚刚删除了三个参数的构造函数导致这个错误那么我们先给它设置为none看效果好那么我们可以看到查询的结果是不是显然这个对象等于none对不对那么这个对象它并不是说
[04:43] 那么并不是说我们建立了这样的关系之后那么他就能够去查出这个对象那么也是需要我们给他去设置一个他这个对象的对吧那么在哪里设置呢需要在这个位置设置设置什么呢就是在这个位置设置那么你在查询这个优越的时候要返回这个card那么我们就给他返回一个这个card那么就去new一个那这样吧我们写到上面吧定一个card然后去new一个card
[05:11] 看了对象把它扭出来那么把这个对象我们导入进来导入进来好那么它也有两个参数的构造函数第一个就是叫做card number那么是一个字符串那我们就随便写一点123456789那么这是它的一个身份证号然后它的UID就是这个UID对吧好那么我们再看对象是不是就可以给它丢到这个里面来
[05:39] OK好那么这样的话我们再去做查询的时候那么是不是就能够查询到他的一个card中的一个数据OK来看一下这样的话是不是就做了一个查询那么其实我们所讲的这个意义呢就是说那么如果我们按照以前的RESTful去做开发的时候对于这个用户跟我们的card查询的话你是不是需要去再两次请求去做一个查询那我们现在是不是在一个请求中就可以做一个完成OK好
[06:07] 这样的话我们就实现了实现了这样的一个关系好嘞那么当然了如果你不想去查询这个card的话那么我们是把它拿掉是不是就是还是我们之前的一个优的查询对吧来看一下是不是没有任何问题好那么如果说你不想去再显示这个优的ID的话是不是只需要查询他的用户的一个身份证号那么我这样显示是不是就可以了是不是只会查询出他的一个身份证号
[06:37] 好 那么这样的话是不是就完成了我们这个对象的一个嵌套对吧在优越中有一个看的对象OK好 那么这样的话我们就实现了这样的一个效果那么修改它这个里面逻辑是不是去增加一个这个card一个对象OK 再段的特别要说明的一点是Grab QL它并不是实现了关联查询而是需要我们自己实现
[07:01] 就是说你这个对象从哪里去查需要你自己去调用你Service来做一个完成OK那么最后的一个测试结果呢就是这样的一个结果好嘞那么关于这个对象的一个嵌套呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 GraphQL，包括创建工程、定义 Schema、构建对象模型（User 和 Card）以及实现数据查询和返回。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示创建新工程的界面，Group Id 为 cn.itcast.GraphQL，Artifact Id 为 itcast-GraphQL-java，Version 为 1.0-SNAPSHOT。
画面 2: 展示构建 Schema 的代码片段，package 为 cn.itcast.GraphQL.demo，import 了 cn.itcast.GraphQL.vo.User。
画面 3: 展示对象嵌套的概念，说明要创建 Card 对象，与 User 对象建立一对一关系。
画面 4: 展示 Card 类的 Java 代码，包含私有字段 cardNumber 和 userId，以及对应的 getter 和 setter 方法。
画面 5: 展示 User 类的 Java 代码，包含私有字段 id、name、age 和 Card card，以及对应的构造函数和 getter/setter 方法。
画面 6: 展示 user.graphqls 文件的内容，定义了 UserQuery 类型和 User 类型，其中 User 类型包含 id、name 和 age 字段。
画面 7: 展示 GraphQLSchema 对象的生成代码，以及根据 Schema 生成 GraphQL 对象的代码。
画面 8: 展示 DataFetcher 的实现代码，用于根据 id 查询 User 对象。
画面 9: 展示运行结果，显示查询成功返回了 User 对象的信息。
画面 10: 展示修改后的 DataFetcher 代码，用于返回包含 Card 对象的 User 对象。
画面 11: 展示修改后的 DataFetcher 代码，用于返回包含 Card 对象的 User 对象。
画面 12: 展示运行结果，显示查询成功返回了包含 Card 对象的 User 对象的信息。
画面 13: 展示 User 类的 Java 代码，包含私有字段 id、name、age 和 Card card，以及对应的构造函数和 getter/setter 方法。
画面 14: 展示测试用例，包括查询 user(id:1) 的 id 和 name，以及查询 user(id:1) 的 id、name、card 和 userId。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
New Project
Group Id: cn.itcast.GraphQL
Artifact Id: itcast-GraphQL-java
Version: 1.0-SNAPSHOT

画面 2:
package cn.itcast.GraphQL.demo;
import cn.itcast.GraphQL.vo.User;

画面 3:
下面，我们创建一个 Card 对象，User 和 Card 对象为一对一的关系。

画面 4:
package cn.itcast.GraphQL.vo;
public class Card {
    private String cardNumber;
    private Long userId;
    public Card() {
    }
    public Card(String cardNumber, Long userId) {
        this.cardNumber = cardNumber;
        this.userId = userId;
    }
    public String getCardNumber() { return cardNumber; }
    public void setCardNumber(String cardNumber) { this.cardNumber = cardNumber; }
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
}

画面 5:
public User() {
    this.id = id;
    this.name = name;
    this.age = age;
}

画面 6:
schema {
    query: UserQuery
    type UserQuery {
        user(id:Long) : User
    }
    type User {
        id:Long!
        name:String
        age:Int
    }
}

画面 7:
// 生成Schema
GraphQLSchema graphQLSchema = new SchemaGenerator().makeExecutableSchema(typeRegistry, wiring);
// 根据Schema对象生成GraphQL对象
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
String query = "{user(id:1)}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.toSpecification());

画面 8:
builder.dataFetcher(fieldName: "user", environment -> {
    Long id = environment.getArgument(name: "id");
    return new User(id, name: "张二" + id, age: 20 + id.intValue(), card: null);
})

画面 9:
String query = "{user(id:100){id,name,age,card(cardNumber,userId)}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.toSpecification());

画面 10:
RuntimeWiring wiring = RuntimeWiring.newRuntimeWiring()
    .type(typeName: "UserQuery", builder -> {
        builder.dataFetcher("user", environment -> {
            Long id = environment.getArgument(name: "id");
            return new User(id, name: "张三" + id, age: 20 + id.intValue(), card: null);
        });
    })
    .build();

画面 11:
RuntimeWiring wiring = RuntimeWiring.newRuntimeWiring()
    .type(typeName: "UserQuery", builder -> {
        builder.dataFetcher("user", environment -> {
            Long id = environment.getArgument(name: "id");
            Card card = new Card(Number: "123456789", id);
            return new User(id, name: "张三" + id, age: 20 + id.intValue(), card);
        });
    })
    .build();

画面 12:
String query = "{user(id:100){id,name,age,card(cardNumber,userId)}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.toSpecification());

画面 13:
public class User {
    private Long id;
    private String name;
    private Integer age;
    private Card card;
    public User() {
    }
    public User(Long id, String name, Integer age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
}

画面 14:
return RuntimeWiring.newRuntimeWiring()
    .type(typeName: "UserQuery", builder -> {
        builder.dataFetcher("user", environment -> {
            Long id = environment.getArgument(name: "id");
            Card card = new Card(Number: "123456789", id);
            return new User(id, name: "张三" + id, age: 20 + id.intValue(), card);
        });
    })
    .build();

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: 标题为“7.2.3、对象嵌套”，内容说明要创建 Card 对象，与 User 对象建立一对一关系。
画面 6: 标题为“7.2.2、构建schema”，内容为 GraphQL Schema 的定义，包括 query 和 type。
画面 14: 标题为“测试”，内容为 GraphQL 查询语句的测试用例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

