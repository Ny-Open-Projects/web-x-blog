# 12-Sentinel-服务降级Feign实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们这一块已经实现了接入我们身体了

但是接入身体了并不表示这一块就可以直接到项目中进行使用了

我们项目中经常会涉及到我们粪接口的一个调用

A服调B服,B服调C服

这个时候如果C服出现了问题

我们的身体目前为止还没法控制

因此我们还要集成我们的粪

那集成粪这一块该怎么做呢?非常简单

第一步首先要开启Central对粪的一个支持

只需要在我们配置文件中配置一下

开启就可以了

粪CentralEnabledIntrude就行了

配置之后呢

那么后面那一块服务降级对应的一个方法该怎么去实现呢?

和我们之前Headchecks那一块没有什么区别

是一样的

这一块首先创建一个类

实现FallbackFactory这个接口

实现之后呢

里面范形记得写

对应的一个粪接口

紧接着这一块

我们还要去在这个粪接口上面去写上FallbackFactory

指向上面这个类

OK

那么其他的就没什么变化了

紧接着我们来实现一下

在这一块呢

首先第一个要注意一下

这里是要去调粪接口的

那么粪接口在这里有这个粪接口

粪接口呢

我们说过要创建一个类

这个类呢

要实现这个类呢

我们就要去创建这个FallbackFactory

对不对

注意这个类呢

一定要交给我们容器管理

注解要去掉

并且这里面要写上一个叫

对应的一个粪的接口

把它给写过来

就可以了

行

这写了之后

紧接着这里不要忘了

不要忘了配置一下

配置一下当前FallbackFactory对象

是指向了刚才创建的这一个类

行

这一块也搞定

紧接着我们就可以进行测试了

那测试的时候呢

注意

这个粪接口呢

其实是掉下面这一个微幅的

那么下面这个微幅呢

这个方法这里我也做了一下处理

你传的参数

如果是大于10

我会抛异常的

如果是小于10

那就无所谓

所以我们等会儿测试一下

这一块会不会进行一个幅降级

我们只需要测试异常

就可以了

好我们开始启动一下这个微幅

启动一次

启动之后呢我们

接着再把这一块也给启动一下

行都给启动一下

启动之后呢我们这个时候开始进行一个测试

来我们访问哪个方法呢

就是他这里提供的这个方法

叫consumer1

就行了

我们刷新一次

在这里输入一下

localhost

consumer1

来个10

这个时候是不会有问题的

因为这个时候

咱们端口是18083

行这个是没有问题

对不对

我们再来刷新几次也没有问题

这个时候我们换成几了

换成11

他就出错了

哎幅降级了

对吧

这总比咱们去抛个异常

是不是要好得多呀

好就是这一块

集成我们

这一块集成我们的一个分接口

的一个相关操作

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于 **Spring Cloud Alibaba Sentinel** 的技术课程，主要讲解如何在 **Feign** 服务调用中集成 Sentinel 以实现服务降级和熔断。讲师通过演示代码和配置，详细说明了：

*   **配置要求**：需要引入 `spring-cloud-starter-alibaba-sentinel` 依赖，并在 `bootstrap.yml` 中配置 Sentinel 的 `transport` 和 `dashboard` 地址。
*   **启用 Feign 支持**：在 `application.yml` 中为 `feign.sentinel.enabled` 设置为 `true`。
*   **实现服务降级**：通过创建一个实现 `FallbackFactory` 接口的类（如 `GoodsFeignFallback`），为 Feign 客户端提供降级逻辑。
*   **代码集成**：在 Feign 客户端接口上使用 `@FeignClient` 注解，并通过 `fallbackFactory` 属性指向自定义的降级工厂类。
*   **效果验证**：启动服务后，访问 Sentinel 控制台，可以观察到服务的实时监控数据，并验证降级逻辑是否生效。

---

### 2) 按时间顺序的章节（带时间点）

