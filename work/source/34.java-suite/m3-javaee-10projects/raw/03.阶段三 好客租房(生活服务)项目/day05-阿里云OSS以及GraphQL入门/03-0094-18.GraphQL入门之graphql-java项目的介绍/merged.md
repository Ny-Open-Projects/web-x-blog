# 18.GraphQL入门之graphql-java项目的介绍

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\18.GraphQL入门之graphql-java项目的介绍【海量资源尽在 ubkz.com】.mp4
- 时长 3分8秒（音频 188s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来学习GraphQL它的Java的一个实现啊那么在官网中呢其实我们可以看到它呢针对于非常多的一些语言呢都有一些这个实现但是呢要注意的是这个Java的这个实现呢它并不是官方所实现的这样的一个具体实现啊而是由第三方的一个团队去做的这样的一个实现
[00:26] 那么我们来看一下那么这个第三方这个团队实现叫什么名字呢叫GraphQL-java这样的一个项目其实官方的也是所推荐的是这样的一个实现那么当然了除了这个实现之外它还会有一些其他的一些实现那么我们在这儿就不做一个讲解了那么要感兴趣的同学也可以去查一下它有哪些的实现
[00:50] 那么既然官方所推荐这种实现那我们就基于这种实现来去实现一下或者我们来去玩一下这个GraphQL到底它怎么样去写对吧因为前面我们只是讲了它的一些规范它的一些定义但是没有具体的实现好那么我们就可以通过使用GraphQL-Java这个项目来实现我们的一个服务端的一个程序了对吧那么我们首先来看一下这个官网
[01:17] 那么在官网呢就是GraphQL这个-java这就是他的一个官网啊这个注意并不是GraphQL他的官网啊是这个第三方实现这样的一个官网那么在这个里面呢其实呢他有一些内容呢需要我们去关注的啊那么首先是他的这个文档啊这个文档那么这个文档呢写的还是非常的好的这样的一个文档那么比如第一个快速的一个开始啊包括他怎么去用啊
[01:46] 他写了很多代码这是一些非常好的一些写的代码或者非常好的一些事例那么帮助我们去做一个入门的学习还有像我们Skymer的一些定义学习有非常多的一些内容这是非常好写的非常好的文档OK好那么就是这样的一些内容那么
[02:09] 他的这个代码的同样的也是托管于什么呢托管于GitHub大家可以去打开这个地址在官网去找到这个地址去打开来看一下那么这个就是他官网的一个这样的地址那么大家也可以把这个编代码你才高的到你的本地去做一些学习那么其实我们可以参考这个官方的一个文档就可以做出这样的学习了哎呀OK好那么这个他的官网的地址下面这个就是他的GitHub的一个主页的一个地址OK好那么
[02:38] 我们来看一下它的GitHub上面的一个人气其实可以看到它的star还是比较多的2720还是比较多的人气还是比较高的这样的一个项目好那么我们对于GraphQL-Java这个项目的一个简单的一个说明我们就说明到这那么下面我们就要去正式的来使用
[03:01] 他来搭建我们的一个服务了OK好那么关于这个项目的一个简单的一个介绍我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 GraphQL 的类型系统概念，并介绍如何使用 graphQL-java 库在 Java 项目中实现 GraphQL 服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 标题：类型系统 (Type System)
- 内容：介绍 GraphQL 查询本质上是选择对象上的字段，并展示一个示例查询和响应。
- 代码示例：
  ```GraphQL
  {
    hero
      name
      appearsIn
  }
  ```
  ```json
  {
    "data": {
      "hero": {
        "name": "R2-D2",
        "appearsIn": [
          "NEWHOPE",
          "EMPIRE",
          "JEDI"
        ]
      }
    }
  }
  ```

