# 53-SpringBoot整合Drools_2 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

刚才咱们这个整合的代码呢

是已经写完了

那么我们直接来启动一下

咱们来启动一下我们这个

Spring Boot的这个项目

然后我们来测试一下

好

咱们这个项目呢

已经启动完了

这个端口号呢

是8080对吧

然后我们看看这个Controller

它是怎么访问的

这个Controller是

-hello-ru了对吧

然后呢

我们打开一个窗口

来访问一下这个Controller

最终呢

我们希望看到的效果

就是这个规则触发了就可以了

这就说明我们这个整合

是没有问题的

log host

然后呢是8080

8080

然后后边是hello

然后是ru了对吧

走

好

大家可以看到

我们这个地方呢

这个规则触发了对吧

这句话呢

是在哪输出的呢

其实就是在咱们这个规则文件

这个地方输出的

那么能够看到这句话

这就说明我们整个规则呢

正常能触发

这就说明我们这个

整合呢

是没有问题的

好

这是这块呢

也是比较简单的

那么主要的代码量呢

其实就是在咱们这个配置类这块

好

那么关于我们Spring Boot

整合D-Rose呢

我们就说到这

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频演示了一个基于 Spring Boot 的项目如何集成 Drools 规则引擎。主要内容包括：
- 创建一个 Spring Boot 项目并配置 Drools。
- 编写一个 `HelloController` 控制器，通过 `@Autowired` 注入 `RuleService`。
- 在 `RuleService` 中配置 Drools 的 `KieContainer` 和 `KieBase`。
- 在 `resources/rules` 目录下创建一个名为 `rule_helloworld.drl` 的规则文件。
- 规则文件中定义了一个简单的规则 `when eval(true) then System.out.println("规则: rule_helloworld触发...");`。
- 通过访问 `http://localhost:8080/hello/rule` 触发控制器方法，进而触发规则引擎执行规则。
- 视频展示了项目结构、代码编写、运行日志以及规则触发的控制台输出。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面没有明确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **00:00 - 00:05**: 项目结构概览。展示 IntelliJ IDEA 中的项目结构，包括 `src/main/java`、`src/main/resources` 和 `src/test` 目录。
- **00:05 - 00:10**: `DroolsApplication.java` 主类。展示 `@SpringBootApplication` 注解和 `main` 方法，用于启动 Spring Boot 应用。
- **00:10 - 00:15**: `HelloController.java` 控制器。展示 `@RestController`、`@RequestMapping("/hello")` 和 `@Autowired` 注解，以及 `ruleService.rule()` 方法。
- **00:15 - 00:20**: `rule_helloworld.drl` 规则文件。展示规则文件内容：`when eval(true) then System.out.println("规则: rule_helloworld触发...");`。
- **00:20 - 00:25**: `DroolsConfig.java` 配置类。展示 `@Configuration`、`@Bean` 和 `@ConditionalOnMissingBean` 注解，以及 `KieFileSystem`、`KieContainer` 和 `KieBase` 的配置。
- **00:25 - 00:30**: 规则触发演示。展示访问 `http://localhost:8080/hello/rule` 后，控制台输出规则触发信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **PPT 页面**: 展示了“规则引擎 Drools”的大纲，包括：
  1. 问题引出
  2. 规则引擎概述
  3. Drools入门案例
  4. Drools基础语法
  5. 规则属性
  6. Spring Boot整合Drools

#### 代码关键内容

- **`DroolsApplication.java`**:
  ```java
  package com.ithema.drools;

  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;

  @SpringBootApplication
  public class DroolsApplication {
      public static void main(String[] args) {
          SpringApplication.run(DroolsApplication.class, args);
      }
  }
  ```

