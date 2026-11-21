# 画面线理解：13_通用说明_多环境配置说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\13_通用说明_多环境配置说明【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:31, 00:54, 01:05, 01:19, 01:24, 01:41, 01:46, 01:49, 01:54, 02:00, 02:40, 03:06, 03:12, 03:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:33:04

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Maven 项目中通过 profiles 配置实现多环境（开发、测试、生产）切换，重点是配置文件的管理与 pom.xml 中的 profile 定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程文档中关于“6.5.1 多环境切换”的说明，指出需在项目根目录下创建三个配置文件：maven_dev.properties、maven_prod.properties、maven_test.properties，并提到默认环境为 test，可通过 package -P 参数指定。
画面 2: 在 IntelliJ IDEA 中，项目结构视图显示了三个配置文件（maven_dev.properties、maven_prod.properties、maven_test.properties）位于 heima-leadnews-common 模块下。
画面 3: 编辑器中显示了 maven_prod.properties 文件内容，包含日志配置、数据库连接（URL、用户名、密码、驱动、包扫描范围）和 Eureka 服务地址。
画面 4: 编辑器中显示了 maven_test.properties 文件内容，数据库 URL 为 localhost:3306/heima_leadnews，其他配置与 prod 相同。
画面 5: 选中并高亮了 maven_test.properties 文件。
画面 6: 编辑器中显示了 pom.xml 文件的依赖部分，包含 mybatis、mybatis-spring、pagehelper-spring-boot-starter、jsoup 等依赖。
画面 7: 编辑器中显示了 pom.xml 文件的插件配置部分，包含 resources 和 testResources 插件配置，其中 filtering 设置为 true。
画面 8: 编辑器中显示了 pom.xml 文件的插件配置部分，已配置好 resources 和 testResources 插件。
画面 9: 编辑器中显示了 pom.xml 文件的 profiles 配置部分，已定义了 id 为 dev 的 profile。
画面 10: 编辑器中显示了 pom.xml 文件的 profiles 配置部分，已定义了 id 为 test 的 profile。
画面 11: 编辑器中显示了 pom.xml 文件的 profiles 配置部分，已定义了 id 为 prod 的 profile。
画面 12: 编辑器中显示了 maven_test.properties 文件内容，其中数据库 URL 为 localhost:3306/heima_leadnews，其他配置与 prod 相同。
画面 13: 编辑器中显示了 maven_test.properties 文件内容，其中数据库 URL 为 localhost:3306/heima_leadnews，其他配置与 prod 相同。
画面 14: 展示了课程文档中关于“6.5.1 多环境切换”的说明，指出需在项目根目录下创建三个配置文件：maven_dev.properties、maven_prod.properties、maven_test.properties，并提到默认环境为 test，可通过 package -P 参数指定。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```text
• InitJacksonConfig 提供自动化配置默认 ObjectMapper，让整个框架自动处理日期和id混淆
6.5 通用环境说明
6.5.1 多环境切换
在每一个微服务的工程中的根目录下创建三个文件，方便各个环境的切换
(1) maven_dev.properties
定义开发环境的配置
(2) maven_prod.properties
定义生产环境的配置
(3) maven_test.properties
定义测试环境的配置，开发阶段使用这个测试环境
默认加载的环境为test，在打包的过程中也可以指定参数打包 package -P test/prod/dev
具体配置，请查看工程下的maven插件的profiles配置
<profiles>
  <profile>
    <id>dev</id>
    <build>
      <filters>
        <filter>maven_dev.properties</filter>
      </filters>
    </build>
  </profile>
```

画面 2:
```text
heima-leadnews
├── heima-leadnews-api
├── heima-leadnews-common
├── heima-leadnews-model
├── heima-leadnews-utils
├── pom.xml
└── target
```

