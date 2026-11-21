# 26-声明式缓存（声明式缓存代码实现_导入工具 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

咱们继续来看我们声明式缓存

接下来一个呢

就是我们需要来导入几个工具类啊

这个呢

一会儿我们在进行缓存处理的时候呢

都会使用到这些工具类

那么我们直接来导入一下就可以

这些工具类呢

在我们资料里边就有啊

大家来看一下

这是我们这个资料里边

有个J2Catch声明式缓存所需的工具类的吧

然后呢我们把它直接来复制一下

整个呢复制到我们这个项目当中来

复制一下

然后把它放在哪呢

咱们在J2Catch下面呢

再来创建一个包啊

就叫做Utils吧

然后呢我们把这个工具类呢

把它直接放在这个下边来

好直接站到这个地方

OK

好然后呢我们可以来看一下

这些呢可以先关一下

整体呢来过一下

这个呢叫做Catch Key Builder

这个工具类呢

其实是处理什么呢

就是处理

我们这个缓存键生成的

也就是我们刚才提到的

你看我们这个地方

我在这个model里边

annotation infer里边

是不是定义了一个key啊

并且呢我提到了

我们这个key呢

它是怎么构成的呢

是不是就是由我们那几部分

动态拼接成的对不对

比如有我们的region

还有region

然后呢还有什么呢

还有就是我们

注解里面所定义的那个key

然后再加上这个动态的参数

对吧

parameters

好然后呢

动态拼接成的

好然后呢

这个值具体拼接的时候呢

就会使用到我们这个工具类

来进行拼接

你看这个是不是叫做generator

对吧generator

好这个就是生成key

那么我们调用这个工具方法

它最终呢就会把我们所需要的

这个动态的这个串呢

给我们拼接成

好

然后还有一个就是

field access

de-secret

对吧

还有这个什么object access

utils

这个这两个类呢

也其实底层呢

就是有我们的这个

catchkey builder来调的

你看在我们这个方法里边

是不是会调用这个

叫做object access utils

对吧

它就会调用到这个类

所以说呢

它们之间呢

是这么一个调用关系

然后在这个里边呢

它可能就会调用到

其他的这些工具类

你看在这里边

它是不是就调用到了

我们这个file

对吧

这个file access

discover

那么这个呢

其实都是用来访问我们

通过反射来访问我们这个目标对象

然后呢

根据我们这个字段

或者属性的值

来

这个参数名

来获得它具体的值

这就是通过反射呢

来获得我们这个目标对象

这是对象访问的工具类

这两个

然后还有一个就是这个

spring application context util

对吧

这是我们spring上下文工具类

在这里边呢

主要就是把我们这个

spring容器

也就是application context

这个上下文对象呢

把它注进来

方便我们在项目当中使用

因为我们会使用它呢

从我们spring容器当中

来获取一些对象对吧

直接调用get的方法

就可以获取了

所以说我们当前这个工具类呢

就是把这个对象给它获得到

把这个对象获得到

然后还有什么spring details

这是字符串工具类

那么处理字符串的

这是咱们导入的

直接把这几个工具类导入进来

后边呢

在我们进行缓存相关处理的时候呢

就会使用到这几个工具类

所以对于这种工具类呢

我们没有必要自己去手动编写

那么

我们可以用这个工具类呢

基本上都是一些成型的

对吧

那么我们直接把它拿过来

使用就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频是关于 **JCache** 缓存框架在 Spring Boot 项目中的实现教程，主要聚焦于 **声明式缓存** 的底层原理。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何构建一个自定义的缓存注解处理器（`CacheAnnotationProcessor`），并详细讲解了其核心组件的实现，包括：

*   **缓存键生成器 (`CacheKeyBuilder`)**：负责根据方法参数动态生成缓存的唯一键。
*   **字段访问描述符 (`FieldAccessDescriptor`)**：用于解析复杂的对象路径（如 `data.address.city.text`），支持访问对象的嵌套属性。
*   **工具类 (`SpringApplicationContextHolder`, `StringGenius`)**：提供 Spring 上下文获取和字符串工具方法，用于支持缓存功能的运行时环境。

整个过程旨在帮助开发者理解声明式缓存是如何在运行时被“翻译”和“执行”的，而不仅仅是使用注解。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:10**: 视频开场，展示项目结构和当前学习的章节 `6.2.3 导入工具类`。
*   **00:10 - 00:25**: 讲师切换到 `CacheHolder.java` 文件，展示缓存持有者类的结构，其中包含 `throwable` 字段和 `return` 语句，用于处理缓存异常。
*   **00:25 - 00:40**: 讲师展示 `CacheKeyBuilder` 类的导入依赖，包括 `SpringApplicationContextHolder` 和 `StringGenius` 等工具类。
*   **00:40 - 01:00**: 讲师开始讲解 `CacheKeyBuilder` 类，展示其 `generate` 方法的实现，用于根据 `key`、`params` 和 `args` 生成缓存键。
*   **01:00 - 01:20**: 讲师切换到 `FieldAccessDescriptor` 类，展示其构造函数和 `parseField` 方法，用于解析复杂的对象路径。
*   **01:20 - 01:40**: 讲师深入讲解 `FieldAccessDescriptor` 中的 `get` 方法，展示如何根据字段路径访问对象的属性，并处理 JSON 对象。
*   **01:40 - 02:00**: 讲师展示 `SpringApplicationContextHolder` 类，讲解如何通过 `@Autowired` 注入 `ApplicationContext` 并提供静态方法 `getApplicationContext()`。
*   **02:00 - 02:20**: 讲师展示 `StringGenius` 工具类，讲解其 `isInteger` 方法，用于判断字符串是否为整数。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **关键代码片段**

