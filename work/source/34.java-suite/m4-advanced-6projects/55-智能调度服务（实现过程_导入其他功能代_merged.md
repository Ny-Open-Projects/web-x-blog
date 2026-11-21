# 55-智能调度服务（实现过程_导入其他功能代 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,前面呢,咱们是已经完成了我们智能调度的第一个环节,也就是订单分类啊,所有代码的开发。

那接下来呢,我们再来梳理一下咱们整个程序它的一个执行流程。

整个程序执行流程是这样的,首先呢,我们是编写了一个定时任务类,对吧?

因为我们这个智能调度啊,是通过定时任务来进行触发的。

好,那么当定时任务触发的时候呢,它其实就是在执行我们这个execute internal这个方法,对吧?

然后在这个方法里边呢,会通过反射是不是来调用一个run方法,那么调用哪个类的run方法呢?

其实就是我们这个dispatch task这个类的run方法,对吧?

就是在这儿。

然后这个地方呢,是不是就会去调我们相应的一些service,比如说我调这个service来完成什么呢?订单分类。

然后再调用其他的service呢?

来完成什么路线规划呀等等。

那么到目前为止呢,我们是已经把这个订单分类的逻辑呢,已经写完了。

所有的代码呢,是不是全都是封装到了我们service的这个execute方法当中。

当然这个过程呢,实行起来还是比较复杂的,对吧?

你看我们整个类呢,是有几百行的代码,这么一个量。

好,这是我们订单分类的逻辑。

然后再往后呢,其实就是关于什么呢?

路线的规划,对吧?

包括一些司机啊,车辆啊,

车次啊,规划。

然后呢,最终是创建我们司机的这个运输作业,对吧?

运输作业。

那么鉴于时间关系呢,我们其他的这些业务代码,也就是订单分类之后的这些业务代码呢,我们就不在课堂上去手敲了。

因为这块这个业务代码,这个量的话呢,其实相对于我们订单分类来说是更多的。

由于我们课堂时间呢,是有限的。

所以剩下的其他的功能代码呢,咱们就直接来导入。

然后大家直接使用这个代码就可以了。

好,那么导入的代码在哪呢?

在我们资料,智能调度服务相关资料。

然后呢,智能调度服务功能代码导入这个目录里边。

然后呢,我们可以来看一下,就是当前这个目录里边。

好,首先呢,我们先来看service,对吧?

你看service的话,它是不是又扩展出来了这么一些接口。

好,但是还有一些呢,是我们已经存在的接口,可能需要扩展方法,对吧?

所以说呢,我们整个呢,就复制一下就可以了。

把这些接口来复制一下。

然后呢,放到哪呢?

放到我们当前这个service包下面来,直接往这粘贴一下。

OK。

你看,它是有相同的,相同的直接覆盖就可以了。

因为在service里边,我们是扩展了其他的方法。

然后呢,我们再到这个IMPL实现类里边来,对吧?

然后呢,把这些实现类呢,也复制过来。

好,直接放到这个IMPL这个包下面。

然后呢,直接来粘贴一下。

好,这里边呢,也有一个相同的。

好,直接覆盖一下。

好,这是service呢,咱们就拷过来了。

然后接下来呢,我们拷什么呢?

service拷完之后呢,我们来拷controller,对吧?

这里边呢,有三个controller。

咱们呢,直接连同这个controller包呢,一块来复制一下就可以了。

好,直接放到品达这层目录下边就可以了。

好,直接往这粘贴一下。

OK。

咱们来看一下。

这是一些什么呢?

都是跟我们这个订单相关的,订单相关的。

其实都是通过controller,叫service,对吧?

都是一些数据库操作。

包括这边,你看,这是我们定时任务的,定时任务分页,对吧?

然后呢,是不是,这个应该是调度信息,查看。

然后呢,保存一个定时任务,是不是,修改定时任务等等这些。

好。

那么基本上都是一些数据库操作。

然后还有呢,就是我们刚才看到的这个dispatch task,对吧?

这块代码呢,是需要完善一下。

咱们来看一下这个task里边,是不是有这个dispatch task。

好。

然后呢,我们直接把这个代码呢,重新整个把这个类呢,覆盖一下就可以了。

把这个类覆盖一下就可以了。

咱们直接复制这个类,对吧?

然后呢,把我们原先这个类呢,覆盖一下。

就可以了。

好。

OK。

好,覆盖一下。

覆盖完了之后呢,咱们来看dispatch task,对吧?

然后呢,这个就不需要了。

然后呢,我们来看一下,它这里边呢,是不是首先是调用我们这个service,这是咱们自己写的,对吧?

