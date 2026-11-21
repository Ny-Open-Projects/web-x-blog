# 12-文件服务课程-文件服务开发（环境搭建_mave — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

继续来看我们Maven工程环境搭建

刚才呢咱们是把我们这个文件服务啊

所涉及到的这些配置文件呢

统一都导入到我们这个PDFile Server

这个工程里面来了

好那么接下来呢

我们需要来导入的是一个什么呢

是一个启动类啊

那么咱们可以来创建一下

这个启动类呢就叫做File Server Application

把这些呢我们可以先关上

找到我们的PDFile Server对吧

那么先把我们这个包结构呢

先来创建一下

先来创建一个包

好看我们的IT黑码

然后呢品达

好因为我们是在品达通用权限系统

这个基础之上来进行开发的

所以我们这个包呢就这样来命名了

当然这个不是固定的

那么大家呢也可以根据自己的情况

去进行命名都是可以的

好

然后呢我们在这个包下边呢

来创建咱们这个类啊

叫做File Server Application

OK

好

那么这个配置这个启动类上面呢

要加很多注解对吧

对于启动类这种呢

相对来说呢非常固定的

那么我们直接导进来就可以了

咱们可以来看一下

整个呢这个类我就不再去手写了

好

保存一下

这是我们的启动类

然后呢上面加入了很多注解对吧

Spring Boot Application

这个呢是我们比较常见的

作为Spring Boot工程对吧

那么启动类上面肯定要加它

然后呢还有这个呢

Enable Discovery Client

这是不是加入我们这个什么呢

我们这个注解呢

它是我们这个Spring Cloud里边的

可以到我们的这个服务注册中心对吧

去查找服务啊

这是Discovery

就是发现客户端对吧

字面翻译过来

然后呢Enable Past Tricks

也就是说这个呢

是启用我们的

开启我们的熔断对吧

然后呢这个是Enable Faint Clients

因为它要进行faint调用对吧

所以说呢可以到这个包下边

去查找我们这些接口

好

最终呢它其实是基于代理

然后呢来进行这个faint远程调用

好

然后呢这个是开启我们这个事务管理

然后呢这个是日志对吧

然后呢这个注解呢

是我们自定义的一个注解

大家可能以前没有见过

叫Enable Form Validator

我们可以按着Ctrl点进来

大家来看啊

它是在我们PD Tools Validator

这个模块

这就是我们脚手架里边啊

给我们提供的这么一个注解

而这个注解呢用来开启什么呢

开启表单校验

验证功能

好

所以直接加这个注解就表示开启了

OK

那么这个地方呢

因为我们重点呢

还是在讲我们的文件服务

所以大家如果有兴趣呢

可以去看一下

自行去研究一下我们这个什么呢

通用权益系统

这里面的这些模块

那么这些模块呢

还是非常多的

这个呢

对应的就是在我们这个PD Tools Validator

这个模块里面所定义的这个注解

刚才我们也已经打开看了

对吧

就是这个Enable Form Validator

就是它

然后接下来呢

就是常规的我们是不是要启动啊

是用Spring Application Run来启动

启动完之后呢

我们在控制台呢

是不是输出了一些信息

其实就是动态的从我们这个变量里边

对吧

从Environment的这个变量里边呢

来获取一些这个环境变量

比如说我们这个应用的名称

对吧

然后呢

动态获得我们当前所在网络的这个IP地址

然后还有我们这个服务的端口号

等等这些

最终呢

为我们拼到这个站位服务里面去

好

这是我们这个启动类呢

就已经搞定了

后边呢

我们就直接运行这个Main方法

来启动我们Spring Boot的工程

好

这一步呢

我们就已经搞定了

再往下呢

就是有一些配置类

这些配置类呢

其实本质上呢

就是一些配置文件

对吧

只不过呢

它是以Java代码的方式表现出来

它起到的作用就是配置的作用

好

那么对于这些配置类呢

我们也就不再继续写了

直接导进来

拿过来用就可以了

那么配置类呢

我们提前整理好了

在我们资料文件服务配置类

这个目录下边

资料

然后呢

