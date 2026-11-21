# 15-HATEOAS介绍-股票服务启动验证 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接着的话呢咱们开始对股票服务呢做个启动和验证

那首先呢我们将服务启动一下

找到Hitstocks不共存

找到它的启动内

在这里面的话呢我们直接启动右键让运行

运行的时候呢注意观察它的日志

看一下有没有出现错误

如果有错误的话呢我们要及时处理

在这一块的话呢它是启动成功的

端口是8080

那么我呢就可以访问一下

我们打开浏览器

直接访问它的8080端口刷新一下

这个时候呢可以看到什么

它的Links对应的资源信息

因为我们实现了什么股票服务对不对

我们给它提供了一个股票的资源

那么股票资源的话

什么Dataless呢帮我们做什么事情呢

它会自动给我们的股票实体呢

生成增商改差的接口

也就是CRUD的接口

这个时候的话大家可以看到

我们的话呢

并没有提供分页的这种查询对不对

也没有提供了修改的相关的一些接口实现

但它呢可以自动提供出来

做对应的CRUD的操作

好这一点的话呢大家要知道

然后呢我们就来访问一下Stox

这个时候是不是可以看到

我们所有的股票资源数据呢

都已经展示出来了对不对

上面的话呢就是我们在Data

Circle里面的话呢

所插入的三条数据

然后下面这部分数据

这里面的话呢

这些节点信息是我们的资源的访问信息

比如说我们要去分页的一些查询

在这里的话呢

它也把我们展示出来了

可以通过这个接口去实现了分页的处理

那么在这里面的话呢

是Profile

然后呢

Search这个Search是什么作用呢

我们来访问看一下

Search的意思可以看到

它是将我们自定义实现的结果的话呢

全部呈现出来了对不对

那我们来看一下在那个JPA层

我们在这里定义了两个

自定义实现的结果

一个是Found by Name对不对

另外一个是Found by Name in Order by ID

然后呢根据ID做了一个排序

这里面的话呢

是查询所对应的所有股票数据对不对

而这个的话呢

是查询根据股票名称的查询出某一条股票数据

在这里呢

它都可以帮我们检索以前的全部返回出来

那么我们都可以不用通过API

就可能直接进行一个访问对不对

那么我们就来测试一下

比如说Found by Name

Found by Name这一块呢

我们来做一个调整

在这里呢

改成Name

我们比如说工商银行

好这个时候是不是能查到工商银行这条数据

那我改成中国平安呢

好这个时候呢

它也能显示出中国平安来对吧

好那我们是不是还有另外一个借口

Found by Name in Order by ID

对不对

这个怎么去用呢

这个话呢也很简单

我们后面换的是一个什么

历史的参数对吧

然后历史参数后面的话呢

比如说要查两只股票

一个是中国平安

还有的是什么工商银行

那么通过什么分割呢

就通过一个逗号

然后呢就工商银行

点击确定

这个时候呢

它是不是就呈现出了我们所对应符合条件的两条数据

一个是中国平安

一个呢是工商银行

这个呢就是股票服务

它呢通过Spring DataList所提供出来的借口

帮我们实现了HitOS的风格

在这里面的话呢

我们通过讲义都可以得到一个

所预期的验证

在这里呢

就是对股票服务的一个启动和验证

这一讲呢

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析：

---

### 1) 视频摘要