画面 3:
```text
# log日志配置
log.level=DEBUG
log.pattern="%d{DEFAULT} [%thread] %-5level %msg%n"

# 本地环境配置
mysql.core.jdbc.url=jdbc:mysql://192.168.220.145:3306/itheima-news?autoReconnect=true&useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Shanghai
mysql.core.jdbc.username=root
mysql.core.jdbc.password=root
mysql.core.jdbc.driver=com.mysql.jdbc.Driver
mysql.core.root.mapper=mappers
mysql.core.aliases.package=com.heima.model.poJos.**
mysql.core.tx.scan.package=execution(* com.heima.service.**.*)
# admin 账户名
admin.username=admin
admin.password=admin
hostname.eureka.server=localhost
eureka.client.serviceUrl.defaultZone=http://localhost:8761/eureka/
```

画面 4:
```text
# log日志配置
log.level=DEBUG
log.pattern="%d{DEFAULT} [%thread] %-5level %msg%n"

# 本地环境配置
mysql.core.jdbc.url=jdbc:mysql://localhost:3306/heima_leadnews?autoReconnect=true&useUnicode=true&characterEncoding=utf8&serverTimezone=Asia/Shanghai
mysql.core.jdbc.username=root
mysql.core.jdbc.password=root
mysql.core.jdbc.driver=com.mysql.jdbc.Driver
mysql.core.root.mapper=mappers
mysql.core.aliases.package=com.heima.model.poJos.**
mysql.core.tx.scan.package=execution(* com.heima.service.**.*)
# admin 账户名
admin.username=admin
admin.password=admin
hostname.eureka.server=localhost
eureka.client.serviceUrl.defaultZone=http://localhost:8761/eureka/
```

画面 6:
```xml
<dependency>
  <groupId>mysql</groupId>
  <artifactId>mysql-connector-java</artifactId>
  <version>${mysql.version}</version>
</dependency>
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis</artifactId>
  <version>${mybatis.version}</version>
</dependency>
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis-spring</artifactId>
  <version>${mybatis.spring.version}</version>
</dependency>
<dependency>
  <groupId>com.github.pagehelper</groupId>
  <artifactId>pagehelper-spring-boot-starter</artifactId>
  <version>${pagehelper.version}</version>
</dependency>
<dependency>
  <groupId>org.jsoup</groupId>
  <artifactId>jsoup</artifactId>
  <version>${jsoup.version}</version>
</dependency>
```

画面 7:
```xml
<plugin>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-maven-plugin</artifactId>
  <configuration>
    <source>${java.version}</source>
    <target>${java.version}</target>
  </configuration>
</plugin>
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-resources-plugin</artifactId>
  <version>3.2.0</version>
  <configuration>
    <encoding>UTF-8</encoding>
    <useDefaultDelimiters>true</useDefaultDelimiters>
    <resource>
      <directory>src/main/resources</directory>
      <includes>
        <include>**/*</include>
      </includes>
      <filtering>true</filtering>
    </resource>
    <testResource>
      <directory>src/test/resources</directory>
      <filtering>true</filtering>
    </testResource>
  </configuration>
</plugin>
```

画面 9:
```xml
<profiles>
  <profile>
    <id>dev</id>
    <build>
      <filters>
        <filter>maven_dev.properties</filter>
      </filters>
    </build>
  </profile>
```

画面 10:
```xml
<profiles>
  <profile>
    <id>test</id>
    <build>
      <filters>
        <filter>maven_test.properties</filter>
      </filters>
    </build>
  </profile>
```

画面 11:
```xml
<profiles>
  <profile>
    <id>prod</id>
    <build>
      <filters>
        <filter>maven_prod.properties</filter>
      </filters>
    </build>
  </profile>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“6.5 通用环境说明”，子标题为“6.5.1 多环境切换”，内容包括创建三个配置文件的说明和默认环境及打包参数的说明。
画面 14: PPT 标题为“6.5 通用环境说明”，子标题为“6.5.1 多环境切换”，内容包括创建三个配置文件的说明和默认环境及打包参数的说明。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
