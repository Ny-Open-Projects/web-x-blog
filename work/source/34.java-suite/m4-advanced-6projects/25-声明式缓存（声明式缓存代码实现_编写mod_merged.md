# 25-声明式缓存（声明式缓存代码实现_编写mod — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看我们声明式缓存

刚才呢,我们是编写了两个注解

一个是缓存的注解,对吧

一个是这个,叫做catch

还有一个呢,就是catchEvector

就是指定清理缓存的这个注解

好,那接下来呢,我们来看下一个

下一个小节呢,就是需要来编写model模型

这个地方呢,我们一共会涉及到这么两个模型啊

一个就是这个annotationInfo

这个呢,其实就是用来封装我们这个缓存信息的

你看,就是catch信息包装

那么这里边主要封装的是什么呢

就是我们当前这个要封装的是哪个这个注解

你看,在这儿是不是指定了一个范形,对吧

然后呢,就是我们这个注解

动态解析出来的这个region还有key

然后呢,这个key的话呢,注意

是我们动态解析之后已经拼完了那个串

前面呢,咱们是不是也解释过了

就是什么呢,这个地方

我们最终呢,在

嗯

这个缓存的时候呢

是不是需要把我们这个region还有key还有parameter对吧

动态的都给它解析出来

然后呢

给它拼成用冒号分隔的这种字符串

作为我们这个缓存的它的这个唯一标识

那么咱们这个地方呢

这个key呢

就是我们经过计算之后的

经过计算之后的这个key

然后还有一个就是region

对吧

就是区域

所以需要这么一个对象

因为呢

我们后边在处理的时候呢

这个方便的能够获取到它的region还有key

对吧

就是从我们注解上把这些信息动态提取到之后呢

我们需要封装成这么一个对象来体现啊

然后呢

方便我们后续处理来使用它啊

就是这个

然后第二个呢

这个model呢

就是我们这个缓存结果啊

就是缓存结果的封装

叫做catchholder

然后呢

你看我们如果说要查用缓存数据

对吧

那么查出来之后呢

咱们就可以把它封装出来

它封装到我们这个value属性上

这是缓存的具体的数据

以及还有一个叫做exist catch

这个就是缓存数据是否存在

对吧

也有可能不存在不存在的话呢

我们也是返回这么一个对象

只不过这个值呢

就是false

还有就是什么呢

在处理缓存的时候有可能会有异常信息

对吧

所以说我们封装这么一个对象叫throwable

那接下来呢

我们就在这儿来编写一下

它是放在我们这个model这个包下边

那接下来呢

我们先把这些呢

都关上

然后呢

在这个这tokatch下面呢

再来创建一个model这么一个包

然后呢

我们在这儿呢

来创建这么一个类啊

一个第一个呢

就是这个annotationinfo

对吧

这个就是我们的catch相关信息的一个封装

或者叫做包装都可以

刚才我们也看到了

它的话呢

是要指定一个范形

对吧

要指定一个范形

在这个地方

bnt

然后呢

继承annotation

就是所有的

注解呢

是不是annotation

其实都是继承了我们这个annotation

所以我们可以在这儿选中它

对吧

然后呢

可以展示一下当前它的一些子类

对吧

那么你看这里边呢

其实就有咱们自己定义的

但这里边的非常多

展示起来了

可能会比较慢

也就是说

我们现在呢

定义的这个这两个注解

对吧

都属于它的这个子类

然后这里边呢

都有哪几个属性呢

刚才我们也看到了

一个是t

就是具体我们封装的是哪个注解

对吧

annotation

好

在这儿指定一下

还有就是一个是region

region

区域

对吧

还有一个呢

就是key

然后刚才也解释了

这个key呢

是动态计算之后的

主要就是有我们这

这个注解里边这三部分

对吧

动态解析完之后

然后拼成的那个字符串

然后呢

存到这个key

这个属性上

好

然后呢

对应的这个get set的方法呢

我们可以给它来填一下

好

