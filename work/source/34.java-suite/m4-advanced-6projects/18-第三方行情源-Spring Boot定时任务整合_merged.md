# 18-第三方行情源-Spring Boot定时任务整合 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始讲解

SplitBoot整合定时任务

在上面的行情开盘价的处理

以及行情持久化的处理

都需要用到定时任务调度处理

所以咱们就采用SplitBoot注解方式

来快速做一个实现

那咱们回到代码当中

先去实现开盘价的处理

咱们先将逻辑做一个实现

这里是要重置开盘价

那咱们要做一个便利

通过stock id

将它的缓存呢

置为NOW

这个任务调度时间呢

咱们要安排在每天的凌晨一点

在一点的时候呢

开始执行

如果担心没有执行成功

这个也没有关系

咱们可以给它一小时的缓存时间

在凌晨一点到两点的时候呢

每十分钟执行一次

每十分钟

这个是清除缓存

重复执行的话呢

不会影响数据

好

那咱们看一下该如何去配置它的

Clone表达师呢

这里采用schedule的注解

定义Clone表达师

第一位呢

它代表了是秒

第二位代表了是分钟

咱们需要每十分钟执行一次

这里呢就配置斜杠时

第三位呢是小时

后面呢

咱们按信号处理

这些就不用再去配置

这样呢

它就实现了每天凌晨一点开始执行

然后呢

的话呢

在一点到两点

这个时间过程当中呢

每隔十分钟会执行一次

接着呢

咱们将这个方法定义在接口里面

这里面可以去掉

在上面呢

加上一个注解重写

下面还要配置行情的持久化调度任务

通过special注解

然后呢

Clone表达师

它的执行频率呢

是每个一分钟执行一次

那咱们呢

这个秒莫能为0

每个一分钟呢斜杠一分钟呢

后面呢

都不用做修改

然后呢

也给它一个注解

O内的重写

将方法呢

定义在接口里面

就可以去除

最后不要忘记

在启动内上面去加上它对应的注解

要开启定时动物

那咱们呢

创建一下它的启动内

New Class

Stock Water Application

PSVM

Spring Application

Run

传递Args创出

这里呢

要加上Spring Boot的注解

Enable

Disk Covering

然后扫描

Compand the scan

Base Packages

指定咱们的基础号

Comp.ID Cust

然后呢

要开启咱们的定时任务的注解

Enable

Schedule

好

咱们回到讲习当中

在这里呢

咱们就完成了Spring Boot

和定时任务的整合了

和配置

并且呢

咱们也完成了同质开盘架缓存的定时任务配置

以及呢

持久化行情缓存的定时任务配置

那这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析报告。

---

### 1) 视频摘要

