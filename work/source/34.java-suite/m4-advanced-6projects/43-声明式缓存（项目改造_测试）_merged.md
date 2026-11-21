# 43-声明式缓存（项目改造_测试） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 那么刚才咱们这个项目改造已经改造完了

那接下来我们可以来测试一下

我这儿的服务已经重启完了

重启完之后呢

我把这边也清理了一下

现在我们这个Redis当中是没有缓存数据的

好 那么我们就可以通过接口的方式来测试一下

好 先刷新一下

咱们要测的是这个address book controller

那么我们先来看一个detail

这个detail掉这个的时候呢

咱们是不是在这个方法上已经加了catch注解

好 那么这个ID的话呢

我们可以到数据库上面来找一下

咱们找一个存在的ID啊

好 那么连到我们这个远程的数据库上面来

找到我们这个users

然后这里边是不是有一个address book对吧

然后呢我们在这里边呢

可以来找一条数据啊

好 比如说我们现在呢

就找这么一条数据

就这条数据

好 我把它直接来复制一下

好 那么复制完

复制完之后呢

注意我这是复制了它的ID啊

然后呢我们把这个ID给它粘到这个位置来

好 粘过来

对吧 粘过来之后呢

注意看我执行 走

好 那么这个数据呢已经出来了

我们看啊 第一次访问的时候呢

它应该是访问操作数据库了

咱们看控制台输出

你看它是不是发出了一个select的语句

对吧 select语句

好 现在呢我再来执行 注意看啊

第二次我再来执行

好 数据又返回了 对吧

还是这个数据 没问题

然后我们看控制台

你看它并没有去发select

这就说明什么呢

说明它走的是缓存

然后呢我们到这里面来看一下

是不是真的有缓存数据

你看它是不是已经给我们这个缓存起来了

好 然后接下来呢我们看啊

当我执行delete的时候

就是删除这条数据的时候呢

它是不是就会清理

同时会清理这个缓存数据

好 所以说呢我们把这个

再调一下什么呢

调一下我们这个delete

这个方法

好 然后呢把这个ID呢

给它粘到这里

把它粘到这个位置来

注意看啊 我现在执行一下

好 这边有断点啊

咱们直接把这个断点放了

好 走

好 这儿也有断点

你看它是不是要给我清理 对吧

那我们就看一下吧

你看它要清理的这个region

是不是就是address book

然后呢这个key的话呢

是它已经动态拼完的

对吧 AV 后边冒号这一串

然后呢我们调用evac的方法

它这就清理了

清理完之后呢

它是不是要调用我们真正的目标方法

也就是调到我们这个

delete方法

这儿来了

好 在这儿呢

它因为要操作数据库了

对吧

真的要remove了

你看 操作数据库

好 这样就会真的删除掉

好 直接放行了

这些断点都不要了

你看控制台

是不是发了一个delete语句

对吧

然后现在呢我们来看

缓存数据应该是没有了

reload一下

应该是没有了

然后呢这个表里面的数据

肯定也就没有了啊

然后呢我们刷新一下

应该就没有了

好

所以这是我们测试了一下

是没有问题的

然后还有一个是

update的方法

咱们是不是也加了一个

清理的这个注解

对吧

所以我们也简单测一下

找一个新的ID吧

比如说我就来这个

咱们就随便来一个就行

复制

然后呢先调一下detail方法

一调这个方法的话

它是不是就会

这个给我们这个

设置缓存数据了

好 把它查出来

你看这个数据

然后到这边来看一下

好 又有了

对吧

然后呢我们调用

这个update的方法

咱们来这个设置一下它

update的方法也就是这个

好

然后try it out

注意这个ID的话呢

你必须得给我传过来

对吧

这个

但是这儿的话呢

也需要传一个ID

好

然后其他的这个值呢

其实改不改都可以啊

这都无所谓了

好

我们直接执行一下

好

这就执行完了

呃

这个地方呢

啊

它报了一个错

对吧

报了一个错

呃

应该是什么呢

这个这个这个日期

这个地方呢

给它传的格式不对啊

这个这个什么time对吧

然后呢

它这个格式不对

你看它这个格式是这样的啊

呃

年月日十分秒

好

干脆呢

我们直接把这个字段给它去掉就可以了

好

然后呢

再来执行

走

好

看这边是不是已经success

好

然后呢

我们来看一下它是不是真的改过来了

刷新一下

呃

刚才改的是哪条数据呢

不太好找了啊

呃

应该改的是哪条数据呢

应该改的是哪条数据呢

应该改的是这条数据对吧

然后呢

你看我们刚才给它传的参数呢

是不是全都是这种什么string

string

这种对吧

因为我没改啊

它这是默认给我们生成的啊

那么这块呢

它改的就是这个啊

这条数据

你看数据已经改过来了

然后呢

看缓存有没有给我们清理掉啊

咱们在这来reload一下

你看已经没有了啊

已经没有了

就是因为我们在这个update的这个方法上呢

加了这个evict这个注解

是吧

它在更新数据的时候呢

那么就已经把这个缓存数据给清理掉了

好

这是我们把这个项目啊

进行了一个改造

改造完成之后呢

那么也进行了一个测试

好

那么关于我们这个声明式缓存

