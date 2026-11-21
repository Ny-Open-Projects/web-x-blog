# 37-声明式缓存（声明式缓存代码实现_编写缓存 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们这个缓存注解处理器,刚才呢我们是把这个process这个方法呢已经写完了,对吧,那接下来呢我们就需要实现剩余的两个,对吧,一个是get catch这个方法,还有一个呢就是这个set catch,对吧,一个是获取缓存,还有一个是设置缓存,这个invoke方法呢我们刚才也已经写完了,比较简单,它其实就是直接放行,对吧,通过我们这个连接点,这个对象呢直接调用proceed的方法,

这就是调用我们目标方法了,好,然后呢我们先来看这个get catch吧,这个就是获取缓存数据,对吧,那么要获取缓存的话呢我们就需要知道从哪个区域根据哪个key来获取,而这个的话呢咱们是不是在这个annotation info里边已经封装好了,对吧,那么我们先把这个region给它取出来,一会儿需要使用,包括这个什么呢key也需要取出来,好,然后呢我们就可以干什么呢,使用这个catch channel,对吧,然后呢先来判断一下是否存在,

exist,好,然后呢把region还有key是不是传进去,好,然后呢如果它存在的话呢我们就可以来取一下了,存在,if exist等于true,对吧,这个时候呢我们就可以调用catch channel点什么呢get方法,然后呢把region还有什么呢key传进去,好,然后呢返回值呢是一个catch object的对象,对吧,然后通过它呢点get value就可以获得我们缓存的数据,

然后呢这个value

的话呢咱们可以在前面

外边定义一下,定义在这上面,好,然后呢给它一个初始值,这个给它整理一下,对齐一下,然后这儿的话呢就直接给这个value来复制,那么如果是这种情况,这说明我们这个缓存数据存在,对吧,然后呢我把它取出来,把这个value拿到,然后呢我们就可以来封装这个返回结果了,注意咱们是不是返回的是一个catch

这个catch holder这个对象,对吧,那么它这里边呢给我们有这么一样的一个结果,然后呢我们就可以来封装这个返回结果了,注意咱们是不是返回的是一个catch

这个catch holder这个对象,对吧,那么它这里边呢给我们有这么一个方法,叫做,来看一下,叫做new一个result,对吧,获得返回结果,然后呢就是把这个什么呢value,还有这个exist catch,这两个值呢,这两个成员变量给它复号值,然后呢直接返回一个catch holder这么一个对象,所以我们直接调这个静态方法就可以了,就不用咱们自己去new这么一个对象了,好,然后呢我们就可以调用这个catch holder,它的这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个价值,这个�

这个什么呢new result,然后呢把这个value是不是传进去,然后呢因为它是存在的啊,所以这是不是来个true,好,直接呢return就可以了,好,这是存在的情况,对吧,如果不存在了,不存在的话呢,我们也需要把它创建出来,只不过呢就是什么呢,这一块,来看一下,就这一块呢是不是给它改成一个false,改成一个false,就可以了,好,那么最终呢都是一样,

然后呢如果呢它是要返回这么一个结果,不同点是什么呢,它如果走的是if这个分支,那这个时候呢说明是存在的,因为我们在这儿已经判断了,对吧,那这个时候呢,这个地方,第二个值呢给的就是true,而这个value呢是不是就是我们从这儿重新复制的这个value,这就是我们缓存的数据,对吧,这是获得,获得,获得缓存结果数据,好,然后呢如果if不成立,这就说明不存在,对吧,这就说明不存在,不存在的话呢,我们可以再来一个结果,好,这个时候呢,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方,这个地方

我们也是返回这么一个对象,只不过呢,这个时候这个value,它是不是都等于空,然后呢,这个exist catch这个boil类型的这个值呢,给的就是false,好,这是我们获取缓存数据,相对来说呢,也是比较简单的,然后接下来呢,还有最后一个方法,就是set catch,set catch是不是就是设置缓存,对吧,设置缓存,那么我们在这儿呢,就可以通过什么呢,我们这个catchchannel.set直接设置就可以了,

而这个region怎么获得呢,咱们这儿是不是有一个成员变量,这个成员变量,而这个成员变量是什么时候附上值的呢,就是我们调查这个构作方法的时候,对不对,那么大家还记得是在哪儿调的这个构作方法吗,是不是在我们这个abstract的,就是这个抽象附类这个地方,是不是在这儿呢,还new的它,在这个地方new的它,所以说呢,我们在这个地方就会去调用它,那这个时候呢,我们这个annotationInfo呢,其实已经附上值了,

那么具体附的值呢,就是调用这个get annotationInfo这个方法,是不是返回的这个值,好,附给它,所以我们在这儿呢,直接使用这个成员变量就可以获得了,并且呢,这里边呢,已经封装好值了,好,这个是get region,然后呢,我们还需要什么呢,get key,好,然后接下来呢,就是什么呢,具体这个缓存的数据,对吧,缓存的数据我是不是通过这个result已经传进来了,所以把它传进去,OK,就这一句话就搞定了,

