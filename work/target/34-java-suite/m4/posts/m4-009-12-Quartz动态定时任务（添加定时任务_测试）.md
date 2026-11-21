---
title: "Quartz 动态定时任务全套操作：暂停、恢复、删除、立即执行与更新，及智能调度服务的数据模型"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 品达物流TMS]
tags: [Java, 项目实战, Quartz]
---

# Quartz 动态定时任务全套操作：暂停、恢复、删除、立即执行与更新，及智能调度服务的数据模型

上一篇写出了动态添加定时任务的 save 方法，这一篇补上 misfire 策略、跑通第一次真实测试，再把生命周期剩余动作一次补齐：暂停、恢复、删除、立即执行、更新触发规则，动态定时任务这套 API 到此完整。后半篇转入第八章的主角智能调度服务（pd-dispatch），讲清业务流程，过一遍六张业务表，为编码做准备。

## 先给结论

- save 收尾：CronScheduleBuilder 链上 withMisfireHandlingInstructionDoNothing，错过触发时间不做任何事，等下一次触发；MySQL 6+ 连接串必须带 serverTimezone 参数，否则启动报时区异常。
- 落库位置：qrtz_cron_triggers 存表达式，qrtz_job_details 存任务实例（job_name 即 withIdentity 的 bizId，job_data 以 BLOB 存 JobDataMap 的值）；jobStore.class 用的 JobStoreTX，重启后任务照常执行、状态照常取到。
- 暂停/恢复/删除/立即执行全靠 JobKey 定位（JobKey.jobKey(bizId)）：pauseJob/resumeJob 改 qrtz_triggers 的 TRIGGER_STATE（PAUSED/ACQUIRED）；deleteJob 清掉 qrtz_triggers、qrtz_cron_triggers、qrtz_job_details 三张表的记录；triggerJob 无视状态，调一次执行一次。
- 更新触发规则四步：TriggerKey 定位原触发器，getTrigger 强转 CronTrigger，getTriggerBuilder 重设 withSchedule 再 build，rescheduleJob 重新调度，不重启即生效。前提：创建 Trigger 也要 withIdentity(bizId)，否则框架随机生成 UUID 般的 trigger name，后面没法定位。
- 智能调度针对单个网点/转运中心：订单分类、路线规划、创建运输任务、规划车次车辆、创建司机运输作业五步；触发两种，Quartz 定时任务自动触发与页面人工"立即运行"，每个机构都有自己的定时任务。
- 业务表六张：schedule_job、schedule_job_log、pd_order_classify、pd_order_classify_order、pd_cache_line、pd_cache_line_detail，加上 Quartz 官方的 QRTZ_ 表，库 pd_dispatch 共 20 张。

## 添加任务的收尾：misfire 策略与 serverTimezone

save 方法还差一处收尾，创建 CronScheduleBuilder 时补调一个方法：

```java
CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule(cronExpression)
        .withMisfireHandlingInstructionDoNothing();
```

withMisfireHandlingInstructionDoNothing 是 misfire（错过触发）的处理策略：动态添加任务时如果已经错过了计划的时间点，什么都不做，直接等下一次触发。比如表达式指定每天上午 10 点执行，10 点之后才添加的任务，今天已错过，下次触发就是明天上午 10 点，错过的那次不补执行。misfire 有好几种策略，课程选的是 DoNothing。

启动服务做第一次测试，直接报错：异常指向数据源，SQL 异常 The server time zone value...，后面跟着一段乱码。这是时区问题，MySQL 6 以后的版本要求连接串必须指定 serverTimezone。原连接串后面已带编码方式、useUnicode=true 等参数，再补 `serverTimezone=Asia/Shanghai`，重启后服务正常，端口 8080。

此时控制台没有任务输出，因为还没添加任务。打开 Swagger UI（localhost:8080/swagger-ui）调添加接口：bizId 给 1001，cron 表达式秒位随手写 1,5,10,20,30,35,55，其余位置星号，周的位置问号。执行返回 OK，控制台按这些秒点输出：自定义Job执行，bizId = 1001，执行时间 10:1:05，接着 20、35、55，完全按表达式走。再加一个 bizId=1002、表达式不同的任务，两个任务各自按节奏执行。

数据库里的落库结果：qrtz_cron_triggers 两条记录，就是页面上输入的两个表达式；qrtz_job_details 里是两个任务实例，job_name 对应 withIdentity 的 bizId，触发执行的是 HelloJob 的 executeInternal。JobDataMap 的值也存在这张表的 job_data 字段上，类型是 BLOB，客户端只能看到一个 228 bytes 的大小，不直观但确实在。这正是上一篇伏笔的答案：配置类里 org.quartz.jobStore.class 用 JDBC 的 JobStoreTX，任务信息才写进这 11 张表；服务重启后两个任务继续按时触发，bizId 照样动态取出，状态不丢。

