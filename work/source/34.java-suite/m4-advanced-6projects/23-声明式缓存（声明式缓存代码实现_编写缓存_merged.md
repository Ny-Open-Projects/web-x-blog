# 23-声明式缓存（声明式缓存代码实现_编写缓存 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们声明式缓存

刚才我们是说了一下

要实现声明式缓存

我们的实现思路大概是什么样子的

刚才我们整体介绍了一下

并且我们也分析了

要实现这个声明式缓存

主要会涉及到下边这些类

还有注解

这个小节我们就需要来具体把它实现出来

首先我们来看

第一个就是来编写什么

我们这个缓存注解

也就是第一个catch注解

这个代码我们写在哪呢

咱们其实可以把它写在

我们这个pduser里边

也可以单独提出来一个main用工程

然后所有的缓存的代码

都写到那个工程里面

其实都是可以的

那么我在这就写到一起了

然后我们可以在这个it黑码下边

再来创建一个包

就叫做j2catch

然后在这个包下边

我们再来创建一个包

叫做annotation

这是不是就是注解的意思

然后呢

把我们这个什么呢

把我们这个catch注解呢

就把它定义在这个annotation

这个包下边

注意注解的话呢

咱们是不是需要在这来选一下annotation

然后呢注解的名字呢叫做catch

这是我们这个缓存注解

先来加一个注释啊

缓存注解

然后呢一般呢

我们在定义注解的时候呢

是不是这个注解上面呢

都会加入一些什么呢

其他的注解

比如说这个什么呢

documenty的对吧

然后呢还有什么呢

就是这个

target

target

这个target呢

其实就是主要指定什么呢

我们当前这个注解呢

它应用在什么元素上面对吧

比如说我们有些注解呢

是加在类上面的

有些注解是加在方法上的

有些注解呢

是加在这个属性上的

等等啊

它是不一样的

那么我们这个地方呢

要指定的就是什么呢

把它加在我们的方法上

那么要加在方法上呢

咱们在这呢

在这个有一个叫做什么呢

叫做element type

元素类型

那么我们可以在这来指定一下

叫做element type点什么呢

method

你看这个method

这个就表示我们当前这个注解

只能加在什么呢

加在方法上了

因为我们也没有必要

把这个注解加在类上

对吧

所以说呢我们在这指定啊

给它加在方法上

然后还有什么呢

可以指定一个叫做retention

retention

然后呢这个呢

一般我们可以指定什么呢

就是指定一下

它这个存在的时间

对吧

存在的时间

那么也是有一个常量啊

retention policy

点什么呢

run time

那么具体这些注解起个什么作用呢

其实在我讲一上呢

都给大家列出来了

大家自己来看一下就行了

应该我们前面呢

也都讲过

自定义注解

对吧

我们自己定义一个注解

一般呢都会加这么一些

然后呢

你看documenty的

它表示什么呢

该注解的元素

应被什么呢

java doc

或者其他的这个

类似的工具啊

文档化

对吧

然后呢

target呢

就是表示这个注解的元素

它的程序元素的种类

那么一般就是这么几种类型

啊

然后还有这个表示什么呢

自动被继承

还有就是这个retention

对吧

表示这个注解保留时间的长短

然后呢

我们可以有这么一些可选的值

啊

咱们一般的用的比较多的

就是这个run time

就是运行式

啊

这是我们把这个上面这几个注解

已经加好了

那接下来呢

我们就需要来想一下

我们当前这个cache注解里边

需要定义哪些元素

我们就需要来想一下

那么它是缓存注解

那我们就来想一下

我们要操作缓存的时候

都需要设计到哪些呀

咱们可以回顾一下

来看一下我们前面

这个地方

address book

对吧

这是我们调用的这个什么呢

J2 cache它的原生的API

比如说我现在呢

要设置

要载入缓存

对吧

也就是设置缓存数据

那么我是不是需要调用这个什么set方法

然后呢

设计了什么

region

就是我们这个缓存

它这里边有一个区域的概念

对吧

就是把我们这个数据放在哪个区域

region

然后呢

后边这个呢

其实就是我们的key对吧

就是key

你看这个

第二个就是key

所以说呢

我们这个地方呢

很显然

我这个注解里边是不是就需要来体现什么呢

我们当前这个数据需要放在哪个区域

以及什么呢

它的这个key是什么

好

实际上我们这个地方呢

一共会涉及到这么三个元素

我先写出来

然后

我们再来解释一下

一个是区域对吧

一个是区域叫做region

叫做region

然后呢

注意啊

它这是不是有两个括号对吧

然后呢

我们可以指定一下default

默认值对吧

比如说我就给它来一个rx

这是一个默认值

然后还有什么呢

就是我们的key

这个默认值呢

我就给一个空串就可以了

然后呢

我们在这呢

还有一个叫做parameters

这是不参数啊

参数

那么这个是怎么回事呢

那么我们就需要来说一下

如果我们加了这个注解之后

最终我们这个数据

它缓存在哪个区域

它使用的key是什么

比如说我们就拿当前这个来说

你看啊

这个地方我们不是set了吗

对吧

set了

我们使用的区域就是我们指定的这个区域

