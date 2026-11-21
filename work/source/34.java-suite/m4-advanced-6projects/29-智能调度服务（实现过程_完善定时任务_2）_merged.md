# 29-智能调度服务（实现过程_完善定时任务_2） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来完善我们这个定时任务这个类,其他的呢,我先关上啊,清晰一点,好,刚才呢,我们是把这个日志信息,这个实体对象呢,是不是封装了一下,然后呢,在这个地方调用我们的service来保存,只不过这个service呢,并不是我们直接通过AutoVar的那个注解注进来的,为什么呢,就是因为我们当前这个类呢,并没有有,并没有交给Spring容器去管理,对吧,

所以它肯定是注不进来的,那怎么办呢,我们可以通过这个工具类,对吧,从Spring容器里面来获得这个service对象,然后呢,来保存就可以了,好,然后呢,我们可以,咱们前面这不是加了一个记录器对象吗,对吧,那么我们可以在控制台上来记录一些日志信息,比如说在这个地方,对吧,try开始的时候呢,这就说明我们这个info,这个定时任务,对吧,定时任务准备执行,准备执行,

那么任务ID,任务ID为,这个地方呢,咱们可以使用一个这种占位符,对吧,这个任务ID呢,可以通过我们这个传进来的这个实体对象,获得的这个实体对象呢,就是它的主件值,对吧,点get ID来获得,好,这是try,如果进了catch呢,是不是说明它这个定时任务执行失败了,对吧,那么如果失败的话呢,咱们也可以给它来加一个,但是这儿呢,改成error,

定时任务,这个执行失败,失败,好,任务ID呢,也是这样来获得,好,这是方便我们调试啊,好,然后呢,我们接下来就来重点看try这个地方,前面我们也说了,在这个地方呢,我们是不是要通过反射来调用我们真正的目标对象,对吧,哎,那这个目标对象怎么获得呢,我们首先呢,需要通过什么呢,这个sprint,通过我们这个sprint容器啊,这个工具类,

对吧,也就是这个地方,sprintcontact,utils这个工具类,然后来获得getbin,注意,这个class呢,不能直接写,因为什么呢,因为我们在数据库里面保存的是bin的name,对不对,是这个bin名称,哎,所以说呢,这个地方传进来的,我们getbin啊,getbin,传进来的应该是bin的名称,而这个名称的话呢,注意,不是写死的,是一个动态的,咱们是不是通过这个实体类能够获得,对吧,get a job,

这里边呢,是不是有一个,

叫做bin name,啊,这样就能获得,啊,但是这个地方呢,它得到的肯定是一个object的对象,这就是我们的target,这是获得目标对象,获得目标对象,然后呢,这个对象里边呢,应该有一个方法,哎,这个方法呢,我们就可以固定给它写死了,就叫run方法就可以,所以我们可以通过这个target对象.getclass.get什么呢,declared method,对吧,哎,获得它这个,

对象的方法,这个方法名呢,叫做run,然后呢,这个方法的参数呢,哎,是有四个,全都是什么呢,全都是这个死罪类型的,咱们后边呢,会翻过头来来写这个类啊,咱们现在呢,先把当前我们这个类给完善了,后边我们会翻过头来来写这个类,那你看这样的话,我是不是就获得了一个什么呢,method,啊,方法对象,对吧,这就是获得目标方法,哎,对象,

你看它是封装成了一个method,啊,然后呢,这个方法呢,必须叫run了,必须叫run,所以一会儿我们在编写那个目标类的时候呢,里边必须有一个run方法,并且呢,这个方法应该有四个参数,而且呢,全都是死罪类型的,全都是死罪类型的,啊,具体这四个死罪类型代表什么含义呢,哎,咱们来看一下,我们这个地方呢,就要来调用什么呢,调用,哎,通过反射,

啊,通过反射来调用我们目标对象的方法,怎么调用呢,非常简单,通过method.invoke,对吧,哎,invoke,咱们学过反射的应该也都用过,啊,哎,这表示我要调这个方法,调哪个方法呢,调这个target,目标对象的方法,而这个方法是不是要求有四个参数,并且都是死罪类型,对吧,那么这四个参数呢,我们在这个地方,你在调这个方法的时候呢,就需要给我传进来,第一个是什么呢,第一个是我们传进来的,其实是这四个参数,

