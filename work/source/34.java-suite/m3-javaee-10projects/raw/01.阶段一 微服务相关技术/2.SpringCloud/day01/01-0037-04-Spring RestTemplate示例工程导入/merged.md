# 04-Spring RestTemplate示例工程导入

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\04-Spring RestTemplate示例工程导入_【海量资源尽在 ubkz.com】.mp4
- 时长 6分19秒（音频 380s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] Spring Template 势力工程导入在这一小节中我们的主要目标是了解Spring REST Template 的应用在上一小节中我们已经了解到服务调用方式有RPC和HTTP两种方式而我们接下来即将要学习的Spring Cloud是基于HTTP的方式进行服务之间的一个调用那么如何在Spring项目中方便地进行HTTP的调用就变得尤为关键好 一般情况下
[00:31] 有如下三种HTTP客户端工具内包都可以方便的进行HTTP服务调用那这三种呢分别是第一个业界中经常用到的HTTP Client另外一个呢是OKHTTP第三个是JDKJDK原生
[01:00] URLConnection好这三种都可以去实现HTTP的服务调用那么Spring自己对这三种呢进行了封装提供了一个叫做RESTTemplate的工具类对上述的三种HTTP客户端工具类进行了封装好可以在
[01:38] Spring项目中使用REST template进行服务调用好这样用起来会比较方便快捷OK那接下来呢我们就打开我们的IDEA去创建工程目录然后呢引入我们今天的一个事例工程来了解REST template的一个应用打开IDEA创建一个工程空的我们起个名字接下来我们学习的是Spring Cloud
[02:17] 好,Spring CloudFinish新的窗口打开这边我们先暂时不创建任何的模块工程把我们今天资料中的那一个势力工程给引入到刚才的这个目录所以打开今天的资料里边有一个势力工程复制到我们刚才创建的这个Spring Cloud目录下来复制过来以后接下来你再打开IDEA把这个工程给引入好,New
[02:49] module from existing sources引入这个工程,点击ok好,导入的是maven的下一步默认,要不要递归去搜索里面有没有聚合子模块工程默认一般勾上比较好以后如果大家的工程里面有那些子工程的话勾上下一步,下一步finish,我们引进来引进来以后,这个呢其实是一个springboard工程它里面呢有对应springboard
[03:21] 的一些依赖用的是2.1.5的依赖没有问题然后引了一些启动器包括测试的我们这个工程呢主要是去了解rest template的使用所以我们打开这个测试类来了解包括我们的启动引导类我们打开来这边有个启动引导类好这都是常规的写法只是这个启动引导类里面呢我们编写了定义了一个bin就是rest template刚才说到rest template呢
[03:53] 对我们刚才说到的HTTP Client OKHTTP还有JDK默认的UIO Connection进行了封装它默认使用的是JDK原生的一种HTTP的工具内包实现好所以我们用了一个也就是在IOC容器中我们在测试的时候呢再把这个工具内给注入再去测试也就是这个情况到我们的测试内里边我们现在注入了这个REST Template然后调用它的一个方法GetForObjects
[04:22] 然后呢指定地址得到以后再把这个返回到JSON格式字符串进行一个返序列化这个rest template呢rest template可以对JSON格式字符串进行返序列化好这个返序列化的意思就是将JSON格式字符串转换成一个DRAW对象好然后如果是序列化那就是把DRAW对象转成一个JSON格式字符串
[04:57] 我们见到它是转成一个对象然后我们在这个输出我们测试一下因为这个地址要可以用才行你先保证一下你的地址是可以使用有数据返回的如果成功的话一样的可以在我们的控制台中输出这个user对象我们来执行测试看一下rest template是否可用如果可用后续我们就可以在springboard或者是spin cloud这些工程中去引用rest template
[05:26] 接着成功的标准就应该是输出这么一个用户信息在我们的控制台我们打开来看它应该是测试完了输出了没有问题这就是我们的一个Spring中用REST Template去执行服务的调用这就是具体的服务调用得到这个结果OK这是我们的REST Template势力工程引入我们了解了这个REST Template回到笔记中如果我们使用了
[06:00] rest template的话我们可以这么做就new一个rest template然后呢调用它的方法去发送请求到具体的服务器然后获得到服务OK这就是rest template事例工程导入完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 Spring Cloud 构建一个基于 RestTemplate 的 HTTP 服务调用示例工程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示课程大纲，包含“3. 服务调用方式说明”、“4. Spring RestTemplate示例工程导入”、“5. Spring Cloud概述”、“6. 创建微服务工程”等章节。
- “目标：能够说出服务调用方式种类”。
- “小结：RPC：基于socket，速度快，效率高；webservice、dubbo；HTTP：基于TCP，封装比较臃肿；对服务和调用方没有任何技术、语言的限制，自由灵活；RESTful，Spring Cloud”。

