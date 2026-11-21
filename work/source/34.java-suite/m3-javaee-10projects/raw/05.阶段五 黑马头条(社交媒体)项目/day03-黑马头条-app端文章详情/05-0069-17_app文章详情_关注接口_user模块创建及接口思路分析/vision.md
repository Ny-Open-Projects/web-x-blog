# 画面线理解：17_app文章详情_关注接口_user模块创建及接口思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\17_app文章详情_关注接口_user模块创建及接口思路分析【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:24, 01:51, 02:57, 03:23, 03:39, 04:14, 04:41, 05:19, 06:34, 07:11, 09:58, 10:36, 15:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:17:38

1) 这一组画面整体在讲什么（一句话）：
创建并配置一个名为 heima-leadnews-user 的 Maven 模块，用于实现用户关注功能，包括工程创建、依赖引入、配置文件复制和主启动类编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了文档目录结构，当前位于“3.3 关注接口”下的“3.3.1 工程创建”部分。
- 文档内容说明：在根项目下创建 Maven 模块，项目名称为 heima-leadnews-user，group id 为 com.heima。
- 文档内容说明：在 heima-leadnews-user/pom.xml 中增加父项目信息。
- 文档内容说明：复制 heima-leadnews-article 下的 dev、test、prod 三个环境配置文件到 heima-leadnews-user 下。
- 文档内容说明：复制 heima-leadnews-article/resources 下的 application.properties、log4j2.xml 文件到 heima-leadnews-user/src/main/resources 下。
- 文档内容说明：复制 heima-leadnews-article/pom.xml 中的依赖 build 内容到 heima-leadnews-user/pom.xml 中。

画面2：
- 展示了 IntelliJ IDEA 中的项目结构，根项目为 heima-leadnews，包含多个子模块，如 heima-leadnews-spis、heima-leadnews-article、heima-leadnews-behavior 等。

画面3：
- 展示了 heima-leadnews-user 模块下的 maven_dev.properties 文件内容。
- 文件内容：
  log_level=DEBUG
  log_pattern=%d(DEFAULT) %M%n %l %t %N %M%n%msg%n

画面4：
- 展示了 heima-leadnews-common 模块下的 application.properties 文件内容。
- 文件内容：
  # 全局字符集设置
  spring.http.encoding.force=true
  spring.http.encoding.charset=UTF-8
  server.tomcat.uri-encoding=UTF-8
  # 全局端口定义
  port.gateway=8081
  port.eureka=8761
  port.boot.admin=8766
  port.login=9001
  port.article=9003
  port.behavior=9004
  port.user=9005
  port.media=9006
  port.admin=9007
  port.crawler=9008
  port.websocket=9009
  port.images=9010
  port.quartz=9011
  port.migration=9012

画面5：
- 展示了 heima-leadnews-behavior 模块下的 pom.xml 文件内容，正在编辑 dependencies 部分。
- 文件内容：
  <dependencies>
    <!-- 引入依赖模块 -->
    <dependency>
      <groupId>com.heima</groupId>
      <artifactId>heima-leadnews-model</artifactId>
      <version>4.0.0</version>
    </dependency>
    <dependency>
      <groupId>com.heima</groupId>
      <artifactId>heima-leadnews-common</artifactId>
      <version>4.0.0</version>
    </dependency>
    <dependency>
      <groupId>com.heima</groupId>
      <artifactId>heima-leadnews-spis</artifactId>
      <version>4.0.0</version>
    </dependency>
  </dependencies>

画面6：
- 展示了文档目录结构，当前位于“3.3.2 初始项目”部分。
- 文档内容说明：创建 com.heima.user.config 包，并复制 heima-leadnews-article 项目下 com.heima.article.config 的 InitConfig、MysqlConfig、SecurityConfig 三个文件。
- 文档内容说明：创建启动类：com.heima.user.UserApplication。
- 文档内容说明：SpringBootApplication 注解类代码：
  @SpringBootApplication
  @EnableDiscoveryClient
  public class UserApplication {
    public static void main(String[] args) {
      SpringApplication.run(UserApplication.class, args);
    }
  }

画面7：
- 展示了 heima-leadnews-user 模块下的 pom.xml 文件内容，正在编辑 dependencies 部分。
- 文件内容：
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
      <groupId>com.fasterxml.jackson.dataformat</groupId>
      <artifactId>jackson-dataformat-xml</artifactId>
    </dependency>
    <dependency>
      <groupId>com.fasterxml.jackson.dataformat</groupId>
      <artifactId>jackson-dataformat-yaml</artifactId>
    </dependency>
  </dependencies>

画面8：
- 展示了 UserApplication.java 文件内容。
- 文件内容：
  package com.heima.user;
  import org.springframework.boot.SpringApplication;
  public class UserApplication {
    public static void main(String[] args) {
      SpringApplication.run(UserApplication.class, args);
    }
  }

画面9：
- 展示了在 IntelliJ IDEA 中右键点击项目目录，弹出“New”菜单，准备创建新文件或目录。

画面10：
- 展示了在 heima-leadnews-model 模块下，正在编辑 UserRelationDto.java 文件。
- 文件内容：
  import ...
  @Data
  public class UserRelationDto {
    // 文章作者ID
    @IdEncrypt
    Integer authorId;
    // 用户ID
    @IdEncrypt
    Integer userId;
    // 文章
    @IdEncrypt
    Integer articleId;
    // 操作方式
    // 0 关注
    // 1 取消
    Short operation;
  }

画面11：
- 展示了在 Word 文档中，正在编辑 FollowBehaviorDto 类。
- 文件内容：
  public class FollowBehaviorDto {
    // 设备ID
    @IdEncrypt
    Integer equipmentId;
    // 文章ID
    @IdEncrypt
    Integer articleId;
    @IdEncrypt
    Integer followId;
  }

画面12：
- 展示了在 Word 文档中，对 FollowBehaviorDto 类添加了注释。
- 文件内容：
  public class FollowBehaviorDto {
    // 设备ID
    @IdEncrypt
    Integer equipmentId;
    // 文章ID
    @IdEncrypt
    Integer articleId;
    @IdEncrypt
    Integer followId;
  }
  1. 根据 equipmentId 或当前登录的 userId 去查询行为实体
  2. 保存关注的行为

画面13：
- 展示了在 Word 文档中，对 UserRelationDto 类添加了注释。
- 文件内容：
  UserRelationDto ap_user_follow APP用户关注信息表
  // 文章作者ID
  @IdEncrypt
  Integer authorId;
  // 用户ID
  @IdEncrypt
  Integer userId;
  // 文章
  @IdEncrypt
  Integer articleId;
  // 操作方式
  // 0 关注
  // 1 取消
  Short operation;

画面14：
- 展示了在 Word 文档中，对 UserRelationDto 类添加了注释。
- 文件内容：
  UserRelationDto ap_user_follow APP用户关注信息表
  // 文章作者ID
  @IdEncrypt
  Integer authorId;
  // 用户ID
  @IdEncrypt
  Integer userId;
  // 文章
  @IdEncrypt
  Integer articleId;
  // 操作方式
  // 0 关注
  // 1 取消
  Short operation;
  1. 通过 dto 中的 userId 去获取关注人的 id，如果没有 userId 可以通过当前的作者 id 去查询，作者的 app 账号信息 followId
  2. 判断用户是否是关注或者取消
  3. 关注
  先去 ap_user_follow 表，检查是否已经关注，再进行保存
  ap_user_follow
  ap_user_fan