然后呢

这个id呢

是不是就是作为我们的key

这个id就是作为我们的key

然后呢

对应存储的值是不是就是这个entity对象

对吧

就是entity对象

那也就是说啊

我保存每一个address book的时候呢

对应的是不是都需要来缓存一份数据

并且呢

使用它的id作为key

其实就是唯一标识对吧

那么我们这个地方呢

是怎么设计呢

是这样的

跟它呢

稍微有一点点不一样

就是什么呢

我们每一个id呢

对应的是parameter

其实是这个参数

对吧

是这个参数

而这个key呢

它代表的是类型

代表的是类型

比如说啊

我们就拿当前这个来举例子

我这个region呢

不使用默认的

我使用address book

作为我们的region

作为我的region

然后呢

再使用什么呢

统一的一个

注意这是address book

address book

然后呢

再使用一个key

作为分类

比如说我在这呢

就叫做什么呢

叫做ab对吧

address book嘛

叫做ab

好

简写

然后再往后呢

跟上这个parameter

它具体传过来的值

因为呢

每一个entity

它是不是都有自己的id啊

都有自己的id啊

所以说呢

比如说这一次它的id是1

那这样的话呢

整体我把这三个连起来

就作为什么呢

就作为我们最终

缓存到我们

缓存到我们这个

这个j2catch当中的key

其中呢

这个呢

就是我们的region

来自于region

而这个ab呢

来自于这个key

而这个1呢

就来自于我们的参数

parameter

而这个参数的话呢

就需要我们去动态的去获取

对吧

因为你这个entity里边

这个id呢

我是不是需要把它动态的解析出来

它有可能等于1

也有可能等于2

也有可能等于任意值

对吧

那么

这个地方呢

我们就需要动态的

把这个参数给它解析出来

然后最终拼成这么一个串

这个呢

就构成了什么呢

我们最终把它缓存到

我们这个j2catch

它的唯一标识

好

也就是说我们在调用什么呢

在调用这个set方法的时候

对吧

那么

就需要把这三部分给它拼起来

三部分拼起来

大概就是这么一个套路

好

所以说呢

这里边的话呢

对于同一类数据

比如说我们要缓存的是这个address book

那么前面这两部分呢

其实都是固定的

对吧

region 区域

key呢

表示分类

而不同的是什么呢

是parameter

而这个parameter呢

就是我们提到的

我可能是从这个entity当中

把那个id取出来

对吧

给它拼成串

最终呢

把这三部分加一块

然后呢

作为我们唯一的标识

好

所以说呢

我们在这个catch当中呢

就需要有这么三个元素来洗线

好

这是我们这个catch

这个注解

它的定义

然后接下来呢

我们还需要再来定义一个注解

那么下一个注解是什么呢

就是我们这个catchEvict

这是不是用来清理缓存的这个注解

对吧

用来清理缓存的注解

好

然后呢

我们在这个annotation

这个下边

来定义

这个

这个注解

注意啊

这个也是选annotation

这个名字呢

叫做catchEvict

然后上面呢

这一块呢

都是一样的

对吧

这一块都是一样的

然后呢

我在这呢

也加一个注释吧

加一个注释

这个是用于清理缓存的

这个注解

好

然后呢

我们需要来考虑

当前这个注解里边

应该定义哪些元素

这个应该定义哪些元素呢

其实应该是什么呢

跟我们这边这个元素

是非常类似的

因为你这边是存

对不对

而我删的时候呢

我清理的时候

是不是也需要去指定什么呢

从哪个区域

然后呢

删除哪个key

对吧

所以说呢

我们在这边呢

是不是也需要再来定义一遍

那这样的话呢

它其实就重复了

那么我们这个注解呢

其实是可以引用的

所以我在这呢

就可以干什么呢

直接来定义一个catch类型

注意看啊

这个catch呢

就是我们刚才定义的这个catch

就是这个catch

好

所以我们呢

所以我直接引用它就可以了

然后呢

我们在这呢

为了灵活起来啊

我可以直接定义成一个数组

就是说什么呢

我在清理的时候呢

我可以一次清理多个

清理多个这个缓存数据

这样的话

我是不是这个catch传进来的时候

我传多个对吧

那么对应的就是多个缓存数据

我就可以锁定了对吧

所以说呢

我们在这呢

就可以直接通过定义catch

然后呢

这个地方指定这个什么呢

数组类型

就是可以一次清理多个缓存数据

然后呢

这个元素呢

我们就叫value就行了

这是默认的对吧

然后呢

给它一个默认值

默认值呢

就是一个这个数组

空的

好

这样的话呢

我们就已经定义好了

第二个注解对吧

这个叫做catch evict

好

这是咱们这两个注解呢

就已经定义好了

第一个呢

就是用来缓存数据的

第二个就是用来清理缓存数据的

好

那么当然了

我们需要知道

本身的这个注解呢

它其实仅仅只是一个标识

对不对

哎

