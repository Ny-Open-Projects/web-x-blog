# 31-声明式缓存（声明式缓存代码实现_编写抽象 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们声明式缓存

刚才我们是把拦截器已经写完了

那接下来我们来看下边一个就是我们抽象的注解处理器

现在咱们是已经把处理器这个类已经创建好了

当然现在我们需要去完善这个类

那接下来我们需要来考虑一下

当前这个类它是作为我们这两个具体的处理器它的负类

那也就是在我们这个抽象的负类里边

需要有一些公共的属性还有方法

然后这些属性还有方法主要是提供给我们具体的这两个子类来使用的

比如说什么呢

比如说我们要操作这个J2Cache缓存

那么我们必须使用到一个Cache Channel对象

那这样的话我们就可以把这个对象

把它声明到我们这个负类当中

然后子类就可以直接使用它了

也就是说我们在这需要来声明一个

这个对象的负类

Protected

是不是叫做Cache Channel

这就是我们J2Cache的这个Cache Channel

但是需要注意

这的话我直接AutoWear的行不行

注意这个地方其实是不可以的

为什么呢

就是因为我们现在这些处理器

它并没有交由我们的Spring容器去管理

你看我们现在这三个类上面

是不是都没有去加什么Component的注解

也就是说我们这两个处理器类是自己NU出来的

那么这个时候

你加AutoWear的注解肯定是不行的

那么它是注不进来的

那怎么办呢

我们可以在构造方法当中

通过我们这个什么呢

前面咱们是不是在工具类里边

已经提供了这个Spring Application Contacts Utils

对吧

然后我们可以直接注入这个什么

我们这个Spring容器对象

然后我们可以通过这个Application Contacts来get bit

把我们容器里边的这个对象把它get出来

为什么容器里边一定有呢

就是因为我们

当前这个PD User里边是不是已经导入了什么呢

咱们这个J2Catch它的这个Main文坐标

这里边已经有了一个Starter

所以只要我们相应的这个配置文件已经配置好了

那这个时候呢

当我们Spring Boot项目启动的时候呢

就会把那个Catch Channel对象呢

直接给我们出示化好

你看咱们前面在咱们这个Controller当中

我们是不是就是直接通过AutoWear的呢

就已经把它注入了

对不对

你看我们在这个地方

是不是直接就可以注入了呢

所以说呢

说明我们这个Spring容器里边

它已经这个创建好

并且存在于容器当中

所以我们只要得到了Spring容器

然后呢

我们调用它的get bit方法

对吧

然后呢

就可以把它获取出来

所以我们这个地方呢

先来声明一下

然后呢

在我们这个构造方法当中

咱们可以提供一个构造方法

在构造方法当中呢

把我们这个Spring容器对象先获得

然后再从容器里面get bit

跟进去呢

根据这个类型来获取

就可以了

所以我们这个地方呢

先来获得我们这个容器对象

怎么获得呢

咱们是不是可以直接调用它的一个静态方法

对吧

调用这个静态方法

然后呢

就可以获得它

而这个的话呢

你看它也是一个静态的

这是在我们这个对象初始化之后呢

它其实就已经把注入的这个对象

复制给这个静态变量了

所以说呢

我们在这呢

就直接通过调用它点get什么呢

先把它引入一下

好

别找错了

应该是J2Catch这个包下边

然后呢

调用它的一个getApplicationContext的

这样呢

就获得我们Spring容器对象

对吧

好

然后呢

我们就可以通过它来get bit

然后获得什么呢

CatchChannel这种类型

然后呢

就可以获得一个CatchChannel

然后呢

咱们直接复制给我们这个成员变量就可以了

这个代码写下来就比较简单了

复给这个成员变量

那这样的话呢

在我们这两个子类里边

咱们随便写一下

我们在里边打开一个子类

在这个子类里边呢

比如说我想使用CatchChannel

我可以在这直接就调用CatchChannel点什么呢

相应的方法

以Veg就可以清理了

所以说呢

咱们在这个副类里边

把这个对象呢

