# 34-声明式缓存（声明式缓存代码实现_编写抽象 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才呢

咱们是把这几个测试方法考过来

然后呢

让大家了解了一下

我们在使用这个注解的时候

我们最终的生成的key

到底是一个什么样的值

它的规则是什么

对吧 这个参数应该怎么写

好 然后接下来呢

我们最后呢

再把这个抽象的缓存注解处理器

稍微完善一下

那么这块需要完善哪呢

就是这个地方

你看我们在这呢

是不是来创建了这么两个处理器

对吧

一个是我们这个catch annotation processor

还有一个是catch evict annotation processor

对吧 两个具体的处理器

然后在创建它的时候呢

其实我们需要把对应的这两个参数呢

给它传进去

要不然的话

你看在这直接new它的话呢

那我们这两个参数

其实就没有意义了

对吧 好

所以说呢 我们在这呢

需要完善一下

把这两个参数

给它继续往里面传一下

好 包括下边这个

也是proceeding

然后呢 把这个catch evict对象传进去

但是现在呢

它肯定会报错

因为什么呢

因为我们这里边没有这样的类

对吧

所以我们在这呢

需要把这个什么的构造方法

给它创建一下

好

create

在这里边把我们这个构造方法传出来

好

然后一会儿呢

我们再去完善这边啊

咱们先把这个抽象类呢

给它搞定

包括这个地方

对吧

也需要来扩展一下

好 这是我们抽象类的这个构造方法

好

那么到这儿的话呢

咱们这个抽象的副类

也就是我们这个抽象的缓存注解处理器呢

就整个都已经写完了

咱们回过头来

可以再来看一下

在这里边呢

提供了一个公共的成员变量

对吧

就是这个catch channel

然后呢

子类呢

都可以使用这个对象呢

来进行什么呢

来进行缓存相关的操作

好

当然了在这儿的话

如果只是这么一个声明的话呢

它是空的

所以说呢

在我们这个地方

在构造方法这个地方呢

我们需要干什么呢

是不是需要来把这个对象给它

从我们sprint容器里面给它获取出来

给它附上值

那这样的话才能去使用它

要不然它是空的

好

然后在下边呢

这个地方呢

我们是不是提供了这么一个方法

get annotation info

就是把我们这个catch注解进行一个分析

重新封装成这么一个annotation info

然后一会儿呢

在我们具体的这两个处理器子类里边呢

就会使用到这个对象

好

包括这个地方

是不是给我们动态生成key的

这个方法呢

好

另外呢

还有一个抽象的这个process方法

对吧

然后这个方法呢

就需要我们这两个子类去具体去实现

好

还有呢

就是获得这两个具体处理器的这两个方法

好

那么到这儿的话

咱们这个抽象复类就全都写完了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段是关于 Spring 框架中基于注解的缓存（Cache）功能的源码剖析。讲师通过 IntelliJ IDEA 开发环境，逐步展示并讲解了 `AbstractCacheAnnotationProcessor` 类的核心逻辑。主要内容包括：
*   **缓存注解处理器的创建与选择**：通过 `getProcessor` 静态方法，根据传入的 `Cache` 或 `CacheEvictor` 注解，动态返回具体的处理器实例（`CachesAnnotationProcessor` 或 `CacheEvictorAnnotationProcessor`）。
*   **缓存键（Key）的动态生成**：在 `generateKey` 方法中，讲师详细解释了如何根据注解参数和目标方法信息（如类名、方法名）动态构建缓存键，以支持灵活的缓存策略。
*   **注解信息的封装**：在 `getAnnotationInfo` 方法中，讲师演示了如何将注解的属性（如 `region`）封装到 `AnnotationInfo` 对象中，为后续的缓存操作提供数据。
*   **抽象类的结构**：讲师展示了 `AbstractCacheAnnotationProcessor` 的抽象结构，包括其构造函数中获取 Spring 应用上下文和 `CacheChannel`，以及其抽象方法 `process`，该方法是所有具体处理器必须实现的核心逻辑。

