# 画面线理解：16-熔断器Hystrix简介

- 阶段：01.阶段一 微服务相关技术
- 章节：2.SpringCloud/day01
- 源文件：01.阶段一 微服务相关技术\2.SpringCloud\day01\16-熔断器Hystrix简介_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:17, 00:56, 01:22, 01:57, 02:14, 02:20, 02:27, 02:35, 02:47, 02:49, 02:58, 03:43, 04:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:16:25

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
  - 需求：可以使用 RestTemplate 访问 http://user-service/user/ 获取服务数据。
  - 可以使用 Ribbon 负载均衡：在执行 RestTemplate 发送服务地址请求的时候，使用 Ribbon 负载均衡算法从服务地址列表中选择一个服务地址，访问该地址获取服务数据。
  - 实现步骤：
    1. 启动多个 user-service 实例（9091,9092）；
