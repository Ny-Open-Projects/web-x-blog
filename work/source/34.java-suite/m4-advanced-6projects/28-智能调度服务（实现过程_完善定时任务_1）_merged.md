# 28-智能调度服务（实现过程_完善定时任务_1） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们这个智能调度符

刚才我们是测试了一下

就是我们这个初始化定时任务

这个工作是能够正常完成的

并且我们是分了两种情况

一种是我们新增出来的定时任务

还有一种就是已有的定时任务

那么如果是新增的话

也就是说我们这些定时任务还没有初始化的时候

它就会执行这个EF这个分支

然后动态的把这个定时任务给我们创建出来

那么如果说它已经存在了的话

我们是不是就执行这个update

就更新一下它就可以了

那么我们是如何判断当前这个定时任务是否已经动态创建了呢

是不是通过我们这个触发器对象

那么如果已经创建过的话

咱们是不是就可以获得相应的这个触发器对象

也就是它不为空

因为每个触发器对象它都有唯一的标识

而我们这个地方

是不是使用的是我们定时任务那个表

就是这个表它的主见值

咱们scatular job

这个表它的主见值来作为唯一标识

所以说它们肯定都是唯一的

这个我们已经测试通过了

没有问题

那接下来我们来看下一个小节

就是翻回头来

我们需要来完善咱们这个定时任务类

注意我们这个地方定时任务类指的就是这个scatular job

这个定时任务类指的就是这个scatular job

就是这个类

这是我们当时只是写了一个半成品

对吧

主要就是测试了一下

在我们控制台能够看到这个语句的输出

这就说明咱们这个定时任务能够正常触发

对吧

那现在我们需要翻回头来看一下

我们当前这个类应该如何去完善

那么首先

我们在写代码之前

需要来明确一下

在我们这个类里面主要做的是什么事情

那么前面咱们其实也说了

对吧

这个定时任务类主要是进行智能调度

其实除了要进行智能调度之外

我们前面在讲这个数据模型的时候

其实也提到了

就是我们每一个定时任务执行的时候

都需要去把这个一条记录

就是这个日志信息

把它记录到这个定时任务

这个日志表里面去

也就是说每一个任务出发的时候

对吧

那么对应的都有一条日志数据

那也就是说在我们当前这个类里边

除了要进行什么呢

这个真正的智能调度相关的这些操作

还要记录什么呢

记录我们的日志信息

也就是说我们在这需要记录日志信息

这个指的是定时任务

定时任务相关相关的这个日志信息

需要把它记录下来

所以说呢

我们这个地方呢

需要有这么两个事来做

然后呢

我们需要再来说一下什么呢

就是真正进行智能调度

这个业务逻辑其实非常复杂

前面我们在也说了

对吧

咱们讲了这个业务说明

还有相应的这个数据模型

也就是说这块呢

相对来说是非常复杂的

那也就是说我们这个地方呢

并不打算直接将我们这个智能调度

这些业务逻辑代码

直接写在当前这个类里面

而是进行一个什么呢

代码的抽取

然后在我们当前这个类里面

直接调那个代码就可以了

什么意思呢

就是在这个地方呢

我们会通过反射来调用我们真正的那个目标对象

然后在这个目标对象中来封装什么呢

来封装我们这个智能调度核心逻辑

相当于我们这个定时任务类呢

他只是调一下他就可以了

那么真正核心的逻辑代码呢

我们就不写到当前这个类里面了

因为什么呢

因为我们这里面是不是还要记录日志信息

如果说所有的代码都写在这个类里面

更准确的说

如果都写到这个方法里面

那我告诉你啊

我们这个方法它的代码量会有多少啊

如果说所有的这些代码全都写在这个方法里面

那么我们当前这个类啊

它的代码量将会是至少是5000行以上

大家可以想一想这个类

如果是5000行的代码的话

这个代码量是非常非常多的

所以我们在这呢是进行了一个拆分

也就是说在我们当前这个类里边

我们不再直接去写这个代码