让

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于 Spring Boot 项目中实现 **声明式缓存**（Declarative Caching）功能的教学内容。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何自定义一个缓存注解 `@Cache`，并为其编写对应的处理器 `CacheEvictor`。视频重点讲解了如何使用 `@Target` 和 `@Retention` 注解来定义注解的使用范围和生命周期，并展示了如何在控制器方法上使用自定义的缓存注解。整个过程旨在帮助开发者理解 Spring 缓存机制的底层实现原理，并掌握如何扩展和定制缓存功能。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:10**: 视频开头，讲师在 IDE 中展示项目结构，并导航到 `6.2 声明式缓存代码实现` 这一章节。
*   **0:10 - 1:00**: 讲师开始编写自定义缓存注解 `@Cache`。首先定义了注解的包名和导入语句，然后逐步添加 `@Documented`、`@Target(ElementType.METHOD)` 和 `@Retention(RetentionPolicy.RUNTIME)` 三个核心注解。
*   **1:00 - 2:00**: 讲师在 `@Cache` 注解中定义了三个默认属性：`String region() default "rx";`、`String key() default "";` 和 `String params() default "";`，用于指定缓存的区域、键和参数。
*   **2:00 - 3:00**: 讲师切换到 `AddressBookController.java` 文件，展示了一个使用 `@PostMapping` 注解的保存方法。在该方法中，讲师演示了如何在业务逻辑中手动调用 `cacheChannel.set(...)` 来实现缓存的写入，以此作为后续自定义注解的对比和铺垫。
*   **3:00 - 4:00**: 讲师回到 `Cache.java` 文件，继续完善注解的定义，确保其功能完整。
*   **4:00 - 5:00**: 讲师开始编写 `CacheEvictor` 接口，用于处理 `@Cache` 注解。他首先在 IDE 中创建了 `CacheEvictor.java` 文件，并开始编写接口定义。
*   **5:00 - 6:00**: 讲师在 `CacheEvictor.java` 文件中定义了 `@CacheEvictor` 注解，并为其添加了 `@Target` 和 `@Retention` 注解，使其能够被编译器识别并在运行时生效。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   课程大纲显示了“6.2 声明式缓存代码实现”及其子章节，如“6.2.1 编写缓存注解”、“6.2.2 编写 model 模型”等。
    *   文档中列出了与缓存相关的几个核心注解处理器：
        *   `CacheEvictor`: 清理缓存注解。
        *   `CacheMethodInterceptor`: 缓存拦截器。
        *   `AbstractCacheAnnotationProcessor`: 抽象缓存注解处理器。
        *   `CachesAnnotationProcessor`: 缓存注解处理器。
        *   `EnableCache`: 开启缓存功能。

*   **代码关键内容**:

    **1. `@Cache` 注解定义 (Cache.java)**

    ```java
    package com.ithema.j2cache.annotation;

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

    **2. `@CacheEvictor` 注解定义 (CacheEvictor.java)**

    ```java
    package com.ithema.j2cache.annotation;

    import java.lang.annotation.*;

    /**
     * 清理缓存注解
     */
    @Documented
    @Target(ElementType.METHOD)
    @Retention(RetentionPolicy.RUNTIME)
    public @interface CacheEvictor {
        // 可以在此处添加更多属性，例如指定要清理的缓存键等
    }
    ```

    **3. 控制器方法示例 (AddressBookController.java)**

    ```java
    @PostMapping("/")
    public Result save(@RequestBody AddressBook entity) {
        if (1 == entity.getIsDefault()) {
            addressBookService.lambdaUpdate().set(AddressBook::getIsDefault, 0).eq(AddressBook::getUserId, entity.getUserId()).update();
        }

        boolean result = addressBookService.save(entity);
        if (result) {
            // 手动写入缓存
            cacheChannel.set(region, entity.getId(), entity);
            return Result.ok();
        }
        return Result.error();
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：创建自定义缓存注解 `@Cache`**
    *   讲师在 `Cache.java` 文件中，首先定义了注解的包名和导入语句。
    *   接着，他逐步添加了 `@Documented`、`@Target(ElementType.METHOD)` 和 `@Retention(RetentionPolicy.RUNTIME)` 注解，解释了每个注解的作用：`@Target` 用于指定注解可以应用在方法上，`@Retention` 用于指定注解在编译后会保留到运行时，以便在运行时被处理器读取。
    *   最后，他定义了三个方法：`region`、`key` 和 `params`，并为它们设置了默认值，用于在缓存中指定缓存区域、键和参数。

*   **场景二：演示手动缓存写入**
    *   讲师切换到 `AddressBookController.java` 文件，展示了一个 `@PostMapping` 注解的方法。
    *   在该方法中，他演示了如何在业务逻辑中手动调用 `cacheChannel.set(...)` 来将数据写入缓存，以此作为后续自定义注解的对比和铺垫。

*   **场景三：创建缓存清理注解 `@CacheEvictor`**
    *   讲师在 IDE 中创建了 `CacheEvictor.java` 文件。
    *   他为该文件定义了 `@CacheEvictor` 注解，并为其添加了 `@Target` 和 `@Retention` 注解，使其能够被编译器识别并在运行时生效。
    *   讲师强调，这个注解将用于后续的缓存清理功能。

---

以上是根据视频画面进行的结构化分析。希望对您有所帮助！
