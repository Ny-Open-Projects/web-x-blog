# 62-规则引擎Drools-Spring整合Drools（Spring — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,刚才咱们Spring Boot整合D-Rose代码都已经开发完成了

现在我们把这个项目跑起来

咱们来看一下能不能正常运行

因为是一个Spring Boot的工程

所以我们直接使用它这种Main方法

这种启动类的方式来运行就可以了

直接来启动一下

好,来观察一下我们这个控制台输出

看看有没有问题

好,现在已经跑起来了

现在已经跑起来了

它这个端口号就是我们在配置文件里面配置的8080

好,接下来我们来访问一下

然后直接来个Localhost

端口号是8080

然后请求路径,大家来看一下

再往后是不是要写我们的这个Controller的请求路径了

那就是-hello-ru了

就是这个路径

好,大家可以看到

我们这个页面上已经返回OK了

对吧

对吧

对吧

然后呢

看我们的控制台

看看是不是已经输出了

在这可以看到它确实已经输出了

这个规则触发了

这就是咱们在这个规则文件里面

是不是写的这个输出语句输出的

好,那么到这儿的话呢

这就说明我们基于Spring Boot

整合咱们这个D-Rose呢

就已经成功了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring Boot 的 DRL（Drools Rule Language）规则引擎项目的启动与初步配置过程。主要内容包括：
- **项目启动**：演示了如何在 IntelliJ IDEA 中运行 `DroolsApplication` 主类，成功启动嵌入式 Tomcat 服务器（端口 8080）。
- **服务验证**：通过访问 `http://localhost:8080/hello/rule` 验证了 Spring MVC 控制器的正常工作。
- **规则引擎集成**：展示了项目结构，包括 `HelloController` 控制器和 `rule_helloworld.drl` 规则文件，为后续的规则引擎功能演示做准备。
- **文档参考**：视频中切换到了一个 Markdown 文档，内容为课程讲义，明确指出当前步骤是“第八步：启动服务，访问 http://localhost:8080/hello/rule”，并介绍了 DROOLS 的 WorkBench 工具。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:04**: 展示项目结构和 `DroolsApplication.java` 主类代码。
*   **00:04 - 00:08**: 点击运行按钮，启动应用。
*   **00:08 - 00:12**: 查看终端日志，确认应用启动成功，Tomcat 服务已启动在 8080 端口。
*   **00:12 - 00:16**: 在浏览器中访问 `http://localhost:8080/hello/rule`，验证控制器功能。
*   **00:16 - 00:20**: 切换到 Markdown 文档，展示课程讲义内容，明确当前步骤为“第八步：启动服务，访问 http://localhost:8080/hello/rule”。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### **代码内容**

1.  **`DroolsApplication.java` (主类)**：
    ```java
    package com.itheima.drools;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;

    @SpringBootApplication
    public class DroolsApplication {
        public static void main(String[] args) {
            SpringApplication.run(DroolsApplication.class, args);
        }
    }
    ```
    *   **功能**：这是一个标准的 Spring Boot 启动类，用于启动整个应用程序。

2.  **`HelloController.java` (控制器)**：
    ```java
    import org.springframework.web.bind.annotation.RestController;

    @RestController("/hello")
    public class HelloController {
        @Autowired
        private RuleService ruleService;

        @RequestMapping("/rule")
        public String rule() {
            ruleService.rule();
            return "OK";
        }
    }
    ```
    *   **功能**：这是一个 RESTful 控制器，提供 `/rule` 接口。当访问此接口时，会调用 `RuleService` 中的 `rule()` 方法（该方法内部会触发 DRL 规则），并返回 "OK"。

3.  **`rule_helloworld.drl` (规则文件)**：
    ```drl
    package "helloworld"
    rule "rule_helloworld"
    when
        eval(true)
    then
        System.out.println("规则: rule_helloworld触发...");
    end
    ```
    *   **功能**：这是一个简单的 DRL 规则，条件为 `eval(true)`（永远为真），触发时会打印一条日志信息。这是为了演示规则引擎的触发机制。

#### **PPT / 文档内容**

*   **Markdown 文档 (课程讲义)**：
    *   **标题**: `第八步：启动服务，访问 http://localhost:8080/hello/rule`
    *   **内容**: 介绍了 DROOLS 的 WorkBench 工具，称其为 KIE-WB，是 Drools-WB 与 BPM-WB 的结合体，是一个可视化的规则编辑器。
    *   **章节**: `8.1 WorkBench简介`

---

### 4) 关键场景与演示描述

1.  **场景一：项目启动与日志监控 (00:04 - 00:12)**
    *   **描述**：讲师在 IntelliJ IDEA 中点击运行按钮，启动 `DroolsApplication`。随后，他将焦点切换到终端窗口，观察日志输出。
    *   **关键演示**：日志显示 `Tomcat started on port(s): 8080`，表明应用已成功启动并监听 8080 端口。日志中还包含 Spring Boot 的初始化信息，如 `Initializing Spring FrameworkServlet 'dispatcherServlet'`，证明了 Spring MVC 框架已加载。

2.  **场景二：服务验证与规则触发 (00:12 - 00:16)**
    *   **描述**：讲师在浏览器中输入 `http://localhost:8080/hello/rule` 并回车。
    *   **关键演示**：浏览器成功访问了该接口，返回了 "OK"。这表明 `HelloController` 中的 `rule()` 方法被正确调用。虽然视频中没有直接展示规则引擎触发的日志，但根据代码逻辑和后续的讲义内容，可以推断 `ruleService.rule()` 方法内部会触发 `rule_helloworld.drl` 中的规则，从而在控制台打印出 "规则: rule_helloworld触发..."。

3.  **场景三：课程讲义切换 (00:16 - 00:20)**
    *   **描述**：讲师切换到课程讲义文档，以确认当前步骤。
    *   **关键演示**：文档明确指出“第八步：启动服务，访问 http://localhost:8080/hello/rule”，并介绍了 WorkBench 工具，为后续的规则编辑和部署做铺垫。

---

**总结**：该视频片段是一个技术演示，旨在展示如何将 DROOLS 规则引擎集成到 Spring Boot 项目中，并通过简单的 HTTP 接口触发规则。整个过程清晰、步骤明确，为学习者提供了直观的实践指导。
