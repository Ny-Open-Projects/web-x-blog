# 17-全局权限控制-公开菜单数据加载 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始讲解和实现

Slimboot初始化加载公开菜单的缓存数据

在前面章节当中

咱们讲解了过滤器权限拦截的处理

之前我们做了白名单的过滤和控制

那么上面采用缓存去处理公开菜单数据

也就是白名单的数据

这个是需要在Slimboot容器启动之后

去加载相关的数据到缓存里面

那么我们如何去实现呢

这就需要借助application run的这个接口

来帮助咱们去实现Slimboot的初始化加载

首先咱们创建global system configuration这个配置内

在admin user configure包下面去创建一个class

在这里注意他要去实现application run的这个接口

要去实现了run方法

该接口的主要作用是在于Slimboot成功启动之后

会自动执行

如果启动过程当中出现了异常

或者还没有启动加载完成

这个run方法是不会被执行

这点大家要理解清楚

那咱们给他加上configuration的图解

还有numbook log4j的图解

给他注册一下

注入对应的属性

首先呢

要将缓存管理器注入进来

这个是缓存的接口管理器

接着咱们还要注入呢

公开菜单的数据省接口

这个是公开菜单的

数据省接口

那咱们看一下在这里面他提供了一个方法

这个方法是获取所有的公开菜单数据

咱们不需要制定设口

直接翻了过就可以查询出他所有的数据

接下来咱们增加一个日资打印

通过这个日资呢

我们就可以知道他有没有进入run方法里面

然后我们要加载公开的菜单数据信息

是缓存当中

首先咱们拿到HQ一下

这里呢要传入他的Key值

Menu Key

然后呢

查询出所有的公开菜单数据

通过咱们注入的数据层接口

查了出所有的数据

接着的话呢

咱们也将它进行一个转换

咱们只需要获取

Auxility No Limit UI对象里面的

UI属性就可以

所以呢

咱们也将它做一个转换

将所有的UI信息

转换保存至Set集合里面

通过流逝处理

No Limit

获取它的UI属性

将它转换为集合

将转换后的数据呢

保存至Ladies缓存里面

给它一个Key

No Limit Key

这个呢就是标识了

公开菜单数据的

缓存键值

将Set存入进去

好这样咱们就实现了

公开菜单缓存数据的

初始化加载

实现了这个功能之后呢

传线过滤器才能够

完成了

公开菜单的判断处理

也就之前咱们所讲的

在这里呢

它会去判断

哪些呢

是允许公开放行的菜单

好

在这里呢

咱们就完成了

公开菜单的缓存数据

初始化加载

那这一讲

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析：

---

### 1) 视频摘要

本视频片段是关于 Spring Boot 应用程序中如何在容器启动后，通过 `ApplicationRunner` 接口，将“公开菜单”的数据加载并缓存到 Redis 中的教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何编写 `GlobalSystemConfiguration` 配置类。该类通过 `@Configuration` 注解定义，实现了 `ApplicationRunner` 接口，其 `run` 方法在 Spring Boot 容器启动后自动执行。核心逻辑是：获取 `CacheManager` 和 `AuthorityNoLimitUriRepository` 的实例，然后从数据库查询公开菜单数据，将其转换为 `Set<String>` 集合，并最终存入 Redis 缓存中，以供后续服务快速访问。整个过程旨在优化系统性能，避免每次请求都查询数据库。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中展示本节内容标题：“3.4 Spring Boot 初始化加载公开菜单的缓存数据”，并说明目标是使用 `ApplicationRunner` 接口在 Spring Boot 容器启动后加载数据。
*   **00:00:06 - 00:00:15**: 讲师切换到 IntelliJ IDEA，展示项目结构，并定位到 `GlobalSystemConfiguration.java` 文件。
*   **00:00:16 - 00:00:30**: 讲师在代码编辑器中展示 `GlobalSystemConfiguration` 类的完整结构，包括 `@Configuration`、`@Log4j2` 注解，以及 `@Autowired` 注入的 `CacheManager` 和 `AuthorityNoLimitUriRepository`。
*   **00:00:31 - 00:00:45**: 讲师将光标移动到 `run` 方法，并开始编写核心逻辑。首先，通过 `cacheManager.getCache(GlobalConstants.AUTHORITY_MENU_KEY)` 获取缓存对象。
*   **00:00:46 - 00:00:55**: 讲师调用 `authorityNoLimitUriRepository.findAll()` 查询数据库中的公开菜单数据，并将其转换为 `Set<String>` 集合。
*   **00:00:56 - 00:01:05**: 讲师将转换后的 `Set<String>` 集合通过 `cache.put(GlobalConstants.AUTHORITY_MENU_NO_LIMIT_KEY, noLimitSet)` 方法存入 Redis 缓存中。
*   **00:01:06 - 00:01:15**: 讲师完成代码编写，光标停留在 `run` 方法末尾，表示初始化逻辑已全部实现。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文本内容**:
    *   **标题**: “3.4 Spring Boot 初始化加载公开菜单的缓存数据”
    *   **核心说明**: “上面采用缓存来处理公开菜单数据，需要在Spring Boot 容器启动之后加载相关数据至缓存，借助ApplicationRunner接口来实现。”
    *   **代码结构**: “GlobalSystemConfiguration类: `@Configuration @Log4j2 public class GlobalSystemConfiguration implements ApplicationRunner { ... }`”

