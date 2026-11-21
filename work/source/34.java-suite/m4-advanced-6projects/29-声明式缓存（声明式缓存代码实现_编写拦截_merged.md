# 29-声明式缓存（声明式缓存代码实现_编写拦截 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么刚才呢,咱们是定义了这么一个叫做EnableCatch这么一个注解,对吧,用它呢来开启我们声明室这种缓存功能,并且呢我们是在这个启动类上是不是来加入它,然后呢我们也测试了一下,发现什么呢,我们现在定义的这个拦截器,对吧,也就是我们这个CatchMethodInterceptor呢,现在已经可以起作用了。

那接下来呢,我们就需要来完善咱们这两个方法,因为咱们现在呢,其实在这也就是只是说出了一句话,然后就直接放行了,对不对,并没有真正进行缓存相关的操作。

所以接下来呢,我们就需要来完善我们这两个方法,先来看上面这个方法,上面这个方法呢,它是用来拦截什么呢,就是我们这个Catch这种注解的,对吧,如果Controller方法上加了这个注解,就会被拦截到,然后呢就会执行我们当前这个代码。

然后呢,我们来看一下。

这个地方我们主要的这个代码实现的思路是什么呢,就是从我们这个连接点呢,先来获得什么呢,我们方法的签名,然后呢,再来获得我们拦截到的Controller的方法。

然后呢,我们再使用工具类呢,把我们方法上加的这个Catch注解给它解析到。

因为什么呢,我们Catch注解里边,咱们是不是定义了Region, Key,还有Parameters啊,我们需要呢,把这三部分信息给它读过来。

所以说呢,咱们需要一步一步来获得这个注解里面的信息。

好,那么首先呢,先从我们这个连接点,是吧,前面我们通过Debug方式也看到了,通过它呢,可以获得很多信息。

那么我们在这儿呢,就可以GetSignature。

然后呢,在这儿的话呢,我们需要给它向下强转一下。

你看它这个Signature呢,它其实是一个什么呢,它其实是一个接口,对吧。

然后呢,我们现在需要转成它的一个实现类。

它的实现类呢,就是这个啊,叫做MethodSignature。

好,给它转成这个,相当于它的一个子接口。

对吧,它的子接口。

好,这个叫做方法签名。

好,来导入一下。

然后呢,强转一下。

然后呢,强转完之后呢,我们就可以通过方法签名呢,来获得什么呢?

我们拦截到的具体是哪个方法,对吧。

这个呢,叫做获得方法签名。

获得方法签名。

这么一个对象,对吧。

然后呢,通过方法签名呢,就可以获得什么呢?

获得我们当前拦截到的。

拦截到的。

这个Controller方法。

方法对象。

注意这个方法呢,是封装成了这么一个Method,对吧。

这么一个方法对象。

然后呢,我们就可以调用什么呢?

这个叫做AnnotationUtils。

注意这个工具类呢,在这个地方。

应该是这个。

我们使用这个Spring提供的这个AnnotationUtils点什么呢?

叫做FindAnnotation。

然后呢,把什么呢?

把咱们这个Method传进去。

然后呢,把这个什么呢?

注解的类型,对吧。

是不是就是我们这个Catch.class。

好。

这样的话呢,我们就能够获得我们这个Catch注解了。

好。

因为有了这个Catch注解之后啊,

咱们是不是就可以去获得什么呢?

它的这个Region啊,还有Key啊,还有Parameters啊,都可以获得到了。

所以说呢,我们在这儿呢,就是动态的去通过,

我们最初的这个连接点,对吧。

然后一步一步把我们这个方法上的这个注解信息给它获取到。

获得什么呢?

这是获得方法上的这个Catch注解信息。

有了这个之后呢,我们就可以获得RegionKey,还有Parameters等等。

但是具体怎么去解析的话呢?

我们可以到后边呢,在我们处理器里面去完成。

现在呢,已经拿到这个注解了,对吧。

具体它这里边这个Region,

还有Key怎么拼接,这个后边再说。

然后呢,我们解析完之后呢,可以在这儿简单判断一下。

Eaf什么呢?

如果说这个Catch啊,如果不等于空,对吧。

不等于空,说明我们确实解析到这个注解了。

