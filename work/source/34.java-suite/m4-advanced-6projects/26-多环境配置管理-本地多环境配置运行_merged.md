# 26-多环境配置管理-本地多环境配置运行 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就开始实现了

本地的开发环境配置使用

来实现基于StockUser用户服务工程

来实现多环境版本的启动配置

在本地环境当中要建立两套配置

一套是本地的DV环境开发环境

另外一套是用于连条集成测试的UAT环境

那么咱们来做个具体实现

咱们找到用户服务工程

然后将它的配置文件先复制一份

这个名称我们就叫DUA

然后咱们再复制另外一份

这个名称就叫UAT集成测试环境

这样是便于咱们的一个测试

那么DUA的话我们可以看到

它是会连到本地的中间键

UAT的话我们可以去修改一下

比如说我们将它的Narcos服务随便改一个

192

这里面的地址就168

然后11

下面这个地址咱们也跟着调整

这样UAT它其实是不可用的

因为这个服务根本就不存在

这个IP是我们随便去定义的

咱们最主要就是要验证一下

对于不同环境的启动

它能否正确读取其中的配置

然后进行服务的连接和启动

咱们来看一下默认的配置文件该怎么去调整

在这里就不需要具体的属性配置

咱们在这里只需要保留一项配置就可以了

这个就是指向你本地配置当中

需要启动的环境版本

这个是一个变量对不对

这个变量咱们可以看一下

我们没有明确指定是哪一个环境

设置的是一个Mavit的变量

最新版本的Idea

它是可以识别出Mavit变量的

也就是我们在PoM文件当中

会做一个变量的定义

那么Idea工具是什么呢?

Idea工具它可以帮我们自动检测出来

但是老版本的话它还不支持

所以这个也没关系

那么咱们来看一下解决办法是怎样

我们要DNG它的启动配置

在这个run菜单下面edit修改它的配置

然后在activeprofile下面去指定配置环境

咱们就来做一个验证

看一下是否能够启动成功

咱们找到stock user application

先右键

run运行让它启动

然后再把它关闭

为什么这么做呢?

这样的话咱们就可以在runedit configuration当中

可以看到这个启动内

stock user application

我们去修改

在这里去指定它的配置环境

比如我们要验证开发环境的配置文件是否读取正确

那么我们就指下DV

然后点击OK

咱们运行一下

这个的话开发环境其实还是沿用咱们之前的配置

对不对

正常的话它应该能够成功启动

咱们注意看它的输出日志有没有错误

整个用户服务它就启动完成

我们可以看到它没有爆出连接方面的异常

这个因为咱们save集群没启动

所以save连接没成功

这个是正常的

下面的话咱们可以看到没有其他方面的连接异常

整个服务能够成功启动

那么我们可以看到最上面的一个输出日志是什么?

这个是正常的

下面的话咱们可以看到没有其他方面的连接异常

整个服务能够成功启动

最上面的一个输出日志

在这里面可以看到它打印了一个激活的配置文件版本信息

它指向的是DV

也就是咱们在这里所定义的DV的环境配置

那么我们将服务关闭

再重新去修改

让它指向UAT

看下能否读取成功

点击OK

找到启动内

右键

让运行

因为咱们知道UAT

我们是做了一个错误的配置

对不对

所以我们可以看到

那么它启动的话应该是失败的

我们来看一下

咱们可以看到它出现了一个异常

对吧

这个异常就是根据咱们UAT当中的配置信息

它进行了一个连接尝试

因为这个ID服务是不存在的

所以爆出了一个连接异常

这个证明它能够正常读取到咱们的UAT配置

对不对

那么我们可以看到最上面的输出日志

它的环境版本是指向的UAT

这个指向是没有问题

说明呢

咱们在视频部的下面的多环境版本配置

是能够正常运行的

我们可以看到我们并没有去重新修改它的配置文件信息

对不对

咱们只是修改了它启动时候的运行配置

通过这个变量去切换不同的环境版本

这样咱们就可以方便的去维护多环境的配置管理

而且每个环境的配置文件

它都是隔离的

对不对

DV有DV的环境配置

UAT有UAT的连接配置

这样也不会出现交错

导致连接配置信息产生错误

好

