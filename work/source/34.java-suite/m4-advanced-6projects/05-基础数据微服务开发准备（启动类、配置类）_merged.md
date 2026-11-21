# 05-基础数据微服务开发准备（启动类、配置类） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面呢,咱们Spring Boot配置文件呢,已经准备好了,对吧,接下来呢,就是服务启动类,其实呢,这个服务启动类呢,大家来看一下,在我们这个项目里面其实也已经提供好了,这个呢,是我们前面啊,在第一章当中,大家还记得吧,在第一章当中,我们是不是已经编写好了,当时呢,是以这个PTBase这个基础为服务,对吧,作为例子呢,我们是测试了一下我们导入的基础环境啊,

是否是,是否有什么问题,所以说呢,当时是已经把这个服务启动类呢,已经编写好了,所以我们这个地方呢,就直接使用它就可以了,好,接下来呢,下一个就是我们配置类,这个配置类呢,其实大家可以看一下,一个呢,是我们买Betis Plus,对吧,那么需要有一个配置类,那么使用它的时候呢,主要要加入的是它这个分页的插件,对吧,就是这个分页的Interceptor,一个拦截器,

那么把它这个配置一下就可以了,

这个呢,我就不再过多解释了,这都是我们前面框架的一些基础知识,咱们直接拿过来使用就可以了,还有一个配置类呢,就是关于我们这个Swagger文档的,那么我们需要来配置它,就是这个Swagger Config,好,那么首先呢,我们可以先来创建一个Config包,用来存放我们这些配置类的,然后呢,我们在这下边来创建一个Package,好,然后呢,在这创建一个类,这个类名呢,跟这个保持一致啊,就叫做买Betis Plus Config,

好,这儿呢,我们可以来加一个买Betis Plus,这是相关的这个配置类,好,既然是一个配置类的话呢,我们是不是需要来加一个Configuration注解,对吧,表示呢,它是一个配置类,然后呢,在这里边呢,咱们是不是需要来创建出来一个并对象,这个并对象呢,就是我们买Betis Plus底层在进行什么呢,分页查询的时候啊,需要使用到的它这个插件,对吧,

分页查询,叫做Pagination Interceptor,好,那么我们在这儿呢,Pagination Interceptor,应该就是这个,对吧,然后呢,这个方法名呢,其实叫什么名字都可以啊,直接给它创建出来就可以了,直接NU一个Pagination Interceptor,好,这个代码呢,还是非常简单的,然后呢,别忘了给它加一个什么呢,并注解,对吧,这样的话呢,我们项目在启动的时候呢,

首先呢,它会扫描到我们当前这个配置类,因为我们在这儿也加了注解了,所以它会扫描到它,然后呢,因为我们这个方法上加了并注解,那么它就会把当前这个实力化的对象呢,加入到我们Spring容器,最终呢,来实现什么呢,实现分页查询,这是买Betis Plus给我们提供的这个分页插件,好,然后呢,这个配置好之后呢,还有一个配置类啊,这个配置类刚才提的啊,就是关于什么呢,关于我们这个SWAG文档呢,

它创建出来,叫做SWAG Config,好,也在这个Config包下面来创建一下,这个呢,是我们这个SWAG文档相关配置类,然后呢,给它加一个什么呢,Configuration,对吧,Configuration注解,然后呢,接下来我们需要来创建的,还有这个,把这个加一下就可以了,就是启用它,叫做什么,Enable SWAG2,

好,

在这来导一下,导入这个类,好,这个表示什么呢,启用,对吧,或者叫做开启,开启我们的SWAG文档功能,好,然后这里边呢,我们这个配置类啊,要开启这个功能,其实主要就是什么呢,需要创建SWAG给我们提供的一个对象,通过这个对象呢,来描述啊,或者来展示我们的这个创建出来的这些接口文档,对吧,

那么,

要创建的是什么呢,叫做Dockit,Dockit呢,其实就是文档对象,对吧,文档对象,但是这里边这个代码呢,我就不再去写了,咱们直接抄过来就可以,同时呢,因为这个SWAG文档呢,它属于我们Web层的,要展示我们这个接口的规范,所以说呢,我们一般呢,都会去继承,继承这么一个叫做Web MVC Configuration support,是一个支持类,这个呢,也基本上都是一些固定的套路了,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

好,

对吧,

给我们提供的这么一个配置的支持类,好,

