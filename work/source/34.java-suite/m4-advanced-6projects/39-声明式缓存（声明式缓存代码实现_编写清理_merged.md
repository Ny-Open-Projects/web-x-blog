# 39-声明式缓存（声明式缓存代码实现_编写清理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那么接下来呢

继续来看咱们这个声明式缓存

刚才呢我们是把这个缓存注解处理器呢

已经进行了一个测试对吧

那么测试完之后呢

接下来我们来看下一个

就是编写失效缓存注解处理器

所谓失效缓存注解处理器呢

就是这个cat evict这个

也就是用我们说白了

就是我们要清理缓存数据对吧

所谓失效呢

就是使缓存数据失效

也就是清理

好那接下来呢

我们来看一下

这个是如何来编写

那么这个地方呢

我们需要来声明一个什么呢

来声明一个成员变量private

并且是一个list的类型的

为什么是list的类型呢

就是因为我们在这个controller

这个地方加注解的时候呢

大家可以来看一下

打开咱们这个地方

比如说我现在要清理对吧

清理的时候呢

我们加的就是这个注解

叫做cat evict

然后它这里边呢

是不是可以引用多个什么呢

多个cat

你看在这里边

咱们是不是定义了一个cat

是一个数组

所以说呢

我们需要把所有的这些cat都解析出来

放在这个list的集合里面去

也就是说我们在这儿呢

需要定义一个list集合

然后里边把它封装成什么呢

还是我们这个annotation info

annotation info

然后呢

它这里边这个范形是什么呢

还是cat类型

这个对应的是谁呢

对应的就是我们

这个类型

这个cat对吧

好把它导入一下

然后呢

咱们这个就叫cat list吧

好直接先给它new出来

new一个arelist

ok

这个属性呢是用来

用来这个封装什么呢

封装我们这个注解信息的集合

好把它这个声明好

然后接下来呢

我们来看这个方法

这个呢是咱们的这个构造方法

对吧

那么这个构造方法呢

主要就是用来初始化

我们当前这个实例对吧

处理器对象

初始化

我们这个清理缓存的这个注解处理器

处理器对象

那么同时呢

需要干什么呢

初始化

初始化一些这个一些这个缓存操作的这个对象

比如说什么呢

我们是不是需要使用到那个cat channel

那么我们在这呢

直接调一下super

为什么一调super就可以创建好呢

大家还记得吧

在咱们这个抽象类里边

我们是不是定义了这么一个成员变量对吧

然后呢

在这里边呢

他是把这个对象的给附上值了

是从我们sprint容器里面获取出来的

这个呢

我们调一下super

那这个cat channel就搞定了

然后接下来呢

就是初始化我们这个list的集合

对吧

需要把解析出来的数据给它放到集合里面去

好

那么解析出来的数据啊

首先呢

我们来看咱们这是不是传进来了一个catch evict

这个catch evict呢

就是从我们这个地方是不是拿过来的解析过来的

所以我们在这呢

需要获得它的value

注意看啊

我们这个地方其实是简写

你看我是value等于是不是这么一个数组对象

是这样的

所以我们在这呢需要通过这个什么呢

catch evict

catch evict.value

来获得什么呢

这个catch数组

相当于就得到了我们这个地方声明的这个数组

然后拿到它之后呢

我是不是就可以干什么了

来便利它

看看我们这个catch里边region key parameters

是怎么配置的

我需要把它取出来

那这个地方呢

因为它是一个数组

所以我们呢可以通过一个for 云环对吧

然后呢每一次拿出来之后呢

都是一个catch对象

好

然后呢

便利一下它

那么每次便利呢

我是不是需要把它封装成一个什么呢

这个annotation info这个对象

大家还记得吗

我们前面是不是在复类里边

也就是我们这个抽象复类里面

是不是已经提供了这么一个叫做get annotation info

这个方法对吧

然后呢我们把谁呢

把这个proceeding join point的传进去

把这个catch传进去

它就会给我们返回封装好的这个annotation info

好

有了之后呢

我们把它装到这个list的集合里面去就可以了

所以我们通过list的点什么呢

add

然后呢把annotation info装进去

OK

所以到这儿的话呢

我们这个初始化也就是这个构造方法呢

就已经写完了

这个构作方法执行完成之后呢

所需要的这些依赖的对象是不是就都已经

搞定了

好那么在这儿呢

这就是为我们后续真正清理缓存处理的时候呢