## 暂停、恢复、删除、立即执行：四个生命周期接口

四个接口套路一致，都比添加简单：用 bizId 封装 JobKey，交给 Scheduler 对应的方法。bizId 就是添加任务时 withIdentity 设置的唯一标识。

暂停用 pauseJob，PUT 方式，参数从请求路径提交（@PathVariable）：

```java
@PutMapping("/pause/{bizId}")
@ApiOperation("暂停定时任务")
public String pause(@PathVariable String bizId) throws Exception {
    JobKey jobKey = JobKey.jobKey(bizId);
    scheduler.pauseJob(jobKey);
    return "OK";
}
```

测试：控制台里 1001、1002 都在输出，调 pause 传 1001，返回 OK 后只剩 1002 在执行；再把 1002 也暂停，控制台彻底安静。底层变化落在 qrtz_triggers 表：pauseJob 改的就是 TRIGGER_STATE 字段，暂停后两个任务的触发器状态都变成 PAUSED。暂停不是删除，任务还在，只是不再触发。

恢复与暂停恰好相反，调 resumeJob：

```java
@PutMapping("/resume/{bizId}")
@ApiOperation("恢复定时任务")
public String resume(@PathVariable String bizId) throws Exception {
    JobKey jobKey = JobKey.jobKey(bizId);
    scheduler.resumeJob(jobKey);
    return "OK";
}
```

两个任务都在 PAUSED 状态时启动服务，控制台没有输出；调 resume 恢复 1001，控制台马上恢复输出，qrtz_triggers 里 1001 那条的状态变成 ACQUIRED，意思是已经获得执行的权利。

删除用 deleteJob，把任务数据真正删掉：

```java
@DeleteMapping
@ApiOperation("删除定时任务")
public String delete(String bizId) throws Exception {
    JobKey jobKey = JobKey.jobKey(bizId);
    scheduler.deleteJob(jobKey);
    return "OK";
}
```

测试删 1001：执行后控制台不再出现 1001，刷新数据库，qrtz_job_details、qrtz_cron_triggers、qrtz_triggers 三张表各少一条记录，都只剩 1002。deleteJob 一次操作，任务实例、触发器、表达式全清掉。

立即执行用 triggerJob。正常情况任务由触发器按规则触发，有时不想等，比如设的是每天下午五点触发，现在就想马上跑一次：

```java
@PutMapping("/run/{bizId}")
@ApiOperation("立即执行定时任务")
public String run(@PathVariable String bizId) throws Exception {
    JobKey jobKey = JobKey.jobKey(bizId);
    scheduler.triggerJob(jobKey);
    return "OK";
}
```

测试现场：1001 已删，只剩 1002，且 1002 处于暂停状态（TRIGGER_STATE 是 PAUSED），控制台无输出。对 1002 调 run，返回 OK，控制台立刻执行一次；再调一次，再执行一次。结论：立即执行跟任务状态无关，只要调这个方法，Job 就执行一次。这些接口在 Swagger 里对应 PUT /quartz/pause/{bizId}、PUT /quartz/resume/{bizId}、PUT /quartz/run/{bizId}、DELETE /quartz。

## 更新定时任务：先把 Trigger 的名字抓在自己手里

更新定时任务主要更新触发时间：原来每天上午 10 点触发，想改成每天下午 5 点。参数两个：bizId 找到原先的触发器，cronExpression 是新规则。

动手前先解决一个隐藏问题。添加任务创建触发器时没给 Trigger 调 withIdentity，Quartz 会自动生成唯一标识。qrtz_triggers 表里看得很清楚：job_name 对应 bizId（1001、1002），trigger name 却是一长串类似 UUID 的随机字符串。框架生成能保证不重复，但我们不知道它生成了什么，后面按标识获取原触发器就没法下手。先把 save 方法改掉，创建触发器时自己指定标识，同样用 bizId：

```java
@PostMapping
@ApiOperation("添加定时任务")
public String save(String bizId, String cronExpression) throws Exception {
    JobDetail jobDetail = JobBuilder.newJob(HelloJob.class).withIdentity(bizId).build();
    jobDetail.getJobDataMap().put("bizId", bizId);
    // 表达式调度构建器
    CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule(cronExpression)
            .withMisfireHandlingInstructionDoNothing();
    Trigger trigger = TriggerBuilder.newTrigger().withIdentity(bizId)
            .withSchedule(cronScheduleBuilder).build();
    // 关联任务实例和触发器对象
    scheduler.scheduleJob(jobDetail, trigger);
    return "OK";
}
```

