# 40-声明式缓存（声明式缓存代码实现_编写清理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们这个清理缓存的这个处理器。

刚才呢,我们是把这个构造方法已经写完了,那接下来呢,我们来写最后一个啊,就是这个process,就是具体清理我们缓存数据的这个逻辑,对吧。

那么这个清理起来其实比较简单啊,我们直接调用什么呢,evict的方法,cat channel的evict的方法就可以了。

只不过呢,这块呢,我们有可能是一次要清理多个缓存数据,因为什么呢,咱们这个evict的这个注解里边,你看我是不是可以配置多个catch。

所以说呢,我们需要去遍历一下什么呢,咱们这个list的集合,对吧。

所以我们在这呢,来遍历一下它。

要清理的话呢,我们是不是需要知道region还有key,所以我们通过这个annotation info可以获得region。

这个呢,前面咱们已经分析过了。

在我们构造方法这里边,其实就已经把它是不是给创建好了。

这里边都已经封装好了,所以在这呢,直接用就可以了。

annotation info.get什么呢,key。

然后呢,我们就可以调用这个什么呢,catch channel对象,对吧。

然后它的这个什么呢,evict的方法,把region传进去,把key传进去。

这样呢,就可以来清理缓存数据。

清理缓存数据。

那么清理完之后呢,我们需要注意啊。

这个地方呢,我们还不可以,

必须要调用我们真正的目标方法。

因为一般情况下呢,我们这个缓存数据呢,跟咱们数据库里面的数据是保持一致的。

就是我们清理完之后呢,一般还会操作数据库。

比如说我们这个地方,对吧。

我在这里边呢,可能就需要来删除数据库里面的数据。

也就是说,我们清理完缓存之后呢,必须要放行,真正执行到我们真正的这个目标方法。

然后在这里边,它是不是可能会调service,service调dao,然后最终删数据库。

所以说,

我们可以调用这个方法。

它这是我们清理缓存呢,跟这个设置缓存,或者获取缓存,那么不同的地方。

比如说我们前面测试的这个,

detail,对吧。

刚才我们测试的是这个方法。

那这个方法呢,是我们第一次调这个方法的时候,没有缓存数据,它会走这个方法。

当我们第二次再调这个方法的时候呢,因为缓存里面已经有数据了,所以这个方法其实就没有执行,对吧。

没有调用到我们真正的这个目标方法。

而我们清理缓存呢,是每一次你

清理,我们这个目标方法都要执行。

目标方法都要执行,因为它可能需要去修改数据库,对吧。

所以我们这个地方呢,处理完之后呢,一定要进行这个什么呢,放行,来调用什么呢?

调用我们这个目标方法。

所谓的目标方法,我已经强调过多次了,就是什么呢?就是我们controller,

controller当中的这个方法。

好。

就当前我们真正要访问的,controller的方法。

好,那么怎么放行呢?咱们是不是通过连接点,

这个对象,调用他的proceed的方法,对吧。

然后呢,把他这个参数呢,给他传进去。

好。

这样的话呢,这就表示放行了,调用到我们目标方法了。

好,这是咱们这个process这个方法,

它的主要的处理逻辑,就这么两个,一个是清理数据,一个是调用目标方法。

好,那么到这儿的话呢,我们这个,

当前的这个清理缓存数据的这个处理器呢,就已经写完了。