画面 2：
- 展示 IntelliJ IDEA 中一个 Spring Boot 项目的结构。
- 代码文件 `Application.java` 内容：
  ```java
  package com.ithema;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import tk.mybatis.spring.annotation.MapperScan;
  @SpringBootApplication
  @MapperScan("com.ithema.Mapper")
  public class Application {
      public static void main(String[] args) {
          SpringApplication.run(Application.class, args);
      }
  }
  ```

画面 3：
- 展示 IntelliJ IDEA 中新建项目对话框，项目名称为“Untitled”，项目位置为“D:\jheima\workspace\untitled”。

画面 4：
- 展示 IntelliJ IDEA 中“Project Structure”对话框，当前选中“Modules”选项。

画面 5：
- 展示 Windows 资源管理器，路径为“D:\jheima\class\Spring Cloud\day01\资料”，包含“http-demo”、“tb_user.sql”、“User.java”等文件。

画面 6：
- 展示 IntelliJ IDEA 主界面，菜单栏中“File”选项被选中，弹出下拉菜单。

画面 7：
- 展示 IntelliJ IDEA 中“Import Module”对话框，根目录为“D:\jheima\workspace\Spring Cloud\http-demo”，并勾选了多个自动导入选项。

画面 8：
- 展示 IntelliJ IDEA 中 `pom.xml` 文件内容，包含 Spring Boot 相关的依赖配置。
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <parent>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-parent</artifactId>
          <version>2.1.5.RELEASE</version>
          <relativePath/>
      </parent>
      <groupId>com.ithema</groupId>
      <artifactId>http-demo</artifactId>
      <version>0.0.1-SNAPSHOT</version>
      <properties>
          <java.version>1.8</java.version>
      </properties>
      <dependencies>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-web</artifactId>
          </dependency>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-test</artifactId>
          </dependency>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter</artifactId>
          </dependency>
          <dependency>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-web</artifactId>
          </dependency>
      </dependencies>
  </project>
  ```

画面 9：
- 展示 IntelliJ IDEA 中 `RestTemplateTest.java` 文件内容，包含测试类定义。
  ```java
  package com.ithema;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  @SpringBootApplication
  public class HttpDemoApplication {
      public static void main(String[] args) {
          SpringApplication.run(HttpDemoApplication.class, args);
      }
  }
  ```

画面 10：
- 展示浏览器中访问 `http://localhost/user/8` 的 JSON 数据响应，内容为用户信息。

画面 11：
- 展示浏览器中访问 `http://localhost/user/8` 的 JSON 数据响应，内容为用户信息。

画面 12：
- 展示 IntelliJ IDEA 中 `RestTemplateTest.java` 文件内容，包含测试方法。
  ```java
  @RunWith(SpringRunner.class)
  @SpringBootTest
  @AutoWired
  public class RestTemplateTest {
      @Autowired
      private RestTemplate restTemplate;
      @Test
      public void test() {
          String url = "http://localhost/user/8";
          User user = restTemplate.getForObject(url, User.class);
          System.out.println(user);
      }
  }
  ```

画面 13：
- 展示课程大纲，包含“4. Spring RestTemplate示例工程导入”章节。
- “目标：了解Spring RestTemplate的应用”。
- “分析：一般情况下有如下三种http客户端工具包都可以方便的进行http服务调用：httpClient、okHttp、JDK原生URL.Connection”。
- “spring提供了RestTemplate的工具类对上述的3种http客户端工具类进行了封装，可在spring项目中使用RestTemplate进行服务调用。”

画面 14：
- 展示课程大纲，包含“4. Spring RestTemplate示例工程导入”章节。
- “目标：了解Spring RestTemplate的应用”。
- “分析：一般情况下有如下三种http客户端工具包都可以方便的进行http服务调用：httpClient、okHttp、JDK原生URL.Connection”。
- “spring提供了RestTemplate的工具类对上述的3种http客户端工具类进行了封装，可在spring项目中使用RestTemplate进行服务调用。”
- “小结：”。
- “5. Spring Cloud概述”。
- “目标：Spring Cloud整合的组件和版本特征”。
- “小结：”。

