# 32-声明式缓存（声明式缓存代码实现_编写抽象 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们这个抽象的缓存注解处理器

刚才呢,我们是编写完了这个,叫做get annotation info,对吧,这个方法

那接下来呢,我们就需要来看下一个呢,就是这个generate key这个方法

这个方法呢,就是动态解析注解信息来生成key,对吧,生成我们这个动态的key

好,那么首先呢,我们先从这个catch当中啊,把我们这个controller上面这个注解信息给它取过来

然后呢,把它原始的key给它取到,什么叫做原始的key呢

其实就是我们在这个controller上面加这个注解的时候呢,我们原始设置这个key的值

比如说是ab,对吧,所以说我们这个地方呢,取到的这个值呢,就是ab

好,但是我们这个地方呢,需要来判断更加精确一些,就是什么呢

假设用户他在使用这个注解的时候呢,他没有写这个key这个属性,他是这样来用的

也就是key没有写

对吧,那么没有写的话呢,大家还记得吧,我们当时在定义的时候,给他的默认值是不是一个空串啊,给他一个空串

但是呢,我们这个地方呢,需要来判断一下,如果他是空串的这种情况下呢,我们就需要给他重新来指定一个值

指定成什么呢,我们可以指定成咱们当前这个目标类,也就是我们这个controller这个类名

然后加上一个冒号,再加上这个方法名,这是我们指定的规则

也就是说啊,他如果没有去指定

这个key的话,也就是现在这个key是空串,对吧,那么我们就使用类名加上冒号,再加上方法名

好,所以我们在这呢,先来判断一下,if什么呢,咱们可以通过streamutils这个工具类,点has text,这就含有文本,对吧

含有文本,如果含有文本,我们是不是就不用管他了,所以说我们在这呢,需要取非,加一个探号,这就表示他是空串

也就是说啊,如果当前这个key为什么呢,空串,对吧

那我们就重新设置啊,重新设置当前key为什么呢,就是我们当前的这个目标,controller,然后呢,类名,然后加上一个冒号,然后再加上什么呢,再加上我们这个方法名

好,咱们就使用这个规则

那我这个目标类到底是哪个,我如何获得啊

咱们其实通过这个连接点对象了,就能够获得

通过这个procedure

proceeding,join point,对吧

然后呢,get什么呢,target,这是不是获得目标对象

然后呢,get class,然后再get simple name,这样就获得我们这个简单类名,class name

好,就是不带包名的,好

然后接下来呢,我们再来看啊,方法名,这个方法名呢,前面咱们是不是已经获得过了啊

是通过什么呢,get这个signature,对吧

这个叫做获得方法签名

当然了,我们需要向下强转一下,对吧

强转成他的一个子接口,叫做method

的signature,好

转完之后呢,我就可以通过他来get什么呢,我们目标方法,然后呢,获得他的name

好,这就是我们的method name,方法名

好,这个时候呢,我就可以重新给这个key来进行复制了

它等于什么呢,就等于我们这个类名加上一个冒号,对吧

然后呢,再加上一个方法名

好,刚才这个解释过了啊

这是当我们这个key是空串的

对吧,然后呢,再加上一个方法名

就等于我们这个key是空串的,对吧

那么这个就是我们的这个类名

然后这样来拼起来

那么如果它本身就有值,比如说我设置的是ab,对吧

那这个时候呢,这个if它其实就没有成立,对吧

那么程序继续往下走

然后再往下就是什么呢

这个key啊,注意,这只是一个中间的过程,对吧

我们最终还要给它拼接上

拼接上什么呢

我们就是传过来的这个参数

传过来的这个参数

比如说我们当前这种情况

假设我传过来的这个id呢

是100

对吧

假设是100

所以我们最终看到的这个效果

这个key应该是等于什么呢

就是ab加上冒号,再加上100

那么如何动态把这个串能拼起来呢

如何能给它拼起来呢

那么我们就需要使用到一个工具类

使用到一个工具类

就是我们前面导入的这个

