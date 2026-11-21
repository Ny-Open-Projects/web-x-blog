# 30-声明式缓存（声明式缓存代码实现_编写拦截 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来编写我们这个catch method interceptor,也就是我们这个拦截器。

刚才呢,我们是把第一个方法,也就是处理这种什么呢,加了catch注解的这种情况,那么具体的处理逻辑呢,刚才已经说过了。

然后接下来呢,我们来看下一个,下一个也就是当我们这个拦截到的是这个catch evict注解的时候,应该是走下面这个方法,对吧。

那么具体这块怎么处理呢,其实跟上面这块呢,是非常类似的。

也就是说,我们首先呢,还是先通过这个连接点,干什么呢,来获得我们的方法签名,来获得方法签名。

好,然后呢,把这个呢,还是改成这个什么呢,method,finger nature,对吧。

然后呢,给它向下转一下,转完之后呢,来获得什么呢,我们这个方法对象,对吧,method的对象。

然后接下来呢,还是通过我们这个annotation,util私点,什么呢,find。

然后呢,把这个方法对象传进去,然后呢,把我们要解析的这种类型,注解的类型,是不是叫做catch evict,对吧,把它传进去。

然后呢,把我们这个注解给解析到。

同样的,还是再来判断一下什么呢,它是否等于空,对吧。

也就是catch evict,如果不等于空,不等于空的话呢,说明确实解析到它了。

那么有这个注解的话呢,我们是不是就需要来进行什么呢?

进行这个切换。

进行这个切换。

进行这个切换。

清理缓存处理。

对吧,因为这个缓存,这个注解啊,我们给它起的作用应该就是清理缓存。

清理缓存处理。

同样呢,这个地方呢,我们是不是也需要来进行什么呢?

创建我们这个具体的处理器,对吧。

也就是跟我们上面这种情况是类似的啊,也是需要创建一个具体的处理器。

所以我们在这个地方呢,需要来创建清理缓存的这个处理器。

好,而这个处理器的话呢,还是通过咱们这个什么呢,抽象类来创建。

好,就是这个,叫做AbstractCatchAnnotationProcessor,对吧。

然后呢,我们可以把这个代码呢,给它复制一下,稍微改造一下就可以。

好,稍微改造一下。

然后呢,这个呢,要返回的是不是应该就是我们这个处理器了啊。

来看一下,应该就是这个,叫做CatchEvakedAnnotationProcessor。

好,这个处理器。

现在呢,我们这个处理器还没有,咱们需要先把它创建出来。

好,把这个类先创建出来。

这个是清理缓存数据,这么一个处理器。

好,然后呢,有了它之后呢,咱们就可以在这儿来直接把这个类型改成CatchEvakedAnnotationProcessor,对吧。

然后呢,这个地方传进来的这个注解呢,是不是应该就是我们这个CatchEvaked,这种注解了。

CatchEvaked,好,这种注解。

然后这个地方呢,我们是不是直接返回什么呢?

直接返回的应该就是它了。

好,这个就不要了。

OK。

这个地方呢,给它改统一了。

这儿。

获得什么呢?

这个应该是清理缓存,对吧。

清理缓存,这么一个注解处理器。

然后呢,我们这个静态方法搞定之后呢,咱们再回到这边来。

我们就可以直接来调用咱们这个抽象类,这个负类,对吧。

AppStriket。

AppStriket,CatchAnnotationProcessor.getProcessor。

你看啊,这两个方法明明是相同的,但是传的参数不一样,对吧。

然后呢,这个也是把这个ProceedingJoinPoint传进去。

然后还有就是我们这个CatchEvaked。

这样的话呢,我们就已经获得了这个什么呢?

Processor对象。

然后呢,具体进行处理。

咱们是不是也是需要在这里边来提供一个什么呢?处理的方法,对吧。

Process方法。

Process方法,我们可以从这边来。

先简单烤一下。

Ctrl-C。

然后呢,把它拿到这边来。

粘贴一下。

具体这个清理缓存,对吧。

这个叫做清理缓存,它的这个处理逻辑。

还是先让这个方法空着。

然后呢,我们在这边呢,就可以直接干什么呢?去调用它了。

直接return,它这个反位置,Processor点,什么了,Process。

