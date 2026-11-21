# 19_mycat路由开发_环境搭建

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\19_mycat路由开发_环境搭建【海量资源尽在 666java.com】.mp4
- 时长 3分44秒（音频 224s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来进入当前的路由开发那什么叫路由开发呢其实这样啊咱们还要回归到当前的这个配置文件这配置文件里边啊说了有一个东西叫 ruler 是吧 ruler 里边呢是有一个当前的分片的算法那这分片算法呢是有一个是其实是有一个缺陷的什么缺陷的比如说啊咱们现在有一个 article 它是分了40是吧
[00:25] 40也就是说咱们需要去分到4把这个数据呢是分别存到40个分片中那40个分片的话比如说咱们的数据啊已经超过4亿那超过4亿如果说达到5亿该怎么办那这时候你这个idea再去存的时候可能就比较混乱了那这时候呢咱们为了能够方便扩展扩容性更强所以说呢咱们自己写一个算法来去实践当前的一个扩容好吧
[00:53] 那行啊那这个的首先呢咱们还是在当前的项目中的进行去创建一个模块啊模块呢就叫当前的Service by cat好拷贝一下啊model好下一步好点下一步好点finish那这个完了之后呢下面来看一下啊首先呢是咱们要去引入一个依赖啊当然了咱们引入依赖之前呢先把这些配容件拷过来啊
[01:29] 首先是当前的咱们经常会去设置的三个的环境三个环境配置文件这样的话你可以在其他的前的工程中的直接考过来就可以了好了根目录下边OK好了这是第一步然后第二个其实还说了个事当前的他们有一些配置文件需要放到config的目录下边哪些配置文件就是基于当前的马开的路由的配置其实就是哪几个就是第一个是他
[01:59] 这个是scammer ruler还有什么还有当前的server.xml我拷贝一下啊为了方便去改啊所以说先考到这啊然后考到哪呢考到当前在这创建一个目录啊叫config根目录哎错了啊创建一个目录啊目录目录好直接考过去就可以了啊这四个好考过去之后呢还少一些东西咱们再来看一下啊这里边呢还需要去加一个jar 包这个jar 包呢是
[02:32] 当前买开的中他的一个jar 包那这包呢在今天的资料中也已经提供了打开当前的资料嗯这有个资料啊资料里边呢是有一个麦开的相关呃里边有两个jar 包啊第一个是麦开的杠serva.1.6另外一个是Service杠当前的买开的啊这个咱们不要用啊用上面那个好吧拷贝一下好哪呢你考到当前的他然后在这再去创建一个目标libs
[03:03] 然后呢就把这个帐包啊卡到利博斯下边然后呢咱们本项目呢直接引用当前这个包就可以了啊用本地的帐包那这个怎么办呢就这会儿呢咱们Movie里边啊也有这么一段配置在POM中直接去打开啊不是它是吧呃MyCat它这个POM这个POM文件啊像这样啊这样的话其实就已经找到了你看到了吗看的话都已经识别了啊都是找的是当前本地的一个小包
[03:36] 好了啊那目前的话咱们环境就打完了下面呢咱们就去实现一个算法的一个操作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置和导入 Mycat 分片中间件，包括创建模块、配置文件、依赖管理及目录结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示了 Mycat 的配置文件 `sequence_db_conf.properties` 的内容，其中包含多个表的定义，如 `ADMIN_QRTZ_CALENDARS`、`ADMIN_QRTZ_JOB_DETAILS` 等，以及 `ap_article_config`、`ap_article_content` 等业务表的定义。
- 文件路径为 `D:\heima\mycat\conf\sequence_db_conf.properties`。
- 代码中包含注释“通用调度器ADMIN_QRTZ表结构”和“文章表”。

画面 2：
- 在 IntelliJ IDEA 中，右键点击项目 `heima-leadnews`，弹出菜单，选中“Copy with”。
- 编辑器中显示 `ArticleTestService` 类中的 `toString` 方法，用于拼接文件名。
- 代码片段：`public static String toString(Object... fields) { StringBuffer sb = new StringBuffer(); if (fields == null || fields.length == 0) { sb.append("0"); } for (int i = 0; i < fields.length; i++) { sb.append(SPLIT_CHAR).append(fields[i]); } }`

画面 3：
- 在 IntelliJ IDEA 中，显示了 `ArticleTestService` 类中的 `toString` 方法，与画面 2 相同。
- 代码片段：`public static String toString(Object... fields) { StringBuffer sb = new StringBuffer(); if (fields == null || fields.length == 0) { sb.append("0"); } for (int i = 0; i < fields.length; i++) { sb.append(SPLIT_CHAR).append(fields[i]); } }`