*   **0:00 - 0:20**：介绍 Sentinel 与 Feign 的集成配置，展示 `bootstrap.yml` 中的 `spring.cloud.sentinel` 配置项。
*   **0:20 - 0:35**：讲解如何在 `application.yml` 中启用 Feign 对 Sentinel 的支持，配置 `feign.sentinel.enabled: true`。
*   **0:35 - 1:00**：演示如何创建服务降级处理工厂类 `GoodsFeignFallback`，并实现 `create` 方法。
*   **1:00 - 1:20**：展示如何在 Feign 客户端接口 `GoodsFeign` 上配置 `@FeignClient` 注解，并设置 `fallbackFactory` 属性。
*   **1:20 - 1:40**：在 IDE 中展示项目结构，定位到 `GoodsFeignFallback.java` 文件。
*   **1:40 - 2:00**：展示 `GoodsFeignFallback` 类的完整代码，包括 `create` 方法和 `one` 方法的降级逻辑。
*   **2:00 - 2:20**：在 IDE 中展示 `GoodsFeign.java` 接口的代码，确认 `@FeignClient` 注解已正确配置。
*   **2:20 - 2:40**：在 IDE 中展示 `GoodsApplication.java` 的启动类代码。
*   **2:40 - 3:00**：在 IDE 中点击运行按钮，启动消费者服务。
*   **3:00 - 3:20**：在浏览器中打开 Sentinel 控制台，地址为 `http://192.168.211.137:8858/#/dashboard/home`。
*   **3:20 - 3:40**：在 Sentinel 控制台中，点击“消费者”服务，查看其监控数据。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **配置文件**：`bootstrap.yml` 中的配置项：
        ```yaml
        spring:
          cloud:
            sentinel:
              transport:
                port: 8719
              dashboard: 192.168.211.137:8858
        ```
    *   **配置文件**：`application.yml` 中的配置项：
        ```yaml
        feign:
          sentinel:
            enabled: true
        ```
    *   **代码示例**：服务降级处理工厂类 `GoodsFeignFallback` 的代码：
        ```java
        @Component
        public class GoodsFeignFallback implements FallbackFactory<GoodsFeign> {
            @Override
            public GoodsFeign create(Throwable throwable) {
                return new GoodsFeign() {
                    @Override
                    public String one(Integer max) {
                        return "服务降级：";
                    }
                };
            }
        }
        ```
    *   **代码示例**：Feign 客户端接口 `GoodsFeign` 的代码：
        ```java
        @FeignClient(value = "goods", fallbackFactory = GoodsFeignFallback.class)
        public interface GoodsFeign {
            @GetMapping(value = "/goods/one/{max}")
            String one(@PathVariable(value = "max") Integer max);
        }
        ```
    *   **Sentinel 控制台地址**：`http://192.168.211.137:8858/#/dashboard/home`

*   **图表**：
    *   **项目结构图**：在 IDE 中展示的项目目录结构，包括 `consumer`、`feign`、`fallback` 等包。
    *   **Sentinel 控制台界面**：浏览器中打开的 Sentinel 控制台，显示“消费者”服务的监控页面。

---

### 4) 关键场景与演示描述

*   **场景一：配置 Sentinel 与 Feign**：
    *   讲师在 IDE 中打开 `bootstrap.yml` 文件，展示如何配置 `spring.cloud.sentinel.transport.port` 和 `spring.cloud.sentinel.dashboard`。
    *   讲师在 `application.yml` 文件中展示如何配置 `feign.sentinel.enabled: true`。

*   **场景二：创建服务降级类**：
    *   讲师在 IDE 中创建 `GoodsFeignFallback.java` 文件，并编写代码。
    *   讲师在 `GoodsFeignFallback` 类中实现 `create` 方法，返回一个匿名的 `GoodsFeign` 实例，并在 `one` 方法中返回降级信息“服务降级：”。

*   **场景三：配置 Feign 客户端**：
    *   讲师在 `GoodsFeign.java` 接口中，使用 `@FeignClient` 注解，并设置 `value` 和 `fallbackFactory` 属性。
    *   讲师在 IDE 中展示 `GoodsFeign.java` 文件，确认配置无误。

*   **场景四：启动服务并访问控制台**：
    *   讲师在 IDE 中点击运行按钮，启动 `GoodsApplication`。
    *   讲师在浏览器中打开 Sentinel 控制台，地址为 `http://192.168.211.137:8858/#/dashboard/home`。
    *   讲师在控制台中点击“消费者”服务，查看其监控数据，验证服务降级功能是否生效。

---

以上是根据视频画面进行的结构化技术分析，希望能帮助您更好地理解该技术课程的内容。
