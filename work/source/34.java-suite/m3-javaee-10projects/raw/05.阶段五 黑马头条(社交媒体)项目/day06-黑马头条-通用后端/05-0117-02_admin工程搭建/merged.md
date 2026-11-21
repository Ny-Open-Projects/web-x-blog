# 02_admin工程搭建

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\02_admin工程搭建【海量资源尽在 666java.com】.mp4
- 时长 5分5秒（音频 305s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好今天咱们第一个模块还是要去实现admin端的一个登录的功能首先咱们还是要干嘛呢还是需要去创建一个新的微服务这微服务就叫admin然后像你要去有配置文件是吧还有POM依赖的还有咱们要拷贝当前的两个配置当然最后还要去创建引导类引入一些其他的这种配置这样咱们就手动来去创建一下把它可以拷贝一下
[00:30] 当前的副功能下面去创建一个模块稍等好考虑了之后呢把这个替换一下啊好创建完之后啊下面咱们就参考着其他的微服务去创建就可以了啊稍等一下啊我看这当前过来了没admin好像是没有刷新一下啊好过来之后呢你可以忽略掉啊可以把它取消忽略取消忽略再刷新一下
[00:59] OK那这样就没事了你看这个是正常的颜色行这个时候咱们就可以去从其他微服务去拷贝了把这三个拷过来拷到当前的目录下边然后要去拷贝它的一个这种依赖信息要拷过来开POM好拷过来之后咱们还有一些配置文件也需要去拿过来比如说这里边的一些这种什么这两个配置文件一个是他一个是他
[01:32] 我考过来之后咱们还要改东西来看一看这俩这个是就叫做admin了叫admin这东西再去说一遍一些这东西都是在哪你还知道吗都是在当前的一个common模块下边有一个什么东西这是不是有个配置文件对配置文件里边是不是已经定义好了或者规定好了当前的这种什么模块的当过号
[02:00] 或者模模块的当前的名称啊是吧所以说你这个内容其实是在这个配置中间中去读的啊去读的啊这个大家一定要知道这个咱们已经创建过很多次了啊大家应该很熟了这一块行那这个创建完之后啊咱们看看还有什么东西啊首先有了有了这个咱们也考过来了是吧刚才也改掉了啊包啊咱们要去创建啊要去创建并且创建一个引导类那咱们就来手中去创建一下啊在这个这个在这在这啊创建一个包
[02:30] 这个包叫什么包啊叫com.黑马admin然后呢咱们下面就在这去创建一个引导类引导类的名字叫什么admin.application是吧然后在上面加个注解sprintbook.application然后下面是有一个慢方法psbm然后是sprintapplication.run先把当前这个类加进去
[03:06] 那这样的话咱们引导类就算设置完了那设置完之后这里边其实还有一些配置前的项目需要有一些其他的配置这个配置的话咱们在这去创建它的包首先你在这去创建一个什么咱们的配置都是放到config然后再往下放下还有什么Service后期会用到的Service还有后期会用到的Controller是吧controllerv1这个包名大家应当熟悉
[03:36] 那这创建完之后咱们在这就可以去参考其他的模块去引过来引过来你可以去打开当前的行为的微服务这里边有个init有一个mycircle走过来走过来之后你看这里边首先是一个mycircle是当前的mybidisk mycircle的一块内容它都是去在这个包下边去扫描的还有一个initinit里边只有一个jaxx
[04:07] 这里边还少一个就是super rate就咱们要登录嘛super rate的东西咱们也要有所以说你需要再拷贝一个这个在哪有知道吗目前的话media跟当前的user都有你可以随便打开一个在config里边有一个super rateconfig来拷贝一下好拷贝完之后这份内容你需要去改一改不是wm这是什么这是admin你也可以去查看当前的com
[04:43] 现在comment到底是哪一个需要去做过滤那你看这个啊咱们之前也讲过内容呢它是分了三个三块内容啊第一个呢是admin第二个呢是app啊这是移动端的是吧还有wm啊这是咱们的一个那种自媒体端的啊现在是用到的是admin好吧行那这个呢咱们工程目前的话呢咱们就搭完了啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中创建并配置 admin 端项目，实现登录功能，包括搭建模块、配置文件、主程序和安全配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT，标题为“admin端功能开发&通用后端封装”，目标包括完成 admin 登录、通用后端封装和熟悉开发流程。
画面 2: 在 IntelliJ IDEA 中，弹出“New Module”对话框，准备创建新模块，父模块为 `com.heima.heima-leadnews:1.0-SNAPSHOT`。
画面 3: 编辑 `pom.xml` 文件，显示父模块配置，`artifactId` 为 `heima-leadnews-admin`，`version` 为 `1.0-SNAPSHOT`。
画面 4: 编辑 `pom.xml` 文件，显示 `dependencies` 部分，引入 `heima-leadnews-model`、`heima-leadnews-common` 和 `heima-leadnews-api` 依赖。
画面 5: 编辑 `application.properties` 文件，配置 `server.port=8080` 和 `spring.application.name=sn.admin`。
画面 6: 在 `heima-leadnews-common` 模块的 `application.properties` 文件中，同样配置 `server.port=8080` 和 `spring.application.name=sn.admin`。
画面 7: 在项目结构中选中 `heima-leadnews-common` 模块，准备进行后续操作。
画面 8: 在 `heima-leadnews-admin` 模块中，弹出“Create New Class”对话框，准备创建 `AdminApplication` 类。
画面 9: 编辑 `AdminApplication.java` 文件，显示 Spring Boot 主类代码，包含 `@SpringBootApplication` 注解和 `main` 方法。
画面 10: 在 `AdminApplication.java` 文件中，右键选择“Run”选项，准备运行程序。
画面 11: 在项目结构中，选中 `heima-leadnews-behavior` 模块，准备进行后续操作。
画面 12: 编辑 `IntConfig.java` 文件，显示 `@Configuration` 注解和 `@ComponentScan` 注解，扫描包 `com.heima.common.common.init`。
画面 13: 在项目结构中，选中 `heima-leadnews-media` 模块，准备进行后续操作。
画面 14: 编辑 `SecurityConfig.java` 文件，显示 `@Configuration` 注解和 `@ComponentScan` 注解，扫描包 `com.heima.common.web.admin.security`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>heima-leadnews</artifactId>
        <groupId>com.heima</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>heima-leadnews-admin</artifactId>