那么解析到之后呢,这个时候呢,是不是要进行这个什么呢?

缓存的设置处理。

你看,因为我们加的是这个注解,

而这个注解呢,是不是就是来设置我们的缓存,对吧。

设置缓存。

好,所以说呢,这一块呢,

咱们把它拿过来啊。

那么需要进行什么呢?

设置缓存数据,这么一个处理。

好,然后呢,如果说,

如果说没有,它等于空,对吧。

也就是说没有解析到这个注解。

那这个时候呢,我们是不是就直接放行就可以了。

所以说,如果程序走到这儿的话呢,

那就说明什么呢?

没有获取到这个Catch,

Catch注解信息。

那么直接什么呢?

直接放行。

好,直接放行。

但是这个地方呢,我们如果不等于空的话呢,

只是输出这么一句话,很显然应该是不行的。

那么再往后应该是怎么写呢?

应该就是获得我们具体的这个什么呢?处理器。

哎,你看我们前面是不是也分析了咱们这个思路分析。

哎,那么在我们的拦截器当中来拦截我们Controller的方法,

拦截到之后呢,需要交给具体的处理器来处理。

比如说现在呢,

我们拦截到的是这个Catch注解,对吧?

那么就需要交给这么一个处理器,

叫做Catch annotation processor。

那么我们如果拦截到的是什么呢?

Catch evictor那个注解呢,

就需要交给这个处理器来进行处理。

所以说呢,我们在这个地方呢,就需要干什么呢?

来创建啊,来创建我们这个处理器。

所以在这儿呢,需要来创建我们这个处理器,对吧?

处理器。

哎,具体干什么呢?

具体来处理我们这个缓存逻辑。

怎么将数据载入缓存,对吧?

那么应该是进行这样的处理。

处理完之后呢,是不是再来进行返回。

因为这个地方呢,是不是也是需要返回的,

返回个object的对象。

那这个地方具体应该是获得哪个处理器呢?

注意,咱们在这儿直接去new这么一个,

new这么一个processor呢,当然是可以的。

但是呢,我们这个地方呢,

不希望让它们之间这个偶合性这么强。

咱们怎么做呢?

我们呢,可以在这个抽象类里面,

我们先创建一个抽象类。

然后呢,在抽象类里面,

帮我们去创建出来对应的对象。

这样的话呢,相当于什么呢?

我们这个拦截器,

跟咱们具体的这个处理器呢,就结偶了。

它们不再直接偶合,

而是跟这个什么呢,抽象类来进行偶合。

而抽象类相对来说呢,

它就有点类似于接口,对吧?

它定义的是一些规范性的东西。

所以说呢,相对来说是比较稳定的。

所以说呢,我们在这个地方呢,

我们这个拦截器,

直接去跟我们这个什么呢,

处理器进行偶合。

所以我们在这个地方呢,

就需要干什么呢?

通过我们这个什么呢,抽象,

这个抽象的处理器来获得一下。

所以说呢,我们需要在这儿呢,

先来创建一个什么呢,抽象的这个处理器。

那么咱们在这个地方呢,来创建一个,

看看它在哪个包下边啊?

抽象的。

在这个processor,这个包下边。

那么我们在这儿来创建一层包。

咱们这个地方呢,一共是涉及到了三个处理器,对吧?

前面我们也说了,一个是抽象的,就是这个。

还有就是两个具体的。

然后呢,我们在这儿来创建一下。

就这个,AppStructCatchAnnotationProcessor。

这个是抽象的。

抽象什么呢?缓存,注解,处理器。

然后咱们在这里边干什么呢?

我们呢,先来提供一个方法。

这个方法呢,就定义成静态方法就可以。

然后它的作用就是什么呢?

返回一个具体的处理器。

返回一个具体的处理器。

而这个具体的处理器呢,就是我们刚才看到的这个。

所以说呢,我先把这个类创建出来。

具体这里边,这个类里边有哪些属性,有什么方法。

一会儿我们再逐渐的去完善它。

所以我们先把所需要的这些类呢,先创建好。

你看这个叫做CatchAnnotationProcessor。

然后这个类呢,是干什么用的呢?

就是缓存注解处理器,对吧?

OK。