是不是准备这些什么呢

所需要的这些对象对吧

一会儿呢

我们来编写真正的这个处理逻辑

咱们就需要在这个process这个方法里面来编写

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于 Java 项目中“声名式缓存”功能开发的教程，具体聚焦于“失效缓存注解处理器”的实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何编写一个自定义注解 `@CacheEvict`，并创建一个对应的注解处理器 `CacheEvictAnnotationProcessor`，用于在运行时根据注解信息动态地清理指定缓存。视频内容包括注解的定义、处理器的构造函数、注解信息的提取与封装，以及核心的 `process` 方法的实现框架。整个过程旨在展示如何利用 Java 注解处理器（APT）来实现动态缓存管理功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开头，展示项目结构和当前正在讲解的章节 `6.2.7 编写失效缓存注解处理器`。
*   **00:00:05 - 00:00:15**：讲师切换到 `CacheEvictAnnotationProcessor.java` 文件，展示其类定义和构造函数。
*   **00:00:15 - 00:00:30**：讲师在构造函数中调用 `super()`，并开始处理注解信息。
*   **00:00:30 - 00:00:45**：讲师编写循环，遍历 `@CacheEvict` 注解的值，并将每个注解信息封装到 `AnnotationInfo` 对象中，添加到 `cacheList` 列表。
*   **00:00:45 - 00:01:00**：讲师将 `process` 方法的实现框架展示出来，为后续的缓存清理逻辑预留空间。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   项目大纲中明确显示了当前章节 `6.2.7 编写失效缓存注解处理器`。
    *   代码文件 `CacheEvictAnnotationProcessor.java` 的包名和类名。
    *   注解 `@CacheEvict` 的定义，包含 `value` 属性。

*   **关键代码片段**：

    **1. `@CacheEvict` 注解定义 (CacheEvict.java)**

    ```java
    @Documented
    @Target({ElementType.METHOD})
    @Retention(RetentionPolicy.RUNTIME)
    public @interface CacheEvict {
        Cache[] value() default {};
    }
    ```

    **2. `CacheEvictAnnotationProcessor` 类构造函数**

    ```java
    public CacheEvictAnnotationProcessor(ProceedingJoinPoint proceedingJoinPoint, CacheEvict cacheEvict) {
        super();
        Cache[] value = cacheEvict.value();
        for (Cache cache : value) {
            AnnotationInfo<Cache> annotationInfo = getAnnotationInfo(proceedingJoinPoint, cache);
            cacheList.add(annotationInfo);
        }
    }
    ```

    **3. `process` 方法框架**

    ```java
    public Object process(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
        return null;
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：环境与目标设定 (00:00:00-00:00:05)**
    *   讲师首先展示了项目的整体结构，通过左侧的项目导航面板，确认当前正在开发的模块是“声名式缓存”下的“失效缓存注解处理器”。
    *   画面中显示了 `CacheEvictAnnotationProcessor.java` 文件，为后续的代码编写做好了准备。

*   **场景二：构造函数实现 (00:00:05-00:00:30)**
    *   讲师在 `CacheEvictAnnotationProcessor` 类的构造函数中，首先调用父类的构造函数 `super()`。
    *   接着，讲师通过 `cacheEvict.value()` 获取注解中定义的缓存配置数组。
    *   通过 `for` 循环遍历这些配置，并调用 `getAnnotationInfo` 方法获取每个配置的详细信息，将其封装成 `AnnotationInfo<Cache>` 对象，并添加到 `cacheList` 集合中，为后续的缓存清理操作做准备。

*   **场景三：核心逻辑预留 (00:00:30-00:01:00)**
    *   讲师将焦点移至 `process` 方法，这是一个核心方法，用于执行实际的缓存清理逻辑。
    *   当前，该方法仅返回 `null`，作为占位符。讲师暗示，后续将在此方法中编写具体的缓存清理代码，例如调用 `cacheChannel` 对象的方法来清除指定缓存。
    *   画面中显示了 `cacheChannel` 对象，这是实现缓存清理的关键组件。

---

**总结**：本视频片段清晰地展示了如何通过 Java 注解处理器来实现一个“失效缓存”功能。讲师通过代码演示，逐步构建了注解处理器的核心逻辑，包括注解信息的提取、封装和处理框架的搭建，为后续的缓存清理功能奠定了基础。整个过程逻辑清晰，步骤明确，对理解注解处理器的使用非常有帮助。