而是什么呢

把我们真正的这个智能调度的逻辑给他抽取到另外一个类里面

然后在我们当前这个类里面呢

通过反射来调它就可以了

这也就更好的能解释什么呢

大家来看一下在咱们这个实体类里面

你看是不是有一个叫做bin name

Springbin的名称对吧

可能原先的我们在解释这块的时候呢

有些同学可能并不是很理解

他可能并不知道我们为什么要设计这么一个属性对吧

但是对应的这个表里面也有这么一个字段bin name

那这个地方呢其实指的就是什么呢

我们通过反射来调那个目标对象

那个目标对象的名字就是这个bin name

你比如说我们这个表里面你看

它这个地方有个bin name对吧

然后叫做dispatch task

这其实后边呢我们就需要来创建这么一个类

然后实体化之后呢

这个bin的name

就是这个名字

所以说呢

我们到时候呢

调的就是这个bin

然后呢

这里面代码量其实还是挺多的

即使抽取完之后呢

我们当前这个类里面代码量也是比较多的

所以我们分步骤来完成

首先呢

我们先来看啊

咱先不说怎么通过反射来调它

先把这个什么日志记录

这个呢比较简单对吧

先把这个简单的东西呢

给它搞定啊

然后我们分多次啊

逐渐把这个代码给它完善出来

因为这块呢

设计的代码量是非常非常庞大的

那么我们不可能一次性的把所有的代码都写出来

所以我们只能是拆解对吧

拆分

然后一点一点逐渐完善

然后呢

这个类里边呢

我们可以先来声明一个什么呢

logger方便我们在控制台来记录一些日志

logger

然后呢

我们直接通过logger factory

来getlogger

然后呢

这个直接get class就可以了

然后呢

得到一个记录器对象对吧

通过它呢

可以

来在我们这个控制台呢

来输出一些日志信息

方便我们调试

好

然后呢

这个地方呢

我们需要来记录日志信息

刚才也看了

具体就是记录到这个表里吧

对吧

这个定时任务日志表

好

那么对应的这个实体类呢

咱们其实已经导进来了

再来简单看一下

就是这个

就是这个schedule job entity

job log entity

对吧

所以说呢

我们要记录日志的话呢

首先需要先把它干什么呢

创建出来

对吧

所以要记录它的话呢

我们可以先来封装一个什么呢

封装我们这个日志对象

就是这个对象

咱们就叫log吧

简单一点

log entity

new一个schedule job log entity

然后呢

我们需要来设置它的一系列的属性

首先呢

我们可以来设置一下它的ID

set id

这个ID的话呢

我们可以使用一个ID utils

有一个工具类

这个ID的话呢

咱们呢

其实已经导入了

就是这个工具类

你看有个ID utils

对吧

然后呢

通过这个工具类呢

帮我们来get

生成一个ID

好

这个是ID

然后还要设置什么呢

log entity.set

咱们来看一下

还有一个job ID

注意这个job ID非常重要

也就是说

当前我们这个日志

它记录的是什么呢

是哪一个任务出发

哪个任务

对吧

job ID

这个job ID怎么获得呢

其实从我们

从我们上面

这个实体

其实就是对应的是

它的ID

.get ID

这样就关联到一块了

对吧

也就是它记录的

它记录的

其实这个地方

这个job ID

记录的是我们

这个照物表

它的主件值

是这么一个关系

也就是这个地方

记录的是

这个表的

主件值

好

然后呢

我们继续来看

还有什么

属性需要设置呢

比如说这个

bin name

对吧

注意这个bin name

怎么设置呢

它其实也是来自于

我们这个实体

因为这里边呢

我们是不是设置了

这个bin name

而这个bin name的话

就是我们对应的

我们这个字段

bin name

然后继续

看看还有什么

其他的属性呢

set

这个parameters

这个parameters呢

也是从这个实体来获得

也是从这个实体来获得

get parameters

咱们看这个表里面的字段

其实就是这个字段的值

好

然后再来

logentity.set