然后呢,咱们在这个抽象类里边呢,是不是来提供一个什么呢?

静态方法。

而这个静态方法呢,就是返回这么一个处理器对象。

Public, Static。

然后呢,返回值呢,是不是就是我们这个CatchAnnotationProcessor。

就是这个。

咱们就叫GetProcessor吧。

然后呢,Get的时候呢,我们需要干什么呢?

给它传一些参数进来,来看一下。

需要传这么两个参数,对吧?

一个是什么呢?一个是咱们这个连接点对象,对吧?

还有一个呢,就是我们解析到的这个注解。

解析到的这个注解对象。

所以说呢,我们在这个地方呢,需要给它提供这么两个参数。

一个叫做ProceedingJoinPoint,还有一个就是这个注解。

先给它引入一下。

ProceedingJoinPoint。

还有一个呢,就是这个Catch注解。

Catch注解。

然后在这个地方呢,我们是不是直接把这个对象呢,给它Nu出来就可以了。

直接Return什么呢?

Nu一个,这个叫做CatchAnnotationProcessor。

OK,那么就是这么一个效果。

这个呢,就是获得什么呢?

这个是获得。

获得我们具体的一个什么呢?缓存注解这么一个处理器对象。

那么有了这个静态方法之后呢,咱们在这个地方呢,是不是就可以直接干什么呢?

去调用这个AbstractCatchAnnotationProcessor,对吧?

然后呢,点GetProcessor。

然后呢,把我们这个连接点对象,还有我们这个Catch注解对象传进去。

然后呢,就可以返回这么一个Processor。

对吧?就可以返回一个Processor。

然后返回这个Processor之后啊,怎么做呢?是不是就应该是具体的处理。

对吧?具体的处理。

所以后边呢,我们需要在咱们这个什么呢?Processor里边来提供一个Process方法。

就是具体它的处理的逻辑。

具体的这个缓存处理的逻辑,应该封装在这个Process方法里面。

所以我们先把这个大体的结构啊,所需要的这些方法,空架子给搭起来。

就是这么一个方法。

你看,叫做Process。

然后呢,我们可以把这个方法呢,给它来创建一下。

叫做Process。

在这儿。

对吧?

那么它需要传一个什么呢?传一个这个ProceedingJoinPoint。

这就是具体的处理逻辑。

然后呢,找到我们这个Processor。

在这里边呢,给它提供这么一个方法。

对吧?咱们在这儿呢,先来一个这个ProceedingJoinPoint。

点什么呢?这个具体怎么处理呢?

具体怎么处理呢?具体怎么处理呢?咱们先来一个Now吧。

因为这里边的处理逻辑呢,其实还是挺复杂的,挺复杂的。

所以我们一会儿呢,再去完善这个方法。

咱们就需要把这个架子搭起来先。

这是具体的这个具体缓存处理逻辑。

那么在这个方法里边。

好,那么现在呢,假设我们这个方法已经有了,对吧?已经写好了。

然后呢,在我们拦截器这边呢,我就可以干什么呢?直接return什么呢?

这个Processor.Process方法。

然后呢,把我们这个连接点对象传进去。

直接返回就可以了。

好,那么大概呢,就是这么一个套路。

现在呢,我们先不管什么呢?先不管具体它这边怎么处理,对吧?

然后呢,这边怎么获得的。

那么我们先把当前我们这个什么的拦截器给它搞定了,对吧?

先把这个方法给它一次性给它完善了。

好。

大概呢,再来读一下这个逻辑啊。

首先呢,我们是通过这个连接点对象。

对吧?来get这个signature。

这就是我们方法签名。

然后呢,通过它呢,获得message。

这就是我们拦截到的那个control的方法。

好,然后呢,接下来呢,我们可以调用我们这个Spring啊。

这是Spring给咱们提供的这么一个工具类。

对吧?看这个名字也能知道annotation utils。

是不是就是专门用来解析注解的。

好,然后呢,我们直接调用它的这个find annotation。

然后呢,把这个方法对象传进去。

然后呢,把这个类型传进去。

它就可以到这个方法上去给我们解析这种东西。

这种类型。对吧?

然后呢,如果有的话呢,就能解析出来。

好,然后我们判断它如果不等于空。

