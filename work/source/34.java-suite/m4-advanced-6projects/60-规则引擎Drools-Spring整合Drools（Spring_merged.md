# 60-规则引擎Drools-Spring整合Drools（Spring — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,刚才呢咱们这个Spring Web整合我们D-Rose呢,代码开发已经开发完了,那接下来呢咱们来测试一下,看看我们这个整合是否成功了。

那接下来呢我们是不是需要把咱们这个Web工程给跑起来,怎么跑起来呢?咱们是不是在我们的POM文件里面配置了一个Talmcat 7的插件对吧?

所以我们可以直接基于这个Talmcat插件来启动一下。

好,但是在启动之前呢最好我们先编译一下,先可恋一下,然后呢我们来编译一下,看看它能不能编译通过,好,Compile,好,编译是没问题的对吧?

好,那接下来呢我们来基于这个插件呢来启动啊,在Plugins里面找到我们Talmcat 7这个插件对吧?

然后呢这是不是有个Run呢?好,直接点右键,debug方式来运行一下。

好,这样的话呢我们Talmcat服务器呢正在启动啊,来观察一下日志。

端口呢是80对吧?

好,这就已经启动成功了,没有报错。

当然了如果说我们可以想看更加详细的日志信息呢,可以将我们的Log4j啊,日志呢组件给它加进来,这样的话呢看到的信息会更加多一些。

你看现在它是不是也提示啊,我们现在并没有去配置相应的一些日志组件。

好,因为现在这个工程比较简单,如果我们真实在这个项目当中啊,肯定是需要配置日志的。

好,那接下来呢我们就来测试一下。

咱们是不是只需要访问一下我们的Controller就可以了,然后看看我们的控制台输出。

因为什么呢?因为我们在这个规则文件里边呢,是不是,大家看,规则文件里边是不是有一句输出语句。

所以呢我们观察我们Talmcat控制台,Talmcat控制台这边。

如果能看到这一句话的话呢,这就说明我们的规则确实是出发了。

然后呢我们如何触发这个规则呢?是不是需要通过访问我们的Controller啊,这样来一步一步出发。

所以我们在这呢来打开一个。

测试一下这个测试器。

然后呢我们看这个地方呢,我是不是后面需要跟是hello,然后呢再跟什么呢,就是这个roola,对吧。

别忘了我们是不是有一个.do结尾,否则是进不了我们这个Spring MVC框架的。

所以说我们这roola.do,注意看,走。

好,它其实已经指引成功了,已经指引成功了,你看这个地方。

当然有人看到这404,404是因为我们是不是没有配置那个什么呢,没有配置我们那个。

视图解析器对吧。

所以说呢它试图要跳转到一个OK那么一个页面,但是呢现在因为没有配置视图解析器,所以它报了一个404。

这个呢我们就不再修复了,因为我们关注点其实并不在这儿。

主要是什么呢,我们看看通过这个这次请求能不能触发这个规则,现在相当于是页面跳转这块报了一个404。

好,那么到这儿的话呢,我们其实就已经验证通过了,这个整合方式是成功的,是正确的。

好,这是关于我们第二种整合方式。

就是在我们原先的整合方式基础之上呢,加入我们的web模块来进行整合。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频教程演示了如何在 Spring Web 应用中集成 Drools 规则引擎。核心内容包括：
- 在 IntelliJ IDEA 中创建并配置一个 Maven 项目 `drools_springweb`。
- 在 `pom.xml` 中引入 Spring Web 和 Drools 的依赖。
- 编写一个 Spring MVC 控制器 `HelloController`，用于处理 HTTP 请求。
- 编写一个 Drools 规则文件 `helloworld.drl`，定义一个简单的规则。
- 通过 `@Autowired` 注入 `RuleService` 服务，并在控制器中调用其 `rule()` 方法来触发规则。
- 使用 Maven 的 `tomcat7-maven-plugin` 插件将项目打包并运行在嵌入式 Tomcat 服务器上。
- 最终通过浏览器访问 `/hello` 接口，成功触发并打印出规则执行结果。