Utils里边有一个叫做catchkeybuilder

这么一个工具类

然后这个工具类呢

这里边给我们封装了这么一个方法

就是什么呢

我们

我们把这个参数名

参数名我是不是通过这个parameters能够获得

再把我们这个目标方法里边这个参数列表的值

传给这个工具类

然后呢

它就会把这个动态的这个100给我们返回

好

所以说呢

我们在这呢

直接来调用什么呢

这个catchkeybuilder对象

它这里边呢

有一个generate方法

你看

那么我们把原始的这个key给它传进去

因为它要在它的基础之上是不是进行追加呀

所以把原始的这个key传进去

然后呢

第二个参数呢

就是我们这个parameters

这个parameters呢

就可以通过这个catch.parameters来获得

好

然后再往下呢

是不是就是我们这个参数列表

也就是我们这个目标方法里边这个参数列表

而这个呢

可以通过我们这个proceeding join point

连接点对象

它这里边有个get args对吧

这样来获得

然后呢

它就会返回一个子幅串

你看

它是返回一个字幅串的字幅串

这个string的形

然后呢把它重新附给我们的key

OK

而这个时候这个key呢

就是经过什么呢

经过我们这个计算之后的

这个时候这个key呢

可能就等于什么了

等于ab冒号

比如说我传过来那个id是100对吧

那么最终它返回的就是这么一个值了

就是ab冒号100

最后呢把这个key返回一下

好

那这个地方它报错

是因为什么呢

是因为我们当前这个方法呢

它是有一个异常信息抛出对吧

throws这么一个异常

然后呢

那怎么办呢

我们把这段呢给它复制一下

也继续往外抛一下

继续往外抛一下

好

那这样的话

它这个地方是不是就没问题了

但是呢

上面你会发现它是不是又报错了

那么我们在这儿呢

给它来这个处理一下

try catch一下就可以

好

try catch

exception

好

OK

那么到这儿的话呢

咱们这个generate key

这个方法呢

就已经写完了

这就是动态来生成我们这个key

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频课程讲解了如何在 Spring Boot 项目中，利用 AOP（面向切面编程）和注解处理器（Annotation Processor）来实现一个通用的缓存注解 `@Cache`。核心思想是通过一个抽象的注解处理器 `AbstractCacheAnnotationProcessor`，动态解析带有 `@Cache` 注解的方法，并自动生成缓存的 key。该 key 由注解中指定的 `region`、方法名、类名以及方法参数共同构成。视频通过一个 `@Cache` 注解的示例，演示了如何在控制器中使用该注解，并展示了处理器如何在运行时动态生成缓存 key 的过程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 课程开场，展示项目结构和 `AbstractCacheAnnotationProcessor.java` 文件。
*   **00:00:05 - 00:00:15**: 展示 `@Cache` 注解的使用示例，位于 `J2cacheController.java` 文件中。
*   **00:00:15 - 00:00:30**: 在 `AbstractCacheAnnotationProcessor.java` 中，讲解 `getAnnotationInfo` 方法，用于获取注解信息。
*   **00:00:30 - 00:00:45**: 讲解 `generateKey` 方法，用于动态生成缓存 key。
*   **00:00:45 - 00:01:00**: 详细演示 `generateKey` 方法的实现逻辑，包括如何获取方法名、类名和参数。
*   **00:01:00 - 00:01:15**: 展示 `CacheKeyBuilder` 类的 `generate` 方法，用于构建最终的 key 字符串。
*   **00:01:15 - 00:01:30**: 将生成的 key 设置回 `AnnotationInfo` 对象，并返回。
*   **00:01:30 - 00:01:45**: 总结整个缓存注解处理器的工作流程。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **核心代码：`AbstractCacheAnnotationProcessor.java`**
    *   **`getAnnotationInfo` 方法**：
        ```java
        protected AnnotationInfo<Cache> getAnnotationInfo(ProceedingJoinPoint proceedingJoinPoint, Cache cache) {
            AnnotationInfo<Cache> annotationInfo = new AnnotationInfo<Cache>();
            annotationInfo.setAnnotation(cache);
            annotationInfo.setRegion(cache.region());
            annotationInfo.setKey(generateKey(proceedingJoinPoint, cache));
            return annotationInfo;
        }
        ```
    *   **`generateKey` 方法**：
        ```java
        protected String generateKey(ProceedingJoinPoint proceedingJoinPoint, Cache cache) {
            String key = cache.key(); // 从注解中获取初始 key
            if (StringUtils.hasText(key)) {
                // 如果 key 不为空，直接返回
                return key;
            }
            // 如果 key 为空，重新设置当前 key 为：目标Controller类名 + 方法名
            String className = proceedingJoinPoint.getTarget().getClass().getSimpleName();
            MethodSignature signature = (MethodSignature) proceedingJoinPoint.getSignature();
            String methodName = signature.getMethod().getName();
            key = className + "." + methodName;
            // 使用 CacheKeyBuilder 构建最终的 key
            key = CacheKeyBuilder.generate(key, cache.params(), proceedingJoinPoint.getArgs());
            return key;
        }
        ```

