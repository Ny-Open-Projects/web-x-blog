# 画面线理解：04-Spring RestTemplate示例工程导入

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\04-Spring RestTemplate示例工程导入_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:45, 02:06, 02:12, 02:22, 02:38, 02:47, 02:58, 03:20, 03:42, 05:09, 05:28, 05:55, 06:01, 06:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:08:35

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
  @MapperScan("com.ithema.mapper")
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
- 展示 Windows 资源管理器，路径为“D:\jheima\class\springcloud\day01\资料”，包含“http-demo”、“tb_user.sql”、“User.java”等文件。

画面 6：
- 展示 IntelliJ IDEA 主界面，菜单栏中“File”选项被选中，弹出下拉菜单。

画面 7：
- 展示 IntelliJ IDEA 中“Import Module”对话框，根目录为“D:\jheima\workspace\springcloud\http-demo”，并勾选了多个自动导入选项。

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
