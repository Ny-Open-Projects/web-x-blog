# 21-swagger2集成-自定义Swagger2启动器实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始讲解和实现了

自定义SWG2的启动器

之前咱们实现了SAFE的自定义启动器

下面我们就采用了

自定义启动器的方式

在项目当中去集成和使用SWG2主件

首先咱们在stock start工程下面

去新建一个主件

咱们回到代码当中

在bustog start下面

右键

6model

点击next

我们给它一个服务名称

叫bustog start SWG

点击next

将名称替换一下

点击finish

创建完成之后

咱们将它的依赖加入进来

从讲义当中进行copy

全选

咱们来看一下

需要用哪些依赖呢

这里需要用到的依赖

有SWG2的主件

然后是Globa工具

这个是谷歌提供出来的

下面的话

是SpringFox SWG2的主件

这个是SWG核心依赖

上面这个是SWG的UI界面的依赖

下面的话

是SpringDataRest的主件依赖

为什么要加入进来

因为咱们在这里要做一个调整和修改

让SpringFox SWG2能够支持DataRest的集成

就是将DataRest的接口

能够显示在SWG2的文档当中

咱们回到代码当中

接着咱们就要去实现它的自动化装配

Configuration配置内

咱们先把这个内容创建一下

先创建它对应的包

这个没有导入生效

对不对

我们重新刷新一下这个工程

Maven Reimport

刷新完成之后

这个就已经高亮显示

咱们再重新创建对应的包

Package

方名叫comitcast.boss.stock start SWG2

方名叫comitcast.boss.stock start SWG2

方名叫comitcast.boss.stock start SWG2

方名叫comitcast.boss.stock SWG2

我们就来创建它的启动列

我们就来创建它的启动列

6加class

当名称的,靠近过来

当名称的,靠近过来

在这里咱们首先加上它对应的注解

咱们看一下这些注解的具体含义

咱们看一下这些注解的具体含义

这个是作为一个配置类的注解标注说明

这个是作为一个配置类的注解标注说明

下面是要开启SWG2的功能

咱们要去生成SWG2文档

咱们要去生成SWG2文档

注解一定要把它加上

下面就是要开启了自动化的装配

然后是一个条件化的配置注解

这条件是基于什么来决定配置呢

根据我们属性当中

有没有配置这个属性项

如果这个配置的这个属性项

它的值是不是等于true

必须要配置这个属性项

并且值等于true

下面的配置才会生效

咱们再回到讲义当中

我们再去将这个属性

加入到咱们的工程代码当中

然后我们再将一些必要的方法copy进来

这些方法copy完成之后

接着咱们就来实现它具体的配置代码

这里还缺少了SWOG的属性配置

咱们将这个实现类copy进来

这个类的作用主要是

记录咱们SWOG当中所配置的属性

里面并没有处理具体的业务逻辑

copy完成之后

咱们来看一下它整体的一个属性信息有哪些

我们来看一下它整体的一个属性信息有哪些

这里面是标记是否开启SWOG

下面是SWOG要解析的保险路径

再往下面是它的解析UIL的配置规则

然后这个是在base pass的基础上面

需要排除的UIL规则

下面就是SWOG的一些标题描述

版本许可生相关的一些信息

海联系人服务条款

然后这个host信息

都在SWOG2文档上面要去显示

和呈现出来的一些信息配置

再往下面是它的全局统一健全的配置

再往下面是它的全局统一健全的配置

大家注意一下

如果是咱们要集成OS2的健全

那么在这里我们要做Hosentization对应的一个配置

咱们可以看到Hosentization具体有哪些属性

有对应的Name

它的健全UIL的配置规则

然后健全的作用域列表

它的Token UIL的历史记录

这里面的话作用域它其实也是一个对象

有它的名称

还有它的描述

SWOG2和OS2的集成健全咱们后面还会做讲解

它的实现方式也会有多种

咱们后面会采用比较简便的方式做对应的实现

再回到咱们刚才的代码当中

我们将必要的一些信息先全部将它加入进来

在这里还需要加上SWOG4place对象的输入

咱们在这里可以看到

这里加了一个条件化的诸解

它的意思就是说

如果没有这个属性对象

那么整个配置的话它就不能生效

这个意思就是基于实例并对象的一个条件化配置

接着咱们就来实现SWOG2的核心代码配置

我们创建一个方法

OK的

这个就是SWOG API文档的具体配置

给它传递了SWOG4place对象

这里面是SWOG的具体属性配置

咱们给它加上一个注解

作为定注入到视频容器当中

加上注释

这个是SWOG2的API文档具体配置

