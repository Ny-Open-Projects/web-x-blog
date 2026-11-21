# 24-声明式缓存（声明式缓存代码实现_应用缓存 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,接下来呢,咱们继续来看我们声明式缓存的实现

刚才呢,我们是定义了这么两个注解,对吧

分别是catch注解,还有这个catch evict注解

好,那接下来呢,我们就来说一下

比如说我们整个这个小的这个声明式缓存这个框架定义完了之后啊

我们最终这个注解是怎么使用的

咱们先来简单演示一下

那么刚才我们也提到了,它是会使用在我们control的方法上,对吧

那假设我们现在所有的都已经实现了

我就剩这个是什么呢,应用了,对吧

比如说呢,我现在呢,就想把它加在我们这个controller的这个detail这个方法上

你看,现在呢,咱们是直接调用到它这个原生的API,对吧

这样来使用的

那假设呢,我现在呢,就想使用我们这个注解这种方式

那么应该怎么做呢

其实就是这样的啊

咱们在这个方法上呢,直接来应用我们这个

在这来加一个catch注解

然后呢,我们在这里边来指定什么呢

指定这三个元素,对吧

一个是region,还有一个是key,还有一个是parameters

然后呢,我们在这来指定region

region的话,比如我这就来一个address book

然后还有什么呢,key,对吧

这个key的话呢,我就叫ab

然后呢,接下来是这个parameters

然后注意,这个parameters呢,不能随便写

那么我们这个地方呢,必须要写id

其实对应的就是我们这个什么呢

这个参数名,参数名称

因为什么呢

我们后边呢

我们具体的那个处理器里边

咱们前面也提到了

要实现的话呢

我们这边是不是需要有具体的咱们这个缓存的处理器,对吧

那么需要在这个处理器这边呢

动态的来进行什么呢

解析

那么我们需要使用什么呢

你传过来的这个id

来作为我们这个parameter它的值

所以它俩呢,是应该有一个对应关系的

然后具体的这个参数名

你看它俩是一致的

然后假设它传过来的值是100,对吧

假设这个id传过来的值是100

那这样的话呢

我们经过加这个注解之后

它最终的就会把我们这个方法它的返回值

这个address book对象呢

进行一个缓存

那么缓存的时候呢

这个key呢就是什么呢

就是我们这个region加上一个冒号

再加上这个key

也就是ab

然后再加上一个冒号

再加上它具体传过来的这个值

假设是100

那这样的话呢

最终构成的这个串

最终构成的这个串

就是我们的key

那么它是这么一个规则

它是这么一个规则

所以说呢

这是我们先来说了一下

我们如果后边所有的都已经写完了

要应用的时候呢

我们直接加这么一个注解

最终呢

它形成的那个唯一标识

就是由这三部分来构成的

对吧

分别是region还有key

然后就是这个parameter

那么关键呢

就在于这个parameter

因为它是一个动态解析的

它所对应的是我们这传过来的这个id的值

所以说呢

这个地方呢

它俩必须名字一致的

要不然的话

你这随便写一个

对吧

随便写一个abc

那这样的话呢

它根本就获取不到值

它根本就获取不到值

因为我们这传过来的这个参数名

是不是叫id呀

所以说呢

它俩必须保持一致

这是因为我们到时候在处理器里面解析的时候呢

就是按照这个相同的这个参数名来进行解析

然后呢

解析出来之后

把这个id具体的值

假设是100

对吧

最终给它拼到这个串里面去

好

所以说呢

这是我们如何来应用

好

那假设呢

我们现在呢

想清理缓存

比如说我在这呢

有一个

你看咱们这是不是有一个delete方法呀

对吧

你看我们原先调用的这种原生的api

对吧

来清理

那现在呢

我们就可以这样来写了

这样来写

就是通过我们这个什么呢

cache evict

对吧

这是咱们定义的这个

而这个cache evict里边呢

我们是不是要来指定具体要清理哪个缓存

通过cache来指定

所以在这呢