我们就先说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频课程旨在演示如何在 Spring Boot 项目中，使用自定义注解 `@CacheEvict` 来实现缓存的更新（Invalidate）功能，从而替代原有的 `jCache` 缓存方案。课程通过一个“地址簿”（Address Book）的 CRUD 示例，详细讲解了如何在控制器层（Controller）中通过注解方式，自动触发缓存的清理操作。核心内容包括：在控制器方法上添加 `@CacheEvict` 注解，配置其 `region` 和 `key` 参数，以及通过自定义注解处理器（`CacheEvictAnnotationProcessor`）在运行时动态获取这些参数并调用缓存清理方法。课程还展示了如何通过 Swagger 接口进行测试，并通过 Redis Desktop Manager 验证缓存数据的更新。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:01:30**：课程开场，介绍项目背景和目标。展示项目结构，包括 `AddressBookController` 和 `AddressBookService`。
*   **00:01:30 - 00:03:00**：讲解 `@CacheEvict` 注解的基本用法。在 `AddressBookController` 的 `update` 方法上添加 `@CacheEvict` 注解，并配置 `region` 和 `key`。
*   **00:03:00 - 00:04:30**：演示如何通过 Swagger 接口调用 `update` 方法，并观察缓存数据的变化。
*   **00:04:30 - 00:06:00**：深入讲解自定义注解处理器 `CacheEvictAnnotationProcessor` 的实现。展示其如何通过 `ProceedingJoinPoint` 获取方法参数，并调用 `cacheChannel.evict(region, key)` 来清理缓存。
*   **00:06:00 - 00:07:30**：演示 `delete` 方法的缓存更新。在 `delete` 方法上添加 `@CacheEvict` 注解，并展示其在数据库删除后自动清理缓存的效果。
*   **00:07:30 - 00:09:00**：通过 Redis Desktop Manager 工具，验证缓存数据在更新和删除操作后确实被清除。
*   **00:09:00 - 00:10:30**：总结课程内容，强调自定义注解处理器在实现缓存更新方面的优势和灵活性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**：
    *   **6.3 项目改造**：PPT 显示了改造步骤，包括在启动类 `UserApplication` 上添加 `@EnableCache` 注解，以及修改 `AddressBookController` 使用注解方式替换原生 `jCache` 代码。
    *   **代码示例**：
        ```java
        @CacheEvict(region = "addressBook", key = "ab", params = "1.id")
        public Result update(@PathVariable(name = "id") String id, @RequestBody AddressBook entity) {
            // 业务逻辑
        }
        ```
        ```java
        @CacheEvict(region = "addressBook", key = "ab", params = "id")
        public Result del(@PathVariable(name = "id") String id) {
            // 业务逻辑
        }
        ```
        ```java
        // CacheEvictAnnotationProcessor.java
        public Object process(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
            for (AnnotationInfo<Cache> annotationInfo : cacheList) {
                String region = annotationInfo.getRegion();
                String key = annotationInfo.getKey();
                cacheChannel.evict(region, key);
            }
            return proceedingJoinPoint.proceed(proceedingJoinPoint.getArgs());
        }
        ```

*   **图表**：
    *   **Swagger 文档截图**：展示了 `address-book-controller` 的 API 接口，包括 `POST /addressBook/save`、`PUT /addressBook/{id}/update`、`DELETE /addressBook/{id}/del` 等。
    *   **Redis Desktop Manager 截图**：显示了 Redis 数据库中的键值对，用于验证缓存数据的更新。

*   **代码**：
    *   **控制器代码**：展示了 `AddressBookController` 中 `update` 和 `del` 方法的代码实现。
    *   **服务层代码**：展示了 `AddressBookService` 中的 `lambdaUpdate()` 方法，用于更新数据库。
    *   **注解处理器代码**：展示了 `CacheEvictAnnotationProcessor` 的核心逻辑，用于处理 `@CacheEvict` 注解并清理缓存。

---

### 4) 关键场景与演示描述

*   **场景一：控制器方法缓存更新**（时间点：00:01:30）
    *   **描述**：讲师在 `AddressBookController` 的 `update` 方法上添加 `@CacheEvict` 注解，并配置 `region` 和 `key` 参数。通过 Swagger 接口调用该方法，观察到缓存数据被自动更新。

*   **场景二：自定义注解处理器实现**（时间点：00:04:30）
    *   **描述**：讲师展示了 `CacheEvictAnnotationProcessor` 的实现代码。该处理器通过 `ProceedingJoinPoint` 获取方法参数，并调用 `cacheChannel.evict(region, key)` 来清理缓存。通过调试器观察到 `cacheList` 中包含 `@CacheEvict` 注解的信息。

*   **场景三：删除方法缓存更新**（时间点：00:06:00）
    *   **描述**：讲师在 `AddressBookController` 的 `del` 方法上添加 `@CacheEvict` 注解。通过 Swagger 接口调用该方法，观察到数据库记录被删除，同时缓存数据也被自动清理。

*   **场景四：Redis 缓存验证**（时间点：00:07:30）
    *   **描述**：讲师使用 Redis Desktop Manager 工具连接到 Redis 服务器，查看缓存数据。在执行 `update` 和 `del` 操作后，对应的缓存键值对被成功删除，验证了缓存更新功能的有效性。

*   **场景五：课程总结**（时间点：00:09:00）
    *   **描述**：讲师总结了课程内容，强调了自定义注解处理器在实现缓存更新方面的优势，如代码简洁、易于维护和扩展。鼓励观众在实际项目中应用该方案。

---