文件服务配置类

在这个里边

那么这有个Config对吧

然后呢

我们直接把它拿过来就可以

咱们把这整个这个包呢

来复制一下

注意啊

不要直接放在我们

回来

找到我们刚才PDFile Server

对吧

不要直接放在我们这个

品达

这个

这个目录下边

因为它中间的还差了一层目录呢

我们需要再来创建一个叫做File的目录

咱们这不是文件服务吗

所以还有一个File目录

然后呢

直接粘贴在这个目录下边

好

这个目录层次啊

大家看

你看在我们File目录下边有个Config

这表示配置对吧

这里面呢

都是一些配置类

DataSource里边呢

是关于数据源的一些配置

对吧

数据源的

这是一些配置

然后呢

这个是MyBattis的一些配置

它这里边呢

使用到了一些

拦截器对吧

而这个配置类呢

继承了另外一个配置类

叫做BaseMyBattisConfiguration

对吧

而这个类呢

在哪呢

它其实是在我们这个

PT Tools Database

也就是在我们这个

脚手架里边

这个Database啊

在这个模块里边

定义的这个基础的配置类

好

你看这里面呢

其实有一些这个拦截器

对吧

还有一些这个注入器

它的配置

还有什么呢

我们的ID生成器

这些配置呢

直接

拷过来就可以了

然后呢

这个Database是关于我们

这个数据库的一些配置

对吧

数据库的一些配置

包括我们这个扫描

对吧

去扫描我们这些实体

然后呢

这里边呢

就是关于我们

Circle Session Template

这是不是我们

要使用MyBattis

来操作数据库

对吧

可能需要用到

这么一个模板对象

然后呢

还有我们的数据源对象

在这个地方呢

我们可以简单来看一下

有两个Data Source

对吧

两个Data Source

数据源

那么具体我们用的是哪一个呢

这个地方呢

实际上我们用的

需要看我们的配置文件

如果我们是在这个

开发环境下边

开发环境下边呢

它用的就是我们

这个下边这个

P6 SPI

对吧

P6 Data Source

其实呢

就是从我们

刚才看到的这个

PDFile DEV

这里面加载的

这个配置

最终呢

封成成这么一个数据源对象

封成成这么一个数据源对象

叫做P6

Data Source

那么刚才我说了

为什么在我们这个

开发环境下边

也就是DEV

对吧

开发环境下边

才会用到它呢

才会创建它呢

就是因为我们在这个地方呢

加了这么一个配置

大家来看

Arraying YouTube.contains

对吧

然后呢

DEV Files

也就是说我们当前呢

如果使用的是DEV环境

那么它就会加载它

如果不是的话呢

直接返回这个Data Source

也就是说

那这个Data Source是谁呢

其实就是我们

上面这个Data Source

你看

它是不是根据我们这个

对象名称来查找

对吧

BIN的名称来查找

然后呢

前面这是一个常亮

对吧

是一个前缀

然后呢

加上这个德鲁伊Data Source

而它的名字

是不是恰好就叫这个

所以说呢

其实就是把这个对象呢

把我们这个Data Source对象

注给了

当前这个Data Source

注到这边来

然后呢

我们来判断一下

如果是开发环境

对吧

然后呢

我就把它重新包装一下

包装成这个P6Data Source

否则的话呢

那么我直接

返回这个Data Source

所以我们用的

相当于还是原版的

这个

这个德鲁伊的

这个Data Source

所以说这个地方呢

稍微有一点点绕

大家来看一下

也就是说

它会根据我们当前

这个环境

来动态地去选择

一个Data Source

数据源对象

然后再往下呢

是我们这个

Circle Session Factory

这个就不用多说了

这是我们MyBetis

它的这个工厂对象

对吧

Circle Session工厂对象

然后呢

这是我们这个

事务管理器对象

对吧

然后呢

这个是事务的

这个拦截器等等

好

然后呢

这个是我们的

这个事务的Advisor

也就是相关

切面相关的

好

切面通知等等这些

好

那么这是关于

跟我们数据库

打交道的这些配置

然后呢

还有一个是

