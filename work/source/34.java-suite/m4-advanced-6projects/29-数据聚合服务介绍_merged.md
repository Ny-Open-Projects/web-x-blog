# 29-数据聚合服务介绍 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么前面呢,关于我们这个altar相关的这个安装配置,还有设置同步任务呢,我们都已经说完了,并且呢,最后测试了一下是没有问题的。

好,那接下来呢,我们来看啊,我们下一个小节呢,就是数据聚合服务介绍。

大家看,在我们当前这个Maven导入的Maven工程里边呢,有这么一个叫做PD-aggregation,对吧。

这个呢,对应的就是我们的数据聚合服务。

呃,本身呢,这个代码其实是非常简单的。

那么我们来了解一下这个服务它到底是干什么用的。

这个数据聚合服务呢,它提供TMS中各种作业,还有单据,还有任务的集中查询功能。

那么它这个里边,这个服务对应操作的数据库呢,就是这个啊,叫做PD-aggregation。

它操作的就是我们这个库啊,咱们来看一下。

这个叫做PD-aggregation。

那么这里边这些表中的数据是怎么来的呢?

其实就是通过我们的altar,哎,表中的这个数据库中的表还有数据都是通过altar从其他的库同步过来的。

而我们当前这个Maven工程呢,就是针对我们同步过来的这些数据进行一些什么呢,查询操作。

注意,只是进行查询操作。

啊,所以我们这一张这个代码呢,就不再去编写了。

因为都是一些什么查询操作。

你看,就是针对这些数据进行一个查询操作。

所以从,呃,本身从这个难度上来说没有任何难度,对吧。

也没有什么新的技术点。

啊,所以说呢,我们就直接使用,啊,就可以了。

哎,你只要知道啊,我们操作的这个数据,对吧。

它是从哪来的?

它就是基于我们这个altar这个技术,从其他的业务数据库当中,然后,呃,把它一个一个同步过来的。

然后在我们这儿呢,集中来进行查询。

好,这是关于咱们这个数据聚合服务。

我们简单介绍一下就可以了。

后边呢,我们直接拿过来用这个服务就可以了。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”中“数据聚合服务开发”的教学内容，主要聚焦于服务的测试验证与代码实现。讲师通过展示 Typora 文档、Navicat 数据库管理工具和 IntelliJ IDEA 开发环境，系统地讲解了如何启动 Canal 的数据同步通道（Channel），以及如何通过 Spring Boot 的 Controller 层实现对数据聚合服务中不同业务模块（如司机、任务、运输单）的查询接口。视频内容旨在帮助学习者理解数据同步的流程和后端服务的开发结构。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**: 展示 Typora 文档，定位到“4.7 测试验证”章节，介绍启动 Channel 的操作。
*   **00:00:05 - 00:00:10**: 在 Navicat 中切换数据库连接，展示 `otter_test` 数据库的表结构。
*   **00:00:10 - 00:00:15**: 在 Navicat 中切换到 `pd_aggregation` 数据库，准备查看目标表结构。
*   **00:00:15 - 00:00:20**: 回到 Typora 文档，再次强调“5. 数据聚合服务介绍”，说明服务对应的数据库和数据同步来源。
*   **00:00:20 - 00:00:25**: 在 IntelliJ IDEA 中打开项目 `pinda-tms-java`，展示项目结构。
*   **00:00:25 - 00:00:30**: 在 IDEA 中打开 `AppDriverController.java`，展示司机相关业务的查询接口。
*   **00:00:30 - 00:00:35**: 在 IDEA 中打开 `WebManagerController.java`，展示后台管理平台的多个查询接口。
*   **00:00:35 - 00:00:40**: 详细展示 `WebManagerController` 中的 `@PostMapping("/transportOrder/page")` 方法，用于查询运输单。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “4.7 测试验证”、“5. 数据聚合服务介绍”。
    *   **关键描述**: “在源表中插入条记录，数据同步到目标表中。”
    *   **服务信息**: 数据聚合微服务对应的 Maven 工程为 `pd-aggregation`，对应数据库为 `pd_aggregation`，数据通过 Otter 从其他库同步过来。
    *   **Channel 管理界面**: 展示了 Canal 的 Channel 管理页面，其中有一个名为 `tms-aggregation` 的 Channel，状态为“停止”，并有“启动”按钮。

*   **代码内容**:
    *   **`AppDriverController.java`**:
        ```java
        @Api(tags = "司机聚合平台")
        @RestController
        @RequestMapping("appDriver")
        public class AppDriverController {
            @Autowired
            private DriverService driverService;

            @PostMapping("/page")
            PageResponse<DriverJobDTO> findByPage(@RequestBody AppDriverQueryDTO dto) {
                return driverService.findByPage(dto);
            }
        }
        ```
    *   **`WebManagerController.java`**:
        ```java
        @Api(tags = "管理后台聚合平台")
        @RestController
        @RequestMapping("webManager")
        public class WebManagerController {
            @Autowired
            private WebManagerService webManagerService;

            @PostMapping("/driverJob/page")
            PageResponse<DriverJobDTO> findDriverJobByPage(@RequestBody DriverJobQueryDTO dto) {
                return webManagerService.findDriverJobByPage(dto);
            }

            @PostMapping("/taskPickupDispatchJob/page")
            PageResponse<TaskPickupDispatchDTO> findTaskPickupDispatchJobByPage(@RequestBody TaskPickupDispatchQueryDTO dto) {
                return webManagerService.findTaskPickupDispatchJobByPage(dto);
            }

            @PostMapping("/transportOrder/page")
            PageResponse<TransportOrderDTO> findTransportOrderByPage(@RequestBody TransportOrderQueryDTO dto) {
                return webManagerService.findTransportOrderByPage(dto);
            }

            @PostMapping("/taskTransport/page")
            PageResponse<TaskTransportDTO> findTaskTransportByPage(@RequestBody TaskTransportQueryDTO dto) {
                return webManagerService.findTaskTransportByPage(dto);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：数据同步验证 (00:00:00-00:00:15)**:
    *   讲师首先在 Typora 文档中定位到“4.7 测试验证”部分，强调需要启动 Canal 的 Channel。
    *   接着，讲师在 Navicat 中切换到 `otter_test` 数据库，展示了源表 `tb_item` 的结构，用于演示数据同步的起点。
    *   随后，讲师切换到 `pd_aggregation` 数据库，准备查看目标表，以验证数据是否已同步。

*   **场景二：服务接口开发 (00:00:20-00:00:40)**:
    *   讲师在 IntelliJ IDEA 中打开 `pinda-tms-java` 项目，展示其模块化结构。
    *   讲师导航到 `AppDriverController.java`，演示了如何通过 `@PostMapping("/page")` 注解定义一个用于查询司机任务的接口。
    *   讲师接着导航到 `WebManagerController.java`，演示了如何为管理后台定义多个查询接口，包括司机任务、运输单和任务运输等，每个接口都通过 `@PostMapping` 注解定义，并调用对应的服务层方法。

*   **场景三：数据同步与服务联动 (00:00:15-00:00:20)**:
    *   讲师在 Typora 文档中强调“5. 数据聚合服务介绍”，说明该服务是整个系统的核心，其数据来源于 Otter 的同步，目标库是 `pd_aggregation`。
    *   讲师通过在 Navicat 中切换数据库，直观地展示了源库和目标库的关系，为后续的接口开发提供了数据背景。

---

以上是根据视频画面整理出的结构化信息，希望能帮助您更好地理解课程内容。