不等于空的话呢,我们就可以获得具体的一个缓存的处理器。

然后调用它的处理逻辑。

然后具体的处理逻辑,一会儿我们需要在这里面来写。

对吧?然后呢,如果说它等于空。

对吧?等于空呢,那这个if不成立。

不成立的话呢,这个呢,是不是就是相当于是直接放行了。

直接放行。OK。

这是咱们这第一个这个方法。

一会儿呢,我们再来玩一下。

完善下边。

这个方法,也就是当我们拦截到的是这种注解的时候。

对吧?这个地方,这个处理逻辑,一会儿再来说。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一个关于 Spring 框架中 **JCache 缓存注解实现原理** 的技术讲解。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何自定义一个缓存注解处理器，以实现对 `@Cache` 和 `@CacheEvict` 注解的拦截和处理。核心内容包括：
*   **项目结构**：展示了一个基于 Spring Boot 的项目，其中包含 `UserApplication` 启动类和 `CacheMethodInterceptor` 拦截器。
*   **注解定义**：自定义了 `@Cache` 注解，包含 `region`, `key`, `params` 等默认属性。
*   **拦截器实现**：编写了 `CacheMethodInterceptor` 类，使用 `@Around` 切面注解来拦截带有 `@Cache` 注解的方法。
*   **处理器抽象**：定义了 `AbstractCacheAnnotationProcessor` 抽象类，用于处理缓存逻辑。
*   **处理器实现**：实现了 `CachesAnnotationProcessor` 类，负责具体的缓存读取和写入逻辑。
*   **核心流程**：演示了从注解解析、处理器创建到最终执行缓存操作的完整流程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 项目启动与主类展示。讲师展示了 `UserApplication.java` 的 `main` 方法，用于启动 Spring Boot 应用。
*   **00:05 - 00:10**: 拦截器类 `CacheMethodInterceptor.java` 的初步展示。讲师介绍了该类的作用是拦截带有缓存注解的方法。
*   **00:10 - 00:15**: `@Around` 注解的使用。讲师在 `CacheMethodInterceptor` 中使用 `@Around` 注解来定义环绕通知。
*   **00:15 - 00:20**: 获取方法签名。讲师演示了如何通过 `MethodSignature` 获取被拦截方法的签名信息。
*   **00:20 - 00:25**: 获取注解信息。讲师演示了如何通过 `AnnotationUtils.findAnnotation` 方法获取方法上的 `@Cache` 注解。
*   **00:25 - 00:30**: 判断注解是否存在。讲师演示了如何判断是否获取到了 `@Cache` 注解，并打印日志。
*   **00:30 - 00:35**: 创建处理器。讲师演示了如何通过 `AbstractCacheAnnotationProcessor.getProcessor` 方法获取具体的缓存处理器。
*   **00:35 - 00:40**: 处理器执行。讲师演示了如何调用处理器的 `process` 方法来执行缓存逻辑。
*   **00:40 - 00:45**: 未找到注解的处理。讲师演示了如果没有找到 `@Cache` 注解，直接执行原方法。
*   **00:45 - 00:50**: 自定义注解 `@Cache` 的定义。讲师展示了自定义注解 `@Cache` 的代码，包含 `region`, `key`, `params` 等属性。
*   **00:50 - 00:55**: 抽象处理器 `AbstractCacheAnnotationProcessor` 的定义。讲师展示了抽象类 `AbstractCacheAnnotationProcessor` 的结构。
*   **00:55 - 01:00**: 具体处理器 `CachesAnnotationProcessor` 的实现。讲师展示了 `CachesAnnotationProcessor` 类的实现，包含缓存读取和写入逻辑。
*   **01:00 - 01:05**: 项目结构与文档。讲师展示了项目的整体结构和相关的文档。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1: `UserApplication.java`**
    ```java
    @SpringBootApplication
    @EnableDiscoveryClient
    @EnableSwagger2
    @EnableCache // 开启声明式缓存功能
    public class UserApplication {
        public static void main(String[] args) {
            SpringApplication.run(UserApplication.class, args);
        }
    }
    ```