*   **`CacheHolder.java`** (00:10)
    ```java
    cacheHolder.throwable = throwable;
    return cacheHolder;
    ```

*   **`CacheKeyBuilder.java`** (00:40)
    ```java
    public static String generate(String key, String params, Object[] args) throws IllegalArgumentException {
        StringBuilder keyBuilder = new StringBuilder();
        if (StringUtils.hasText(key)) {
            keyBuilder.append(key);
        }
        if (StringUtils.hasText(params)) {
            String paramsResult = ObjectAccessUtils.get(args, params, String.class, delimiter);
            keyBuilder.append(paramsResult);
        }
        return keyBuilder.toString();
    }
    ```

*   **`FieldAccessDescriptor.java`** (01:00)
    ```java
    public static Object get(Object target, String fieldPath, Class<?> clazz, String delimiter, String nullText) {
        // ... (省略部分逻辑)
        if (fieldPath.startsWith("*")) {
            throw new IllegalArgumentException("路径不能以*开头");
        }
        if (target instanceof JSON) {
            targetElement = (JSON) target;
        } else {
            String jsonText = JSONObject.toJSONString(target);
            targetElement = (JSON) JSONObject.parse(jsonText);
        }
        if (targetElement == null) {
            throw new IllegalArgumentException("无法以json形式访问目标对象");
        }
        FieldAccessDescriptor fieldAccessDescriptor = FieldAccessDescriptor.parseFieldPath(fieldPath);
        Object valueElement = getValue(targetElement, fieldAccessDescriptor);
        if (valueElement == null) {
            return null;
        } else {
            return valueElement;
        }
    }
    ```

*   **`SpringApplicationContextHolder.java`** (01:40)
    ```java
    @Component
    public class SpringApplicationContextUtils {
        @Autowired
        private ApplicationContext applicationContext;
        @PostConstruct
        private void init() {
            springContext = applicationContext;
        }
        public static ApplicationContext getApplicationContext() {
            return springContext;
        }
    }
    ```

*   **`StringGenius.java`** (02:00)
    ```java
    public static boolean isInteger(String text) {
        if (!StringUtils.hasText(text)) {
            return false;
        }
        Pattern pattern = Pattern.compile("^[\\+\\-]?\\d+$");
        return pattern.matcher(text).matches();
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：缓存持有者 (`CacheHolder`) 的返回** (00:10)
    *   **描述**：讲师在 `CacheHolder.java` 文件中，演示了当缓存操作发生异常时，如何将异常信息封装到 `cacheHolder` 对象中，并将其作为结果返回。这体现了缓存处理的异常捕获机制。

*   **场景二：缓存键生成器 (`CacheKeyBuilder`) 的实现** (00:40)
    *   **描述**：讲师在 `CacheKeyBuilder.java` 文件中，演示了如何通过 `StringUtils.hasText` 方法判断输入参数是否为空，并使用 `StringBuilder` 拼接 `key` 和 `params` 生成最终的缓存键。这展示了缓存键的动态生成逻辑。

*   **场景三：字段访问描述符 (`FieldAccessDescriptor`) 的路径解析** (01:00)
    *   **描述**：讲师在 `FieldAccessDescriptor.java` 文件中，演示了如何解析复杂的对象路径（如 `data.address.city.text`）。代码通过 `split` 方法将路径分割，并使用 `get` 方法逐级访问对象属性。同时，代码还支持 JSON 对象的访问，通过 `JSONObject` 进行转换。

*   **场景四：Spring 上下文工具类 (`SpringApplicationContextUtils`) 的初始化** (01:40)
    *   **描述**：讲师在 `SpringApplicationContextUtils.java` 文件中，演示了如何通过 `@Autowired` 注入 `ApplicationContext`，并在 `@PostConstruct` 注解的方法中将其赋值给静态变量 `springContext`。这确保了在任何地方都可以通过静态方法获取到当前的 Spring 上下文。

*   **场景五：字符串工具类 (`StringGenius`) 的整数判断** (02:00)
    *   **描述**：讲师在 `StringGenius.java` 文件中，演示了 `isInteger` 方法的实现。该方法首先检查字符串是否为空，然后使用正则表达式 `^[\\+\\-]?\\d+$` 来判断字符串是否为整数。这展示了如何使用正则表达式进行字符串校验。