画面 2：
- 标题：Java
- 内容：介绍 graphQL-java 库，并展示一个用于执行 hello world GraphQL 查询的 Java 代码示例。
- 代码示例：
  ```java
  import GraphQL.ExecutionResult;
  import GraphQL.GraphQL;
  import GraphQL.schema.GraphQLSchema;
  import GraphQL.schema.StaticDataFetcher;
  import GraphQL.schema.idl.RuntimeWiring;
  import GraphQL.schema.idl.SchemaGenerator;
  import GraphQL.schema.idl.SchemaParser;
  import GraphQL.schema.idl.TypeDefinitionRegistry;

  public class HelloWorld {
      public static void main(String[] args) {
          String schema = "type Query { hello: String }";
          SchemaParser schemaParser = new SchemaParser();
          TypeDefinitionRegistry typeDefinitionRegistry = schemaParser.parse(schema);
          RuntimeWiring runtimeWiring = newRuntimeWiring()
                  .type("Query", builder -> builder.dataFetcher("hello", new StaticDataFetcher("Hello World")))
                  .build();
          SchemaGenerator schemaGenerator = new SchemaGenerator();
          GraphQLSchema graphQLSchema = schemaGenerator.makeExecutableSchema(typeDefinitionRegistry, runtimeWiring);
      }
  }
  ```

画面 3：
- 标题：7、GraphQL 的 Java 实现
- 内容：介绍 GraphQL 的 Java 实现，推荐使用官方推荐的 graphQL-java，并提供其官网和 GitHub 地址。
- 文本内容：
  百网：https://www.GraphQL-java.com/
  github：https://github.com/GraphQL-java/GraphQL-java

画面 4：
- 标题：GraphQL Java Home
- 内容：展示 GraphQL Java 官网首页，显示最新版本和博客文章。

画面 5：
- 标题：Documentation
- 内容：展示 GraphQL Java 文档的导航页面，包含多个文档模块，如 Getting started、Schema、Data fetching 等。

画面 6：
- 标题：How to use the latest release with Gradle / Maven
- 内容：展示如何在 Gradle 和 Maven 项目中添加 graphQL-java 依赖。
- 代码示例：
  ```gradle
  repositories {
      mavenCentral()
  }
  dependencies {
      compile 'com.GraphQL-java:GraphQL-java:11.8'
  }
  ```
  ```xml
  <dependency>
      <groupId>com.GraphQL-java</groupId>
      <artifactId>GraphQL-java</artifactId>
      <version>11.8</version>
  </dependency>
  ```

画面 7：
- 标题：Documentation
- 内容：再次展示 GraphQL Java 文档导航页面。

画面 8：
- 标题：Schema
- 内容：展示 GraphQL 的 Schema 定义示例，包括枚举、接口和类型。
- 代码示例：
  ```GraphQL
  enum Episode {
      NEWHOPE
      EMPIRE
      JEDI
  }

  interface Character {
      id: ID!
      name: String!
      friends: [Character]
      appearsIn: [Episode]!
  }

  type Human implements Character {
      id: ID!
      name: String!
      friends: [Character]
      appearsIn: [Episode]!
      homePlanet: String
  }

  type Droid implements Character {
      id: ID!
      name: String!
      friends: [Character]
      appearsIn: [Episode]!
      primaryFunction: String
  }
  ```

画面 9：
- 内容：空白页面，无有效信息。

画面 10：
- 标题：GraphQL Java implementation
- 内容：展示 graphQL-java 的 GitHub 仓库主页，显示项目信息和文件结构。

画面 11：
- 标题：License
- 内容：展示 graphQL-java 的许可证信息，说明其基于 MIT License。

画面 12：
- 标题：7、GraphQL 的 Java 实现
- 内容：再次展示 PDF 文档中的相关内容，与画面 3 类似。

画面 13：
- 标题：7.1.1、创建工程
- 内容：展示在 IDE 中创建新项目的界面，设置工程名和 GroupId、ArtifactId。

画面 14：
- 标题：github：https://github.com/GraphQL-java/GraphQL-java
- 内容：展示 GitHub 仓库地址，与画面 10 类似。

