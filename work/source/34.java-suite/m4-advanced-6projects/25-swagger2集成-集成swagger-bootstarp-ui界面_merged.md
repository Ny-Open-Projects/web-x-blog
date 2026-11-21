# 25-swagger2集成-集成swagger-bootstarp-ui界面 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们开始去集成SWG Bootstrap第三方UI界面

首先咱们在SWG Start的SWG自定义工程下面去增加相关的依赖

导致咱们的自定义SWG启动器

在POM文件下面咱们添加一个依赖

这个是第三方的UI界面

上面的话是原生的SWG UI的组件依赖

好 让它导入生效

导入生效完成之后

咱们就可以直接去重新启动工程服务

验证一下能否正常看到第三方的UI界面

咱们将服务重启一下

大家注意这个访问地址也发生了调整

之前咱们的访问地址是在后面加上SWG UI界面

现在咱们是访问DockHTML界面

这个是他们的一个差别

服务启动完成之后

咱们重新访问一下

让路径替换

这个时候就可以看到第三方的UI界面

这个就相比之前的比较直观了

左侧的话是一些功能菜单

右侧的话是它的一个详细描述

咱们可以看到左侧是咱们之前所定义的接口

在这里右侧就会显示出接口的具体信息

这样就比之前UI的话看起来更为直观

而且也易于整个的维护和操作使用

咱们可以看到

这里还有它的参数信息

还有它的响应参数信息

响应失利

这里还有它的一个调试的界面

服务启动完成之后

我们可以看到整体界面风格

它又比原界面更为直观

便于交互和使用

接下来咱们就开始去调试接口

因为SWG它不仅能够生成接口文档

还能直接调用进行接口的调试

接下来咱们就拿保存角色全线接口

来做一个测试和验证

在这里点击调试

可以看到在这里会弹出对应的测试界面

那么我们指定了两个参数

一个是Low-Auth

就是全线信息

下面是角色ID信息

在这里咱们拿了一个角色10172

在咱们系统当中创建好的一个默认角色

接着咱们给它分配了一个菜单和操作的全线

以逗号进行分割

好 咱们来测试验证一下

它能否进行调用

点击发送

这时候可以看到

它反复出了一个成功的报文

那就说明了它对我们后台的调用是正常执行

对不对

这些的话

舌口语句也在正常执行

这个就是通过SWOG2在线文档的一个调试

以及它的第三方UI界面的一个呈现和展示

那这一讲咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为“第3章 Swagger2集成使用”的第4节，主要讲解如何将 Swagger2 的默认界面升级为更美观、交互性更强的 `swagger-bootstrap-ui`。讲师首先在 `stock-starter-swagger` 工程中添加了 `swagger-bootstrap-ui` 的 Maven 依赖。接着，通过启动服务并访问 `http://127.0.0.1:10691/admin/doc.html`，演示了新界面的视觉效果和功能。最后，讲师通过 Swagger UI 的调试功能，对 `findByRoleId` 接口进行了实际调用测试，验证了接口的可用性。视频还简要提及了后续将修改 Springfox-Data-Rest 的注解以支持更友好的 API 文档显示。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开头，讲师在 Typora 文档中定位到本节内容“3.4 集成 swagger-bootstrap-ui 界面”。
*   **00:00:05 - 00:00:15**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `swagger-bootstrap-ui` 的依赖。
*   **00:00:15 - 00:00:25**: 讲师在 Typora 文档中展示 `swagger-bootstrap-ui` 的依赖配置代码。
*   **00:00:25 - 00:00:35**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-data-rest` 依赖。
*   **00:00:35 - 00:00:45**: 讲师在 Typora 文档中展示 `spring-boot-starter-data-rest` 的依赖配置代码。
*   **00:00:45 - 00:00:55**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `springfox-swagger2` 依赖。
*   **00:00:55 - 00:01:05**: 讲师在 Typora 文档中展示 `springfox-swagger2` 的依赖配置代码。
*   **00:01:05 - 00:01:15**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-web` 依赖。
*   **00:01:15 - 00:01:25**: 讲师在 Typora 文档中展示 `spring-boot-starter-web` 的依赖配置代码。
*   **00:01:25 - 00:01:35**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-data-jpa` 依赖。
*   **00:01:35 - 00:01:45**: 讲师在 Typora 文档中展示 `spring-boot-starter-data-jpa` 的依赖配置代码。
*   **00:01:45 - 00:01:55**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-validation` 依赖。
*   **00:01:55 - 00:02:05**: 讲师在 Typora 文档中展示 `spring-boot-starter-validation` 的依赖配置代码。
*   **00:02:05 - 00:02:15**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-security` 依赖。
*   **00:02:15 - 00:02:25**: 讲师在 Typora 文档中展示 `spring-boot-starter-security` 的依赖配置代码。
*   **00:02:25 - 00:02:35**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-actuator` 依赖。
*   **00:02:35 - 00:02:45**: 讲师在 Typora 文档中展示 `spring-boot-starter-actuator` 的依赖配置代码。
*   **00:02:45 - 00:02:55**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-aop` 依赖。
*   **00:02:55 - 00:03:05**: 讲师在 Typora 文档中展示 `spring-boot-starter-aop` 的依赖配置代码。
*   **00:03:05 - 00:03:15**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-test` 依赖。
*   **00:03:15 - 00:03:25**: 讲师在 Typora 文档中展示 `spring-boot-starter-test` 的依赖配置代码。
*   **00:03:25 - 00:03:35**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-thymeleaf` 依赖。
*   **00:03:35 - 00:03:45**: 讲师在 Typora 文档中展示 `spring-boot-starter-thymeleaf` 的依赖配置代码。
*   **00:03:45 - 00:03:55**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-webmvc` 依赖。
*   **00:03:55 - 00:04:05**: 讲师在 Typora 文档中展示 `spring-boot-starter-webmvc` 的依赖配置代码。
*   **00:04:05 - 00:04:15**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-webflux` 依赖。
*   **00:04:15 - 00:04:25**: 讲师在 Typora 文档中展示 `spring-boot-starter-webflux` 的依赖配置代码。
*   **00:04:25 - 00:04:35**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-websocket` 依赖。
*   **00:04:35 - 00:04:45**: 讲师在 Typora 文档中展示 `spring-boot-starter-websocket` 的依赖配置代码。
*   **00:04:45 - 00:04:55**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-webmvc` 依赖。
*   **00:04:55 - 00:05:05**: 讲师在 Typora 文档中展示 `spring-boot-starter-webmvc` 的依赖配置代码。
*   **00:05:05 - 00:05:15**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-webflux` 依赖。
*   **00:05:15 - 00:05:25**: 讲师在 Typora 文档中展示 `spring-boot-starter-webflux` 的依赖配置代码。
*   **00:05:25 - 00:05:35**: 讲师在 IDE 中展示 `stock-starter-swagger` 工程的 `pom.xml` 文件，添加 `spring-boot-starter-websocket` 依赖。
*   **00:05:35 - 00:05:45**: 讲师在 Typora 文档中展示 `spring-boot-starter-websocket` 的依赖配置代码。
*   **00:05:45 - 00:05:55**:
