# 25_用户行为功能_项目导入及接口定义

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\25_用户行为功能_项目导入及接口定义【海量资源尽在 666java.com】.mp4
- 时长 5分21秒（音频 322s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好那咱们继续往下讲刚才咱们是把这个思路给说了一下下面呢咱们就来去做点当前的这个行为的这种保存操作那首先呢这是另外一个微服务所以说咱们要去创建一个这样的模块那这模块啊这已经创建完了所以说呢咱们只需要从资料中导入进来就可以那怎么导入呢非常简单啊打开这个后台代码出示代码里边有一个叫什么呢
[00:29] 叫黑马力的news有一个behaviour然后复制它复制到哪呢复制到你当前的这个这个代码存放的位置啊打开它本地的目录好直接放到这个下边就可以放进来之后呢大家看啊这已经有了那有之后呢那这个现在还不行是吧咱们需要呢导入进来导入进来啊导入进来呢其实也很容易咱们直接去找到当前的模块啊你看一下这个模块啊
[01:01] 是双击它的这个项目的泡沫文件就可以啊点OK那这时候呢你看这个项目就算是导进来了你看这个颜色它已经变了啊那这个项目其实呢基本的环境或者基础的环境已经搭完了但是里边代码都还没写啊咱们可以简单看一下啊那比如说这是个工程是吧里边有一个泡沫文件啊泡沫文件里边呢就是跟咱们之前搭建Article其实是差不多的好吧
[01:29] 然后下面还有这三个文件这三个文件的话咱们也直接去拿过来就可以好吧如果说你要自己创建的话也行你参考当前的第一个模块就是Article那个微服务呢去创建就可以好吧然后下面还有啊下面的话这里边还有一个东西就是在当前的resource下边呢就是创建两个文件一个是日志的是吧然后第二个第二个呢是当前的一个application.properties
[01:54] 里边呢就有两个内容大家需要去设置一个是当前的端口号第二个是应用的名称这个咱们之前讲过这个是不是在common中已经把这个端口号和名称定义好了呀你只需要去引用一下就可以好吧然后下面这个包名啊咱们也包几个啊咱们也创建完了这是com.hema.behind是吧然后下面是有一个引导类直接去启动这个项目就可以OK那咱们呢下面呢就来去测一下
[02:24] 看看这个项目有没有什么问题来执行走他正在build稍等一下这个build完了之后咱们移动一下看看能不能行好那目前的话这个项目就已经启动起来了他这个段口号是9004也没有报错没有问题行那导进来之后咱们下面就来去做开发首先咱们要去做一个接口的定义做接口定义之前咱们还要再去做一个DTO
[03:05] 当前DTO其实已经存在了就在当前的这个包下面大家可以去查看一下来打开当前哪儿来你给我说到哪儿到哪找是不是所有的DTO都在model下面OK打开model然后下面是有一个什么behaviour是吧然后是DTOS哪个呢就是当前的有一个show behavior DTO好
[03:34] 就是两个一个是设备ID另外一个是什么呢就是Article ID其实就是一个文章的列表信息好那当前咱们之前就在这个思路分析里边已经说了它需要从前台传递两个参数过来第一个是当前的设备第二个是第二个文章列表好那这时候咱们就需要干嘛呢就需要去定义一个接口那这接口在哪定义呢
[04:02] 很显然咱们是不是还要在当前的这个接口工程中去定义啊好往下走走好就在这去定义可以了啊然后是新建一个这里叫啥呢咱们来拷贝一下啊这是一个接口接口里边有什么方法呢这个方法的话呢应该就是保存当前的这种行为是吧OK啊咱们把这个方法名也可以拷一下行那里边参数刚才说了这个参数的话就是当前的什么
[04:38] so 看到吗to 是吧ok 没问题然后这个返回值的话咱们之前也讲过接口返回值咱们统一都会响应什么responseresponseresponseresult对吧那这个接口咱们就算是印完了这个接口主要就是保存保存保存用户点击文章的什么
[05:13] 行为那这接口啊我们就先定义到这下面呢咱们就来去实现一下这个接口

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中导入行为模块、定义 DTO、控制器接口并启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示课程大纲，当前讲解“导入 heima-leadnews-behavior 工程”，并展示 ShowBehaviorDto 类定义。
画面 2: 展示文件资源管理器，定位到 “heima_leadnews” 项目下的 “code” 文件夹。
画面 3: 在 IntelliJ IDEA 中，导入 “heima-leadnews-article” 项目，弹出 Maven 依赖更新对话框。
画面 4: 展示 “heima-leadnews-behavior” 项目的 pom.xml 文件，其中包含 Spring Boot Starter Web 和多个日志依赖的排除配置。
画面 5: 在 IDEA 中，选中 “heima-leadnews-behavior” 项目的 “maven_test.properties” 文件。
画面 6: 展示 “application.properties” 文件，内容为 server.port=3 和 spring.application.name=sn.behavior。
画面 7: 展示 “BehaviorJarApplication.java” 启动类，控制台显示 Spring Boot 启动日志。
画面 8: 控制台日志显示 Spring Boot 启动完成，包括数据源和 Web 服务初始化。
画面 9: 控制台日志显示 Tomcat 服务器成功启动在端口 9004。
画面 10: 展示 “ShowBehaviorDto.java” 文件，高亮显示 “@Data” 注解和 “equipmentId” 字段。
画面 11: 在项目结构中，导航至 “heima-leadnews-model” 模块下的 “dto” 包。
画面 12: 在 IDEA 中，右键点击 “dto” 包，弹出创建新文件的菜单。
画面 13: 展示课程大纲，当前讲解“定义控制器以及控制接口”，并展示 BehaviorControllerApi 接口定义。
画面 14: 展示 “BehaviorControllerApi.java” 文件，定义了 saveShowBehavior 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Data
public class ShowBehaviorDto {
    // 设备id
    @IdEncrypt
    Integer equipmentId;
    List<Article> articleIds;
}
```
画面 4:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <!-- 排除默认的logback日志，使用log4j2 -->
    <exclusions>
        <exclusion>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-logging</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-web</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-slf4j-impl</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-to-slf4j</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-jul</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-jcl</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-jsr250</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-jmx</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </exclusion>
        <exclusion>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</