那么为什么要继承它呢,继承它之后呢,大家可以看到,在这个类里面呢,它其实是有一些什么呢,生命周期方法的,对吧,生命周期方法,咱们来看一下,这个地方呢,我们主要使用到的是这个,叫做Add Resource Handlers,对吧,你看,它这是不是有个override呀,那么也就是说,在我们这个里边呢,有一些生命周期方法,在这儿呢,就可以来加入一些什么呢,来加入一些资源,加入一些资源,好,

那么到这边来,我们这个代码呢,我就不再去手敲了,基本上也都是固定的套路,咱们呢,可以大概来读一下,那么主要的就是这个方法,看到没有,这个方法名其实无所谓,重点呢,返回值,这个返回值不要写错了,叫做Dockit,对吧,然后呢,在这个地方,我们需要来创建一个什么Dockit的对象,那么在创建它的时候呢,需要来指定什么呢,最重要的就是这个,我们要扫描哪个包,对吧,因为一般呢,我们是不是都是来扫描Control了,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

对吧,

当然了,

这个地方呢,

要设置这个API的信息呢,

那么代码比较复杂,

所以说呢,

我们单独又提出来了一个方法,

也叫API info,

那么其实就是它,

然后返回值呢,

就是一个API info对象,

对吧,

然后呢,

我们直接在这儿来指定什么呢,

这个API info它的title,

它的标题,

它的版本等等这些信息,

好,

好,

整个代码呢,

我们就直接抄过来了,

最后呢,

还有这个生命周期方法,

对吧,

add resource handlers,

在这儿我们也指定了解决什么呢,

静态资源无法访问的这些问题,

好,

直接拿过来,

这个呢,

也都是一些固定的套路代码,

所以大家可以看到,

我们对于这些配置类的话呢,

其实并不需要自己去手敲,

因为你自己去敲这类的代码呢,

其实没有多大意义,

我们更多的呢,

还是我们真正的开发的时候工作量呢,

还是一些什么呢,

我们的业务代码,

对吧,

业务代码呢,

那么就需要根据我们实际的业务去编写,

它是没有办法实现,

呃,

变成这种模板化的,

对吧,

而对于这种配置类的呢,

它其实本质上相当于就是配置文件的作用,

对吧,

那么对于这种固定的模板代码呢,

我们一般呢,

就直接抄过来,

只要呢,

大家能看懂,

对吧,

会改,

比如说我们会改造,

那么就可以了,

好,

那么这个地方呢,

只加入了一些这个精彩资源,

对吧,

好,

主要就是我们需要访问到我们swag它的文档,

到时候呢,

我们会通过这个页面,

对吧,

叫swag-ui.html来访问,

好,

防止我们这个Sprite MVC框架把它给拦截了,

好,

那么这是关于我们配置类,

咱们在这呢,

一共是不是涉及到了这么两个,

一个是买,

Battis Plus的配置类,

还有一个呢,

就是我们这个swag文档的配置类,

好,

那么关于配置类呢,

我们先写到这,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于一个名为“品达物流TMS项目”的基础微服务开发教程，主要聚焦于 Spring Boot 项目的核心配置与功能实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个基础的 Spring Boot 启动类、配置 MyBatis Plus 的分页插件、集成 Swagger2 API 文档，并处理静态资源路径冲突问题。课程内容结构清晰，旨在为开发者提供一个可复用的基础服务框架。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 课程开场，展示项目结构和 `BaseApplication` 启动类。
*   **00:10 - 00:25**: 讲解 `BaseApplication` 启动类，包含 `@SpringBootApplication` 和 `@EnableDiscoveryClient` 注解。
*   **00:25 - 00:45**: 进入 `2.3 配置类`，演示 `MybatisPlusConfig` 类，用于配置 MyBatis Plus 的分页插件。
*   **00:45 - 01:00**: 展示 `SwaggerConfig` 类，用于集成 Swagger2 API 文档。
*   **01:00 - 01:15**: 详细讲解 `SwaggerConfig` 中的 `createRestApi` 方法，配置 API 文档的扫描包和基础信息。
*   **01:15 - 01:30**: 讲解 `WebMvcConfigurationSupport` 类的源码，分析其如何处理请求映射和拦截器。
*   **01:30 - 01:45**: 展示 `addResourceHandlers` 方法，解决 Swagger 文档静态资源访问路径冲突的问题。
*   **01:45 - 02:00**: 进入 `2.4 Id生成器` 章节，展示 `IdentifierGenerator` 的相关导入和注解。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   项目结构：`pd-base` 项目包含 `src/main/java`、`resources`、`pom.xml` 等标准目录。
    *   章节大纲：清晰列出“第2章 基础数据服务开发”下的子章节，包括“2.1 SpringBoot配置文件”、“2.2 服务启动类”、“2.3 配置类”、“2.4 Id生成器”等。
    *   代码注释：PPT 中包含对代码功能的说明，如“解决静态资源无法访问”、“防止@EnableWebMvc把默认的静态资源路径覆盖了”。