来一个是这个吧

create data

这就是创建时间

对吧

咱们直接

用一个data

当前系统时间

就可以了

好

然后呢

还有什么其他的属性呢

咱们可以来看一下

id设置了

这个设置了

这个设置了

然后这个也设置了

注意这个状态

这个状态呢

指的是我们当前

这一次这个定时任务执行

是成功还是失败的呢

对吧

那么我们在这个地方呢

你并不知道它成功失败

所以我们可以写一个什么呢

try catch对吧

如果它进了catch呢

肯定就是这个失败了

如果不进catch呢

那就是成功了

所以我们在这个地方呢

可以先来加一个try catch

指的就是我们这个定时任务

是成功还是失败的吧

所以一会儿呢

我们在这儿就需要通过反射来调

对吧

如果调成功了

那肯定就是说明我们这个定时任务执行成功

所以我先把这个代码结构呢

我们先给它写出来

然后呢

还需要有一个finally

好

是这样的

那么如果是在try里边

对吧

那么我们可以这个地方呢

来设置什么呢

设置它这个状态啊

set status

set status是一

一代表的是成功

代表的是成功

那么如果进catch呢

那说明执行失败了

对吧

这个时候呢

我就set status 0

0是不是代表的是失败

对吧

好

咱们可以来看一下

你看这个是不是0代表失败

然后如果是失败的话呢

你看我们这里边呢

是不是还有一个什么呢

还有一个这个失败的信息

对吧

失败的信息

所以如果是进catch的话呢

我们需要再来设置一下什么呢

设置一下set error

就是执行失败的信息

然后这个信息呢

咱们直接从这个异常这儿来获得就可以了

那么我们直接调用一个工具类

exception

exception

有个工具类

然后呢

get error

然后呢

这个其实就是什么呢

把我们这个异常信息呢

给我们返回一下

返回成字符串类型

好

直接调用这个工具类就可以了

这都是关于异常信息的一些封装

好

然后呢

还有一个

还有一个比较关键的

就是什么呢

你看这里边属性

还有一个叫做

times

这个times是啥呢

就是耗时

说白了就是我们当前这个定时任务

它有一个定时任务

它用了多长时间执行完

对吧

那这个的话我们肯定需要去计算

对吧

怎么算呢

首先呢

你得有一个起始时间

你看在我们try的这个地方

一会儿我们是不是就要去调它的这个

通过反射来调真正的这个核心逻辑

对吧

那么在调之前呢

我们可以来记录一个系统的当前时间

system.currentTimeMillions

好

这个呢

咱们就叫startTime吧

startTime

好

然后呢

在这个final time的时候呢

在这个final time的时候呢

在这个final time的时候呢

在这个final time的时候呢

在这个final time的时候呢

在这个final time的时候呢

在这个地方呢

是不是表示它已经执行完了

对吧

它已经执行完了

所以我们在这个地方呢

再用系统时间减去这个startTime

是不是它的差值就是它的耗时

对吧

所以我们这个地方呢

就可以怎么做呢

就可以通过我们这个

system.currentTimeMillions

然后减去什么呢

减去咱们这个startTime

这个呢

是不是就是我们这个耗时

好

这个地方呢

需要来调整一下

在这儿呢

来计算一下

对吧

来计算一下

times

但是这个需要强转一下

因为啥呢

因为它这个是浪形的

对吧

它是浪形的

而我们这个times呢

要的是这个int类型

好

你看我在这儿呢

把这个差值一算

这就是当前时间减去开始时间

开始时间是在前面这个地方

对吧

获得了

然后呢

它们一差值

算出来的就是耗时

然后呢

我们给这个logentity.setTimes

好

然后呢

把这个times传进去

对吧

这就是我们定时任务的耗时

好

设置好之后呢

咱们在这个地方呢

是不是就需要把我们这个数据给它保存了

把这个logentity对象给它保存一下就可以了

这个其实还是比较简单的

那么我们需要在这儿呢

来获得一个service

来获得一个service

