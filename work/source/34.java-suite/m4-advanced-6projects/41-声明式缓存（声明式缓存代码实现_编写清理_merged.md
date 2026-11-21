# 41-声明式缓存（声明式缓存代码实现_编写清理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才呢

咱们这个清理缓存的这个注解处理器呢

已经写好了

那接下来呢

我们可以来测试一下

现在呢

我把服务呢

也重启完了啊

重启完之后呢

我们现在呢

就可以再来测试一下

那么我们可以通过调用我们导入的这个controller的哪个方法呢

咱们就调这个方法就可以啊

就是这个evict方法

对吧

那么它是一个这种get的方式请求

把ID给我们传过来

好

然后呢

我们调它

调它的时候呢

它就会给我们清理

咱们可以来看一下

我们这里边呢

是不是那会儿测试的时候呢

有这么两个缓存数据

重新刷新一下

确认一下这个数据

稍等一下

它这个因为是远程的

这个反应速度稍微有点慢

重新这个disconnect的

重新连接一下

好

那么这是咱们那会儿呢

刚才测试的这两条数据

对吧

一个ID是123

还有一个是1234

然后现在呢

我就需要把它

给清理掉

那么怎么清理呢

就调用我们当前这个方法

evict这个方法

好

然后呢

我们把这边来刷新一下

这度cat control了

然后里边呢

我们找一下

应该是这个方法

evict这个方法

好

然后呢

try it out

咱们输入一个什么呢

123

注意啊

我们可以加一个断点

咱们来跟一下

来跟一下

从哪跟呢

还是

先把其他的都关上

有点乱

还是从我们这个拦截器这开始跟

注意

这回呢

我们应该进的就是

下面这个方法了

对吧

因为它拦截的是cat evict

好

在这加一个断点

注意看啊

我现在呢

直接走

好

他已经过来了

好

你看

在这呢

也能够看到啊

我们当前这个

拦截器

它拦截到的这个目标对象呢

还是这度cat control了

方法呢

就是这个evict的方法

参数呢

我们传过来的还是123

对吧

然后呢

我们继续往下走

注意看啊

走

走

走

解析注解

好

这已经解析完了

好

都已经这个从这能看到

对吧

这个value这

你看啊

有key是user

然后呢

这个地方呢

不太一样啊

因为我们这个地方

这个key是user

刚才呢

我们这边呢

设置的这个缓存数据呢

不一样

他们不是一套啊

所以应该是清理不了

你看这边

这边的话

你看

我们现在设置的是什么呢

再来看一下

看这个

你看它这个区域的话呢

这个region是2x

对吧

对吧

然后呢

这个key是user

跟我们刚才设置的数据呢

不一致

但是不妨碍它执行啊

不妨碍它执行

然后呢

我们可以来看一下

走

好

走

它获得这个处理器

对吧

获得处理器

然后呢

我们看处理器里面

这两个属性

一个是catch channel

已经封装好了

还有一个是catch list

对吧

也已经封装好了

是user

冒号123

region是2x

好

那这个时候呢

它执行process方法

一执行的话呢

它是不是就

到了我们这个process这儿了

然后在这儿加一个断点

好

放行过来

然后这里边呢

因为这个缓存数据呢

它其实不存在

对吧

它不存在

好

你看

它又报了这么一个错误

来看一下

应该又是那个连接超时了

对吧

这个连接中断了

还是这个问题

当然了

我们可以重新再来一次啊

重新再来一次执行

好

然后呢

往那放

好

又到这儿来了

对吧

然后呢

走

走

好

evict执行

它并没有报错

对吧

它并没有报错

但是呢

因为缓存数据不存在啊

好

走

然后呢

它是不是要调用我们这个目标对象

对吧

调用目标对象的这个方法

也就是调到我们control了的这个

这个地方

这个方法

好

然后呢

我们在这加一个断点

走过来

好

你看它是不是执行到这边来

然后呢

程序往下走一步

控制台删除数据库

看到这一句

然后呢

返回一个这个什么evict的success

对吧

好

这个流程已经走完了

流程已经走完了

你看这是不是已经返回了

但是呢

这个缓存数据它肯定是没有清掉的

因为我们刚才这个接口清的不是这个缓存数据

连region都不一样

那怎么办呢

我们需要用同一套啊

咱们可以来看一下

我们可以来设置一下

设置的时候呢

咱们调哪个方法呢

调

上面这个方法

你看这个是rx

什么user

然后这个是id

对吧

然后呢

我们调这个方法

这个是get

什么

cachedata

咱们调这个方法

getcachedata

应该是这个

好

然后呢

try it out

把这个id传过去

这个id呢

我来个101

好

注意看

执行

好

它已经执行完了

你看这是返回的结果

对吧

返回的结果

然后呢

我们看这个

这边重新刷一下

好

你看是不是变成三个rx

这里边是不是多出来一个101

现在呢

我就需要来把它清理掉

把它清理掉

怎么清理呢

还是调我们刚才这个evict的这个方法呢

对吧

那么需要传过去的这个id呢

就是什么呢

注意这evict的方法

传过去的id是101

好

执行

好

又到这边来了

对吧

然后呢

我们直接放行

走

到这来

它是不是开始清理

好

现在呢

其实已经清理完了

然后呢

我们放行

让它执行到我们真正的目标方法

你看这边

好

又到这边来了

好

现在呢

这个数据呢

已经这个清理完了

缓存数据已经清理完了

咱们重新在这review一下

reload一下

应该是不是又变成两个了