把这个什么呢,连接点对象,传进去。

然后我们在这个地方呢,我们可以直接连接到这个方法。

这个地方呢,可以简单来说一下。

就是说我们这个地方,为什么这个Process方法必须要传一个连接点这个对象进来啊?

就是因为我们在这个方法里边,有可能需要去放行,去调我们真正的那个目标Controller的方法。

比如说我们现在呢,这个清理缓存,对吧。

我们在这儿呢,可能需要调用这个什么Catch Channel。

我们调用Evade方法,或者Clear方法,对吧。

清理缓存。

清理完之后呢,我们真正的那个Controller方法呢,可能需要去删除这个库的数据,对吧。

所以说呢,我们在这儿呢,还是需要去通过反射去调我们真正的那个Controller方法。

所以说呢,我们在这儿呢,传一个连接点对象进来。

然后到时候我们想放行的时候呢,是不是就是通过它调用它的Proceed方法。

这样呢,就调用到我们真正的目标方法了。

大家明白这个意思吧?

这就是为什么我们必须要传一个连接点,这么一个对象进来。

好。

包括我们这个,

Catch Annotation。

这个地方呢,这个Processor,你看,我们在这儿呢,要进行这个缓存处理。

那么它在第一次调用这个方法的时候,有可能我们这个J2Catch当中是没有缓存的。

那么没有缓存的话呢,咱们是不是就需要去放行,去调我们真正的那个目标方法,对吧。

Controller里边那个方法。

然后呢,把那个方法调用完之后,它会给我们返回结果。

并且呢,我们再把这个结果给它缓存起来。

等下一次再调的时候呢,我们是不是就直接从那个缓存里面来取。

然后呢,就不再去调什么呢,真正的目标方法了。

所以说呢,我们在这个地方,在第一次调的时候,没有缓存的时候呢,也是会通过这个Join Point调用到我们真正目标方法。

然后呢,有可能去查数据库,对吧。

把这个数据给它获取到。

好。

所以说呢,我们这个地方就是解释了一下,为什么必须要传这么一个参数进来。

然后呢,我们再来看一下。

大家可以看到我们这两个类啊,这两个具体的处理类呢,是不是都有这么一个Process方法。

对吧。

哎。那这样吧。

这样的话呢,我们其实就可以往上提一层,就是什么呢。

在咱们这个抽象类,哎,这是它的负类,对吧。

哎,你看它下面有这两个子类。

好。

也就是说,我们需要让这两个类呢,继承我们这个负类。

继承我们这个AbstractCatAnnotationProcessor。

包括另外一个,也是需要继承的。

好。

Extents继承。

那么继承之后啊。

继承之后呢。

咱们这两个类里边呢,是不是都有Process方法。

这样的话呢,我们就可以再往上提一层,对吧。

就是在我们这个抽象的负类里边,来提供一个什么呢,抽象的方法。

然后呢,这两个子类呢,具体去实现这两个方法。

哎。

那么这个Process就是处理。

因为不管你是清理缓存,还是设置缓存,或者查询缓存。

那么都是需要进行处理的。

所以这个方法呢,我们就可以给它往上提一层。

提成一个负类的抽象方法。

这是我们一般框架都是这样来玩的。

所以我们在这儿呢,再往上提一层。

但是这个呢,需要给它改成一个什么呢,Abstract。

好。

OK。

然后呢,这样的话,我们这个类呢。

呃。

这个来检查一下,看看Abstract Public Object Process。

这个有什么问题吗?

然后呢,我们这个是具体去。

哦,我这儿定义了个Abstract的。

那我这个类呢,也必须是一个Abstract。

OK。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

好。

要不然的话,它这个地方呢,它不允许我们定义抽象方法。

是这样的啊。

然后呢,把这个地方呢,改成Abstract的。

这就是表示是一个抽象类。

然后呢,这个就是我们在抽象类里面定义一个抽象方法。

抽象方法。

那么,这是处理什么呢,缓存操作,对吧。

那么具体应该由,哎,什么呢,由这个子类,哎,具体实现。

好。

相当于在我们这个,这就类似于。

接口里边,我定义这么一个规范,对吧。

生命一个方法。