一会儿呢,我们也来测试一下。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频是一节关于 Spring 框架中 `@CacheEvict` 注解的自定义注解处理器（Annotation Processor）的开发教程。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何创建一个自定义的 `CacheEvictAnnotationProcessor` 类，该类继承自 `AbstractCacheAnnotationProcessor`。其核心功能是：在编译时扫描带有 `@CacheEvict` 注解的方法，并在运行时（通过 AOP）调用 `CacheChannel` 的 `evict` 方法来清除指定缓存区域和键的缓存数据。视频重点讲解了处理器的初始化逻辑、如何解析注解信息、以及如何在目标方法执行前调用缓存清除操作。整个过程旨在展示如何通过自定义注解处理器来实现对 Spring 缓存机制的深度定制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**: 视频开场，展示项目结构和 `CacheEvictAnnotationProcessor.java` 文件的初始状态。
*   **00:16 - 00:40**: 讲师讲解 `CacheEvictAnnotationProcessor` 类的构造函数，说明其作用是初始化 `proceedingJoinPoint` 和 `cacheEvictor` 对象，并遍历 `@CacheEvict` 注解的值，将每个注解信息存入 `cacheList` 列表。
*   **00:41 - 01:00**: 讲师将光标移动到 `process` 方法，开始讲解核心的缓存清除逻辑。该方法接收 `proceedingJoinPoint` 参数，用于在目标方法执行前进行操作。
*   **01:01 - 01:20**: 讲师在 `process` 方法中遍历 `cacheList`，从每个 `AnnotationInfo<Cache>` 对象中提取 `region` 和 `key`。
*   **01:21 - 01:35**: 讲师演示如何调用 `cacheChannel.evict(region, key)` 方法来实际清除缓存。
*   **01:36 - 01:50**: 讲师在 `process` 方法末尾添加注释，说明下一步是调用目标方法。
*   **01:51 - 02:00**: 讲师将光标移动到 `return` 语句，并演示如何调用 `proceedingJoinPoint.proceed()` 来执行原始方法。
*   **02:01 - 02:15**: 讲师回顾了整个处理器的逻辑，强调其在编译时收集注解信息，在运行时执行缓存清除操作。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **类定义**:
        ```java
        public class CacheEvictAnnotationProcessor extends AbstractCacheAnnotationProcessor {
        ```
    *   **成员变量**:
        ```java
        private List<AnnotationInfo<Cache>> cacheList = new ArrayList<>();
        ```
    *   **构造函数**:
        ```java
        public CacheEvictAnnotationProcessor(ProceedingJoinPoint proceedingJoinPoint, CacheEvictor cacheEvictor) {
            super();
            Cache[] value = cacheEvictor.value();
            for (Cache cache : value) {
                AnnotationInfo<Cache> annotationInfo = getAnnotationInfo(proceedingJoinPoint, cache);
                cacheList.add(annotationInfo);
            }
        }
        ```
    *   **核心处理方法**:
        ```java
        public Object process(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
            for (AnnotationInfo<Cache> annotationInfo : cacheList) {
                String region = annotationInfo.getRegion();
                String key = annotationInfo.getKey();
                cacheChannel.evict(region, key);
            }
            // 调用目标方法
            return proceedingJoinPoint.proceed(proceedingJoinPoint);
        }
        ```
    *   **注解处理器的注释**:
        ```java
        /**
         * 具体清理缓存处理逻辑
         * @param proceedingJoinPoint
         * @return
         * @throws Throwable
         */
        ```

---

### 4) 关键场景与演示描述

*   **场景一：初始化处理器** (00:16-00:40)
    *   讲师在 IDE 中定位到 `CacheEvictAnnotationProcessor` 类。
    *   他逐行讲解构造函数，说明 `super()` 调用父类构造函数，`cacheEvictor.value()` 获取注解的值数组，然后通过 `for` 循环遍历每个 `Cache` 对象，调用 `getAnnotationInfo` 方法获取注解信息并添加到 `cacheList` 中。
    *   他强调了 `cacheList` 的作用是存储所有需要处理的注解信息。

*   **场景二：实现缓存清除逻辑** (00:41-01:35)
    *   讲师将光标移动到 `process` 方法。
    *   他解释了 `process` 方法的作用是在目标方法执行前执行缓存清除。
    *   他演示了如何遍历 `cacheList`，并从每个 `AnnotationInfo<Cache>` 对象中提取 `region` 和 `key`。
    *   他演示了如何调用 `cacheChannel.evict(region, key)` 方法来清除缓存。

*   **场景三：调用目标方法** (01:36-02:00)
    *   讲师在 `process` 方法末尾添加了注释“调用目标方法”。
    *   他演示了如何调用 `proceedingJoinPoint.proceed(proceedingJoinPoint)` 来执行原始方法。
    *   他强调了 `return` 语句的作用是将目标方法的返回值返回给调用者。

*   **场景四：总结与回顾** (02:01-02:15)
    *   讲师总结了整个处理器的逻辑：在编译时收集注解信息，在运行时执行缓存清除操作。
    *   他强调了自定义注解处理器的强大功能，可以实现对 Spring 缓存机制的深度定制。