这个business id,哎,是这个字段的值,这个值呢,怎么获得呢,还是从我们这个,从这个实体对象这儿来获得,这是第一个参数,get business id,这是第一个参数,然后第二个参数呢,也是从他这儿来获得,是什么呢,是parameters,parameters呢,对应的就是传进来的是,呃,来看一下,哎,这个字段的值,这个字段的值,啊,然后第三个呢,就是我们这个job id,get id,

job id呢,对应的就是我们这个主件值,哎,主件值,然后还有一个是什么呢,就是我们这个日志表的主件,日志呢,你看我们前面这边已经封装了吗,就是这个log entity,对吧,啊,然后呢,并且我们在这是不是已经set他的id了,哎,所以在这个地方呢,传进来的就是这个日志表的主件,get id,ok,

那,这个地方呢,这就是咱们通过反射,对吧,来调用目标对象的这个目标方法,啊,

那么大概就是这么几句代码,哎,这么几句代码,哎,那么我们在这个地方呢,通过反射来调他就可以了,一会儿呢,我们就会重点去写另外一个目标类,对吧,哎,这个类名呢,叫什么呢,就跟我们这个bin的名称保持一致吧,就叫dispatch task,哎,dispatch其实就是什么呢,就是什么分发呀,或者是,呃,这个转换呢,哎,等等,这一类的意思,啊,这么一个任务类,啊,然后在这里边呢,去干什么呢,去封装我们真正的这个智能调码,啊,这个任务类呢,就跟我们这个bin的名称保持一致吧,就叫dispatch task,啊,这个任务

啊,只能调度这块的逻辑,啊,所以关于我们当前这个定时任务类呢,我们先完善到这儿

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析。

---

### 1) 视频摘要

本视频片段展示了一个基于 Spring 和 Quartz 的定时任务调度系统的核心实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了 `ScheduleJob` 类中 `executeInternal` 方法的逻辑。该方法的核心是利用 Java 反射机制，在运行时动态获取并调用一个指定的业务方法。整个过程被封装在一个日志记录的上下文中，用于记录任务的执行状态、耗时和异常信息。视频重点讲解了如何通过 `SpringContextUtils.getBean()` 获取目标对象，再通过 `Class.getDeclaredMethod()` 获取目标方法，最后调用 `Method.invoke()` 来执行该方法。

---

### 2) 按时间顺序的章节（带时间点）

由于提供的画面没有明确的时间戳，以下时间点是根据画面内容的逻辑顺序进行的推断：

*   **00:00 - 00:05**: 展示 `ScheduleJob.java` 文件的整体结构和 `executeInternal` 方法的入口。
*   **00:05 - 00:10**: 代码开始执行，创建日志实体 `logEntity` 并设置基础信息（ID、Bean名、参数、创建时间）。
*   **00:10 - 00:15**: 记录任务开始执行的时间戳 `startTime`。
*   **00:15 - 00:20**: 通过 `SpringContextUtils.getBean()` 获取目标对象 `target`。
*   **00:20 - 00:25**: 通过 `target.getClass().getDeclaredMethod()` 获取名为 `run` 的目标方法 `method`。
*   **00:25 - 00:30**: 调用 `method.invoke(target, ...)` 方法，传入业务参数和日志对象，执行核心业务逻辑。
*   **00:30 - 00:35**: 在 `try` 块成功执行后，设置日志状态为成功 (`setStatus(1)`)。
*   **00:35 - 00:40**: 在 `catch` 块捕获异常后，设置日志状态为失败 (`setStatus(0)`) 并记录异常堆栈。
*   **00:40 - 00:45**: 在 `finally` 块中计算并记录任务耗时，然后将日志实体保存到数据库。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

**关键代码片段：**