Exception Configuration

这是一个

异常处理对吧

异常处理的一个配置

当然这个类呢

非常简单

直接继承了一个

叫做Default Global

Exception Handler

而这一个附类在哪呢

它是在我们这个

PT Tools Common

也就是我们

脚鼠架里边

提供的这个

Common模块里边

在这里边呢

我们提供了很多

这个注解对吧

Exception Handler

那么统一的来

拦截我们相关的

这些异常

然后呢

进行异常处理

把我们常用的

这些异常呢

基本上全都处理掉了

全都处理掉了

所以说呢

你看我们使用

脚鼠架的话

就是有这样的好处

在脚鼠架里边呢

我们已经把

这些异常呢

其实都已经处理好了

那么我们在这个地方呢

直接继承它

就可以拿过来用了

好

这是通过我们这种

Control Advice

这个注解

然后呢

来统一的去拦截

我们这些Control

加了这个注解的

这些Control

一个是Rest Control注解的

还有一个是Control注解的

这些控制器类

对吧

然后来拦截

它们所抛出的异常

统一呢

在这儿进行处理

好

所以这是一个

全局的异常处理

还有一个是Web处理

对吧

然后呢

它其实也是

直接继承了一个

Base Config

Base Config

是一个基础的配置

而这个基础的配置

在哪呢

也是在我们PD2

Komen通用模块里边

好

然后这个地方呢

其实用到了一个

这么一个对象转换的

对吧

Jason转换的这么一个对象

叫做Object Mapper

好

然后呢

这个也是啊

跟这个Jason转换相关的

然后呢

这个是日期转换相关的

一些转换器

对吧

Converter

全都是Converter

不同类型的

好

那么

这是我们导入了什么呢

我们这个PD File Server里边

所使用到的一些配置类

咱们直接拿过来用

就可以了

这些东西呢

大家可以看到

我们是直接拿过来

因为都是一些基础的配置

所以说我们在这个地方呢

并没有作为重点去开发它

那么直接拷过来

然后呢

根据我们需要的情况

对吧

简单修改一下就可以了

好

所以这些配置类

直接导过来

就拿过来用就可以了

然后呢

还有就是一些工具类

工具类呢

这个地方有两个

一个是这个File Data Type

Util

还有个ZIP

Util

这是跟

这个工具类

我们这个文件上传下载

相关的这些工具类

那么我们也直接把它拿过来

同样是在我们资料目录下

有一个叫文件服务工具类

对吧

然后呢

我们直接资料文件服务工具类

然后呢

把这个Utils目录呢

拷抖

直接来复制一下

然后直接放到我们这个File目录下边

直接粘贴在这层目录下边

好

大家可以看到啊

有这么一个叫做File Data Type Util

对吧

然后呢

这个是根据类型的工具类型

类型来识别的这么一个工具类

比如说我们上传的文件呢

有多种类型

对吧

可能有这种图片的

然后呢

视频的

然后呢

还有这种类型DIR的

对吧

然后呢

还有这个音频的

还有普通的文本的

那么我们最终呢

都会给它识别出来

根据它的这个后缀

对吧

根据这些类型

然后呢

最终来指定啊

它这个具体这个文件类型到底是什么样子的

是这么一个类

然后呢

还有个ZIP Util

这个呢

是作为我们这个文件的这个什么呢

文件的这个

大家来看一下下载的时候会用到啊

然后呢

你给我传过来一个输出流

对吧

一个文件名

然后一个输入流

然后在这个地方的进行

从这个输入流来进行读取

通过输出流来来输出

最终呢

把这个文件把它下载到我们本地

文件名呢

就是我们传过来这个文件名啊

所以在这呢

我们是封装了一下

OK

这是关于我们这个文件服务啊

用到的工具类

咱们就直接导过来了

到时候呢

我们用到哪个类呢

咱们再具体来看一下

它这个代码实现就可以了

好

然后还有第十步呢

是导入我们这个配置属性类

因为呢

我们在这个配置文件里面

是不是配置了很多这种属性啊

对吧

尤其是在我们PDFile Server里边

配置的属性比较多