订单分类。

订单分类之后呢,然后调这个service,这是我们刚才考进来的一个service,对吧?

好。

这个是做什么呢?

做路线规划的这个service。

好。

好。

路线规划完成之后呢,是不是,就是。

就是创建运输任务啊,关联运单啊,等等这些。

这就是一个service。

然后接下来呢,是规划车次车辆司机。

然后呢,是不是完善什么运输任务,创建司机作业任务等等。

好。

也就是这些环节呢,我们全都是封装到一个一个的service当中来。

而这些呢,其实也都是一些数据库操作啊,数据库操作。

所以说呢,我们这块呢,由于代码量还是非常非常多的,所以我们就不在课堂上去手敲了。

咱们直接把代码拿过来。

然后呢。

拿过来直接使用就可以了。

好。

这是关于我们整个智能调度这一块啊。

那么其他的功能代码,我们直接导进来使用即可。

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一节关于“智能调度”系统核心代码实现的教学演示。讲师通过 IntelliJ IDEA 开发环境，逐步讲解了从定时任务触发、订单分类、路线规划到创建运输任务的完整业务流程。核心代码位于 `DispatchTask.java` 中，它通过 Spring 的 `@Component` 注解被注册为一个定时任务，并调用多个服务（如 `orderClassifyService`、`routePlanningService`、`businessOperationService`）来完成复杂的业务逻辑。视频重点展示了如何通过反射机制动态调用目标方法，并对整个流程进行了日志记录和异常处理，体现了典型的分层架构和面向接口编程的设计思想。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00:00 - 00:00:05**：视频开场，展示项目结构和 `ScheduleJob.java` 文件，介绍这是一个定时任务。
*   **00:00:05 - 00:00:15**：讲解 `ScheduleJob.java` 中的 `try-catch-finally` 块，重点是通过反射调用目标方法 `target.getClass().getDeclaredMethod("run", ...)`。
*   **00:00:15 - 00:00:25**：切换到 `DispatchTask.java` 文件，展示其作为调度任务的入口。
*   **00:00:25 - 00:00:35**：展示 `DispatchTask` 类的成员变量和 `run` 方法的签名，参数包括 `businessId`, `params`, `jobId`, `logId`。
*   **00:00:35 - 00:00:45**：展示 `DispatchTask` 中调用 `taskOrderClassifyService.execute(...)` 方法进行订单分类。
*   **00:00:45 - 00:00:55**：展示 `DispatchTask` 中调用 `routePlanningService.execute(...)` 方法进行路线规划。
*   **00:00:55 - 00:01:05**：展示 `DispatchTask` 中调用 `businessOperationService.createTransportOrderTask(...)` 方法创建运输任务。
*   **00:01:05 - 00:01:15**：展示 `OrderLocusController.java` 和 `ScheduleJobController.java`，说明调度任务由控制器层发起。
*   **00:01:15 - 00:01:25**：展示 `DispatchTask` 的完整代码结构，包括 `@Component`、`@Autowired` 注解和 `@SneakyThrows` 注解。
*   **00:01:25 - 00:01:35**：展示 `DispatchTask` 中的 `log.info` 日志语句，用于记录任务执行过程。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **关键代码片段 1 (ScheduleJob.java)**：
    ```java
    try {
        // 通过反射调用目标对象方法，在目标对象中封装智能调度核心逻辑
        logger.info("定时任务准备执行，任务id为: {}", scheduleJob.getId());
        // 获取目标对象
        Object target = SpringContextUtils.getBean(scheduleJob.getBeanName());
        // 通过反射调用目标方法
        Method method = target.getClass().getDeclaredMethod("run", String.class, String.class, String.class, String.class);
        method.invoke(target, scheduleJob.getBusinessId(), scheduleJob.getParams(), scheduleJob.getJobId(), scheduleJob.getLogId());
        logEntity.setStatus(1); // 成功
    } catch (Exception ex) {
        logEntity.setStatus(0); // 失败
        logger.error("定时任务执行失败，任务id为: {}", scheduleJob.getId());
    } finally {
        int times = (int) (System.currentTimeMillis() - startTime);
    }
    ```

