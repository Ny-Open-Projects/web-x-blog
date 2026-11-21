# 30-Gateway聚合配置-自定义OAuth2与管理 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来咱们就要去通过制定OS2启动器和后台管理服务做一个集成运用

那怎么去实现呢

首先咱们将OS2的启动器要集成在stockadmin后台管理服务工程当中

咱们将这个依赖扣取过来

放在admin user home文件下面

咱们鼠标cancel

看一下能否找到

好这个没有问题

接着的话咱们要增加OS2的认证配置

这个咱们之前做了讲解

在这里咱们直接copy引入进来

放在配置文件下面

这个我们已经放入进去了

这里面要保障OS2的认证地址是正确的

以及CANON的ID的相关信息配置

然后这个inlogic url就是咱们不需要进行认证扫描的接口路径

如果说有些特殊接口不需要做认证扫描了

那么在下面去追加就可以了

接下来咱们就可以做一个测试和验证

首先去

去启动认证服务

然后去启动后台管理服务

咱们就去访问一个接口

这个接口的话可以随便拿一个接口

比如说是根据机构预置类型来获取所有菜单

验证OS2这块健全能否正常生效

咱们启动认证服务

找到OS工程

找到stratab

启动内

右键启动后台管理服务

做一个重启

把用户管理服务启动成功

接着的话

咱们就来

访问一个接口地址

咱们将这个地址拷贝下

通过浏览器进行访问

可以看到

他提示出咱们没有经过认证

对不对

不能去访问对应的资源

说明这个接口资源是受到OS2的认证保护

那接着的话

咱们就去通过Bossman来申请一个token

我们要访问那个9199端口

拿到token之后

咱们再来做一个访问

咱们copy这个token

回到刚才的接口地址

当中再追加XS token

把它copy进去

点击回车

这个时候就可以看到没有刚才的认证保护提示

对不对

可以正常访问到这个数据接口上的数据信息

通过刚才的测试

咱们就可以看到

自定义的OS2启动器和后台管理服务

整个基层配置就已经正常实现

这一讲

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程主要讲解如何将自定义的 OAuth2 认证服务集成到后台管理服务（`stock-admin-user`）中，并实现 Swagger2 API 文档的鉴权访问。课程内容包括：
- 在 `pom.xml` 中添加 OAuth2 启动器依赖。
- 在 `bootstrap-dev.yml` 配置文件中配置 OAuth2 客户端信息和资源服务器地址。
- 配置 Swagger2 的 `ignore-urls`，以排除登录、Swagger 文档和 CSRF 相关路径，使其能被访问。
- 通过浏览器访问受保护的 API 接口，验证 OAuth2 认证和 Swagger2 鉴权功能是否正常工作。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：课程标题页，显示“Swagger与Gateway整合”。
*   **00:00:05 - 00:00:15**：进入章节“3.3 自定义OAUTH2启动器与后台管理服务集成使用”，讲解第一步：在 `pom.xml` 中添加依赖。
*   **00:00:15 - 00:00:30**：展示 `pom.xml` 中添加的 Maven 依赖，`groupId` 为 `com.itcast.trade`，`artifactId` 为 `bulls-stock-starter-oauth2`。
*   **00:00:30 - 00:00:45**：讲解第二步：在 `bootstrap-dev.yml` 中配置 OAuth2。
*   **00:00:45 - 00:01:00**：展示 `bootstrap-dev.yml` 中的 `security.oauth2` 配置，包括 `resource.loadBalanced`、`token-info-uri`、`client` 等关键参数。
*   **00:01:00 - 00:01:15**：讲解第三步：配置 Swagger2 的 `ignore-urls`，以排除特定路径。
*   **00:01:15 - 00:01:30**：展示 `ignore-urls` 的配置内容，包括 `/webjars/**`、`/login/**`、`/swagger-resources/**` 和 `/csrf/**`。
*   **00:01:30 - 00:01:45**：讲解第四步：启动认证服务和后台管理服务。
*   **00:01:45 - 00:02:00**：在浏览器中访问后台管理服务的接口，验证功能。
*   **00:02:00 - 00:02:15**：在浏览器中访问 Swagger2 API 文档，验证鉴权功能。
*   **00:02:15 - 00:02:30**：展示 Swagger2 返回的 JSON 数据，验证接口访问成功。
*   **00:02:30 - 00:02:45**：进入下一章节“3.4 Swagger2实现鉴权访问”，讲解如何解决 Swagger2 访问受保护资源的问题。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