```java
public class ScheduleJob extends QuartzJobBean {

    private Logger logger = LoggerFactory.getLogger(getClass());

    @Override
    protected void executeInternal(JobExecutionContext context) throws JobExecutionException {
        ScheduleJobEntity scheduleJob = (ScheduleJobEntity) context.getMergedJobDataMap().get(ScheduleUtils.JOB_PARAM_KEY);
        System.out.println(new Date() + "定时任务开始执行...定时任务id: " + scheduleJob.getId());

        // 封装日志对象
        ScheduleJobLogEntity logEntity = new ScheduleJobLogEntity();
        logEntity.setId(IdUtils.get());
        logEntity.setJobId(scheduleJob.getId());
        logEntity.setBeanName(scheduleJob.getBeanName());
        logEntity.setParams(scheduleJob.getParams());
        logEntity.setCreateDate(new Date());

        long startTime = System.currentTimeMillis();

        try {
            // 通过反射调用目标对象，在目标对象中封装智能调度核心逻辑
            logger.info("定时任务准备执行，任务id为: {}", scheduleJob.getId());

            // 获取目标对象
            Object target = SpringContextUtils.getBean(scheduleJob.getBeanName());

            // 获取目标方法
            Method method = target.getClass().getDeclaredMethod("run", String.class, String.class, String.class, String.class);

            // 通过反射调用目标对象的方法
            method.invoke(target, scheduleJob.getBusinessId(), scheduleJob.getParams(), scheduleJob.getId(), logEntity.getId());

            logEntity.setStatus(1); // 成功
        } catch (Exception ex) {
            logEntity.setStatus(0); // 失败
            logEntity.setError(ExceptionUtils.getStackTrace(ex));
            logger.error("定时任务执行失败，任务id为: {}", scheduleJob.getId());
        } finally {
            int times = (int) (System.currentTimeMillis() - startTime);
            logEntity.setTimes(times); // 耗时
            IScheduleJobLogService scheduleJobLogService = SpringContextUtils.getBean(IScheduleJobLogService.class);
            scheduleJobLogService.save(logEntity);
        }
    }
}
```

**关键注释：**

*   `// 通过反射调用目标对象，在目标对象中封装智能调度核心逻辑`
*   `// 获取目标对象`
*   `// 获取目标方法`
*   `// 通过反射调用目标对象的方法`

---

### 4) 关键场景与演示描述

1.  **场景一：环境与代码概览**
    *   **描述**：视频开始时，画面显示了 IntelliJ IDEA 的项目结构和 `ScheduleJob.java` 文件。讲师首先展示了 `executeInternal` 方法的完整框架，包括日志记录、任务开始时间、核心执行逻辑和最终的数据库保存。

2.  **场景二：创建日志实体**
    *   **描述**：讲师将光标移动到代码中 `ScheduleJobLogEntity logEntity = new ScheduleJobLogEntity();` 这一行，强调在任务执行前需要创建一个日志对象来记录所有相关信息。

3.  **场景三：获取目标对象**
    *   **描述**：讲师将光标移动到 `Object target = SpringContextUtils.getBean(scheduleJob.getBeanName());` 这一行。他通过鼠标悬停或点击，展示了 `SpringContextUtils.getBean()` 方法的调用，该方法用于从 Spring 容器中获取一个由 `scheduleJob.getBeanName()` 指定的 Bean 实例。

4.  **场景四：获取目标方法**
    *   **描述**：讲师将光标移动到 `Method method = target.getClass().getDeclaredMethod("run", String.class, String.class, String.class, String.class);` 这一行。他通过鼠标悬停，展示了 `Class.getDeclaredMethod()` 方法的调用，该方法用于获取目标对象 `target` 的 `run` 方法，并传入其参数类型。

5.  **场景五：执行目标方法**
    *   **描述**：讲师将光标移动到 `method.invoke(target, ...);` 这一行。他通过鼠标悬停，展示了 `Method.invoke()` 方法的调用，该方法会动态执行目标对象的 `run` 方法，并传入业务参数和日志对象。

6.  **场景六：异常处理与日志记录**
    *   **描述**：讲师将光标移动到 `try` 和 `catch` 块。他强调在 `try` 块中，如果执行成功，会将日志状态设置为 `1`；在 `catch` 块中，如果发生异常，会将日志状态设置为 `0` 并记录异常堆栈。

7.  **场景七：计算耗时与保存日志**
    *   **描述**：讲师将光标移动到 `finally` 块。他展示了如何计算任务耗时 `int times = (int) (System.currentTimeMillis() - startTime);`，并将耗时设置到日志对象中。最后，他通过 `SpringContextUtils.getBean(IScheduleJobLogService.class)` 获取日志服务，并调用 `save(logEntity)` 方法将日志持久化到数据库。