</project>
```

画面 4:
```xml
<dependencies>
    <!-- 引入依赖 -->
    <dependency>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews-model</artifactId>
    </dependency>
    <dependency>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews-common</artifactId>
    </dependency>
    <dependency>
        <groupId>com.heima</groupId>
        <artifactId>heima-leadnews-api</artifactId>
    </dependency>
</dependencies>
```

画面 5:
```properties
server.port=8080
spring.application.name=sn.admin
```

画面 6:
```properties
server.port=8080
spring.application.name=sn.admin
```

画面 9:
```java
package com.heima.admin;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AdminApplication {
    public static void main(String[] args) {
        SpringApplication.run(AdminApplication.class, args);
    }
}
```

画面 12:
```java
package com.heima.admin.config;

import org.springframework.context.annotation.ComponentScan;

@Configuration
@ComponentScan("com.heima.common.common.init")
public class IntConfig {

}
```

画面 14:
```java
package com.heima.admin.config;

import org.springframework.context.annotation.ComponentScan;

@Configuration
@ComponentScan("com.heima.common.web.admin.security")
public class SecurityConfig {

}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“admin端功能开发&通用后端封装”，下方列出“今日目标”，包括三个目标：
- 目标一：能够完成admin端的登录功能
- 目标二：能够清晰通用后端的好处
- 目标三：能够完成通用后端的代码开发
- 目标四：熟悉前端的开发流程

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