在这里咱们就实现了本地的开发环境配置使用

那么大家再思考一下

接下来咱们如何进行打包处理呢

MAMMEN它又是怎么去识别不同环境的配置呢

这种多环境版本配置是否会存在冲突问题呢

好

这个在咱们下面档件还会做一个具体的实现讲解

那这一讲咱们就先讲到这里

好

谢谢大家

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程讲解了 Spring Boot 项目如何在本地开发环境和集成测试环境（UAT）中使用不同的配置文件。核心内容包括：
- **多环境配置机制**：通过 `application.properties` 或 `application.yml` 文件配合 `spring.profiles.active` 属性来激活特定环境的配置。
- **本地开发环境配置**：演示了如何通过 `bootstrap-dev.yml` 文件配置本地开发环境，包括登录信息、Redis、Nacos 等服务的地址。
- **集成测试环境配置**：演示了如何通过 `bootstrap-uat.yml` 文件配置集成测试环境，并展示了如何通过 Maven 的 `profiles` 功能来区分和打包不同环境的项目。
- **配置文件加载顺序与激活**：介绍了如何通过 Maven 变量 `${package.environment}` 动态设置激活的 profile，并在 IDEA 中通过 Run Configuration 指定。
- **环境切换与验证**：通过启动应用并观察控制台日志，验证了不同配置文件的加载情况，并演示了如何通过修改 Maven `pom.xml` 文件来实现多环境打包。

---

### 2) 按时间顺序的章节（带时间点）

由于无法获取精确的时间戳，以下章节是根据画面内容和逻辑顺序推断的：

- **0:00 - 0:30**：课程引言，介绍本章目标是讲解 Spring Boot 多环境配置与打包发布。
- **0:30 - 1:30**：讲解 Spring Boot 多环境配置规则，包括如何定义多个配置文件（如 `application-dev.yml`、`application-uat.yml`）以及如何通过 `spring.profiles.active` 属性激活它们。
- **1:30 - 3:00**：深入讲解本地开发环境配置。展示 `bootstrap-dev.yml` 文件内容，包括登录信息、Redis、Nacos 配置等。演示如何通过 `spring.profiles.active=dev` 来激活该配置。
- **3:00 - 4:30**：讲解集成测试环境配置。展示 `bootstrap-uat.yml` 文件内容，包括 Nacos 服务发现配置、Sentinel 限流配置等。演示如何通过 `spring.profiles.active=uat` 来激活该配置。
- **4:30 - 5:30**：讲解如何通过 Maven 的 `profiles` 功能来区分和打包不同环境的项目。展示 `pom.xml` 文件中 `<profiles>` 的配置。
- **5:30 - 6:30**：演示如何在 IDEA 中通过 Run Configuration 指定激活的 profile，以实现不同环境的启动。
- **6:30 - 7:30**：演示如何通过修改 `pom.xml` 文件来实现多环境打包，并展示打包后的 jar 文件。
- **7:30 - 8:30**：总结本章内容，强调多环境配置在实际项目中的重要性。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

- **PPT 内容**：
  - 课程大纲：包括“3.1 Spring Boot 多环境配置介绍”、“3.2 Spring Boot 多配置规则”、“3.3 本地的开发环境配置使用”、“3.4 多环境打包配置”。
  - 关键概念：`spring.profiles.active`、`bootstrap.yml`、Maven Profiles。
  - 代码示例：`spring: profiles: active: ${package.environment}`。

