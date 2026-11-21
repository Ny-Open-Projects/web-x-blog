# 16-熔断器Hystrix简介

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\16-熔断器Hystrix简介_【海量资源尽在 ubkz.com】.mp4
- 时长 4分40秒（音频 280s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 熔断器Histrix简介在这一小节中我们的主要目标是了解熔断器Histrix的作用那现在我们打开讲义来了解熔断器HistrixHistrix在英文里面的意思是豪猪它的logo我们看下面的图看出来它是一头豪猪满身是刺满身的刺与伪装不过都是一种对自身的保护Histrix在微服系统中是一款提供保护机制的组件和Eureka一样也是由
[00:30] Netflix公司开发在讲解更多之前大家要跟我读两遍这个单词High Streaks不好发音的同学很抱歉我没有找到对应的中文对这个单词进行发音那接下来去查看一下High Streaks的主页访问这个链接打开主页在主页中描述了High Streaks的当前状态现在这个High Streaks项目是处于维护状态不在
[01:07] 进行新功能的开发不过在Spring Cloud项目中大多使用的还是High Streaks进行服务降级和熔断所以我们回到讲义中继续学习和了解High StreaksHigh Streaks的作用是什么呢具体要保护什么呢High Streaks是Netflix开源的一个延迟和容错库用于隔离防卫远程服务第三方库防止出现急连失败也就是High Streaks是一个库
[01:39] 可以做什么防止出现集联失败下面我们来了解雪崩问题微服中服务间调用关系错综复杂一个请求可能需要调用多个微服接口才能实现会形成非常复杂的调用链路我们看这个图一个请求要用到四个服务那这四个服务呢在正常提供的情况下这个请求是顺利的去被处理完的后面的请求也就也一样的
[02:10] 顺利的进入并处理如果在这个请求调用这些服务的过程中有一个服务出现了异常的话也就是出现异常那么这个请求呢就不能顺利的结束不能顺利结束的时候他就继续进行等待进行等待过程中Tomcat呢也不会释放这一个请求的现成那不释放的话越来越多的用户请求到来就会越来越多的现成会阻塞而服务器
[02:44] 支持的现成和并发数又有限请求一直阻塞那么会导致服务器资源耗尽从而导致所有其他的服务也都不可以使用形成雪崩效应也就是说请求越来越多一直被阻塞那么Tomcat的整个资源被耗尽导致最终整个Tomcat当机无法处理任何请求OK这就是一个雪崩效应
[03:12] 这就好比一个汽车生产线生产不同的汽车需要使用不同的零件如果某个零件因为种种原因无法使用那么就会造成整台车无法装配陷入等待零件的状态直到零件到位才能继续组装那这时候如果有很多其他车型都要用到这个零件整个工厂都将陷入等待的状态导致所有生产都陷入瘫痪那这也就是一个零件的波及范围不断被扩大那我们的
[03:43] 解决血泊问题的手段主要是服务降级那包括我们的现成隔离跟服务熔断具体我们后面会讲到OK这就是我们的的内容那么回到笔记中来进行小结是一个延迟和容错库他能够做什么呢用于隔离
[04:22] 访问远程服务防止出现集联失败这就是我们熔断器HighStrix的简介所有内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Hystrix 熔断器的作用、雪崩问题及其解决方案，包括线程隔离和服务降级。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/

画面 2:
- 浏览器页面：GitHub - Netflix/Hystrix
- 标题：Hystrix: Latency and Fault Tolerance for Distributed Systems
- 内容：Hystrix Status，说明 Hystrix 已进入维护模式，最新稳定版本为 1.5.18。

画面 3:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/

画面 4:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 5:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 6:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 7:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 8:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 9:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 10:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 11:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 12:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 13:
- PPT 标题：8. 熔断器 Hystrix
- 小节标题：8.1. 简介
- 内容：Hystrix 在英文里的意思是豪猪，它的 logo 看下面的图是一头豪猪，它在微服务系统中是一次提供保护机制的组件，和 Eureka 一样也是由 netflix 公司开发。
- 主页：https://github.com/Netflix/Hystrix/
- 问题：那么 Hystrix 的作用是什么呢？具体要保护什么呢？
- 解释：Hystrix 是 Netflix 开源的一个延迟和容错库，用于隔离访问远程服务、第三方，防止出现级联失败。

画面 14:
- 文档标题：Spring Cloud 一个不完整项目.md - Typora
- 内容：
  - 需求：可以使用 RestTemplate 访问 http://user-Service/user/ 获取服务数据。
  - 可以使用 Ribbon 负载均衡：在执行 RestTemplate 发送服务地址请求的时候，使用 Ribbon 负载均衡算法从服务地址列表中选择一个服务地址，访问该地址获取服务数据。
  - 实现步骤：
    1. 启动多个 user-Service 实例（9091,9092）；