*   **关键代码片段 2 (DispatchTask.java)**：
    ```java
    @Component("dispatchTask")
    @Slf4j
    public class DispatchTask {
        @Autowired
        private ITaskOrderClassifyService taskOrderClassifyService;
        @Autowired
        private ITaskRoutePlanningService routePlanningService;
        @Autowired
        private ITaskTripsSchedulingService truckSchedulingService;
        @Autowired
        private IBusinessOperationService businessOperationService;

        @SneakyThrows
        public void run(String businessId, String params, String jobId, String logId) {
            log.info("智能调度正在执行，参数为: {}, {}, {}, {}", businessId, params, jobId, logId);
            // 订单分类
            List<OrderClassifyGroupDTO> classifyGroupDTOs = taskOrderClassifyService.execute(businessId, jobId, logId);
            // 路线规划
            List<OrderLineSimpleDTO> orderLineSimpleDTOs = routePlanningService.execute(classifyGroupDTOs, businessId, jobId, logId, params);
            // 创建运输任务
            Map<String, TaskTransportDTO> transportTaskMap = businessOperationService.createTransportOrderTask(orderLineSimpleDTOs);
            log.info("运输任务创建完成: {}", LOGID, transportTaskMap);
        }
    }
    ```

*   **关键代码片段 3 (OrderClassifyService.java)**：
    ```java
    public List<OrderClassifyGroupDTO> execute(String agencyId, String jobId, String logId) {
        // 用于存放当前机构下的订单
        List<OrderClassifyGroupDTO> orderClassifyDTOs = new ArrayList<>();
        // 获取当前机构下所有的订单数（分为新订单和中转订单）
        orderClassifyDTOs.add(buildNewOrder(agencyId));
        orderClassifyDTOs.add(buildTransferOrder(agencyId));
        // 进行订单分类
        Map<String, OrderClassifyGroupDTO> orderClassifyDTOGroup = orderClassifyDTOs.stream()
                .collect(Collectors.groupingBy(OrderClassifyGroupDTO::getOrderType));
        // 对象转换，将当前Map对象转为 List<OrderClassifyGroupDTO> 类型
        orderClassifyDTOGroup.forEach((key, value) -> {
            builder.key(key);
            // 获取原始订单对象
        });
    }
    ```

*   **关键代码片段 4 (ScheduleJobController.java)**：
    ```java
    @GetMapping("/dispatch/{id}")
    @ApiOperation("调度信息")
    public Result dispatchInfo(@PathVariable("id") String id) {
        LambdaQueryWrapper<ScheduleJobEntity> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(ScheduleJobEntity::getBusinessId, id);
        ScheduleJobEntity scheduleJobEntity = scheduleJobService.getOne(wrapper);
        if (scheduleJobEntity == null) {
            return Result.error(code: 404, msg: "机构没有任务信息");
        }
        ScheduleJobDTO schedule = new ScheduleJobDTO();
        BeanUtils.copyProperties(scheduleJobEntity, schedule);
        return Result.ok().put("data", schedule);
    }
    ```

---

### 4) 关键场景与演示描述

*   **场景一：定时任务触发与反射调用 (00:00:00-00:00:15)**
    讲师首先展示了 `ScheduleJob.java` 文件，这是一个定时任务的实现。他通过 `SpringContextUtils.getBean(...)` 获取目标对象，然后使用 `Method` 类的 `getDeclaredMethod` 方法获取目标方法 `run`，并使用 `invoke` 方法动态调用该方法。整个过程被包裹在 `try-catch-finally` 块中，用于处理异常和记录执行时间。

*   **场景二：调度任务核心逻辑 (00:00:15-00:01:35)**
    讲师切换到 `DispatchTask.java` 文件，这是一个被 `@Component` 注解标记的调度任务。他展示了该类的成员变量，包括 `taskOrderClassifyService`、`routePlanningService`、`businessOperationService` 等服务接口。在 `run` 方法中，他依次调用这些服务的方法：首先调用 `taskOrderClassifyService.execute(...)` 进行订单分类，然后调用 `routePlanningService.execute(...)` 进行路线规划，最后调用 `businessOperationService.createTransportOrderTask(...)` 创建运输任务。每个步骤都伴随着日志记录，用于追踪任务执行状态。

*   **场景三：服务层实现 (00:00:35-00:00:55)**
    讲师在 `DispatchTask.java` 中展示了 `orderClassifyService.execute(...)` 的调用。他通过 `@Autowired` 注解注入了 `ITaskOrderClassifyService` 接口的实现类，并在 `run` 方法中调用其 `execute` 方法。这体现了面向接口编程的设计模式，使得业务逻辑与具体实现解耦。

*   **场景四：控制器层交互 (00:01:05-00:01:15)**
    讲师展示了 `ScheduleJobController.java` 文件，其中包含一个 `@GetMapping("/dispatch/{id}")` 的接口，用于获取调度任务信息。该接口通过 `Lambda