注意我们当前这个类呢

并没有交给Spring容器去管理

所以你在这儿呢

就不能通过AutoVar

来注入了

那怎么办呢

我们可以使用咱们一个工具类啊

使用咱们这个Spring容器

这个工具类

叫SpringContextUtils

对吧

这个工具类

然后呢

我们可以直接getbin

来获得一个bin对象

来获得一个bin对象

那么获得哪个bin对象呢

咱们在这个地方呢

是不是需要一个service

对吧

需要一个service

那么这个service呢

是不是应该就是用来操作咱们那个日志表的

对吧

嗯

对吧

对吧

对吧

对吧

对吧

对吧

对吧

对吧

关于这块的代码呢

我就不再写了啊

咱们直接从讲义上啊

嗯

在这个地方

把这个service呢

拷过来就可以了

你看这叫做

iSchedulerJobLogService

对吧

继承我们这个MyBusPlus

给我们提供的这个iService

好

然后再提供一个实现类就可以了

好

咱们在这儿呢

是不是需要一个service包

对吧

你看现在我们还没有service包

这个就比较简单了啊

service

好

然后呢

这个接口的话呢

就叫这个名字

好

这是interface

然后这个里边的代码呢

我们就直接复制过来了

然后你会看到啊

它这里边呢

除了继承它之外呢

是不是又扩展了两个方法

一个是配置

分页的方法

对吧

还有一个是get

根据ID查询的方法

好

这个呢

其实咱们当前没有用到啊

后边会用到

所以我们就一块把它抄过来了

好

当前咱们其实这两个方法

即使没有也没有关系

因为

当前我们

这个地方呢

并没有使用到它这个两个方法

因为后边会用到

所以呢

一块把它抄过来就可以了

然后呢

我们需要来提供一个实现类

对吧

这个实现类呢

咱们再给它创建一个impl

这么一层包

在这里边来创建

这个实现类

那么对于这些类呢

我们就不再手敲了

直接拿过来

然后呢

整个这块复制过来

复制一下

然后呢

整个这块替换一下

好

这里边这就是get方法对吧

然后呢

上面这块呢

就是咱们这个分页的方法

好

OK

那这个service呢

就已经搞定了

好

并且呢

我们是不是也加了这个注解

对吧

被Spring容器管理了

那么管理起来之后呢

咱们这个地方呢

getbin就可以直接根据什么呢

我们这个接口类型啊

就是这个

接口类型

把咱们这个service对象是不是来获得到

先把它导入一下

这个地方呢

它是

导不进来

你看它这个提示呢

有点问题

先不用管它

getbin

service

然后呢

它这儿

这个地方呢

忘了加一个什么呢

class对吧

好

这样

那这样的话呢

我们是不是从Spring容器里边呢

就把这个bin对象给它get出来了

get出来之后呢

直接来保存一下就可以了

对吧

这里边是不是有个save方法

然后呢

把我们这个什么呢

log entity对象呢

来传进去

log entity对象

传进去

这样就保存到数据库了

好

所以你看我们

这块写的呢

是在咱们这个定时任务执行的时候

触发的时候呢

会记录一条日志信息

对吧

所以我们这块呢

比较简单

就是把需要的这个日志对象

给它封装一下

然后呢

在finally里边呢

把这个数据呢

保存一下

把日志信息保存到数据库

就可以了

一会儿呢

我们就需要重点写try这块

也就是什么呢

通过反射

调用我们真正的那个目标对象

对吧

然后呢

在那个对象里面

来完成了这个日志信息

我们就能用什么呢

真正的这个核心逻辑

只能调度的核心逻辑

好

那么这块这个代码呢

我们先完善到这个程度

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面截图，对技术课程内容进行的结构化中文输出。

---

### 1) 视频摘要