把它创建出来

通过这种方式

把它get出来

然后呢

复制给成员变量

然后由子类来拿过来使用就可以

这个构造方法主要就是初始化一些什么呢

在这里边

初始化

公共属性

那么公什么呢

我们这个子类来使用

好

这是这个方法

然后接下来呢

我们还需要再来提供一个公共方法

这个公共方法是干什么呢

就是获得我们的这个注解信息

获得注解信息

我们注解信息不是已经获得了吗

注意啊

我们现在呢

是需要把那个Catch注解进行一个解析

然后呢

把它封闭了

封装成我们的这个model对象

大家还记得吧

前面我们是不是创建了这么一个叫做annotationinfo

对吧

这是我们这个注解信息相关封装的

那么把这个region呢

还有key啊

给它这个创建出来

对吧

然后呢

负的值呢

就是我们动态解析出来的参数

并且我们也提到这个key呢

是我们经过这个字符串拼接之后

最终形成的那个key

所以说呢

我们这个地方呢

就是什么呢

通过解析咱们这个Catch注解

最终呢

把它封装成这么一个annotationinfo

这么一个对象

所以这个方法呢

我们可以在这来创建一下public

然后返回值呢

就叫做annotationinfo

对吧

这个就叫做get什么呢

annotationinfo

好

getannotationinfo

然后我们如果说这个方法呢

只想让子类来调用的话呢

我们可以把这个public.info

给它改成protected

这样的话呢

只有子类是不是才能调用这个方法

然后其他的类呢就调用不了了

就把它保护起来

然后这个地方呢

我们是不是需要指定一个份型对吧

这个份型呢

我们指定Catch就可以

那有的同学可能就说了

你这个地方指定Catch

那我们那个什么

那我们还有一个叫做CatchEvator呢

那怎么办呢

大家来看啊

其实我们这个地方呢

为什么只要指定Catch就可以

因为我们这个CatchEvator这个注解

它其实这里边是不是还是引用到我们的Catch

所以说最终呢还是反映到Catch这个注解

所以我们就解析它就可以

那也就是说我们这个地方呢

这个份型指定成这个Catch注解

就可以

然后呢这个地方呢

我们需要传进来两个参数

哪两个参数呢

一个是我们的连接点

叫做proceedingJoinPoint

这个呢因为在这个方法里边

一会我们就会用到

还有一个呢就是我们这个具体的那个Catch注解

好Catch注解

OK

好那下边呢

我们是不是就需要来完善一下咱们这个方法

那么我们这个方法呢

是返回这个Catch

这个annotationInfo对吧

这个地方呢

这就是封装吧

封装我们这个注解信息

好

返回成这种对象

那这样的话呢

我们是不是就需要把这个对象呢

给它来创建一下对吧

再来创建一下annotationInfo

这个份型呢指定成

Catch

好

annotationInfo

咱们先把它new出来啊

new一个annotationInfo

好

然后new出来之后呢

我们来看一下这里边是不是需要有三个值来设置

对吧

第一个呢就是这个annotation

就是它封装的我们传过来的这个Catch注解

好

所以说这个比较简单

annotationInfo.set

annotation

而这个annotation呢我们就指定成Catch就可以

好

然后呢还有一个就是

annotationInfo.set

是这个

这个region对吧

这个region比较简单

那么我们通过这个Catch呢

是不是能够获得点什么呢

region

好

这个就是设置它的这个缓存的区域对吧

关键呢还有一个就是那个key

然后这个key的话呢

我们可以单独再来封装一个方法

就是专门来这个生成key的

因为我们这个地方下一个是不是就要调用这个set key了

对吧

而这个key的话没那么简单

并不是简单的

就是Catch点什么key

对吧

没那么简单啊

因为这个地方呢我们前面也解释过了

就是这个key呢它是一个动态解析的

这个动态解析的

它是由我们这三部分是不是来构成

就是什么呢

动态把region解析出来

而这个key呢一般就是一个

就是一个字符串

而这个parameter呢

就是跟我们传过来的参数是不是有关系