你看这里面属性很多

然后呢

这些配置呢

我们最终呢

需要把它读取过来

封装成我们一个Java对象

对吧

所以说呢

这就是需要使用到我们的配置属性类

来进行输出流来进行输出流

对吧

进行封装

好

在我们资料下边

有一个叫做文件服务配置属性类

咱们呢

把它也导进来

好

再把整个啊

把这个Properties目录来复制一下

放到我们PDFile Server

好

就在这个File下边来粘贴一下就可以了

贴在这儿

好

然后配置属性类呢

只有一个

但是呢

虽然看到的只有这么一个文件

对吧

实际上这里边呢

还有一个内部类

对吧

你看这里边还藏了一个类呢

叫做Properties

好

然后呢

这个类啊

你看它这个通过Prefix前缀

对吧

然后呢

指定评达点File

那这样的话呢

它是不是就会去加载我们评达点

这个

来找一下啊

评达点这个File

在这儿

对吧

然后呢

再往下是不是有Title

还有什么Base Package啊

所以你看这里边是不是有这个

来找一下Type

这UI Prefix

对吧

然后呢

这些东西

然后呢

还有这个属性对吧

这些属性

而这些属性的话呢

对应的就是我们继续再往下找

这些啊

什么Local

阿里

这是具体每一个策略啊

这些属性

然后呢

就会继续往下封装

封装到这里面来

封装到这里面来

好

这是关于我们这个配置属性类啊

你看这不是Enable Configuration Properties吗

表示这是一个配置属性类

这个呢

我们到时候呢

也会直接拿过来用了就

然后呢

这个地方是Type

指定了一下什么呢

我们文件存储类型

而这个类呢

我们是不是

这就是我们这个

枚矩对吧

在我们刚才导入的这个Entity模块里面啊

然后呢

我们具体用的是哪一种这个存储策略

这是关于我们这个配置属性类

直接导进来

然后最后呢

就是关于我们这个MyBatties啊

它需要使用到的我们这个Mapper接口

对吧

其实就是我们的DAO接口啊

跟我们导入的那个映射文件呢

是一个对应的关系啊

应该是放在哪上

放在DAO这个目录下边

咱们呢

把这个DAO目录呢

也给它创建出来

然后呢

把这两个Mapper接口文件呢

直接拷进来

在我们这个文件服务相关Mapper接口

这个目录下边

你看

刚才我那个DAO呢

已经创建好了

这个目录

所以我们就直接把这两个接口文件放在这下边来

好

你看一个是AttachmentMapper

对吧

这里边的其实就是一些这个增程改查的方法定义啊

然后还有个是FileMapper

OK

这是关于我们这个Mapper接口就已经导进来了

到时候呢

我们进行数据操作呢

直接调用它就可以了啊

然后呢

它跟我们刚才导入的这些映射文件呢

都是一一对应的

跟这些映射文件是一个一一对应的关系

你看在这儿呢

我们通过这个什么呢

在这个地方有个Namespace对吧

正好对应的就是它

这是关于我们MyBatties相关的这些配置

那么到这儿的话呢

我们整个这个Maven工程的环境呢

才已经搭建完

所以大家可以看到我们真正在进行文件服务开发之前

其实是需要依赖这么多的环境的

对吧

一共涉及到了这么十一步

那么把这些准备好之后呢

后边我们就可以来开发我们文件服务相关的业务代码了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对这段技术课程进行的结构化中文输出。

---

### 1) 视频摘要

本视频课程为一个名为“文件服务”的微服务模块的开发教程，主要讲解了如何从零开始搭建一个支持文件上传、下载、分片上传等功能的文件服务。课程内容覆盖了项目初始化、环境搭建（数据库、Nacos、Nginx）、核心代码实现（Spring Boot 启动类、数据库配置、异常处理、文件类型识别、文件压缩、配置属性类、Mapper 接口）以及设计模式（策略模式）的应用。整个过程在 IntelliJ IDEA 开发环境中进行，使用了 Spring Boot、MyBatis、Nacos、Hystrix、Feign 等主流技术栈。

---