本视频片段是关于“品达物流TMS项目”中“智能调度服务”模块的开发教学。讲师正在讲解如何完善一个基于 Quartz 的定时任务类 `ScheduleJob`。核心内容包括：
- **任务背景**：在完成定时任务的初始化和触发后，需要完善任务执行过程中的日志记录和状态管理。
- **核心逻辑**：通过反射机制，将智能调度的核心逻辑封装到目标对象中。
- **技术实现**：在 `ScheduleJob` 类的 `executeInternal` 方法中，创建 `ScheduleJobLogEntity` 对象，记录任务的 ID、名称、参数、开始时间、状态和耗时，并通过 `SpringContextUtils` 获取目标对象进行后续处理。
- **代码结构**：演示了 `ScheduleJob` 类、`ScheduleJobLogEntity` 实体类、以及 `IScheduleJobLogService` 服务接口和其实现类 `ScheduleJobLogServiceImpl` 的代码编写。

---

### 2) 按时间顺序的章节（带时间点）

由于截图中未提供具体的时间戳，以下章节结构是根据画面内容推断的逻辑顺序：

- **3.3.4 完善定时任务** (0:00 - 0:30)
  - 讲师回顾了前文内容，即定时任务已能实现初始化和根据 Cron 表达式触发。
  - 引入本节目标：完善定时任务类 `ScheduleJob`，使其在执行时能记录日志和状态。

- **3.3.4.1 任务执行核心逻辑** (0:30 - 1:00)
  - 讲师在 `ScheduleJob.java` 文件中，定位到 `executeInternal` 方法。
  - 展示了如何创建 `ScheduleJobLogEntity` 对象，并设置其属性（如 ID、名称、参数、创建时间）。
  - 通过反射调用目标对象，将智能调度核心逻辑封装进去。

- **3.3.4.2 异常处理与状态记录** (1:00 - 1:30)
  - 讲师在 `try-catch-finally` 块中演示了如何记录任务状态。
  - `try` 块中，如果任务成功，设置状态为 1；如果失败，设置状态为 0 并记录异常堆栈。
  - `finally` 块中，计算任务耗时，并设置到 `logEntity` 对象中。

- **3.3.4.3 服务层实现** (1:30 - 2:00)
  - 讲师切换到 `ScheduleJobLogServiceImpl.java` 文件。
  - 展示了如何实现 `IScheduleJobLogService` 接口中的 `page` 和 `get` 方法，用于处理日志数据的分页和查询。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容
- **文档标题**：`TMS项目实战_智能调度.md - Typora`
- **章节标题**：`3.3.4 完善定时任务`
- **文档结构**：
  - `品达物流TMS项目`
    - `第8章 智能调度服务 (pd-dispatch)`
      - `1. 定时任务组件Quartz`
        - `2.1 数据模型`
        - `2.2 环境搭建`
        - `2.3 实现定时任务`
      - `3. 智能调度服务`
        - `3.1 业务说明`
        - `3.2 数据模型`
        - `3.3 实现过程`
          - `3.3.1 基础环境`
          - `3.3.2 编写定时任务`
          - `3.3.3 初始化定时任务`
          - `3.3.4 完善定时任务` ← 当前章节
          - `3.3.5 编写智能调度组件`

#### 代码关键内容

**1. `ScheduleJob.java` (定时任务核心类)**