首先咱们要对它的Base Path做处理

如果SWOGProperties里面getBase Path

这个尾空的话

咱们就要做一个复习

我们需要添加它的基础路径Base

咱们可以看到它Base Path具体是配置什么

配置的是所有的路径

这里相当于就是同位符

这个同位符的话就是匹配所有的路径

接着的话是遍历Base Path

并且转换Path路径格式

就转成了SWOG2所能识别的路径格式

它怎么去处理呢

首先咱们要去定义一个集合

它的对象是PlatK的

类型是String

Base

创建一个新的ValueList

然后我们就拿到SWOG2的对象

它的Base Path

Path里面咱们要将它的Path路径做一个转换

把它放在Base Path里面

通过PathSelect

按Path

咱们可以看到

按的方法里面

它将我们的按的Path

转换为了一个PlatK的对象

在这里面做完记录之后

第三步我们要做排除

排除不需要加入SWOG2本档的路径

同样咱们首先先做一个判断

从它的属性当中

去判断它配置是否为空

如果它为空

咱们就添加默认的属性配置

选

Render X2 Paths

Add All

咱们可以看一下

在这里它默认的将错误

还有监控相关的一些接口

可以排除掉了

不需要展示在SWOG2文档当中

同样咱们在这里

再创建一个对象

Bedicate

类型是String

这个是以Tool Paths

New

And List

然后通过SWOG2里面的XSchool Paths

做一个编辑处理

Paths

让它添加到XSchool Paths记录当中

这些属性配置完成之后

接着咱们就会去创建一个API配置

New Bulkier

标识它是SWOG2文档

Use Report

这个是否需要设置呢?

默认的强行消息

咱们不需要

然后host

主机的名称

咱们就从配置当中去获取

这个话再配置它的API

Info

这个API info咱们来看一下

咱们通过这个方法

将SWOG2 Properties里面

配置的API相关的描述信息

全部输出进来了

大家可以看到

对不对

将它创建给API info view的对象当中

接着咱们再来做配置

配置API的信息

VSMAS的

annotation

这个是什么意思呢?

这个意思就是说

它会去基于这个注解进行扫描

然后发现

对应的方法上面

如果是有加上API operation

就会将这个方法

纳入到SWOG2的文档管理当中

比如说咱们可以查找一下API operation

在这里面

像这个Authletic Menu

Operation这个数据层接口

在这里加入一个API operation的注解

它就会将这个方法

加入到SWOG2的文档当中

好

再往下面是配置它的Path信息

Credit Case

End

这个是NOT

这个就是HOD

这个是HOD关系

Path Pass

咱们来看一下它具体意思

它的意思是一个END的关系

对不对?

end的话拿两项

一个是这个项目

另外的话是这么个项目

那么的话

它会将这个路径

加入到SWOG2的文档当中

然后这个条目

大家注意它是一个NOT

也就是说它只要

在排除的路径当中

它就不会加入到SWOG2的文档当中

是这么一个意思

外层是END

内层的话它是一个NOT

这个要理解清楚

好

然后点S1

是UIUI

是KMS这个方法

我们来看一下

这里面是具体如何配置的

它在这里是一个全局预制参数的配置

这样的话

就不必要每个接口调用的时候

都去预制对应的参数

只要做一个全局配置就可以了

它全局配置什么参数呢

它配置一个Authentication

这个是用于Auth2的一个集成配置

后面章节咱们用到的时候

还会做一个使用上的讲解

好

方法下面是securitycontents

这里要采用一个集合regs.securitycontext.auth

这个就与跟路径开头

咱们看一下这个方法

这个方法的意思

它是配置默认的全局健全策略的开关

它通过正则表达式进行匹配

默认的话

它会匹配所有的URL

这里会配置一个健全的认证表达师

这里会配置一个健全的认证表达师

如果是这个路径匹配的话

那么就会进行了健全的处理

我们看一下deployedauth

它是如何进行配置的

这个是默认的全局策略控制

这里面的话

它会去设定了Authentication

它会去设定了Authentication

配置相关的信息

咱们就按照这种默认方式进行配置就可以了

这里会设置它关联的认证信息

这里会设置它关联的认证信息

以及它的作用域范围

这一块就是Swog2文档的一个具体代码配置

这一块就是Swog2文档的一个具体代码配置

咱们再回到讲义当中做一个回顾

咱们再回到讲义当中做一个回顾

这个配置咱们首先要开启Enable Swog2的注解

这个配置咱们首先要开启Enable Swog2的注解

然后实现它的条件化配置

这个条件化是根据它的一个属性

Swog2Enable去进行控制的

如果是它等于Q