本视频片段是关于使用 Spring Boot 和 HATEOAS 构建 RESTful API 的技术演示。主要内容是验证一个股票服务的启动和功能，特别是通过 HATEOAS 生成的超媒体链接进行数据查询。演示者首先启动了股票服务，然后通过浏览器访问其 REST 接口，尝试使用 HATEOAS 提供的链接来查询股票数据。演示过程中，演示者展示了如何在代码中定义 HATEOAS 的 `@RepositoryRestResource` 注解，并通过 `@Param` 注解来支持参数化查询。最后，演示者在浏览器中尝试访问一个由 HATEOAS 生成的链接，但遇到了 HTTP 400 错误，这表明请求的参数格式可能不符合预期。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 视频开始，显示了课程的 PPT 页面，标题为“3.7 启动股票服务验证”。
*   **00:00:05 - 00:00:15**: 演示者在 IntelliJ IDEA 中打开项目 `hateaos-stocks`，并展示了 `HateaosStocksApplication` 的启动类代码。
*   **00:00:15 - 00:00:30**: 演示者点击运行按钮，启动了 Spring Boot 应用，并在控制台中查看了启动日志，确认应用在端口 8080 上成功启动。
*   **00:00:30 - 00:00:45**: 演示者切换到 `StocksRepository` 接口文件，展示了如何使用 `@RepositoryRestResource` 注解来定义 RESTful 资源，并定义了两个查询方法：`findByNamelInOrderByld` 和 `findByName`。
*   **00:00:45 - 00:01:00**: 演示者在浏览器中访问了股票服务的根路径 `http://127.0.0.1:8080/`，并查看了返回的 JSON 数据，其中包含了 HATEOAS 生成的 `_links` 字段。
*   **00:01:00 - 00:01:15**: 演示者在浏览器地址栏中输入了一个由 HATEOAS 生成的链接，用于查询股票数据，但返回了 HTTP 400 错误。
*   **00:01:15 - 00:01:30**: 演示者在浏览器中尝试访问另一个由 HATEOAS 生成的链接，但同样返回了 HTTP 400 错误。
*   **00:01:30 - 00:01:45**: 演示者切换回 PPT 页面，显示了“3.8 启动订单服务验证”的标题。
*   **00:01:45 - 00:02:00**: 演示者在 PPT 页面上展示了如何使用 `restTemplate` 发起 HTTP 请求来添加股票数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 内容**:
    *   **章节标题**: “3.7 启动股票服务验证” 和 “3.8 启动订单服务验证”。
    *   **关键信息**: “启动股票服务，通过 HTTP 访问，来查看 Rest 接口信息”，并提供了服务地址 `http://127.0.0.1:8080/`。
*   **代码内容**:
    *   **`HateaosStocksApplication.java`**:
        ```java
        @SpringBootApplication
        @ComponentScan(basePackages = {"com.icast"})
        @EntityScan(basePackages = {"com.icast"})
        @EnableJpaRepositories(basePackages = {"com.icast"})
        public class HateaosStocksApplication {
            public static void main(String[] args) {
                SpringApplication.run(HateaosStocksApplication.class, args);
            }
        }
        ```
    *   **`StocksRepository.java`**:
        ```java
        @RepositoryRestResource(path = "/stocks")
        public interface StocksRepository extends JpaRepository<StocksEntity, Long> {
            // 根据股票名称查找对应的股票数据
            @Param("list")
            @Return
            List<StocksEntity> findByNamelInOrderByld(@Param("list") List<String> list);

            // 根据名称查询股票信息
            @Param("name")
            @Return
            List<StocksEntity> findByName(@Param("name") String name);
        }
        ```
    *   **HTTP 请求示例**:
        ```java
        ResponseEntity<Resource<StocksEntity>> resp = restTemplate.exchange(
            req,
            new ParameterizedTypeReference<Resource<StocksEntity>>() {}
        );
        log.info("add stocks == {}", resp);
        return resp.getBody();
        ```

---

### 4) 关键场景与演示描述

*   **场景一：启动股票服务** (00:00:15 - 00:00:30)
    *   **描述**: 演示者在 IntelliJ IDEA 中点击运行按钮，启动了 `HateaosStocksApplication`。在控制台中，可以看到 Spring Boot 的启动日志，包括 `Tomcat started on port(s): 8080`，确认服务已成功启动。
*   **场景二：查看 HATEOAS 生成的链接** (00:00:45 - 00:01:00)
    *   **描述**: 演示者在浏览器中访问了服务的根路径 `http://127.0.0.1:8080/`。返回的 JSON 数据中包含了 `_links` 字段，其中包含了指向 `findByNameInOrderByld` 和 `findByName` 方法的链接。
*   **场景三：尝试使用 HATEOAS 链接查询数据** (00:01:00 - 00:01:15)
    *   **描述**: 演示者在浏览器地址栏中输入了一个由 HATEOAS 生成的链接，用于查询股票数据。但浏览器返回了 `HTTP Status 400 – Bad Request` 错误，表明请求的参数格式可能不符合预期。
*   **场景四：演示订单服务验证** (00:01:45 - 00:02:00)
    *   **描述**: 演示者切换到 PPT 页面，展示了如何使用 `restTemplate` 发起 HTTP 请求来添加股票数据。代码片段显示了如何构造请求并处理响应。