```java
package com.itehima.pinda.execute;

import com.itehima.pinda.common.utils.SpringContextUtils;
import com.itehima.pinda.entity.ScheduleJobEntity;
import com.itehima.pinda.entity.ScheduleJobLogEntity;
import com.itehima.pinda.service.IScheduleJobLogService;
import com.itehima.pinda.utils.ExceptionUtils;
import com.itehima.pinda.utils.IdUtils;
import com.itehima.pinda.utils.ScheduleUtils;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.quartz.QuartzJobBean;
import java.lang.reflect.Method;
import java.util.Date;

/**
 * 定时任务
 */
public class ScheduleJob extends QuartzJobBean {

    private Logger logger = LoggerFactory.getLogger(getClass());

    @Override
    protected void executeInternal(JobExecutionContext context) throws JobExecutionException {
        ScheduleJobEntity scheduleJob = (ScheduleJobEntity) context.getJobDetail().getJobDataMap().get("scheduleJob");
        System.out.println(new Date());

        // 记录定时任务相关信息
        ScheduleJobLogEntity logEntity = new ScheduleJobLogEntity();
        logEntity.setJobId(scheduleJob.getJobId());
        logEntity.setBeanName(scheduleJob.getBeanName());
        logEntity.setParams(scheduleJob.getParams());
        logEntity.setCreateDate(new Date());

        try {
            // 通过反射调用目标对象，在目标对象中封装智能调度核心逻辑
            logEntity.setStatus(1); // 成功
        } catch (Exception ex) {
            logEntity.setStatus(0); // 失败
            logEntity.setError(ExceptionUtils.getStackTrace(ex));
        } finally {
            long startTime = System.currentTimeMillis();
            int times = (int) (System.currentTimeMillis() - startTime);
            logEntity.setTimes(times); // 耗时
        }
    }
}
```

**2. `ScheduleJobLogEntity.java` (日志实体类)**

```java
@Table(name = "schedule_job_log")
public class ScheduleJobLogEntity implements Serializable {

    private static final long serialVersionUID = 1L;

    @TableId(value = "id", type = IdType.INPUT)
    private String id;

    private String jobId;
    private String beanName;
    private String params;
    private Date createDate;
    private Integer status;
    private String error;
    private Integer times;
}
```

**3. `IScheduleJobLogService.java` (服务接口)**

```java
package com.itehima.pinda.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.itehima.pinda.DTO.ScheduleJobLogDTO;
import com.itehima.pinda.entity.ScheduleJobLogEntity;

import java.util.Map;

/**
 * 定时任务日志
 */
public interface IScheduleJobLogService extends IService<ScheduleJobLogEntity> {
    IPage<ScheduleJobLogEntity> page(Map<String, Object> params);
    ScheduleJobLogDTO get(Long id);
}
```

**4. `ScheduleJobLogServiceImpl.java` (服务实现类)**

```java
@Service
public class ScheduleJobLogServiceImpl extends ServiceImpl<ScheduleJobLogMapper, ScheduleJobLogEntity> implements IScheduleJobLogService {

    @Override
    public IPage<ScheduleJobLogEntity> page(Map<String, Object> params) {
        // 实现分页查询逻辑
    }

    @Override
    public ScheduleJobLogDTO get(Long id) {
        // 实现根据ID查询逻辑
    }
}
```

---

### 4) 关键场景与演示描述

- **场景一：任务执行日志记录**
  - 讲师在 `ScheduleJob.java` 中，演示了如何在 `executeInternal` 方法中创建 `ScheduleJobLogEntity` 对象。
  - 通过 `set` 方法，依次设置任务 ID、名称、参数、创建时间等属性。
  - 使用 `try-catch-finally` 块来处理任务执行过程中的异常和状态记录。

- **场景二：反射调用与状态管理**
  - 讲师在 `try` 块中，通过 `logEntity.setStatus(1)` 记录任务成功。
  - 在 `catch` 块中，通过 `logEntity.setStatus(0)` 记录任务失败，并调用 `ExceptionUtils.getStackTrace(ex)` 获取异常堆栈信息。
  - 在 `finally` 块中，计算任务耗时 `System.currentTimeMillis() - startTime`，并设置到 `logEntity.setTimes(times)`。

- **场景三：服务层实现**
  - 讲师切换到 `ScheduleJobLogServiceImpl.java` 文件。
  - 展示了如何实现 `IScheduleJobLogService` 接口中的 `page` 和 `get` 方法。
  - 通过 `ServiceImpl` 类，可以快速实现 MyBatis-Plus 的分页和单条查询功能。

- **场景四：代码调试与提示**
  - 讲师在编写代码时，IDE 提示了 `expected: Identifier expected`，表明代码中存在语法错误。
  - 讲师通过 `Ctrl+Shift+O` 或其他快捷键，自动导入缺失的包或修复语法错误。
  -