然后呢,它的子类呢,就需要去具体去实现。

哎,因为呢,我们这两个子类呢,处理方式不一样。

一个是清理,一个是设置。

当然设置的时候呢,也会去第一次是设置,第二次是查询,对吧。

哎,也就是处理方式不一样。

那么,但是呢,它们都需要去实现这个方法,Process方法。

好。

到这儿的话呢,咱们回过头来,再来看一下我们这个拦截器。

当然同时它又是一个切面,对吧。

然后这个类呢,就已经完善好了。

好。

然后后边的话呢,我们就需要来具体去看什么呢。

另外这三个类。

一个是这个抽象的负类。

还有就是两个具体的处理子类。

好。

那么关于咱们这个拦截器呢,我们到这儿就已经全都完成了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 Spring Cache 框架中 `@CacheEvict` 注解的实现原理与源码分析。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何编写一个自定义的缓存清除拦截器 `CacheEvictAnnotationProcessor`，并将其与框架的 `AbstractCacheAnnotationProcessor` 基类集成。核心内容包括：
- **分析 `@CacheEvict` 注解的拦截逻辑**：通过 `@Around` 切面，获取方法上的注解信息。
- **动态创建处理器**：根据注解类型（`Cache` 或 `CacheEvict`），调用 `AbstractCacheAnnotationProcessor.getProcessor()` 方法获取具体的处理器实例。
- **实现处理器**：编写 `CacheEvictAnnotationProcessor` 类，继承自 `AbstractCacheAnnotationProcessor`，并实现 `process(ProceedingJoinPoint)` 方法，用于执行具体的缓存清除逻辑。
- **代码演示**：通过在 `CacheMethodInterceptor` 中调用 `getProcessor()` 方法，并展示如何将 `CacheEvict` 注解与 `Cache` 注解的处理器区分开来。

整个过程旨在帮助学习者理解 Spring Cache 框架如何通过注解驱动、动态代理和处理器模式来实现缓存的读写与清除功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 展示 `CacheMethodInterceptor` 类中 `invokeCacheEvictAllMethod` 方法的代码，介绍其作用是拦截带有 `@CacheEvict` 注解的方法。
*   **00:10 - 00:25**: 逐步演示如何从方法对象中获取 `@CacheEvict` 注解，并通过 `AnnotationUtils.findAnnotation` 方法获取注解实例。
*   **00:25 - 00:40**: 代码中调用 `AbstractCacheAnnotationProcessor.getProcessor(proceedingJoinPoint, cacheEvictor)` 方法，讲师解释这是获取具体的缓存处理器。
*   **00:40 - 00:55**: 展示 `CacheEvictAnnotationProcessor` 类的创建过程，包括继承 `AbstractCacheAnnotationProcessor` 并实现 `process` 方法。
*   **00:55 - 01:10**: 在 `CacheEvictAnnotationProcessor` 类中，讲师演示了如何实现 `process` 方法，并通过 `@Override` 注解标记，以确保方法签名与父类一致。
*   **01:10 - 01:25**: 展示 `CacheAnnotationProcessor` 类的代码，用于处理 `@Cache` 注解，与 `CacheEvictAnnotationProcessor` 形成对比。
*   **01:25 - 01:40**: 回到 `CacheMethodInterceptor`，讲师总结了 `@CacheEvict` 注解的处理流程：获取注解 -> 创建处理器 -> 执行处理器逻辑。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

*   **`CacheMethodInterceptor.java` 中的 `invokeCacheEvictAllMethod` 方法**：
    ```java
    @Around("@annotation(com.iteima.jcache.annotation.CacheEvict)")
    public Object invokeCacheEvictAllMethod(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        MethodSignature signature = (MethodSignature) proceedingJoinPoint.getSignature();
        Method method = signature.getMethod();
        CacheEvict cacheEvict = AnnotationUtils.findAnnotation(method, CacheEvict.class);
        if (cacheEvict != null) {
            System.out.println("清理缓存处理...");
            AbstractCacheAnnotationProcessor processor = AbstractCacheAnnotationProcessor.getProcessor(proceedingJoinPoint, cacheEvict);
            return processor.process(proceedingJoinPoint);
        }
        return proceedingJoinPoint.proceed(proceedingJoinPoint.getArgs());
    }
    ```