*   **关键代码片段**:
    *   **类定义**:
        ```java
        @Configuration
        @Log4j2
        public class GlobalSystemConfiguration implements ApplicationRunner {
        ```
    *   **依赖注入**:
        ```java
        @Autowired
        private CacheManager cacheManager;
        
        @Autowired
        private AuthorityNoLimitUriRepository authorityNoLimitUriRepository;
        ```
    *   **核心业务逻辑**:
        ```java
        @Override
        public void run(ApplicationArguments args) throws Exception {
            // 1. 获取缓存对象
            Cache cache = cacheManager.getCache(GlobalConstants.AUTHORITY_MENU_KEY);
            
            // 2. 查询数据库并转换为 Set<String>
            List<AuthorityNoLimitUri> noLimitMenuList = authorityNoLimitUriRepository.findAll();
            Set<String> noLimitSet = noLimitMenuList.stream()
                .map(nolimit -> nolimit.getNoLimitUri())
                .collect(Collectors.toSet());
            
            // 3. 将数据存入缓存
            cache.put(GlobalConstants.AUTHORITY_MENU_NO_LIMIT_KEY, noLimitSet);
        }
        ```

*   **关键常量**:
    *   `GlobalConstants.AUTHORITY_MENU_KEY`: 用于获取缓存对象的键。
    *   `GlobalConstants.AUTHORITY_MENU_NO_LIMIT_KEY`: 用于存储公开菜单数据的键。

---

### 4) 关键场景与演示描述

*   **场景一：环境与项目定位 (00:00:06 - 00:00:15)**
    *   讲师在 IntelliJ IDEA 中打开项目 `bulls-stock-admin-user`，并导航到 `config` 包下的 `GlobalSystemConfiguration.java` 文件，为后续代码编写做准备。

*   **场景二：代码结构与注解说明 (00:00:16 - 00:00:30)**
    *   讲师在代码编辑器中高亮显示 `@Configuration` 注解，说明这是一个 Spring 配置类。接着高亮 `@Log4j2` 注解，表示使用 Log4j2 日志框架。然后展示 `implements ApplicationRunner`，说明该类将在 Spring Boot 容器启动后执行 `run` 方法。

*   **场景三：依赖注入与变量声明 (00:00:31 - 00:00:45)**
    *   讲师将光标移动到 `@Autowired` 注解，说明 `cacheManager` 和 `authorityNoLimitUriRepository` 会由 Spring 容器自动注入。他通过鼠标悬停或高亮，展示了这些变量的类型和作用。

*   **场景四：核心逻辑实现 (00:00:46 - 00:01:05)**
    *   讲师在 `run` 方法中，首先通过 `cacheManager.getCache(...)` 获取缓存对象。接着，他调用 `findAll()` 方法获取数据库中的公开菜单数据，并使用 `Stream` API 将其转换为 `Set<String>` 集合。最后，他调用 `cache.put(...)` 方法将数据存入缓存。

*   **场景五：代码完成与总结 (00:01:06 - 00:01:15)**
    *   讲师完成所有代码编写，光标停留在 `run` 方法末尾。他通过高亮 `cache.put(...)` 行，强调这是整个初始化流程的最终一步，数据已成功加载并缓存。