那这是我们把这个,

这个get catch从缓存获取数据,还有什么呢,set catch设置缓存数据已经写好了,包括前面invoke呢,也已经写完了,那么到这儿的话呢,咱们整个这个什么呢,缓存注解处理器呢,就都已经写完了,一会儿呢,我们可以来测试一下,来测试一下,看看我们这个缓存处理器啊,到底能不能正常执行。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一个关于 Spring 框架中自定义注解缓存处理机制的编程教学演示。讲师通过 IntelliJ IDEA 开发环境，逐步讲解并实现一个名为 `@Cache` 的自定义注解处理器。该处理器的核心功能是：在方法执行前，先检查缓存中是否存在对应结果；如果存在，则直接返回缓存数据，避免重复计算；如果不存在，则执行目标方法，并将返回结果存入缓存，供后续调用复用。整个过程通过 `CacheAnnotationProcessor` 类实现，它继承自 `AbstractCacheAnnotationProcessor`，并利用 `CacheChannel` 接口进行缓存操作。视频重点展示了代码的逻辑结构、关键方法的实现以及如何通过注解驱动缓存行为。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:01:00**: 视频开场，展示项目结构和 `CacheMethodInterceptor.java` 文件，介绍本节将实现一个缓存注解处理器。
*   **00:01:00 - 00:02:00**: 讲解 `CacheAnnotationProcessor` 类的结构，包括其构造函数和 `process` 方法，用于初始化和处理缓存逻辑。
*   **00:02:00 - 00:03:00**: 详细讲解 `getCache` 方法，用于获取缓存信息（如缓存区域和键），并检查缓存中是否存在数据。
*   **00:03:00 - 00:04:00**: 讲解 `invoke` 方法，用于调用目标方法并获取其返回值。
*   **00:04:00 - 00:05:00**: 讲解 `setCache` 方法，用于将目标方法的返回值存入缓存。
*   **00:05:00 - 00:06:00**: 总结整个缓存处理流程，并演示如何通过 `@Cache` 注解来使用该处理器。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **`CacheAnnotationProcessor` 类的构造函数**:
        ```java
        public CachesAnnotationProcessor(ProceedingJoinPoint proceedingJoinPoint, Cache cache) {
            super();
            annotationInfo = getAnnotationInfo(proceedingJoinPoint, cache);
        }
        ```
    *   **`process` 方法**:
        ```java
        public Object process(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
            Object result = null;
            boolean existsCache = false;
            // ... 缓存逻辑 ...
        }
        ```
    *   **`getCache` 方法**:
        ```java
        private CacheHolder getCache(AnnotationInfo<Cache> annotationInfo) {
            String region = annotationInfo.getRegion();
            String key = annotationInfo.getKey();
            boolean exists = cacheChannel.exists(region, key);
            if (exists) {
                CacheObject cacheObject = cacheChannel.get(region, key);
                Object value = cacheObject.getValue();
                return CacheHolder.newResult(value, existsCache: true);
            }
            return CacheHolder.newResult(null, existsCache: false);
        }
        ```
    *   **`invoke` 方法**:
        ```java
        private Object invoke(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
            return proceedingJoinPoint.proceed(proceedingJoinPoint.getArgs());
        }
        ```
    *   **`setCache` 方法**:
        ```java
        private void setCache(Object result) {
            cacheChannel.set(annotationInfo.getRegion(), annotationInfo.getKey(), result);
        }
        ```
    *   **`CacheChannel` 接口方法**:
        ```java
        boolean exists(String region, String key);
        void set(String region, String key, Object value);
        Object get(String region, String key);
        ```

*   **关键注解**:
    *   `@Cache`：自定义注解，用于标记需要缓存的方法。
    *   `@Cacheable`：Spring 原生注解，用于缓存方法的返回值。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与类定义** (00:00:00 - 00:01:00)
    *   讲师在 IntelliJ IDEA 中展示了项目结构，重点介绍了 `CacheMethodInterceptor.java` 文件。
    *   通过代码高亮，讲师展示了 `CacheAnnotationProcessor` 类的定义，包括其继承关系和构造函数。

*   **场景二：缓存逻辑实现** (00:02:00 - 00:05:00)
    *   讲师逐步演示了 `getCache` 方法的实现，通过 `cacheChannel.exists` 方法检查缓存是否存在。
    *   如果缓存存在，讲师展示了如何通过 `cacheChannel.get` 获取缓存对象，并提取其值。
    *   讲师演示了 `invoke` 方法，用于调用目标方法并获取其返回值。
    *   讲师演示了 `setCache` 方法，用于将目标方法的返回值存入缓存。

*   **场景三：注解驱动缓存** (00:05:00 - 00:06:00)
    *   讲师总结了整个缓存处理流程：先检查缓存，再调用方法，最后存入缓存。
    *   讲师通过代码高亮和注释，展示了如何通过 `@Cache` 注解来使用该处理器。

---

以上是根据视频画面进行的结构化技术分析。