我们来指定什么呢

你注意看

它是不是一个这个

包括

这个Value号啊

相当于它是一个数组

对吧

数组类型

但是这个Value呢

我们可以省略

对于Value呢

可以省略

所以这块呢

我们就可以减写成这个

这个Value等号就可以去掉了

然后这里边写什么呢

就是写我们的cache

因为你看它是cache这种类型

所以我们在这来写cache

然后cache的话呢

这里面是不是又有regent

这里面又有

这得加一个at

然后呢

在这呢

来指定什么regent

对吧

这个regent的话呢

我们就来address book

这又一样了

对吧

address book

然后呢

在这是不是来指定key

假设这个key呢

还是ab

然后呢

又是parameters

对吧

这个parameters呢

又是id

注意

这个parameters呢

这个地方这个id

还是需要跟这个参数名保持一致

对吧

那这样的话

它在清理的时候呢

又是把这三部分是不是连成串

对吧

连成串

然后呢

最终拼成的呢

跟我们当时设置的时候

这个

key呢

是保持一致的

这个唯一标是保持一致

这样的话呢

我们缓存的时候呢

加这个注解

清理的时候呢

加这个catchEvaked注解

对吧

然后呢

它就可以清理指定缓存了

那么比如说我们所有的都已经写完了

对吧

我应用完之后呢

我们其实这块呢

就可以直接把这句话给去掉了

就不用再去调用它原生API了

对吧

因为我们已经加了这个注解了

包括我们这个地方

你看我们是不是想缓存数据啊

缓存数据的时候呢

因为我已经加了这个注解了

所以我们这个代码里边跟注解相关的这些代码

这个

还有这个其实都可以去掉了

你看最终呢

就变成了这里面只有这一句

操作数据库的这一句

对吧

那么当我们第一次调用这个方法的时候呢

因为还没有缓存数据

对吧

所以说呢

我们当前这个方法呢

就会被调用

那这里面它就会查明数据库

查完数据库之后是不是把这个结果返回

那

这个时候呢

我们就已经进行了缓存

因为加了这个注解

所以当我们第二次再调这个方法

当然了

你传过来ID还是同一个ID

对吧

那么因为前面的已经缓存了

所以这个时候呢

它就会直接从缓存这边来走

所以当前这个方法呢

就不会不再执行了

相当于直接在我们处理器那边就已经返回了

所以这个数据库呢

就不再多次查询了

这就是我们应用完咱们这个注解之后呢

我们的程序代码呢

其实它就变成了这么一个效果了

但是现在呢

我们还没有完全实现

咱们只是把注解定义上了

对吧

这只是我们先来给大家演示一下

如果说我们所有的都实现了

从应用上面来说

其实就是这个样子的

然后这儿呢

清理缓存这句代码呢

也就不需要了

你看这里面就跟缓存相关的这些

Java代码就都没有了

那么最终呢

就是这么一个效果

这是我给大家来展示一下

我们如果说所有的代码都实现了

那么我们在应用的时候如何来使用这个注解

好

我来按了这点

然后我进入那个栏

开始键暗注进去

表示可以 Beго 雙和

ás

as

ーヾ

looks.

Let's go

姜

G

朝

avi

st

s

te

m

officer

勿

cast

St

em

s

as

消

