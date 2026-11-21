# 02-导入功能代码 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好那接下来呢

我们就来看我们第11章的第一部分

也就是导入功能代码

这个功能代码呢

在咱们资料当中已经准备好了

你像这个快递员端

司机端这一端呢

是在我们当前这个文件夹里边

咱们可以来看一下

这是我们的资料对吧

然后在资料里边

有个TMS司机端服务对吧

PDWeb Driver代码导入

这里边分别有什么呢

就是我们这些配置文件

包括我们的Java代码对吧

那么你对应的

把它拷到我们项目当中来

就可以了

对应拷进来就可以了

那么这个呢

我提前已经拷好了

咱们可以来看一下

在我们这个地方

一个是PDWeb Driver对吧

这个代码呢

我已经拷进来了

其实都是一样的对吧

然后呢这是配置文件啊

这是我们的配置文件

然后呢这边是我们的Java代码

这些代码

大家对应的拷过来就可以了

然后还有一个呢

就是我们这个快递员端对吧

快递员端呢是在这儿呢

在我们资料这个TMS快递员端

对吧服务

然后呢在这个里边

那么对应的呢

你把这个代码呢

把它拷到哪呢

把它拷到我们这个PDWeb Courier

对应的位置去就可以了

我这个呢都已经提前拷好了

大家自己来拷一下就可以了

然后这里边呢

其实全都是一些什么呢

接口调用啊

比如说我们这个Controller对吧

然后呢这里边有这个CourierController

然后呢这里边都是关于什么呢

快递员的一些操作

一些业务操作

你看快递员业务对吧

那么快递员主要有这么什么呢

比如说他这个带取件对吧

带妥投

但是这个呢其实是一个查询

就是查询什么呢

查询他的一些任务对吧

这个快递员当前有哪些带取件的任务

还有带这个投递的任务对吧

那么通过调用我们这个接口呢

就能够获得

但是这里边呢

他全都是什么呢

FIN调用

你看全都是FIN调用

那么具体他调用了哪些FIN呢

涉及到的其实还是非常多的

你看我选中了这么多的

那么这个呢

他其实对应的就是调我们这个PD Work对吧

来获得什么呢

获得一些这个取件的

派件的一些任务信息

然后Other呢

这是不是调的就是我们这个OMS这个服务对吧

来获得一些订单信息

然后这个呢

也是OMS对吧

然后呢Area呢

这个调的就是我们这个权限服务

权限服务来获得什么呢

可能是获得一些这个区域信息啊

或者是什么呢

或者是

这个是根据不同的

不同的条件对吧

不同的参数来进行查询啊

那么最终查的其实都是区域啊

然后呢

这个Goods Type这个调的就是什么呢

调用的是我们的基础为服务

获得的就是什么呢

一些货物的类型信息对吧

然后呢Transport

这个呢调的还是我们这个PD Work

Work这里边呢

主要就是跟我们这个运单相关的一些操作

对吧Transport Order

这就是运单

所以说呢我们通过这呢也能看到

他其实呢全都是什么呢

全都是一些Fain接口调用

然后调用我们下边的这些一个一个的微服务

对吧

最终呢来完成一个业务操作

好

那么我们对应的导过来就可以了

导过来之后呢

你就可以把服务跑起来

然后呢通过SWAG文档呢

能够更加清晰的能够看到

我们当前这个司机端包括快递员端

对吧

他都提供了哪些服务接口

好

这个呢大家自行导入就可以了

你只要在这个套件里面

就通过这些 你就可以看到

这个服务的室内的主页

这些有充满运电的

还有还有一个就是

这个就是现在在体验的

这个是移动体验

我们在这边我们可以看到

我们现在觉得这就是一个

一个很简单的一种

非常简单的设计

因为我们这个 cs2 运行

它就继续在拨打周边

然后我们就能看到

这个设计的动作