就会激活对应的配置

也就是咱们在代码当中所编写的这一系列的代码配置

就会激活对应的代码配置

SplintBoot服务它会提供一些默认的接口

比如说像L错误接口

监控收集Aggregator相关的接口

监控收集Aggregator相关的接口

这些接口我们不需要在文档中体现

可以排除UI了

写在Docky的parts当中

也在上面当中我们做了一个

排除的属性定义

排除的属性定义

接着就是Swog2 property的属性配置类

接着就是Swog2 property的属性配置类

在这里面并没有具体的配置代码

以及实现逻辑

以及实现逻辑

包括主机的配置

UI路径配置等信息

最后在Resource目录下面

去创建MetaINF

要遵循SPI机制

创建SplintFactories

指定它的路径

我们就来做一个实现

在下面创建一个目录

在下面创建一个目录

叫MetaINF

创建一个文件名称

NuFireSplint

然后将这段代码

迷倒计过来

大家注意这个路径一定要配置正确

我们将这个路径重新扩比一下

很久可以看到了

它能够正常识别

在这里就完成了Swog2

制定义启动器的配置实现

好 这讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析：

---

### 1) 视频摘要

本视频片段是关于在 Spring Boot 项目中自定义集成 Swagger2 的技术教程。讲师通过 IntelliJ IDEA 开发环境，演示了如何创建一个自定义的 Starter 项目 `stock-starter-swagger`，并编写核心配置类 `AutoSwaggerConfiguration`。该配置类负责整合 Swagger2、Swagger-UI、Spring Data Rest 等组件，并通过 `SwaggerProperties` 配置类读取外部配置，最终将 API 文档集成到项目中。视频重点讲解了如何通过 `@ConfigurationProperties` 注解绑定配置文件，如何使用 `Docket` 对象构建 API 文档，以及如何通过 `@EnableSwagger2` 注解和 `@ConditionalOnProperty` 条件注解来控制 Swagger2 的启用与配置。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，讲师在 Typora 文档中展示课程大纲，定位到“3.1 自定义Swagger2启动器”章节。
*   **00:00:05 - 00:00:15**：讲师在 IDEA 中展示项目结构，创建了 `stock-starter-swagger` 模块，并在 `pom.xml` 中添加了 Swagger2、Swagger-UI 和 Spring Boot Data Rest 的依赖。
*   **00:00:15 - 00:00:30**：讲师在 `AutoSwaggerConfiguration.java` 中编写核心配置类，定义了 `Docket` 对象，并开始配置 `ApiInfo` 和 `securitySchemes`。
*   **00:00:30 - 00:00:45**：讲师展示 `SwaggerProperties.java` 配置类，其中定义了 `host`、`contactUrl`、`termsOfServiceUrl` 等配置项，并通过 `@Value` 注解绑定外部配置。
*   **00:00:45 - 00:01:00**：讲师在 `AutoSwaggerConfiguration.java` 中继续编写代码，配置 `basePath`、`excludePath`（排除路径）和 `securitySchemes`（安全策略）。
*   **00:01:00 - 00:01:15**：讲师展示如何通过 `@EnableSwagger2` 注解启用 Swagger2，并通过 `@ConditionalOnProperty` 注解根据配置属性 `swagger.enabled` 来控制其是否激活。
*   **00:01:15 - 00:01:30**：讲师在 Typora 文档中展示如何在 `resources/META-INF/spring.factories` 文件中配置自动装配类，以便 Spring Boot 自动扫描并加载 `AutoSwaggerConfiguration`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`3.1 自定义Swagger2 启动器`、`3.2 后台管理服务集成Swagger2`。
    *   **关键说明**：
        *   “通过Spring Boot 自定义Starter方式，封装Swagger组件，集成项目中方便配置使用。”
        *   “要开启EnableSwagger2注解”
        *   “ConditionalOnProperty自动化配置激活条件是根据swagger.enabled属性，havingValue = “true” 则激活配置。”
        *   “Spring boot 服务会提供些默认的接口，比如错误处理接口、收集/actuator等，这些接口我们不需要在文档中体现，可以写入到 Docket的Paths，通过排除策略做过滤处理。”