*   **关键代码**:

    **2.2 服务启动类 (`BaseApplication.java`)**
    ```java
    @SpringBootApplication
    @EnableDiscoveryClient
    public class BaseApplication {
        public static void main(String[] args) {
            SpringApplication.run(BaseApplication.class, args);
        }
    }
    ```

    **2.3 配置类 (`MybatisPlusConfig.java`)**
    ```java
    @Configuration
    public class MybatisPlusConfig {
        @Bean
        public PaginationInterceptor paginationInterceptor() {
            return new PaginationInterceptor();
        }
    }
    ```

    **2.3 配置类 (`SwaggerConfig.java`)**
    ```java
    @Configuration
    @EnableSwagger2
    public class SwaggerConfig extends WebMvcConfigurationSupport {
        private static final String splitter = ",";

        @Bean
        public Docket createRestApi() {
            return new Docket(DocumentationType.SWAGGER_2)
                    .apiInfo(apiInfo())
                    .select()
                    .apis(RequestHandlerSelectors.basePackage("com.ithema.pinda.controller"))
                    .paths(PathSelectors.any())
                    .build();
        }

        private ApiInfo apiInfo() {
            return new ApiInfoBuilder()
                    .title("品达物流管理后台基础数据-Swagger文档")
                    .version("1.0")
                    .build();
        }
    }
    ```

    **`WebMvcConfigurationSupport` 类关键方法 (`addResourceHandlers`)**
    ```java
    @Override
    protected void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/swagger-ui.html")
                .addResourceLocations("classpath:/META-INF/resources/");
        registry.addResourceHandler("/webjars/**")
                .addResourceLocations("classpath:/META-INF/resources/webjars/");
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：项目初始化与启动类配置 (00:00-00:25)**
    *   讲师在 IntelliJ IDEA 中打开 `BaseApplication.java` 文件，展示其作为 Spring Boot 应用的入口点。
    *   通过 `@SpringBootApplication` 注解，自动配置 Spring Boot 的核心组件。
    *   通过 `@EnableDiscoveryClient` 注解，启用服务发现功能，便于后续微服务集成。

*   **场景二：MyBatis Plus 分页插件配置 (00:25-00:45)**
    *   讲师切换到 `MybatisPlusConfig.java` 文件，展示如何通过 `@Configuration` 注解定义一个配置类。
    *   在类中使用 `@Bean` 注解，将 `PaginationInterceptor` 对象注册为 Spring 容器中的 Bean，从而在所有 MyBatis 查询中自动启用分页功能。

*   **场景三：Swagger2 API 文档集成 (00:45-01:15)**
    *   讲师展示 `SwaggerConfig.java` 文件，通过 `@Configuration` 和 `@EnableSwagger2` 注解启用 Swagger2 功能。
    *   详细演示 `createRestApi` 方法的构建过程，包括设置文档标题、版本、扫描的包路径等。
    *   通过 `Docket` 对象的链式调用，配置 API 文档的详细信息。

*   **场景四：解决静态资源路径冲突 (01:15-01:30)**
    *   讲师在 `SwaggerConfig` 类中，通过 `extends WebMvcConfigurationSupport` 继承父类。
    *   重写 `addResourceHandlers` 方法，手动配置 Swagger UI 和 WebJars 的静态资源路径，避免与 Spring MVC 默认的静态资源路径冲突。

*   **场景五：Id生成器模块介绍 (01:45-02:00)**
    *   讲师切换到 `2.4 Id生成器` 章节，展示 `IdentifierGenerator` 的相关导入和注解。
    *   为后续开发自定义 ID 生成器做准备，如雪花算法、数据库自增等。

---

以上是根据视频画面整理出的技术课程结构化分析，希望能帮助您更好地理解课程内容。