- **代码关键内容**：

  - **配置文件 `bootstrap-dev.yml`**：
    ```yaml
    # 登录名
    login-username: admin
    # 登录密码
    login-password: admin123
    # 监控后台开关，开启后可通过后台管理查看
    enabled: true
    # Redis 缓存配置
    redis:
      host: 127.0.0.1
      password: 
      port: 6379
    # spring security 配置
    security:
      resource:
        loadBalanced: true
        token-uri: http://trade-auth/oauth/check_token
        client:
          client-id: app
          client-secret: app
          scope: server
    ```

  - **配置文件 `bootstrap-uat.yml`**：
    ```yaml
    server:
      port: 10681
    spring:
      application:
        name: stock-user
      cloud:
        discovery:
          server-addr: 192.168.11.1:8848
        config:
          server-addr: 192.168.11.1:8848
        sentinel:
          transport:
            # Sentinel管理后台的连接配置
            dashboard: 127.0.0.1:8090
        datasource:
          nacos:
            server-addr: 127.0.0.1:8848
            dataId: sentinel-user-degrade
    ```

  - **`pom.xml` 文件中的 Maven Profiles 配置**：
    ```xml
    <profiles>
      <profile>
        <id>dev</id>
        <activation>
          <activeByDefault>true</activeByDefault>
        </activation>
      </profile>
    </profiles>
    ```

  - **Spring Boot 启动类 `StockUserApplication.java`**：
    ```java
    @SpringBootApplication
    @EnableDiscoveryClient
    @EnableFeignClients
    @ComponentScan(basePackages = {"com.ictast"})
    @MapperScan({"com.ictast.trade.bulls.stock.user.dao", "com.ictast.bulls.stock.common.system.dao"})
    @EnableTransactionManagement
    public class StockUserApplication {
        public static void main(String[] args) {
            SpringApplication.run(StockUserApplication.class, args);
        }
    }
    ```

---

### 4) 关键场景与演示描述

- **场景一：本地开发环境配置演示**
  - **描述**：讲师在 IDEA 中打开 `bootstrap-dev.yml` 文件，展示其内容。然后在 `StockUserApplication` 启动类中，通过 `spring.profiles.active=dev` 来激活该配置。启动应用后，控制台日志显示成功加载了 `bootstrap-dev.yml` 文件中的配置。

- **场景二：集成测试环境配置演示**
  - **描述**：讲师在 IDEA 中打开 `bootstrap-uat.yml` 文件，展示其内容。然后在 `StockUserApplication` 启动类中，通过 `spring.profiles.active=uat` 来激活该配置。启动应用后，控制台日志显示成功加载了 `bootstrap-uat.yml` 文件中的配置。

- **场景三：Maven Profiles 配置演示**
  - **描述**：讲师在 IDEA 中打开 `pom.xml` 文件，展示其中的 `<profiles>` 配置。然后在 IDEA 的 Run Configuration 中，通过修改 `Active Profile` 输入框来指定激活的 profile。启动应用后，控制台日志显示成功加载了指定的配置文件。

- **场景四：配置文件加载顺序与激活演示**
  - **描述**：讲师在 IDEA 中打开 `bootstrap.yml` 文件，展示其内容。然后在 `StockUserApplication` 启动类中，通过 `spring.profiles.active=${package.environment}` 来动态设置激活的 profile。启动应用后，控制台日志显示成功加载了 `bootstrap.yml` 文件中的配置，并根据 `package.environment` 的值加载了相应的配置文件。

- **场景五：环境切换与验证演示**
  - **描述**：讲师在 IDEA 中打开 `StockUserApplication` 启动类，通过修改 `spring.profiles.active` 的值来切换不同的环境。然后启动应用，观察控制台日志，验证不同环境的配置是否被正确加载。例如，当 `spring.profiles.active=dev` 时，日志中会显示 `bootstrap-dev.yml` 的配置；当 `spring.profiles.active=uat` 时，日志中会显示 `bootstrap-uat.yml` 的配置。

- **场景六：多环境打包配置演示**
  - **描述**：讲师在 IDEA 中打开 `pom.xml` 文件，展示其中的 `<profiles>` 配置。然后在 IDEA 中通过 Run Configuration 指定激活的 profile。启动应用后，控制台日志显示成功加载了指定的配置文件。讲师随后演示了如何通过修改 `pom.xml` 文件来实现多环境打包，并展示了打包后的 jar 文件。

- **场景七：配置文件加载失败演示**
  - **描述**：讲师在 IDEA 中打开 `bootstrap-uat.yml` 文件，展示其内容。然后在 `StockUserApplication` 启动类中，通过 `spring.profiles.active=uat` 来激活该配置。启动应用后，控制台日志显示 `java.lang.IllegalStateException: failed to req API/nacos/v1/ns/service/list after all servers`，表明配置文件加载失败。讲师随后演示了如何通过修改 `bootstrap-uat.yml` 文件中的 `server-addr` 配置来解决该问题。