整个过程旨在帮助观众理解 Spring 缓存注解是如何在编译期或运行期被处理，以及其底层是如何通过 AOP（面向切面编程）和注解处理器来实现的。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示项目结构和 `JCacheController` 中的两个缓存方法 `getCacheDataBody` 和 `getCacheDataParams`，并强调它们是用于演示缓存功能的。
*   **00:05 - 00:15**: 跳转到 `AbstractCacheAnnotationProcessor.java` 文件，开始讲解缓存注解处理器的逻辑。
*   **00:15 - 00:25**: 讲解 `getProcessor` 方法，演示如何根据传入的 `Cache` 或 `CacheEvictor` 注解，返回对应的处理器实例。
*   **00:25 - 00:35**: 重点讲解 `generateKey` 方法，演示如何动态解析注解信息并生成缓存键，包括处理空键的逻辑。
*   **00:35 - 00:45**: 讲解 `getAnnotationInfo` 方法，演示如何封装注解信息到 `AnnotationInfo` 对象中。
*   **00:45 - 00:55**: 展示 `AbstractCacheAnnotationProcessor` 的构造函数，讲解其如何获取 Spring 应用上下文和 `CacheChannel`。
*   **00:55 - 01:05**: 展示抽象方法 `process`，并强调这是所有具体处理器必须实现的核心方法。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**：
    *   **`generateKey` 方法**：
        ```java
        protected String generateKey(ProceedingJoinPoint proceedingJoinPoint, Cache cache) throws IllegalAccessException {
            String key = cache.key(); // 获取注解中定义的 key
            if (!StringUtils.hasText(key)) { // 如果 key 为空
                String className = proceedingJoinPoint.getTarget().getClass().getSimpleName();
                MethodSignature signature = (MethodSignature) proceedingJoinPoint.getSignature();
                String methodName = signature.getMethod().getName();
                key = CacheKeyBuilder.generateKey(key, cache.params(), proceedingJoinPoint.getArgs()); // 生成新的 key
                return key;
            }
        }
        ```
    *   **`getAnnotationInfo` 方法**：
        ```java
        protected AnnotationInfo<Cache> getAnnotationInfo(ProceedingJoinPoint proceedingJoinPoint, Cache cache) {
            AnnotationInfo<Cache> annotationInfo = new AnnotationInfo<>();
            annotationInfo.setAnnotation(cache);
            annotationInfo.setRegion(cache.region());
            try {
                annotationInfo.setKey(generateKey(proceedingJoinPoint, cache));
            } catch (Exception e) {
                e.printStackTrace();
            }
            return annotationInfo;
        }
        ```
    *   **`getProcessor` 方法**：
        ```java
        public static CachesAnnotationProcessor getProcessor(ProceedingJoinPoint proceedingJoinPoint, Cache cache) {
            return new CachesAnnotationProcessor(proceedingJoinPoint, cache);
        }

        public static CacheEvictorAnnotationProcessor getProcessor(ProceedingJoinPoint proceedingJoinPoint, CacheEvictor cacheEvictor) {
            return new CacheEvictorAnnotationProcessor(proceedingJoinPoint, cacheEvictor);
        }
        ```
    *   **`AbstractCacheAnnotationProcessor` 构造函数**：
        ```java
        public AbstractCacheAnnotationProcessor() {
            ApplicationContext applicationContext = SpringApplicationContextUtils.getApplicationContext();
            cacheChannel = applicationContext.getBean(CacheChannel.class);
        }
        ```

*   **关键概念**：
    *   `ProceedingJoinPoint`：AOP 中的连接点，用于获取目标方法的执行信息。
    *   `Cache` 和 `CacheEvictor`：Spring 缓存注解，分别用于缓存和清除缓存。
    *   `AnnotationInfo`：一个自定义类，用于封装注解的属性信息。
    *   `CacheKeyBuilder`：一个工具类，用于生成缓存键。
    *   `CacheChannel`：一个接口或类，用于处理缓存操作。

---

### 4) 关键场景与演示描述

*   **场景 1：展示缓存方法** (00:00-00:05)
    *   讲师在 IDE 中打开了 `JCacheController.java` 文件，高亮显示了两个缓存方法 `getCacheDataBody` 和 `getCacheDataParams`。
    *   通过注释说明，这两个方法用于演示缓存功能，其中 `getCacheDataBody` 方法的 `key` 是 `user`，`getCacheDataParams` 方法的 `key` 是 `rx`。
    *   讲师强调，这两个方法在实际应用中会用于查询数据库并返回数据。

*   **场景 2：讲解 `getProcessor` 方法** (00:15-00:25)
    *   讲师将光标移动到 `AbstractCacheAnnotationProcessor.java` 文件中的 `getProcessor` 方法。
    *   通过 IDE 的自动补全功能，讲师演示了如何根据传入的 `Cache` 或 `CacheEvictor` 注解，返回对应的处理器实例。
    *   讲师解释了 `getProcessor` 方法的作用是获取具体的缓存注解处理器对象。

*   **场景 3：讲解 `generateKey` 方法** (00:25-00:35)
    *   讲师将光标移动到 `generateKey` 方法。
    *   讲师逐行讲解了方法的逻辑：首先获取注解中定义的 `key`，如果 `key` 为空，则根据目标类名和方法名生成新的 `key`。
    *   讲师特别强调了 `CacheKeyBuilder.generateKey` 方法的作用，即根据注解参数和方法参数生成缓存键。

*   **场景 4：讲解 `getAnnotationInfo` 方法** (00:35-00:45)
    *   讲师将光标移动到 `getAnnotationInfo` 方法。
    *   讲师演示了如何将注解的属性（如 `region`）封装到 `AnnotationInfo` 对象中。
    *   讲师强调了 `getAnnotationInfo` 方法的作用是封装注解信息，为后续的缓存操作提供数据。

*   **场景 5：展示 `AbstractCacheAnnotationProcessor` 构造函数** (00:45-00:55)
    *   讲师将光标移动到 `AbstractCacheAnnotationProcessor` 的构造函数。
    *   讲师演示了如何通过 `SpringApplicationContextUtils.getApplicationContext()` 获取 Spring 应用上下文，并通过 `applicationContext.getBean(CacheChannel.class)` 获取 `CacheChannel`。
    *   讲师解释了 `CacheChannel` 的作用是处理缓存操作。

*   **场景 6：展示抽象方法 `process`** (00:55-01:05)
    *   讲师将光标移动到 `process` 方法。
    *   讲师强调了 `process` 方法是所有具体处理器必须实现的核心方法。
    *   讲师指出，`process` 方法的实现逻辑决定了缓存的具体行为。