s

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的 Java 项目中，如何使用自定义注解 `@CacheEvict` 来实现缓存的读取（`@Cache`）和清除（`@CacheEvict`）功能。讲师通过在 `AddressBookController` 中的 `detail` 和 `del` 方法上添加注解，演示了如何将缓存操作与业务逻辑解耦。核心内容包括：
*   **缓存读取 (`@Cache`)**：在查询方法上使用 `@Cache` 注解，通过 `cacheChannel.get(region, id)` 从缓存中获取数据，若缓存命中则直接返回，避免数据库查询。
*   **缓存写入 (`@Cache`)**：在成功查询到数据后，通过 `cacheChannel.set(region, id, addressBook)` 将数据写入缓存。
*   **缓存清除 (`@CacheEvict`)**：在删除方法上使用 `@CacheEvict` 注解，通过 `cacheChannel.evict(region, id)` 清除缓存中对应的数据，确保数据一致性。
*   **自定义注解 `@CacheEvict`**：讲师还展示了自定义注解 `@CacheEvict` 的源码，它是一个 `@Retention(RUNTIME)` 的接口，用于在运行时动态处理缓存清除逻辑。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 展示 `AddressBookController` 中的 `detail` 方法，演示缓存读取逻辑。
*   **00:05 - 00:10**: 为 `detail` 方法添加 `@Cache` 注解，并演示其作用。
*   **00:10 - 00:15**: 展示 `@CacheEvict` 注解的源码，解释其定义。
*   **00:15 - 00:20**: 在 `del` 方法上添加 `@CacheEvict` 注解，演示缓存清除逻辑。
*   **00:20 - 00:25**: 展示 `@CacheEvict` 注解的使用方式和效果。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **代码片段 1 (缓存读取)**：
    ```java
    @GetMapping("/detail/{id}")
    @Cache(region = "addressBook", key = "ab", params = "id")
    public AddressBook detail(@PathVariable(name = "id") String id) {
        // 查询缓存
        CacheObject cacheObject = cacheChannel.get(region, id);
        if (cacheObject.getValue() != null) {
            return (AddressBook) cacheObject.getValue();
        }

        AddressBook addressBook = addressBookService.getById(id);
        if (addressBook != null) {
            // 写入缓存
            cacheChannel.set(region, id, addressBook);
        }

        return addressBook;
    }
    ```

*   **代码片段 2 (缓存清除)**：
    ```java
    @DeleteMapping("/id")
    @CacheEvict(region = "addressBook", key = "ab", params = "id")
    public Result del(@PathVariable(name = "id") String id) {
        boolean result = addressBookService.removeById(id);
        if (result) {
            // 清理缓存
            cacheChannel.evict(region, id);
        }
        return Result.ok();
    }
    ```

*   **自定义注解 `@CacheEvict` 源码**：
    ```java
    package com.itehima._2cache.annotation;

    import java.lang.annotation.*;

    @Documented
    @Target(ElementType.METHOD)
    @Retention(RetentionPolicy.RUNTIME)
    public @interface CacheEvict {
        Cache[] value() default {};
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景 1: 缓存读取演示**
    *   讲师在 `AddressBookController` 的 `detail` 方法上添加了 `@Cache` 注解。
    *   代码逻辑首先尝试从缓存中获取数据 (`cacheChannel.get(region, id)` )。
    *   如果缓存命中 (`cacheObject.getValue() != null`)，则直接返回缓存中的数据，避免了数据库查询。
    *   如果缓存未命中，则从数据库查询数据 (`addressBookService.getById(id)`)，并将查询到的数据写入缓存 (`cacheChannel.set(region, id, addressBook)`)，以供下次查询使用。

*   **场景 2: 缓存清除演示**
    *   讲师在 `AddressBookController` 的 `del` 方法上添加了 `@CacheEvict` 注解。
    *   代码逻辑首先执行数据库删除操作 (`addressBookService.removeById(id)`)。
    *   如果删除成功 (`result == true`)，则立即调用 `cacheChannel.evict(region, id)` 清除缓存中对应的数据。
    *   这样可以确保缓存中的数据与数据库中的数据保持一致，避免了缓存雪崩和数据不一致的问题。

*   **场景 3: 自定义注解 `@CacheEvict` 源码展示**
    *   讲师切换到 `CacheEvict` 注解的源码文件。
    *   展示了注解的定义，包括 `@Documented`、`@Target(ElementType.METHOD)` 和 `@Retention(RetentionPolicy.RUNTIME)`。
    *   通过 `Cache[] value() default {};` 定义了注解的参数，用于指定缓存的区域和键。

---

以上是根据视频画面截图进行的结构化技术分析。