### 2) 按时间顺序的章节（带时间点）

由于截图中未提供明确的时间戳，以下章节结构是根据画面内容和逻辑顺序推断的：

*   **第 1 节：项目初始化与环境搭建 (00:00 - 00:15)**
    *   展示了项目目录结构，包括 `pom.xml`、`src/main/java` 和 `src/main/resources`。
    *   介绍了 `FileServerApplication.java` 启动类，其中包含 `@SpringBootApplication`、`@EnableDiscoveryClient`、`@EnableHystrix`、`@EnableFeignClients` 等注解。
    *   展示了 `application.properties` 配置文件。

*   **第 2 节：数据库配置与 MyBatis 配置 (00:15 - 00:30)**
    *   展示了 `BaseMybatisConfiguration.java`，其中定义了 `PaginationInterceptor` 分页拦截器。
    *   展示了 `FileDatabaseAutoConfiguration.java`，其中配置了 `DruidDataSource` 和 `DataSource`，并根据 `spring.profiles.active` 环境变量决定使用 `PGDataSource` 还是 `DataSource`。

*   **第 3 节：全局异常处理 (00:30 - 00:45)**
    *   展示了 `DefaultGlobalExceptionHandler.java`，其中定义了对 `BizException` 和 `HttpMessageNotReadableException` 的统一处理逻辑。

*   **第 4 节：JSON 序列化与反序列化配置 (00:45 - 01:00)**
    *   展示了 `BaseConfig.java`，其中配置了 `Jackson2ObjectMapperBuilderCustomizer`，用于解决 `LocalDateTime` 类型在 JSON 序列化和反序列化时的格式问题。

*   **第 5 节：文件类型识别工具类 (01:00 - 01:15)**
    *   展示了 `FileDataTypeUtil.java`，其中定义了 `getDataType(String mime)` 方法，根据 MIME 类型返回 `IMAGE`、`TEXT` 或 `OTHER`。

*   **第 6 节：文件压缩工具类 (01:15 - 01:30)**
    *   展示了 `ZipUtils.java`，其中定义了 `zipFilesByInputStream` 方法，用于将多个文件流压缩成一个 ZIP 文件。

*   **第 7 节：配置属性类 (01:30 - 01:45)**
    *   展示了 `FileServerProperties.java`，其中定义了 `FileStorageType` 类型的 `type` 属性和 `uriPrefix` 属性，用于配置文件存储方式和访问前缀。

*   **第 8 节：文件处理策略设计 (01:45 - 02:00)**
    *   展示了 PPT 页面，介绍了“文件处理策略”章节。
    *   展示了策略模式的 UML 图，包含 `AbstractFileStrategy` 抽象类和 `FileStrategy` 接口。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容：**
    *   **章节标题：** “5.2 文件处理策略”。
    *   **核心思想：** 为了提供统一的文件服务接口，需要对底层具体的文件存储方式（如本地、阿里云 OSS、FastDFS）进行抽象，采用策略模式进行设计。
    *   **UML 图：** 展示了 `AbstractFileStrategy` 抽象类和 `FileStrategy` 接口，用于定义文件处理的策略。