重新添加一个 bizId=1003 的任务，qrtz_triggers 里 trigger name 变成 1003，触发器和任务用同一个标识，一一对应。

然后是 update 方法，PUT：

```java
@PutMapping
@ApiOperation("更新定时任务")
public String update(String bizId, String cronExpression) throws Exception {
    // 获取触发器的唯一标识
    TriggerKey triggerKey = TriggerKey.triggerKey(bizId);
    // 获得原有的触发器
    CronTrigger trigger = (CronTrigger) scheduler.getTrigger(triggerKey);
    // 构造新的触发规则
    CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule(cronExpression)
            .withMisfireHandlingInstructionDoNothing();
    // 重新构建触发器
    trigger = trigger.getTriggerBuilder().withIdentity(bizId).withSchedule(cronScheduleBuilder).build();
    // 重新按新的规则进行调度
    scheduler.rescheduleJob(triggerKey, trigger);
    return "OK";
}
```

四步：TriggerKey.triggerKey(bizId) 拿触发器唯一标识；scheduler.getTrigger(triggerKey) 获得原触发器，返回类型是 Trigger，原触发器基于 cron 表达式，向下强转成 CronTrigger（CronTrigger 继承 Trigger）；trigger.getTriggerBuilder() 拿到构建器，withIdentity 沿用原标识、withSchedule 换新规则构建器，build 出新触发器直接赋回原变量，不必声明新变量；最后 rescheduleJob(triggerKey, trigger) 按新规则重新调度。不重启服务，触发规则就已经变了。

测试：1003 的表达式秒位是 1,10，控制台按这两个秒点输出，下一次执行在 33 分 01 秒。Swagger 里调更新接口，bizId=1003，表达式抄过来秒位改成 11,20。执行后看数据库：qrtz_cron_triggers 里 1003 的 CRON_EXPRESSION 已变成新表达式，qrtz_triggers 里下次触发时间从 33 分 01 秒变成 33 分 11 秒，trigger name 还是 1003，一眼看出哪个触发器被改了。控制台随后按 11 秒、20 秒输出，中间 MisfireHandler 处理了一条错过触发的事件，属正常日志。

## 智能调度服务：业务流程与数据模型

Quartz 部分收口，第八章第三部分进入正题：智能调度服务。代码写在 pd-dispatch 这个 Maven 工程，对应数据库也叫 pd_dispatch，共 20 张表。表名大写、QRTZ_ 开头的是 Quartz 官方自带表，智能调度用定时任务并持久化，这套表跟着进来；其余是业务表。

智能调度的业务：针对物流公司的网点、转运中心这些机构，对它们的订单进行处理，最终生成司机的运输作业，司机按作业执行货物运输。网点揽回来的件目的地五花八门，都要装车转运；北京发上海的货往往不是一车拉到底，先到济南的转运中心换车，到南京卸下一部分，再换车到上海。怎么转、转几次、走哪条线路、哪个司机、哪个车次、哪辆车，全是智能调度要考虑的细节。

流程拆成五个阶段：

```mermaid
flowchart LR
    A[订单分类] --> B[路线规划]
    B --> C[创建运输任务]
    C --> D[规划车次车辆]
    D --> E[创建司机运输作业]
```

订单分类：按订单收件人地址所属网点分类，收货网点相同的归一类，因为它们很可能装同一辆车；发上海的和发新疆的方向不同，一般不会装同一辆车。路线规划：根据当前网点和目的地网点查符合条件的线路，分直达和中转两类，中转占绝大多数（像北京到天津这种近距离才有直达），并确定每类订单走哪条线路。创建运输任务：按规划结果创建运输任务，更新订单状态，让运输任务关联运单。规划车次车辆：查符合条件的车次车辆，包括由哪个司机执行。创建司机运输作业：司机不关心前面的复杂过程，司机端只看到一个个作业，从哪拉到哪、开哪辆车、几点走、拉哪些货，接单执行即可。

触发方式两种：Quartz 定时任务自动触发，比如每天下午五点或六点，触发时对某个网点下的所有订单走一遍流程；人工干预，管理页面点"立即运行"马上调度。调度粒度要强调：智能调度针对某一个网点或转运中心，不是全国的单子一起调度，数据量庞大也没必要。所以定时任务有多个，每个网点、转运中心都有自己的定时任务。管理页面左侧是机构树，点开某个机构（如石家庄网点）能看到它对应的定时任务和 cron 表达式（每天 18 点触发），表达式可直接改写；小店区网点配的就是另外的表达式。

数据模型六张业务表。第一张 schedule_job 定时任务表：网点加转运中心若有 1000 个，这张表就该有 1000 条记录。