比如说是什么呢

比如说是我们这个address book

地址部的ID

对吧

那么那个ID呢就会动态拼接进去

最终呢把这三部分加在一块

形成我们最终的那个key

所以说呢这个key的话呢

我们就需要专门再来封装一个方法

那个方法呢就是专门用来生成key的

专门用来生成key的

那么我们在这下面呢来

封装这么一个方法

protected

然后呢返回值呢就是一个普通字符串

咱们这个就叫什么呢

generate key吧

generate key

好

然后呢这个generate key呢

需要传什么参数过程呢

好

这个ctrl c复制过来呢

其实还是我们这两个参数

还是这两个参数啊

在这来

ctrl c复制过来

放在这个位置

在这个里边呢

就是动态的来生成我们最终的那个key

对吧

具体怎么拼接

一会儿呢我们再来看这个方法

这个就是动态解析我们这个注解

注解信息

然后呢生成我们的key

好

一会儿呢我们再来看这个方法怎么写

完事了对吧

那我们在这儿的话呢

是不是就可以直接调用我们这个generate key

方法

然后呢把这个连接点对象

还有我们这个catch对象

传进去

好

这样呢是不是就形成了这个key

然后呢形成这个key之后呢

咱们最终是不是来return一下

return什么呢

我们这个annotation info

OK

那么到这儿的话呢

咱们这上面这个方法就已经写完了

对吧

这个方法呢就是接收我们这个连接点对象

还有呢就是我们这个

这个方法上加的这个注解对象

对吧

然后呢拿过来之后呢

把它进行一个转换

最终呢封装成了一个annotation info对象

因为后边在咱们这个具体的处理器里面呢

需要把这个对象获取到

把这个对象获取到

这样方便我们去使用它

而这个地方呢我们set这么三个东西

对吧

一会儿呢我们就需要来重点来写这个方法

就是generate key

就是如何把我们这个最终的动态的这个key

给它生成出来

好

那么关于我们这个抽象的这个方法呢

那么关于我们这个抽象的这个key给它生成出来

好

那么关于我们这个抽象类呢