2x那个就不存在了

好

这是我们测试了一下

这个清理缓存是没有问题的

大家注意的时候

测试的时候也一定要小心一点

你看看它清理的跟我们设置的

当时是不是同一套

对吧

如果不是同一套的话

它肯定是清理不成功的

那么这个region我们是2x

并且呢

在我们这个地方呢

我其实都已经定义好了

你看我们这两个区域

一个是2x

一个是addressbook

好

这是我们测试了一下

还有其他的

比如说我们来加一个这种缓存

来加一个这个

你看我是不是只有region还有key

而没有那个parameter

那这样的话

它最终生成的那个key呢

就是什么呢

就是我们那个users

好

当然了

还要加上前面

最终设置到我们这个j2cache当中之后

设置到redis当中之后呢

它是把这个region

还有这两个是给我们加一块的

好

咱们可以调一下这个方法

这个叫做getAllData

而这个呢

这个方法呢

不需要这个参数

好

来看一下

getAllData

就是这个

好

我们来调一下这个接口

注意看

走

好

调用

这个是反回来

反过来对吧

再调的话又反回了

然后这个时候呢

它应该已经给我们把缓存设置好了

你看

这是不是users

好

然后我们要清理它呢

对应的应该调哪个方法去清理呢

那你看啊

它这个key是不是users

region是2x

那你看谁清理的是这个呀

应该就是这个

这个方法

你看

2x users

然后呢

也是没有设置那个parameter

所以说它最终这个key呢

也是这个值

那么调用的方法呢

就是这个evakedAll这个方法

evakedAll就是这个方法

好

然后呢

我们来执行这个没有参数

走

好

这边呢

直接过了

走

走

好

它已经清理完了

清理完之后呢

把这边重新来刷新一下

reload一下

你看是不是又清理掉了

好

把那个users就给清理掉了

这是我们整体来测了一下

大家呢

也可以自己来测一下

那么我们这个control里面这些方法呢

都是经过测试的

都是没有问题的

大家呢

也可以自行来测试一下

好

那么关于我们这个声明式缓存呢

我们就说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频课程主要讲解如何在 Spring Boot 项目中，通过自定义注解和 AOP（面向切面编程）技术，实现对缓存的“驱逐”（Evict）功能。核心内容包括：
- **目标**：为 `@CacheEvict` 注解提供一个可编程的、支持动态参数（如 region, key, params）的缓存驱逐功能。
- **技术栈**：Java, Spring Boot, Spring AOP, 自定义注解处理器。
- **核心流程**：
  1.  在控制器方法上使用 `@CacheEvict` 注解，指定缓存驱逐的规则。
  2.  AOP 切面 `CacheMethodInterceptor` 捕获带有该注解的方法调用。
  3.  切面通过 `CacheEvictAnnotationProcessor` 处理注解信息，解析出 `region`, `key`, `params` 等参数。
  4.  调用 `CacheChannel` 的 `evict` 方法，根据解析出的参数，从缓存中移除指定数据。
  5.  最终调用原方法，完成业务逻辑。
- **演示**：通过 Swagger UI 调用接口，观察控制台日志和缓存驱逐效果。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**：课程开场，展示项目结构和 `CacheEvictAnnotationProcessor` 类的初始化代码。
*   **00:06 - 00:15**：介绍 `CacheMethodInterceptor` 类，展示其 `@Around` 切面方法，用于拦截带有 `@CacheEvict` 注解的方法。
*   **00:16 - 00:25**：深入 `CacheMethodInterceptor` 的 `invokeCacheEvictAllMethod` 方法，展示如何通过 `AnnotationUtils.findAnnotation` 获取注解信息，并创建处理器。
*   **00:26 - 00:35**：进入 `CacheEvictAnnotationProcessor` 的 `process` 方法，展示如何遍历注解信息列表，解析 `region` 和 `key`。
*   **00:36 - 00:45**：演示 `CacheChannel.evict(region, key)` 方法调用，观察控制台日志输出“清理缓存处理...”。
*   **00:46 - 00:55**：展示 `JCacheController` 中的 `evict` 方法，演示如何在控制器中使用 `@CacheEvict` 注解。
*   **00:56 - 01:05**：通过 Swagger UI 调用 `evict` 接口，观察控制台日志和缓存驱逐效果。
*   **01:06 - 01:15**：展示 `CacheChannel` 的 `evict` 方法实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **01:16 - 01:25**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **01:26 - 01:35**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **01:36 - 01:45**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **01:46 - 01:55**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **01:56 - 02:05**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **02:06 - 02:15**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **02:16 - 02:25**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **02:26 - 02:35**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **02:36 - 02:45**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **02:46 - 02:55**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **02:56 - 03:05**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **03:06 - 03:15**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **03:16 - 03:25**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **03:26 - 03:35**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **03:36 - 03:45**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **03:46 - 03:55**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **03:56 - 04:05**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **04:06 - 04:15**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **04:16 - 04:25**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **04:26 - 04:35**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **04:36 - 04:45**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **04:46 - 04:55**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **04:56 - 05:05**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **05:06 - 05:15**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **05:16 - 05:25**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **05:26 - 05:35**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明其如何根据 `region` 和 `key` 驱逐缓存。
*   **05:36 - 05:45**：展示 `CacheEvictAnnotationProcessor` 的 `process` 方法中，如何处理 `params` 参数，并将其添加到 `cacheList` 中。
*   **05:46 - 05:55**：展示 `CacheChannel` 的 `evict` 方法的完整实现，说明