*   **代码关键内容**：

    *   **`pom.xml` 依赖配置**：
        ```xml
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger2</artifactId>
            <version>${swagger.version}</version>
        </dependency>
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger-ui</artifactId>
            <version>${swagger.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-rest</artifactId>
        </dependency>
        ```

    *   **`SwaggerProperties.java` 配置类**：
        ```java
        @ConfigurationProperties(prefix = "swagger")
        public class SwaggerProperties {
            @Value("${swagger.contact.email}")
            private String contactEmail = "";
            @Value("${swagger.termsOfServiceUrl}")
            private String termsOfServiceUrl = "";
            @Value("${swagger.host}")
            private String host = "";
            @Value("${swagger.version}")
            private String version = "";
        }
        ```

    *   **`AutoSwaggerConfiguration.java` 核心配置类**：
        ```java
        @Configuration
        @EnableSwagger2
        @ConditionalOnProperty(name = "swagger.enabled", havingValue = "true")
        public class AutoSwaggerConfiguration {
            @Bean
            public Docket api(SwaggerProperties swaggerProperties) {
                return new Docket(DocumentationType.SWAGGER_2)
                    .useDefaultResponseMessages(false)
                    .host(swaggerProperties.getHost())
                    .apiInfo(apiInfo(swaggerProperties))
                    .select()
                    .apis(RequestHandlerSelectors.withMethodAnnotation(ApiOperation.class))
                    .paths(PathSelectors.any())
                    .build()
                    .securitySchemes(securitySchemes(swaggerProperties))
                    .securityContexts(securityContexts(swaggerProperties));
            }

            private ApiInfo apiInfo(SwaggerProperties swaggerProperties) {
                return new ApiInfoBuilder()
                    .title(swaggerProperties.getTitle())
                    .description(swaggerProperties.getDescription())
                    .license(swaggerProperties.getLicense())
                    .licenseUrl(swaggerProperties.getLicenseUrl())
                    .termsOfServiceUrl(swaggerProperties.getTermsOfServiceUrl())
                    .contact(new Contact(
                        swaggerProperties.getContactName(),
                        swaggerProperties.getContactUrl(),
                        swaggerProperties.getContactEmail()
                    ))
                    .version(swaggerProperties.getVersion())
                    .build();
            }

            private List<SecurityScheme> securitySchemes(SwaggerProperties swaggerProperties) {
                List<SecurityScheme> securitySchemes = new ArrayList<>();
                // ... 配置安全策略
                return securitySchemes;
            }

            private List<SecurityContext> securityContexts(SwaggerProperties swaggerProperties) {
                List<SecurityContext> securityContexts = new ArrayList<>();
                // ... 配置安全上下文
                return securityContexts;
            }
        }
        ```

    *   **`META-INF/spring.factories` 文件内容**：
        ```
        # Auto Configure
        org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
        com.itcast.stock.starter.swagger.AutoSwaggerConfiguration
        ```

---

### 4) 关键场景与演示描述

*   **场景一：创建自定义 Starter** (00:00:05)
    *   **描述**：讲师在 IntelliJ IDEA 中，通过右键菜单在 `stock-starter` 工程下新建一个名为 `stock-starter-swagger` 的模块。随后，他打开该模块的 `pom.xml` 文件，添加了 Swagger2、Swagger-UI 和 Spring Boot Data Rest 的 Maven 依赖，为后续开发做准备。

*   **场景二：编写核心配置类** (00:00:15)
    *   **描述**：讲师在 `stock-starter-swagger` 模块的 `src/main/java` 目录下创建了 `AutoSwaggerConfiguration.java` 文件。他首先定义了一个 `@Configuration` 类，并使用 `@EnableSwagger2` 注解启用 Swagger2。接着，他编写了一个 `@Bean` 方法，用于返回一个 `Docket` 对象，该对象是 Swagger2 的核心配置。

*   **场景三：配置 Swagger2 属性** (00:00:30)
    *   **描述**：讲师创建了 `SwaggerProperties.java` 配置类，使用 `@ConfigurationProperties(prefix = "swagger")` 注解将其与外部配置文件（如 `application.yml`）中的 `swagger` 前缀属性绑定。类中定义了 `host`、`contactEmail`、`termsOfServiceUrl`、`version` 等私有属性，并通过 `@Value` 注解注入配置值。

*   **场景四：构建 API 文档** (00:00:45)
    *   **描述**：讲师在 `AutoSwaggerConfiguration.java` 中，通过 `Docket` 对象的链式调用，配置了 API 文档的元信息（`apiInfo`）、路径选择器（`select().apis(...).paths(...)`）、排除路径（`excludePath`）和安全策略（`securitySchemes` 和 `securityContexts`）。他特别演示了如何通过 `PathSelectors.any()` 来包含所有路径，并通过 `excludePath` 排除 `/error` 和 `/actuator` 等默认路径。

*   **场景五：启用与条件控制** (00:01:00)
    *   **描述**：讲师在 `@Configuration` 类上添加了 `@ConditionalOnProperty(name = "swagger.enabled",