把这几个都选上

OK

然后呢

还有一个to stream方法呢

也给它加一下吧

一个to stream方法

直接从这儿抄过来了

好

这个to stream呢

就是什么呢

是把它转成json

这种方式来返回

好

你看

如果说这个annotation

等于空的话呢

那就没有意义了

直接返回空

对吧

不等于空的话

就把当前对象呢

转成json

好

这是这个

好

annotation

info

对吧

这是封装我们缓存的信息

然后还有一个就是什么呢

我们这个缓存取出来之后

对吧

它的结果信息

也是需要一个封装的

那么

这个呢

叫做catchholder

就是下面这个

好

我把这个类名呢

直接control c拿过来

然后呢

我们在这儿来创建一下

这些呢

在我们后续啊

在进行处理的时候

都会使用到

所以我们提前把它创建好

然后这里边代码呢

我就不再手敲了

然后呢

直接

复制过来

稍等一下

刚才考的有点问题啊

应该是这样

应该是最后多一个花块

对吧

好

那么这是咱们当前这个类

这是缓存结果的封装

对吧

你看这里边有什么呢

有value

然后呢

还有exist catch

刚才也说了

对吧

这是缓存数据是否存在

上面呢

就是缓存的具体的数据

然后还有一个throwable

对吧

好

那这个代码的话呢

我们简单给它整理一下

就可以了

这是关于我们这两个啊

这是编写model模型

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“品达物流TMS项目”的Java后端开发课程，具体聚焦于“声明式缓存”功能的实现。讲师正在讲解如何通过自定义注解和模型类来实现缓存逻辑。核心内容包括：
*   **自定义注解 `@CacheVector`**：用于标记需要缓存的方法。
*   **模型类 `AnnotationInfo<T>`**：用于封装缓存的元数据，如缓存键（key）、区域（region）和值（value）。
*   **缓存结果封装类 `CacheHolder`**：用于封装缓存操作的结果，包括成功结果、异常结果以及缓存是否存在等状态。
*   **代码演示**：讲师通过IDE（IntelliJ IDEA）逐步编写和展示上述类的代码，并解释其作用。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:03**: 开场，展示课程大纲，定位到“6.2 声明式缓存”章节下的“6.2.2 编写model模型”。
*   **0:03 - 0:07**: 展示 `@CacheVector` 注解的定义，解释其 `@Retention` 和 `@Target` 注解的含义。
*   **0:07 - 0:12**: 展示 `AnnotationInfo<T>` 模型类的定义，讲解其泛型 `T` 和三个私有成员变量 `annotation`, `key`, `region`。
*   **0:12 - 0:16**: 展示 `AnnotationInfo<T>` 类的 `getAnnotation()` 方法，用于获取注解信息。
*   **0:16 - 0:20**: 展示 `AnnotationInfo<T>` 类的 `setRegion()` 和 `setKey()` 方法，用于设置缓存区域和键。
*   **0:20 - 0:24**: 展示 `AnnotationInfo<T>` 类的 `toString()` 方法，用于将对象转换为JSON字符串。
*   **0:24 - 0:28**: 展示 `CacheHolder` 类的定义，用于封装缓存结果。
*   **0:28 - 0:32**: 展示 `CacheHolder` 类的 `newResult()` 静态方法，用于创建成功缓存结果。
*   **0:32 - 0:36**: 展示 `CacheHolder` 类的 `newError()` 静态方法，用于创建失败缓存结果。
*   **0:36 - 0:40**: 展示课程大纲，切换到“6.2.3 导入工具类”章节。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **课程大纲**：清晰地列出了课程的章节结构，包括“jcache多级缓存”、“用户服务数据模型”、“声明式缓存”等。
*   **代码注释**：在代码中提供了详细的中文注释，如 `// Cache信息封装`、`// 缓存结果封装`、`// @param value 结果`、`// @param existsCache 是否存在缓存`、`// @return 缓存`。

#### 代码关键内容