| 字段 | 含义 |
| :--- | :--- |
| id | 主键 |
| bean_name | Spring bean 名称，任务逻辑写在对应的 bean 里（如 dispatchTask，其中有 run 方法） |
| params | 参数，路线规划策略：transfer 转运最少、cost 费用最低、distance 距离最短，类似地图导航的多策略 |
| cron_expression | 表达式，决定触发时间（测试数据里为快速出效果配过每 5 秒触发） |
| status | 任务状态，0 暂停 1 正常；网点歇业改成 0 就不再触发 |
| business_id | 关键字段，网点/转运中心在组织机构表里的主键值，决定本次调度处理哪个机构的订单 |
| remark / creator / create_date 等 | 备注、创建人、创建时间、更新人、更新时间 |

params 补一句：多条线路都能从起点走到终点，按哪个策略规划全靠这个参数。business_id 是重点中的重点：每次触发时，要调度的就是它对应机构的订单。

第二张 schedule_job_log 日志表，任务每触发一次记一条：job_id 对应定时任务主键，bean_name、params 随任务带过来，status 记任务状态，error 记失败信息，times 记耗时（执行了多长时间），create_date 创建时间。

第三张 pd_order_classify 订单分类表，分类结果持久化到这里，每个分类一条数据。一个网点一天 1000 个订单，按目的地分出一两百个类，每类一条。字段：job_id（对应哪个定时任务，逻辑外键，没真正建外键约束）、job_log_id（本次调度的日志 id）、start_agency_id（起始机构，揽件网点的 id）、end_agency_id（结束机构，负责派送收件人地址的网点 id）、classify（订单类别）、total（该类订单数量，10 个订单归一类 total 就是 10）、create_date。classify 的构成是关键：当前机构、起始机构、目的机构三个 id 用井号拼接，三者完全相同的订单就是同一类，拼接逻辑写代码时能看到。

第四张 pd_order_classify_order 关联表：分类表只记"某一类"，1000 个订单每个属于哪一类靠这张中间表，order_classify_id 关联订单分类主键，order_id 是订单 id，一个分类对应多个订单。

第五张 pd_cache_line 缓存路线表，路线规划成功后往里插数据。前提要先明确：规划不是凭空算路，基础线路数据必须提前存在，维护在基础模块 pd_base 对应数据库的 pd_transport_line 线路表里（北京到天津、天津到济南这些线路都要先有）。规划就是在已有线路里找组合：先看北京到上海有没有直达，有最好；没有就北京到天津、天津到济南、济南到南京、南京到上海一条条拼起来，多次中转到达目的地。线路数据维护不全时会出现怎么拼都到不了目的地的情况，所以基础线路数据必须完整。字段：start_agency_id（寄件人所在网点 id）、end_agency_id（收件地址对应派送网点的 id；寄件只写详细地址，这个 id 是按地址算出来的，取离收件地址最近的网点）、verify_key（校验线路是否可用的 key，后面用到再展开）、distance 距离、cost 成本、estimated_time 预计到达时间、transfer_count 中转次数、version（本次计算出的线路版本号）、is_current（是否当前最新版本，0 否 1 是）、create_date。distance、cost、estimated_time、transfer_count 全是基于已有线路算出来的，不存在人工表单录入。这张表只体现从哪个网点到哪个网点，具体走哪几条线说不清。

说不清的部分在第六张 pd_cache_line_detail 缓存路线子表：cache_line_id 对应主表主键；start_agency_id 数据冗余；transport_line_id 记录具体某条线路的 id，指向 pd_base 里 pd_transport_line 表的主键值，逻辑外键；sort 排序从 1 开始，决定先走哪条后走哪条。北京到上海的方案若是四条线路（北京到天津、天津到济南、济南到南京、南京到上海），子表就是四条记录，sort 为 1、2、3、4，按顺序一条条走最终到上海。主表管"从哪到哪"，子表管"具体怎么走"，合起来才是一次完整的规划结果。

## 小结

这一篇给动态添加收尾：misfire 选 DoNothing，错过的触发不补；连接串补 serverTimezone 后测试跑通，qrtz_cron_triggers、qrtz_job_details 里能看到落库结果，重启后任务照常执行。pauseJob、resumeJob、deleteJob、triggerJob 全用 JobKey 定位，前两个改触发器状态，删除一次清三张表，立即执行无视状态调一次跑一次；更新走 TriggerKey 加 rescheduleJob 四步，前提是触发器也用 bizId 做标识。智能调度服务 pd-dispatch 针对单个机构做五步调度，每个机构一个定时任务，可自动触发也可人工立即运行；六张业务表从任务定义、执行日志、订单分类、分类关联到缓存路线主子表，构成了后面编码要对着实现的图纸。