*   **代码关键内容：**

    *   **Spring Boot 启动类 (`FileServerApplication.java`)**
        ```java
        @SpringBootApplication
        @EnableDiscoveryClient
        @EnableHystrix
        @EnableFeignClients(value = {
            "com.itheima.pinda"
        })
        @EnableTransactionManagement
        @Slf4j
        public class FileServerApplication {
        }
        ```

    *   **数据库配置 (`FileDatabaseAutoConfiguration.java`)**
        ```java
        @Bean(name = DATABASE_PREFIX + "DruidDataSource")
        @ConfigurationProperties(prefix = "spring.datasource.druid")
        public DataSource druidDataSource() {
            return DruidDataSourceBuilder.create().build();
        }

        @Bean(name = DATABASE_PREFIX + "DataSource")
        public DataSource dataSource(@Qualifier(DATABASE_PREFIX + "DruidDataSource") DataSource dataSource) {
            if (ArrayUtils.contains(DEV_PROFILES, this.profiles)) {
                return new PGDataSource(dataSource);
            } else {
                return dataSource;
            }
        }
        ```

    *   **全局异常处理器 (`DefaultGlobalExceptionHandler.java`)**
        ```java
        @ControllerAdvice(annotations = {RestController.class, Controller.class})
        @ResponseBody
        @Slf4j
        public abstract class DefaultGlobalExceptionHandler {
            @ExceptionHandler(BizException.class)
            public R biz(BizException ex, HttpServletRequest request) {
                log.warn("BizException: ", ex);
                return R.result(ex.getCode(), StrUtil.EMPTY, ex.getMessage()).setPath(request.getRequestURI());
            }

            @ExceptionHandler(HttpMessageNotReadableException.class)
            public R httpMessageNotReadable(HttpMessageNotReadableException ex, HttpServletRequest request) {
                log.warn("HttpMessageNotReadableException: ", ex);
                if (StrUtil.containsAny(message, "Could not read document")) {
                    // 处理逻辑
                }
            }
        }
        ```

    *   **JSON 序列化配置 (`BaseConfig.java`)**
        ```java
        @Bean
        public Jackson2ObjectMapperBuilderCustomizer jackson2ObjectMapperBuilderCustomizer() {
            return builder -> builder
                .serializerByType(LocalDateTime.class, new LocalDateTimeSerializer(DateTimeFormatter.ISO_LOCAL_DATE_TIME))
                .deserializerByType(LocalDateTime.class, new LocalDateTimeDeserializer(DateTimeFormatter.ISO_LOCAL_DATE_TIME))
                .serializerByType(LocalDate.class, new LocalDateSerializer(DateTimeFormatter.ISO_LOCAL_DATE))
                .deserializerByType(LocalDate.class, new LocalDateDeserializer(DateTimeFormatter.ISO_LOCAL_DATE))
                .serializerByType(LocalTime.class, new LocalTimeSerializer(DateTimeFormatter.ISO_LOCAL_TIME))
                .deserializerByType(LocalTime.class, new LocalTimeDeserializer(DateTimeFormatter.ISO_LOCAL_TIME));
        }
        ```

    *   **文件类型识别工具类 (`FileDataTypeUtil.java`)**
        ```java
        public static DataType getDataType(String mime) {
            if (mime == null || "".equals(mime)) {
                return DataType.OTHER;
            }
            if (mime.contains("image")) {
                return DataType.IMAGE;
            } else if (mime.startsWith("application/vnd.ms-excel") ||
                       mime.startsWith("application/msword") ||
                       mime.startsWith("application/pdf") ||
                       mime.startsWith("application/vnd.ms-project") ||
                       mime.startsWith("application/x-javascript")) {
                return DataType.TEXT;
            }
            return DataType.OTHER;
        }
        ```

    *   **文件压缩工具类 (`ZipUtils.java`)**
        ```java
        public static void zipFilesByInputStream(ZipOutputStream out, String fileName) throws IOException {
            byte[] buf = new byte[1024];
            out.putNextEntry(new ZipEntry(fileName));
            while ((len = is.read(buf)) > 0) {
                out.write(buf, 0, len);
            }
            out.closeEntry();
            if (is != null) {
                is.close();
            }
        }
        ```

    *   **配置属性类 (`FileServerProperties.java`)**
        ```java
        @ConfigurationProperties(prefix = "pinda.file")
        @RefreshScope
        public class FileServerProperties {
            private FileStorageType type = FileStorageType.LOCAL;
            private String uriPrefix = "";
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景 1：项目初始化与环境搭建**
    *   **描述：** 讲师在 IntelliJ IDEA 中展示了项目结构，包括 `pom.xml`、`src/main/java` 和 `resources` 目录。重点演示了 `FileServerApplication.java` 启动类，解释了 `@SpringBootApplication`、`@EnableDiscoveryClient`、`@EnableHystrix`、`@EnableFeignClients` 等注解的作用，以及 `application.properties` 文件用于配置。

*   **场景 2：数据库配置与 MyBatis 配置**
    *   **