*   **核心工具类：`CacheKeyBuilder.java`**
    *   **`generate` 方法**：
        ```java
        public static String generate(String key, String params, Object[] args) throws IllegalAccessException {
            StringBuilder keyBuilder = new StringBuilder(key);
            if (StringUtils.hasText(params)) {
                String paramsResult = ObjectAccessUtils.getArgs(args, params, String.class, delimiter: ",");
                keyBuilder.append(paramsResult);
            }
            return keyBuilder.toString();
        }
        ```
    *   **`ObjectAccessUtils.getArgs` 方法**：用于从方法参数中提取指定参数的值，用于构建 key。

*   **示例代码：`J2cacheController.java`**
    ```java
    @RequestMapping("/cache")
    public class J2cacheController {
        @GetMapping("/detail/{id}")
        @Cache(region = "addressBook", key = "ab", params = "id")
        public AddressBook detail(@PathVariable(name = "id") String id) {
            AddressBook addressBook = new AddressBook();
            addressBook.setId(id);
            addressBook.setAddress("beijing");
            System.out.println("查询数据库...");
            return addressBook;
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：展示注解使用**
    *   **描述**：讲师在 IDE 中打开了 `J2cacheController.java` 文件，高亮显示了 `@Cache` 注解的使用。注解中指定了 `region` 为 `"addressBook"`，`key` 为 `"ab"`，`params` 为 `"id"`。
    *   **目的**：说明用户在业务代码中如何使用该注解。

*   **场景二：动态生成 key 的逻辑**
    *   **描述**：讲师在 `AbstractCacheAnnotationProcessor.java` 中，将光标移动到 `generateKey` 方法。他首先检查注解中是否指定了 `key`，如果指定了，则直接返回。如果未指定，则通过 `proceedingJoinPoint` 获取当前方法的类名和方法名，拼接成一个默认的 key。
    *   **目的**：演示处理器如何动态解析注解信息，并根据注解内容生成缓存 key。

*   **场景三：构建最终的 key**
    *   **描述**：讲师调用 `CacheKeyBuilder.generate` 方法，将前面生成的 key、参数名和方法参数值组合起来，生成最终的缓存 key。
    *   **目的**：展示如何将方法参数动态地加入到缓存 key 中，以确保缓存的唯一性。

*   **场景四：返回缓存信息**
    *   **描述**：在 `getAnnotationInfo` 方法中，讲师将生成的 key 设置到 `AnnotationInfo` 对象中，并返回该对象。
    *   **目的**：说明处理器最终返回的是一个包含缓存配置信息的对象，供后续的缓存拦截器或处理器使用。

---

通过以上分析，我们可以清晰地看到，该课程通过一个具体的例子，详细讲解了如何利用 AOP 和注解处理器实现一个通用的缓存注解，其核心在于动态解析注解信息并生成唯一的缓存 key。