我们先写到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段为一个关于 Spring Boot 项目中使用 JCache 注解实现缓存功能的实战教学。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何构建一个自定义的缓存注解处理器（`AbstractCacheAnnotationProcessor`）。核心内容包括：
- 项目依赖的配置（`pom.xml`），特别是 `jcache-spring-boot-starter` 和 `jcache-core`。
- 定义一个抽象的缓存处理器基类，该类负责初始化 Spring 上下文并获取一个 `CacheChannel` 实例。
- 通过 `@Cache` 注解的元数据（如 `region` 和 `key`）来封装缓存信息。
- 展示了如何通过 `@CacheEvict` 注解来实现缓存的清除操作。
- 整个过程旨在说明如何通过 AOP（面向切面编程）和注解处理器来实现对缓存操作的自动化管理。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 展示项目结构，定位到 `AbstractCacheAnnotationProcessor.java` 文件。
*   **00:03 - 00:07**: 讲师在 `AbstractCacheAnnotationProcessor` 类中，将 `protected CacheChannel cacheChannel;` 字段的访问修饰符从 `public` 改为 `protected`，并解释其作用。
*   **00:07 - 00:11**: 讲师在构造函数中，通过 `SpringApplicationContexUtils` 获取 Spring 上下文，并使用 `getBean` 方法注入 `CacheChannel` 实例。
*   **00:11 - 00:15**: 讲师在 `getAnnotationInfo` 方法中，创建一个 `AnnotationInfo<Cache>` 对象，并设置其 `region` 属性。
*   **00:15 - 00:19**: 讲师继续在 `getAnnotationInfo` 方法中，调用 `generateKey` 方法生成缓存键，并设置到 `AnnotationInfo` 对象中。
*   **00:19 - 00:23**: 讲师展示 `CacheEvict` 注解处理器的实现，其 `process` 方法会根据注解参数生成缓存清除指令。
*   **00:23 - 00:27**: 讲师在 `CacheEvict` 处理器中，通过 `cacheChannel` 调用 `evict` 方法来执行实际的缓存清除操作。
*   **00:27 - 00:31**: 讲师在 `CacheEvict` 处理器中，通过 `cacheChannel` 调用 `put` 方法来执行实际的缓存写入操作。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段**:
    *   **`AbstractCacheAnnotationProcessor` 类的构造函数**:
        ```java
        public AbstractCacheAnnotationProcessor() {
            ApplicationContext applicationContext = SpringApplicationContexUtils.getApplicationContext();
            cacheChannel = applicationContext.getBean(CacheChannel.class);
        }
        ```
    *   **`getAnnotationInfo` 方法**:
        ```java
        protected AnnotationInfo<Cache> getAnnotationInfo(ProceedingJoinPoint proceedingJoinPoint, Cache cache) {
            AnnotationInfo<Cache> annotationInfo = new AnnotationInfo<Cache>();
            annotationInfo.setAnnotation(cache);
            annotationInfo.setRegion(cache.region());
            annotationInfo.setKey(generateKey(proceedingJoinPoint, cache));
            return annotationInfo;
        }
        ```
    *   **`CacheEvict` 处理器的 `process` 方法**:
        ```java
        public Object process(ProceedingJoinPoint proceedingJoinPoint, CacheEvict cacheEvict) {
            // 根据注解参数生成缓存清除指令
            cacheChannel.evict(cacheEvict.region(), cacheEvict.key());
            return proceedingJoinPoint.proceed();
        }
        ```
    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>net.oschina.jcache</groupId>
            <artifactId>jcache-spring-boot-starter</artifactId>
            <version>2.8.0-release</version>
        </dependency>
        <dependency>
            <groupId>net.oschina.jcache</groupId>
            <artifactId>jcache-core</artifactId>
            <version>2.8.0-release</version>
        </dependency>
        ```

*   **关键注解**:
    *   `@Cache`: 用于定义缓存操作，包含 `region` 和 `key` 等属性。
    *   `@CacheEvict`: 用于定义缓存清除操作，包含 `region` 和 `key` 等属性。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与依赖配置** (00:00-00:03)
    *   讲师首先展示了项目的整体结构，包括 `pom.xml` 文件。
    *   他强调了项目中需要引入 `jcache-spring-boot-starter` 和 `jcache-core` 依赖，以支持 JCache 注解功能。

*   **场景二：抽象处理器基类的构建** (00:03-00:11)
    *   讲师在 `AbstractCacheAnnotationProcessor.java` 文件中，定义了一个抽象类。
    *   他将 `cacheChannel` 字段的访问修饰符从 `public` 改为 `protected`，以便子类可以访问。
    *   在构造函数中，他通过 `SpringApplicationContexUtils` 获取 Spring 上下文，并使用 `getBean` 方法注入 `CacheChannel` 实例。

*   **场景三：注解信息的封装** (00:11-00:19)
    *   讲师在 `getAnnotationInfo` 方法中，创建了一个 `AnnotationInfo<Cache>` 对象。
    *   他通过 `setAnnotation`、`setRegion` 和 `setKey` 方法，将注解的元数据（如 `region` 和 `key`）封装到 `AnnotationInfo` 对象中。

*   **场景四：缓存清除操作的实现** (00:19-00:27)
    *   讲师展示了 `CacheEvict` 注解处理器的实现。
    *   他通过 `cacheChannel` 调用 `evict` 方法，根据注解参数执行缓存清除操作。
    *   他强调了 `CacheEvict` 注解的 `region` 和 `key` 属性在缓存清除中的作用。

*   **场景五：缓存写入操作的实现** (00:27-00:31)
    *   讲师展示了 `CacheEvict` 注解处理器的 `process` 方法。
    *   他通过 `cacheChannel` 调用 `put` 方法，根据注解参数执行缓存写入操作。
    *   他强调了 `CacheEvict` 注解的 `region` 和 `key` 属性在缓存写入中的作用。