- **`HelloController.java`**:
  ```java
  package com.ithema.drools.controller;

  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.web.bind.annotation.RequestMapping;
  import org.springframework.web.bind.annotation.RestController;

  @RestController
  @RequestMapping("/hello")
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

- **`DroolsConfig.java`**:
  ```java
  package com.ithema.drools.config;

  import org.kie.api.KieServices;
  import org.kie.api.builder.KieBuilder;
  import org.kie.api.builder.KieFileSystem;
  import org.kie.api.builder.KieModule;
  import org.kie.api.builder.KieRepository;
  import org.kie.api.runtime.KieContainer;
  import org.kie.api.runtime.KieSession;
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.context.annotation.Conditional;
  import org.springframework.context.annotation.ConditionalOnMissingBean;

  @Configuration
  public class DroolsConfig {

      @Bean
      @ConditionalOnMissingBean
      public KieFileSystem kieFileSystem() throws IOException {
          KieRepository kieRepository = kieServices.getRepository();
          KieFileSystem kieFileSystem = kieRepository.newKieFileSystem();
          return kieFileSystem;
      }

      @Bean
      @ConditionalOnMissingBean
      public KieContainer kieContainer() throws IOException {
          KieRepository kieRepository = kieServices.getRepository();
          KieBuilder kieBuilder = kieServices.newKieBuilder(kieFileSystem());
          kieBuilder.buildAll();
          return kieServices.newKieContainer(kieRepository.getDefaultReleaseId());
      }

      @Bean
      @ConditionalOnMissingBean
      public KieBase kieBase() throws IOException {
          return kieContainer().getKieBase();
      }

      @Bean
      @ConditionalOnMissingBean
      public KModuleBeanFactoryPostProcessor kiePostProcessor() {
          return new KModuleBeanFactoryPostProcessor();
      }
  }
  ```

- **`rule_helloworld.drl`**:
  ```drl
  package "rule_helloworld"

  rule "rule_helloworld"
      when
          eval(true)
      then
          System.out.println("规则: rule_helloworld触发...");
  end
  ```

---

### 4) 关键场景与演示描述

- **场景一：项目结构与主类创建**
  - 演示者在 IntelliJ IDEA 中展示项目结构，重点是 `src/main/java` 和 `src/main/resources` 目录。
  - 创建并编写 `DroolsApplication.java`，使用 `@SpringBootApplication` 注解，并在 `main` 方法中调用 `SpringApplication.run()` 启动应用。

- **场景二：控制器与服务层创建**
  - 创建 `HelloController.java`，使用 `@RestController` 和 `@RequestMapping("/hello")` 注解。
  - 在控制器中定义 `@RequestMapping("/rule")` 方法，该方法调用 `ruleService.rule()`。
  - 创建 `RuleService` 类（在 `DroolsConfig.java` 中配置），用于管理 Drools 的 `KieContainer` 和 `KieBase`。

- **场景三：规则文件编写与配置**
  - 在 `resources/rules` 目录下创建 `rule_helloworld.drl` 文件。
  - 编写规则：`when eval(true) then System.out.println("规则: rule_helloworld触发...");`。
  - 在 `DroolsConfig.java` 中配置 `KieFileSystem`、`KieContainer` 和 `KieBase`，并使用 `@ConditionalOnMissingBean` 注解确保 Bean 只在缺少时创建。

- **场景四：规则触发演示**
  - 运行 `DroolsApplication`，查看控制台日志，确认应用启动成功。
  - 访问 `http://localhost:8080/hello/rule`，触发控制器方法。
  - 控制台输出：`规则: rule_helloworld触发...`，证明规则引擎成功执行。

- **场景五：集成与调试**
  - 展示了 `DroolsConfig.java` 中的 `@Bean` 和 `@ConditionalOnMissingBean` 注解，用于 Spring Boot 的自动配置。
  - 通过 `KieServices.Factory.get()` 获取 `KieServices` 实例，用于创建 `KieFileSystem`、`KieContainer` 和 `KieBase`。
  - 规则文件的路径通过 `RULES_PATH` 变量指定。

---

以上是根据视频画面进行的结构化技术分析。