整个过程展示了 Spring MVC 与 Drools 规则引擎的集成方式，以及如何通过 HTTP 请求触发规则执行。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 项目初始化与环境检查。在 IntelliJ IDEA 中打开项目 `drools_springweb`，并确认已检测到 Spring Web 框架。
*   **00:04 - 00:07**: 编写控制器代码。在 `HelloController.java` 中定义一个 `@RequestMapping("/hello")` 的控制器方法。
*   **00:08 - 00:11**: 配置 Maven 插件。在 `pom.xml` 中配置 `tomcat7-maven-plugin`，设置 `port` 为 80。
*   **00:12 - 00:15**: 执行 Maven 构建。点击 `Run` 按钮，执行 `mvn clean package` 命令，将项目打包成 `war` 文件。
*   **00:16 - 00:19**: 启动 Tomcat 服务器。在 Maven 插件中选择 `tomcat7:run`，启动嵌入式 Tomcat 服务器。
*   **00:20 - 00:23**: 查看服务器日志。在控制台中观察 Tomcat 启动日志，确认服务器已成功启动。
*   **00:24 - 00:27**: 编写 Drools 规则。在 `helloworld.drl` 文件中编写一个名为 `rule_helloworld` 的规则，其条件为 `eval(true)`，执行体为 `System.out.println("规则: rule_helloworld触发...");`。
*   **00:28 - 00:31**: 配置服务类。在 `RuleService.java` 中定义 `rule()` 方法，用于执行 Drools 规则。
*   **00:32 - 00:35**: 在控制器中注入服务。在 `HelloController.java` 中使用 `@Autowired` 注入 `RuleService`。
*   **00:36 - 00:39**: 调用规则服务。在控制器的 `rule()` 方法中调用 `ruleService.rule()`。
*   **00:40 - 00:43**: 访问 Web 接口。在浏览器中访问 `http://localhost:80/hello`。
*   **00:44 - 00:47**: 观察结果。在控制台中看到规则执行成功的日志输出。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **标题**: “7.2 Spring整合Drools+web”
    *   **正文**: “本小节我们来进行Drools和Spring Web的整合。具体操作步骤如下：第一步：创建maven的war工程drools_springweb并在pom.xml文件中导入相关maven坐标”
    *   **PPT 中的代码片段**:
        ```xml
        <project xmlns="http://maven.apache.org/POM/4.0.0"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                 http://maven.apache.org/xsd/maven-4.0.0.xsd">
            <modelVersion>4.0.0</modelVersion>
            <groupId>com.ithema</groupId>
            <artifactId>drools_springweb</artifactId>
            <version>1.0-SNAPSHOT</version>
            <packaging>war</packaging>
            <properties>
                <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
                <maven.compiler.source>1.8</maven.compiler.source>
                <maven.compiler.target>1.8</maven.compiler.target>
                <drools.version>7.10.0.Final</drools.version>
                <spring.version>5.0.5.RELEASE</spring.version>
            </properties>
        </project>
        ```

*   **代码内容**:
    *   **`HelloController.java`**:
        ```java
        @Controller
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
    *   **`helloworld.drl`**:
        ```drl
        package helloworld
        rule "rule_helloworld"
        when
            eval(true)
        then
            System.out.println("规则: rule_helloworld触发...");
        end
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与控制器编写**
    *   **描述**: 视频首先展示了 IntelliJ IDEA 中的项目结构，重点是 `src/main/java` 下的 `controller` 包。随后，开发者在 `HelloController.java` 中编写了控制器代码，使用 `@Controller` 和 `@RequestMapping("/hello")` 注解定义了处理 `/hello` 路径的控制器。
*   **场景二：Maven 依赖与插件配置**
    *   **描述**: 开发者在 `pom.xml` 文件中配置了 `tomcat7-maven-plugin`，并设置了 `port` 为 80。这允许项目在本地运行时通过 `http://localhost:80/` 访问。
*   **场景三：Maven 构建与服务器启动**
    *   **描述**: 通过点击 `Run` 按钮，执行 `mvn clean package` 命令，将项目打包成 `war` 文件。随后，通过 `tomcat7:run` 启动嵌入式 Tomcat 服务器。控制台输出了服务器启动日志，确认服务器已成功启动。
*   **场景四：Drools 规则编写与服务注入**
    *   **描述**: 在 `helloworld.drl` 文件中，开发者编写了一个简单的规则 `rule_helloworld`，其条件为 `eval(true)`，执行体为打印日志。在 `RuleService.java` 中，开发者定义了 `rule()` 方法来执行规则。在 `HelloController.java` 中，通过 `@Autowired` 注入 `RuleService`。
*   **场景五：规则触发与结果验证**
    *   **描述**: 在浏览器中访问 `http://localhost:80/hello`。当请求到达时，Spring MVC 控制器会调用 `ruleService.rule()` 方法，从而触发 Drools 规则。在控制台中，可以看到规则执行成功的日志输出，证明了规则引擎已成功集成并生效。