*   **代码片段 2: `CacheMethodInterceptor.java`**
    ```java
    @Around("@annotation(com.iteima.j2cache.annotation.Cache)")
    public Object invokeCacheAllMethod(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        MethodSignature signature = (MethodSignature) proceedingJoinPoint.getSignature();
        Method method = signature.getMethod();
        Cache cache = AnnotationUtils.findAnnotation(method, Cache.class);
        if (cache != null) {
            System.out.println("需要进行设置缓存数据处理...");
            CachesAnnotationProcessor processor = AbstractCacheAnnotationProcessor.getProcessor(proceedingJoinPoint, cache);
            return processor.process(proceedingJoinPoint);
        }
        return proceedingJoinPoint.proceed(proceedingJoinPoint.getArgs());
    }
    ```

*   **代码片段 3: `Cache.java` (自定义注解)**
    ```java
    package com.iteima.j2cache.annotation;

    import java.lang.annotation.*;

    /**
     * 缓存注解
     */
    @Documented
    @Target(ElementType.METHOD)
    @Retention(RetentionPolicy.RUNTIME)
    public @interface Cache {
        String region() default "rx";
        String key() default "";
        String params() default "";
    }
    ```

*   **代码片段 4: `AbstractCacheAnnotationProcessor.java`**
    ```java
    package com.iteima.j2cache.aop.processor;

    /**
     * 抽象缓存注解处理器
     */
    public class AbstractCacheAnnotationProcessor {
        public static CachesAnnotationProcessor getProcessor(ProceedingJoinPoint proceedingJoinPoint, Cache cache) {
            // 实现获取具体处理器的逻辑
            return new CachesAnnotationProcessor(proceedingJoinPoint, cache);
        }
    }
    ```

*   **代码片段 5: `CachesAnnotationProcessor.java`**
    ```java
    public Object process(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        Object result = null;
        boolean readcache = false;
        CacheHolder cacheHolder = getCache(proceedingJoinPoint, annotationInfo);
        if (cacheHolder.hasError() && cacheHolder.isExistsCache()) {
            if (result == null) {
                readcache = true;
            }
        }
        if (readcache) {
            result = doInvoke(proceedingJoinPoint);
        }
        return result;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 项目启动与主类展示 (00:00-00:05)**
    讲师在 IntelliJ IDEA 中打开了 `UserApplication.java` 文件，展示了 `main` 方法。通过点击“Run”按钮，成功启动了 Spring Boot 应用，终端显示“Compilation completed successfully”。

*   **场景 2: 拦截器类 `CacheMethodInterceptor.java` 的实现 (00:05-00:15)**
    讲师在 `CacheMethodInterceptor.java` 文件中，使用 `@Around` 注解定义了一个环绕通知。该通知会拦截所有带有 `@Cache` 注解的方法。

*   **场景 3: 获取方法签名与注解信息 (00:15-00:25)**
    讲师通过 `MethodSignature` 获取了被拦截方法的签名信息，并通过 `AnnotationUtils.findAnnotation` 方法获取了方法上的 `@Cache` 注解。如果注解存在，则执行缓存处理逻辑。

*   **场景 4: 创建处理器并执行 (00:25-00:35)**
    讲师演示了如何通过 `AbstractCacheAnnotationProcessor.getProcessor` 方法获取具体的缓存处理器，并调用其 `process` 方法来执行缓存逻辑。

*   **场景 5: 自定义注解 `@Cache` 的定义 (00:45-00:50)**
    讲师展示了自定义注解 `@Cache` 的代码，该注解包含 `region`, `key`, `params` 等属性，用于指定缓存的区域、键和参数。

*   **场景 6: 抽象处理器 `AbstractCacheAnnotationProcessor` 的定义 (00:50-00:55)**
    讲师展示了抽象类 `AbstractCacheAnnotationProcessor`，该类负责获取具体的缓存处理器。

*   **场景 7: 具体处理器 `CachesAnnotationProcessor` 的实现 (00:55-01:00)**
    讲师展示了 `CachesAnnotationProcessor` 类的实现，该类负责具体的缓存读取和写入逻辑。

*   **场景 8: 项目结构与文档 (01:00-01:05)**
    讲师展示了项目的整体结构和相关的文档，包括 `pd-user` 模块的目录结构和 `md` 格式的文档。

---

以上是根据视频画面进行的结构化技术分析。