画面 4：
- 在 IntelliJ IDEA 中，显示了 `Service-mycat` 模块的 `pom.xml` 文件内容。
- 代码片段：
  ```xml
  <project xmlns="http://maven.apache.org/POM/4.0.0"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <parent>
          <artifactId>heima-leadnews</artifactId>
          <groupId>com.heima</groupId>
          <version>1.0-SNAPSHOT</version>
      </parent>
      <artifactId>Service-mycat</artifactId>
  </project>
  ```

画面 5：
- 显示了技术文档的页面，标题为“4.2 依赖导入”。
- 文档内容：开发Mycat的分片策略，需要依赖Mycat-server-1.6.7.1-release.jar文件。在项目中以本地文件方式进行导入，操作步骤如下：
  - 在 Service-mycat 下新建文件夹 libs。
  - 把网页定义资料下面的 Mycat-server-1.6.7.1-release.jar 到 libs 中。
  - 在 Service-mycat/pom.xml 中做以下依赖配置。
- 代码片段：
  ```xml
  <dependencies>
      <dependency>
          <groupId>com.mycat</groupId>
          <artifactId>mycat-server</artifactId>
          <version>1.0.0</version>
          <scope>system</scope>
          <systemPath>${basedir}/libs/Mycat-server-1.6.7.1-release.jar</systemPath>
      </dependency>
  </dependencies>
  ```

画面 6：
- 在 IntelliJ IDEA 中，显示了 `Service-mycat` 模块下的 `maven_dev.properties` 文件。
- 文件内容为空。

画面 7：
- 在 IntelliJ IDEA 中，右键点击项目 `heima-leadnews`，弹出菜单，选中“New”。
- 菜单中包含“Module”、“File”、“Directory”等选项。

画面 8：
- 在 IntelliJ IDEA 中，显示了 `Service-mycat` 模块下的 `config` 文件夹中的 `mycat-server` 配置文件。
- 代码片段：
  ```xml
  <user name="root" password="123456" />
  <user name="schemas" value="heima-news" />
  ```

画面 9：
- 显示了 Windows 文件资源管理器中的 `conf` 文件夹内容。
- 文件夹内包含多个配置文件，如 `server.xml`、`schema.xml`、`rule.xml`、`sequence_db_conf.properties` 等。
- 文件夹路径为 `D:\develop\mycat\conf`。

画面 10：
- 在 IntelliJ IDEA 中，显示了 `Service-mycat` 模块下的 `config` 文件夹。
- 项目结构中显示了 `maven_dev.properties`、`maven_prod.properties`、`maven_test.properties` 等文件。

画面 11：
- 在 IntelliJ IDEA 中，显示了 `Service-mycat` 模块下的 `libs` 文件夹。
- 项目结构中显示了 `maven_dev.properties`、`maven_prod.properties`、`maven_test.properties` 等文件。

画面 12：
- 在 IntelliJ IDEA 中，显示了 `heima-leadnews` 项目的 `pom.xml` 文件内容。
- 代码片段：
  ```xml
  <artifactId>heima-leadnews</artifactId>
  <packaging>pom</packaging>
  <version>1.0-SNAPSHOT</version>
  <modules>
      <module>heima-leadnews-common</module>
      <module>heima-leadnews-utils</module>
      <module>heima-leadnews-spis</module>
      <module>heima-leadnews-article</module>
      <module>heima-leadnews-model</module>
      <module>heima-leadnews-behavior</module>
      <module>heima-leadnews-common</module>
      <module>Service-mycat</module>
  </modules>
  <parent>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-parent</artifactId>
      <version>2.1.5.RELEASE</version>
  </parent>
  ```

画面 13：
- 在 IntelliJ IDEA 中，显示了 `Service-mycat` 模块下的 `pom.xml` 文件。
- 文件内容为空。

画面 14：
- 显示了技术文档的页面，标题为“4.2 依赖导入”和“4.3 算法设计”。
- 文档内容：在项目中分片字段命名规范为 `burst`，类型为 String，格式为 `datalog`，`datalog` 用于分组 ID 计算。
- 算法设计：分片 ID = (datalog / volume) * step + 分片 ID / mod。
- 代码片段：
  ```xml
  <dependencies>
      <dependency>
          <groupId>com.mycat</groupId>
          <artifactId>mycat-server</artifactId>
          <version>1.0.0</version>
          <scope>system</scope>
          <systemPath>${basedir}/libs/Mycat-server-1.6.7.1-release.jar</systemPath>
      </dependency>
  </dependencies>
  ```