也有几个运动性的

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是“品达物流管理客户端”项目第10章的技术课程，主要演示了如何将已有的功能代码导入到 `pd-web-customer` 项目中，并展示了该微服务应用的接口文档（Swagger）和前端原型设计。课程内容聚焦于 Spring Boot 微服务架构，涉及控制器（Controller）的编写、Feign 客户端的定义、以及如何通过 Swagger UI 进行接口测试和前端交互设计。视频通过 IntelliJ IDEA 开发环境和 Swagger UI 等工具，直观地展示了后端代码与前端需求的对接过程。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开头，展示项目文件夹 `pd-web-customer` 的结构，包含 `java` 和 `resources` 目录。
*   **00:03 - 00:07**: 进入 IntelliJ IDEA，打开 `pd-web-customer` 项目，展示项目结构和 `AddressBookController.java` 文件。
*   **00:07 - 00:12**: 详细讲解 `AddressBookController` 中的 `@Api(tags = "地址簿")` 注解和 `@RequestMapping("address")` 映射。
*   **00:12 - 00:17**: 展示 `AddressBookController` 中的构造函数，注入 `AddressBookFeign` 和 `AreaApi` 两个依赖。
*   **00:17 - 00:22**: 代码演示：在 `AddressBookController` 中，通过 `CompletableFuture` 并发获取省、市、区的映射关系，并填充到 `AddressBookDTO` 对象中。
*   **00:22 - 00:27**: 切换到 `AttachmentController.java`，展示 `@FeignClient` 注解定义的 Feign 客户端 `AttachmentClient`。
*   **00:27 - 00:32**: 展示 `AttachmentClient` 中的 `@PostMapping` 接口，用于处理文件上传，包含 `@RequestPart` 注解的文件和参数。
*   **00:32 - 00:37**: 切换到 `MailingController.java`，展示其 `@Api(tags = "业务接口")` 注解和 `@RequestMapping` 映射。
*   **00:37 - 00:42**: 展示 `MailingController` 中注入的多个 Feign 客户端依赖，如 `AgencyScopeFeign`, `OrgApi`, `TransportOrderFeign` 等。
*   **00:42 - 00:47**: 切换到 `UserController.java`，展示其 `@Api(tags = "用户管理")` 注解和 `@RequestMapping` 映射。
*   **00:47 - 00:52**: 展示 `UserController` 中的 `memberService.detail(userId)` 方法调用，并通过 `Result.ok().put("data", ...)` 返回 `UserProfileDTO` 对象。
*   **00:52 - 00:57**: 切换到浏览器，打开 Swagger UI (`http://localhost:8164/swagger-ui.html`)，展示项目所有接口的文档列表。
*   **00:57 - 01:02**: 在 Swagger UI 中点击“业务接口”下的 `MailingController`，展示其具体接口文档。
*   **01:02 - 01:07**: 切换到 Axure RP 设计工具，展示“移动端-司机端”的产品原型图，包含“首页”、“寄件”、“查询”、“我的”等模块。
*   **01:07 - 01:12**: 在 Axure RP 中点击“首页”模块，展示其详细页面设计和交互逻辑。
*   **01:12 - 01:17**: 在 Axure RP 中点击“查询”模块，展示其详细页面设计和交互逻辑。
*   **01:17 - 01:22**: 在 Axure RP 中点击“我的”模块，展示其详细页面设计和交互逻辑。
*   **01:22 - 01:27**: 切换回 Markdown 文档，展示“1. 导入功能代码”章节，说明将资料中的代码导入到 `pd-web-customer` 工程中即可，并附上 Swagger 接口文档截图。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / Markdown 文档**:
    *   标题：“品达物流管理客户端APP--Swagger文档 6.6”。
    *   内容：“1. 导入功能代码”、“2. RabbitMQ”、“3. 分布式链路追踪”。
    *   图表：Swagger UI 的接口列表截图，以及 Axure RP 的产品原型图。

*   **代码**:
    *   **`AddressBookController.java`**:
        ```java
        @Api(tags = "地址簿")
        @RestController
        @RequestMapping("address")
        public class AddressBookController {
            private final AddressBookFeign addressBookFeign;
            private final AreaApi areaApi;
            public AddressBookController(AddressBookFeign addressBookFeign, AreaApi areaApi) {
                this.addressBookFeign = addressBookFeign;
                this.areaApi = areaApi;
            }
        }
        ```
    *   **`AddressBookController.java` (核心逻辑)**:
        ```java
        if (addressBook == null) {
            return Result.error();
        }
        Set<Long> areaSet = new HashSet<>();
        areaSet.add(addressBook.getProvinceId());
        areaSet.add(addressBook.getCityId());
        areaSet.add(addressBook.getCountyId());
        CompletableFuture<Map<Long, Area>> areaMapFuture = FeignClient.getAreaMapFuture();
        // ... (后续代码)
        ```
    *   **`AttachmentClient.java`**:
        ```java
        @FeignClient(
            name = "${pinda.feign.authority-server:pd-file-server}",
            path = "/attachment"
        )
        public interface AttachmentClient {
            @PostMapping(
                value = "/upload",
                consumes = MediaType.MULTIPART_FORM_DATA_VALUE
            )
            Object upload(
                @RequestPart(value = "file") MultipartFile file,
                @RequestParam(value = "isSingle", required = false, defaultValue = "false") Boolean isSingle,
                @RequestParam(value = "id", required = false) Long id,
                @RequestParam(value = "bizId", required = false) String bizId,
                @RequestParam(value = "bizType", required = false) String bizType
            );
        }
        ```
    *   **`UserController.java`**:
        ```java
        Member member = memberService.detail(userId);
        if (member != null) {
            return Result.ok().put("data", UserProfileDTO.builder()
                .id(userId)
                .avatar(member.getAvatar())
                .name(member.getName())
                .phone(member.getPhone())
                .build());
        } else {
            return Result.ok().put("data", UserProfileDTO.builder().build());
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目导入与结构展示 (00:00-00:07)**:
    *   **描述**: 视频首先展示了项目文件夹 `pd-web-customer` 的结构，然后在 IntelliJ IDEA 中打开项目，清晰地展示了项目模块的层级结构，包括 `pd-web-customer`、`pd-web`、`pd-user` 等子模块，以及 `AddressBookController` 等核心控制器文件。

*   **场景二：控制器代码详解 (00:07-00:47)**:
    *   **描述**: 课程详细讲解了多个控制器文件的代码。首先讲解了 `AddressBookController` 中的注解和构造函数，然后重点演示了如何使用 `CompletableFuture` 并发处理地址簿数据的省、市、区信息。接着展示了 `AttachmentController` 中的文件上传接口定义，以及 `MailingController` 中的多个 Feign 依赖注入。最后，演示了 `UserController` 中如何根据用户 ID 查询用户信息并返回 `UserProfileDTO` 对象。

*   **场景三：接口文档与前端原型展示 (00:52-01:22)**:
    *   **描述**: 视频切换到浏览器，访问 Swagger UI (`http://localhost:8164/swagger-ui.html`)，展示了项目所有接口的文档列表，包括“业务接口”、“公共信息”、“地址簿”、“文件上传”等模块。随后，视频切换到 Axure RP 设计工具，展示了“移动端-司机端”的产品原型图，包括“首页”、“寄件”、“查询”、“我的”等模块的详细页面设计和交互逻辑，直观地展示了后端接口与前端页面的对应关系。

*   **场景四：课程总结与文档回顾 (01:22-01:27)**:
    *   **描述**: 视频最后