*   **`@CacheVector` 注解定义**：
    ```java
    @Target({ElementType.METHOD})
    @Retention(RetentionPolicy.RUNTIME)
    public @interface CacheVector {
        Cache[] value() default {};
    }
    ```
    *   `@Target`：指定该注解只能用于方法。
    *   `@Retention`：指定该注解在运行时保留，以便在运行时通过反射读取。

*   **`AnnotationInfo<T>` 模型类**：
    ```java
    public class AnnotationInfo<T> extends Annotation {
        private T annotation;
        private String key;
        private String region;

        public T getAnnotation() {
            return annotation;
        }

        public void setAnnotation(T annotation) {
            this.annotation = annotation;
        }

        public String getRegion() {
            return region;
        }

        public void setRegion(String region) {
            this.region = region;
        }

        public String getKey() {
            return key;
        }

        public void setKey(String key) {
            this.key = key;
        }

        public String toString() {
            if (annotation == null) {
                return null;
            }
            return JSONObject.toJSONString(object: this);
        }
    }
    ```
    *   该类继承自 `java.lang.annotation.Annotation`，用于封装缓存的元数据。
    *   `toString()` 方法将对象转换为JSON字符串，便于序列化和传输。

*   **`CacheHolder` 缓存结果封装类**：
    ```java
    public class CacheHolder {
        private Object value; // 缓存的数据
        private boolean existsCache; // 缓存数据是否存在
        private Throwable throwable; // 异常

        private CacheHolder() {
        }

        public Object getValue() {
            return value;
        }

        public boolean hasError() {
            return throwable != null;
        }

        public static CacheHolder newResult(Object value, boolean existsCache) {
            CacheHolder cacheHolder = new CacheHolder();
            cacheHolder.value = value;
            cacheHolder.existsCache = existsCache;
            return cacheHolder;
        }

        public static CacheHolder newError(Throwable throwable) {
            CacheHolder cacheHolder = new CacheHolder();
            cacheHolder.throwable = throwable;
            return cacheHolder;
        }
    }
    ```
    *   该类用于封装缓存操作的结果，包括成功结果和失败结果。
    *   `newResult()` 方法用于创建成功缓存结果。
    *   `newError()` 方法用于创建失败缓存结果。

---

### 4) 关键场景与演示描述

*   **场景一：自定义注解 `@CacheVector` 的定义与讲解 (0:03-0:07)**
    *   讲师在IDE中展示 `@CacheVector` 注解的代码。
    *   讲解 `@Target` 注解的作用是限制注解只能用于方法。
    *   讲解 `@Retention` 注解的作用是让注解在运行时保留，以便在运行时通过反射读取。

*   **场景二：模型类 `AnnotationInfo<T>` 的编写 (0:07-0:24)**
    *   讲师在IDE中逐步编写 `AnnotationInfo<T>` 类。
    *   首先定义了三个私有成员变量：`annotation`, `key`, `region`。
    *   然后编写了 `getAnnotation()`, `setAnnotation()`, `getRegion()`, `setRegion()`, `getKey()`, `setKey()` 等方法。
    *   最后编写了 `toString()` 方法，用于将对象转换为JSON字符串。

*   **场景三：缓存结果封装类 `CacheHolder` 的编写 (0:24-0:36)**
    *   讲师在IDE中逐步编写 `CacheHolder` 类。
    *   定义了三个私有成员变量：`value`, `existsCache`, `throwable`。
    *   编写了 `getValue()` 方法用于获取缓存值。
    *   编写了 `hasError()` 方法用于判断缓存操作是否出错。
    *   编写了 `newResult()` 静态方法用于创建成功缓存结果。
    *   编写了 `newError()` 静态方法用于创建失败缓存结果。

*   **场景四：课程大纲切换 (0:36-0:40)**
    *   讲师在IDE中切换到课程大纲，定位到“6.2.3 导入工具类”章节，为后续内容做准备。

---

以上是根据视频画面进行的结构化技术分析。