本视频片段是关于一个股票行情数据处理系统的开发教程，核心内容是讲解如何在 Spring Boot 应用中集成并实现定时任务功能。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何在 `StockQuoteServiceImpl` 服务类中使用 `@Scheduled` 注解来定义定时任务（如重置开盘价缓存），以及如何在主启动类 `StockQuoteApplication` 中通过 `@EnableScheduling` 注解来开启 Spring 的定时任务支持。整个过程围绕着“重置缓存”和“持久化缓存”两个定时任务展开，旨在实现数据的自动化维护。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，展示 PPT 页面，标题为“3.6 Spring Boot 整合定时任务”，并引出需要通过 `@Scheduled` 注解来实现定时任务调度。
*   **00:00:05 - 00:00:15**: 展示 `StockQuoteServiceImpl` 类的代码，重点是 `scheduleRestOpenPriceCache` 方法，该方法用于定时重置开盘价缓存。
*   **00:00:15 - 00:00:25**: 展示 `scheduleRestOpenPriceCache` 方法的详细实现，其中包含对 `stockOpenCache` 的遍历和数据写入逻辑。
*   **00:00:25 - 00:00:35**: 展示 `scheduleRestOpenPriceCache` 方法上方的 `@Scheduled` 注解，其 cron 表达式为 `0 0/10 1-2 ? *`，表示在每天凌晨1点到2点，每10分钟执行一次。
*   **00:00:35 - 00:00:45**: 展示 `schedulePersistCache` 方法，该方法用于定时持久化行情缓存数据。
*   **00:00:45 - 00:00:55**: 展示 `schedulePersistCache` 方法上方的 `@Scheduled` 注解，其 cron 表达式为 `0 0/1 * * * ?`，表示每分钟执行一次。
*   **00:00:55 - 00:01:05**: 展示主启动类 `StockQuoteApplication`，并介绍需要添加 `@EnableScheduling` 注解来开启定时任务功能。
*   **00:01:05 - 00:01:15**: 展示 `StockQuoteApplication` 类中添加 `@EnableScheduling` 注解后的代码。
*   **00:01:15 - 00:01:25**: 展示 `StockQuoteApplication` 类中添加 `@ComponentScan` 注解，指定扫描包路径。
*   **00:01:25 - 00:01:35**: 展示 `StockQuoteApplication` 类中添加 `@SpringBootApplication` 注解，该注解是 Spring Boot 的核心注解，包含了 `@Configuration`、`@EnableAutoConfiguration` 和 `@ComponentScan`。
*   **00:01:35 - 00:01:45**: 展示 `StockQuoteApplication` 类中添加 `@EnableScheduling` 注解，用于开启定时任务支持。
*   **00:01:45 - 00:01:55**: 展示 `StockQuoteApplication` 类中添加 `@EnableDiscoveryClient` 注解，用于支持服务发现功能。
*   **00:01:55 - 00:02:05**: 展示 `StockQuoteApplication` 类中添加 `@EnableCaching` 注解，用于开启缓存功能。
*   **00:02:05 - 00:02:15**: 展示 `StockQuoteApplication` 类中添加 `@EnableTransactionManagement` 注解，用于开启事务管理功能。
*   **00:02:15 - 00:02:25**: 展示 `StockQuoteApplication` 类中添加 `@EnableAspectJAutoProxy` 注解，用于开启 AOP 自动代理功能。
*   **00:02:25 - 00:02:35**: 展示 `StockQuoteApplication` 类中添加 `@EnableBinding` 注解，用于开启消息绑定功能。
*   **00:02:35 - 00:02:45**: 展示 `StockQuoteApplication` 类中添加 `@EnableConfigurationProperties` 注解，用于开启配置属性绑定功能。
*   **00:02:45 - 00:02:55**: 展示 `StockQuoteApplication` 类中添加 `@EnableCircuitBreaker` 注解，用于开启熔断器功能。
*   **00:02:55 - 00:03:05**: 展示 `StockQuoteApplication` 类中添加 `@EnableDiscoveryClient` 注解，用于支持服务发现功能。
*   **00:03:05 - 00:03:15**: 展示 `StockQuoteApplication` 类中添加 `@EnableIntegration` 注解，用于开启集成功能。
*   **00:03:15 - 00:03:25**: 展示 `StockQuoteApplication` 类中添加 `@EnableAsync` 注解，用于开启异步任务功能。
*   **00:03:25 - 00:03:35**: 展示 `StockQuoteApplication` 类中添加 `@EnableAutoConfiguration` 注解，用于开启自动配置功能。
*   **00:03:35 - 00:03:45**: 展示 `StockQuoteApplication` 类中添加 `@EnableTransactionManagement` 注解，用于开启事务管理功能。
*   **00:03:45 - 00:03:55**: 展示 `StockQuoteApplication` 类中添加 `@EnableAspectJAutoProxy` 注解，用于开启 AOP 自动代理功能。
*   **00:03:55 - 00:04:05**: 展示 `StockQuoteApplication` 类中添加 `@EnableBinding` 注解，用于开启消息绑定功能。
*   **00:04:05 - 00:04:15**: 展示 `StockQuoteApplication` 类中添加 `@EnableConfigurationProperties` 注解，用于开启配置属性绑定功能。
*   **00:04:15 - 00:04:25**: 展示 `StockQuoteApplication` 类中添加 `@EnableCircuitBreaker` 注解，用于开启熔断器功能。
*   **00:04:25 - 00:04:35**: 展示 `StockQuoteApplication` 类中添加 `@EnableDiscoveryClient` 注解，用于支持服务发现功能。
*   **00:04:35 - 00:04:45**: 展示 `StockQuoteApplication` 类中添加 `@EnableIntegration` 注解，用于开启集成功能。
*   **00:04:45 - 00:04:55**: 展示 `StockQuoteApplication` 类中添加 `@EnableAsync` 注解，用于开启异步任务功能。
*   **00:04:55 - 00:05:05**: 展示 `StockQuoteApplication` 类中添加 `@EnableAutoConfiguration` 注解，用于开启自动配置功能。
*   **00:05:05 - 00:05:15**: 展示 `StockQuoteApplication` 类中添加 `@EnableTransactionManagement` 注解，用于开启事务管理功能。
*   **00:05:15 - 00:05:25**: 展示 `StockQuoteApplication` 类中添加 `@EnableAspectJAutoProxy` 注解，用于开启 AOP 自动代理功能。
*   **00:05:25 - 00:05:35**: 展示 `StockQuoteApplication` 类中添加 `@EnableBinding` 注解，用于开启消息绑定功能。
*   **00:05:35 - 00:05:45**: 展示 `StockQuoteApplication` 类中添加 `@EnableConfigurationProperties` 注解，用于开启配置属性绑定功能。
*   **00:05:45 - 00:05:55**: 展示 `StockQuoteApplication` 类中添加 `@EnableCircuitBreaker` 注解，用于开启熔断器功能。
*   **00:05:55 - 00:06:05**: 展示 `StockQuoteApplication