*   **章节标题**：
    *   `3.3 自定义OAUTH2启动器与后台管理服务集成使用`
    *   `3.4 Swagger2实现鉴权访问`
*   **关键说明**：
    *   “将OAUTH2启动器集成至 stock-admin-user 工程中”
    *   “ignore-urls配置的地址，是将swagger2接口文档相关路径放行。”

#### 代码

*   **Maven 依赖 (在 `pom.xml` 中)**：
    ```xml
    <!-- OAUTH2认证自定义启动依赖 -->
    <dependency>
        <groupId>com.itcast.trade</groupId>
        <artifactId>bulls-stock-starter-oauth2</artifactId>
        <version>${project.stock.version}</version>
    </dependency>
    ```

*   **Spring Security OAuth2 配置 (在 `bootstrap-dev.yml` 中)**：
    ```yaml
    # spring security 配置
    security:
      oauth2:
        resource:
          loadBalanced: true
          token-info-uri: http://trade-auth/oauth/check_token
        client:
          client-id: app
          client-secret: app
          scope: server
          access-token-uri: http://trade-auth/oauth/token
          user-authorization-uri: http://trade-auth/oauth/authorize
    ```

*   **Swagger2 忽略路径配置 (在 `bootstrap-dev.yml` 中)**：
    ```yaml
    ignore-urls:
      - /webjars/**
      - /login/**
      - /swagger-resources/**
      - /csrf/**
    ```

*   **Spring Boot 启动类 (在 `StockAdminUserApplication.java` 中)**：
    ```java
    @EnableRepositories(basePackages = "com.itcast")
    @EnableTransactionManagement
    public class StockAdminUserApplication {
        public static void main(String[] args) {
            SpringApplication.run(StockAdminUserApplication.class, args);
        }
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：添加 OAuth2 依赖**
    *   **描述**：讲师在 `pom.xml` 文件中添加了 `bulls-stock-starter-oauth2` 依赖，用于集成自定义的 OAuth2 认证服务。
    *   **演示**：在 IDE 中展示 `pom.xml` 文件，高亮显示新添加的依赖项。

*   **场景二：配置 OAuth2 客户端信息**
    *   **描述**：讲师在 `bootstrap-dev.yml` 文件中配置了 OAuth2 的客户端信息，包括 `client-id`、`client-secret`、`token-info-uri` 和 `access-token-uri`。
    *   **演示**：在 IDE 中展示 `bootstrap-dev.yml` 文件，高亮显示 `security.oauth2` 配置块。

*   **场景三：配置 Swagger2 忽略路径**
    *   **描述**：讲师在 `bootstrap-dev.yml` 文件中配置了 `ignore-urls`，以排除 Swagger2 API 文档的访问路径，使其能被正常访问。
    *   **演示**：在 IDE 中展示 `bootstrap-dev.yml` 文件，高亮显示 `ignore-urls` 配置项。

*   **场景四：访问受保护的 API 接口**
    *   **描述**：讲师在浏览器中访问后台管理服务的接口，验证 OAuth2 认证和 Swagger2 鉴权功能。
    *   **演示**：在浏览器中输入接口地址，显示返回的 JSON 数据，验证接口访问成功。

*   **场景五：访问 Swagger2 API 文档**
    *   **描述**：讲师在浏览器中访问 Swagger2 API 文档，验证鉴权功能。
    *   **演示**：在浏览器中输入 Swagger2 文档地址，显示返回的 JSON 数据，验证接口访问成功。

---

以上是根据视频画面整理的结构化技术课程分析。