*   **`AbstractCacheAnnotationProcessor.java` 中的 `getProcessor` 方法**：
    ```java
    public static CacheAnnotationProcessor getProcessor(ProceedingJoinPoint proceedingJoinPoint, Cache cache) {
        return new CacheAnnotationProcessor();
    }

    public static CacheEvictAnnotationProcessor getProcessor(ProceedingJoinPoint proceedingJoinPoint, CacheEvict cacheEvict) {
        return new CacheEvictAnnotationProcessor();
    }
    ```

*   **`CacheEvictAnnotationProcessor.java` 类定义**：
    ```java
    public class CacheEvictAnnotationProcessor extends AbstractCacheAnnotationProcessor {
        @Override
        public Object process(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
            return null;
        }
    }
    ```

*   **`CacheAnnotationProcessor.java` 类定义**：
    ```java
    public class CacheAnnotationProcessor extends AbstractCacheAnnotationProcessor {
        @Override
        public Object process(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
            return null;
        }
    }
    ```

#### **关键注解与类**

*   `@CacheEvict`：用于标记需要清除缓存的方法。
*   `@Cache`：用于标记需要读取或写入缓存的方法。
*   `AbstractCacheAnnotationProcessor`：抽象基类，定义了获取处理器的通用逻辑。
*   `CacheAnnotationProcessor`：处理 `@Cache` 注解的处理器。
*   `CacheEvictAnnotationProcessor`：处理 `@CacheEvict` 注解的处理器。
*   `ProceedingJoinPoint`：AOP 中的连接点对象，用于获取方法签名和执行方法。
*   `AnnotationUtils.findAnnotation`：工具类，用于从方法上查找指定的注解。

---

### 4) 关键场景与演示描述

1.  **场景一：拦截 `@CacheEvict` 注解的方法**
    *   讲师在 `CacheMethodInterceptor.java` 文件中，定位到 `invokeCacheEvictAllMethod` 方法。
    *   通过 `@Around` 注解，明确该方法会拦截所有带有 `@CacheEvict` 注解的方法。
    *   代码中通过 `MethodSignature` 和 `getMethod()` 获取方法对象，并使用 `AnnotationUtils.findAnnotation` 获取 `@CacheEvict` 注解实例。

2.  **场景二：动态创建处理器**
    *   讲师演示了如何通过 `AbstractCacheAnnotationProcessor.getProcessor()` 方法动态创建处理器。
    *   根据传入的注解类型（`CacheEvict`），该方法会返回一个 `CacheEvictAnnotationProcessor` 实例。
    *   代码中通过 `if (cacheEvict != null)` 判断，如果找到注解，则创建处理器并调用其 `process` 方法。

3.  **场景三：实现 `CacheEvictAnnotationProcessor`**
    *   讲师在 `CacheEvictAnnotationProcessor.java` 文件中，创建了一个新的类。
    *   该类继承自 `AbstractCacheAnnotationProcessor`。
    *   通过 `@Override` 注解，重写了 `process` 方法，该方法目前返回 `null`，用于占位。
    *   讲师强调，`process` 方法是实际执行缓存清除逻辑的地方，需要后续实现。

4.  **场景四：对比 `@Cache` 与 `@CacheEvict` 处理器**
    *   讲师在 `CacheAnnotationProcessor.java` 文件中，展示了如何处理 `@Cache` 注解。
    *   通过对比，说明 `CacheAnnotationProcessor` 和 `CacheEvictAnnotationProcessor` 的职责不同。
    *   `CacheAnnotationProcessor` 用于处理缓存的读写，而 `CacheEvictAnnotationProcessor` 用于处理缓存的清除。

5.  **场景五：代码调试与编译**
    *   讲师在 IDE 中对代码进行编译，确保没有语法错误。
    *   在 `CacheEvictAnnotationProcessor` 类中，IDE 提示 `process` 方法需要实现父类的抽象方法。
    *   讲师通过 `@Override` 注解，确保方法签名与父类一致，从而通过编译。

通过以上场景，讲师清晰地展示了 Spring Cache 框架中 `@CacheEvict` 注解的实现原理，以及如何通过自定义处理器来扩展其功能。
