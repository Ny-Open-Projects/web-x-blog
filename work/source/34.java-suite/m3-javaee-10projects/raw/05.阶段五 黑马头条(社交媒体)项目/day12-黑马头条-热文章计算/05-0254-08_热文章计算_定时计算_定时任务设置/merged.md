# 08_热文章计算_定时计算_定时任务设置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\08_热文章计算_定时计算_定时任务设置【海量资源尽在 666java.com】.mp4
- 时长 6分41秒（音频 401s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就接着往下看啊然后这块呢还有一个定时任务咱们需要去设置其实咱们今天分析需求的时候已经说了这个呢咱们要去每天凌晨的0.05分就要去执行当前那个什么热数据的计算对吧那首先呢咱们要去集成当前的quad所以说呢咱们先在这先去集成quad的行啊那quad啊我再专门去说一下啊咱们之前说过一次再去说一下啊
[00:28] 这个你要去集成其实你把包给扫一下是吧这包扫一下然后加一个当前的这种NA包scan就就可以了但是这里边有一个问题就是你必须在当前加载它之前先把mysearch回加载因为它是急于库的因为它是一个什么它是一个集群的对吧所以说他们先要去急于当前的mysearch去传数据库才行所以说这个一定要放到前边
[00:55] 好那这是一个啊就这块我已经做完了啊就是你打开当前的引进的config啊然后呢这里边啊就是已经集成了当前的mycircle和当前的quotes好这个东西好那这个加完之后啊那下面呢咱们就可以去干嘛呢去可以创建一个这种正式的任务类你打开当前的这个article这块啊右键在这去创建一个job比如说job的无线夹然后呢呃创建一个类
[01:28] 这类怎么办呢这类叫首先要去基层将你的obstruct的job写两个方法这第一个呢就是前面什么完表达式这个呢就是你真正要执行的业务是吧当然你也还可以去psc这个呢其实是描述是吧描述啊我们可以描述一下每天0005分
[02:04] 执行一次好这个说完之后啊咱们在这在这可以去加一个东西叫compoundcompound是log4接好加上之后啊咱们在这就可以去把这个方法给写下了啊首先第一个要去设置的是当前的一个时间是吧时间是0然后是0-55分吧然后第三个也是0就是0点每天的0点去执行是吧然后是星星
[02:34] 那就可以了这么写呢我们测试不方便啊所以说我们在这先去不要然后呢咱们这个改成星哎改成星这个呢改成二那是每两分钟执行一次好吧你们一会先测试啊先这么用测试的话咱们还得用这个OK那这里边该怎么写呢首先呢你要去注入当前刚才写的一个Service啊叫什么呀啊是叫AP HOT是吧AP HOT Service
[03:05] AP HOT SERVICE好进来之后呢你可以直接去定用方法就可以了这个方法就是整个计算分值的方法然在这也可以要之前套路先去拿到一个时间计算一下他执行的时间点吧好拿到时间之后呢咱们在这打一个log info开始计算分值开始定时定时啊下面呢咱们就可以在这去再打一个log.info
[03:45] 然后是怎么着计算分值完成然后是耗时system.g这样的话咱们就算是设置完了设置完之后你说现在能接测试吗其实按理来说我可以直接去启动当前的项目是不是会自动去执行的没问题但是这块咱们用的是当前的一个分布式的quad所以说你要干嘛
[04:18] 你要去检查一下你这里边有没有这个表有没有这个表很显然你看你打开你的原始的表叫appseq里边有没有article开启了呢找一找是不是没有那没有的话这时候你就要去创建表创建表那这个过程咱们既然没有导入的话咱们这次就去做一下我在下面就去准备了一些表这个表其实就是在上一天的笔记中考过来然后在前面去加了一个前缀叫article
[04:50] 这个是后边固定的然后前面是你的业务这个业务其实就是当前的微服务的名称是吧所以说咱们在这直接拷贝一下拷贝完之后咱们在这去执行一下你在这拷贝一下执行这个表你可以刷新一下刷新一下右键然后刷新你看这里边这个article是不是有了咱们数一数2345
[05:24] 6 7 8 9 10 11上次说过是不是11张表了你说现在结束了吗现在还没有结束因为咱们现在用的是什么呢用的是当前的mycat所以说呢你还要在当前的scammer中打开当前的mycat的配置这有个scammer然后你需要把这几张表给配置一下那配置的方式呢其实你就直接去参考之前的这种调度表就可以了
[05:54] 非常简单怎么办你可以去拷贝一个然后来看这一块是什么是一个一爱是吧你可以拷贝一下前面这个给他替换了就可以了我看看有没有好的方式这样的话就改完了改完之后你保存一下然后你再去启动这时候就能去找到这些表
[06:34] 那行那这个咱们都配完了该配的都配完了下面呢咱们就干嘛呢就来去测试一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 Quartz 定时任务框架，并配置其数据表结构。

2) 按时间顺序列出每张画面的要点：
画面 1:
要点：展示课程标题“2.5 定时任务”，并说明将之前 MySQL 的配置集成到 Quartz 配置中。显示了 InitConfig.java 文件中的 @Configuration、@ComponentScan 和 @EnableScheduling 注解，以及创建 AppHotArticleQuartz 类的说明。

画面 2:
要点：在 IDEA 中展示项目结构，选中 InitConfig.java 文件，显示其包路径为 com.heima.article.config，内容与画面 1 相同。

画面 3:
要点：在 IDEA 中展示项目结构，选中 job 包下的 InitConfig.java 文件，显示其包路径为 com.heima.article.config，内容与画面 1 相同。

画面 4:
要点：在 IDEA 中展示 AppHotArticleQuartz.java 文件内容，该类继承 AbstractJob，包含 triggerCron 方法，返回空数组。

画面 5:
要点：在 IDEA 中展示 AppHotArticleQuartz.java 文件内容，鼠标悬停在 executeInternal 方法上，显示其签名和抛出的异常。

画面 6:
要点：在 IDEA 中展示 AppHotArticleQuartz.java 文件内容，显示了 desTrigger 方法的注释“每天00:05分执行一次”。

画面 7:
要点：在 IDEA 中展示 AppHotArticleQuartz.java 文件内容，显示了 @Autowired 注解注入的 appHotArticleService。

画面 8:
要点：在 IDEA 中展示 AppHotArticleQuartz.java 文件内容，显示了 executeInternal 方法中调用 appHotArticleService.computHotArticle()。

画面 9:
要点：在 IDEA 中展示 AppHotArticleQuartz.java 文件内容，显示了 executeInternal 方法中添加了日志记录，记录开始和结束时间。

画面 10:
要点：在 Navicat for MySQL 中展示数据库表结构，显示了 CRAWLER_QRTZ_SIMPLE_TRIGGERS 表的 DDL 语句。

画面 11:
要点：在 Typora 中展示 Quartz 数据库表结构的 SQL 代码，包含 CRAWLER_QRTZ_SIMPLE_TRIGGERS、ARTICLE_QRTZ_BLOB_TRIGGERS、ARTICLE_QRTZ_CALENDARS、ARTICLE_QRTZ_PAUSED_TRIGGER_GRPS、ARTICLE_QRTZ_TRIGGERS 等表的创建语句。

画面 12:
要点：在 Navicat for MySQL 中展示数据库表结构，显示了 ADMIN_QRTZ_TRIGGERS、ARTICLE_QRTZ_TRIGGERS 等表。

画面 13:
要点：在 Notepad++ 中展示 Quartz 数据库表结构的 XML 配置，包含多个 table 元素，dataNode="DNSQ" type="global"。

画面 14:
要点：在 Navicat for MySQL 中展示数据库表结构，显示了 ARTICLE_QRTZ_BLOB_TRIGGERS 表的 DDL 语句。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
@Configuration
@ComponentScan({"com.heima.common.mysql.core","com.heima.common.common.init","com.heima.common.quartz"})
@EnableScheduling
public class InitConfig {
}
```

画面 2:
```java
package com.heima.article.config;

import ...

@Configuration
@ComponentScan({"com.heima.common.mysql.core","com.heima.common.common.init","com.heima.common.quartz"})
@EnableScheduling
public class InitConfig {
}
```

画面 3:
```java
package com.heima.article.config;

import ...

@Configuration
@ComponentScan({"com.heima.common.mysql.core","com.heima.common.common.init","com.heima.common.quartz"})
@EnableScheduling
public class InitConfig {
}
```

画面 4:
```java
package com.heima.article.job;

import com.heima.common.quartz.AbstractJob;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class AppHotArticleQuartz extends AbstractJob {

    @Override
    public String[] triggerCron() {
        return new String[]{};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {

    }
}
```

画面 5:
```java
package com.heima.article.job;

import com.heima.common.quartz.AbstractJob;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class AppHotArticleQuartz extends AbstractJob {

    @Override
    public String[] triggerCron() {
        return new String[]{};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {

    }
}
```

画面 6:
```java
package com.heima.article.job;

import com.heima.common.quartz.AbstractJob;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class AppHotArticleQuartz extends AbstractJob {

    @Override
    public String[] triggerCron() {
        // return new String[]{"0 0/5 * * * ?"};
        return new String[]{"0 0/5 * * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {

    }

    @Override
    public String desTrigger() {
        return "每天00:05分执行一次";
    }
}
```

画面 7:
```java
package com.heima.article.job;

import com.heima.common.quartz.AbstractJob;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class AppHotArticleQuartz extends AbstractJob {

    @Override
    public String[] triggerCron() {
        // return new String[]{"0 0/5 * * * ?"};
        return new String[]{"0 0/5 * * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {

    }

    @Override
    public String desTrigger() {
        return "每天00:05分执行一次";
    }
}
```

画面 8:
```java
package com.heima.article.job;

import com.heima.common.quartz.AbstractJob;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class AppHotArticleQuartz extends AbstractJob {

    @Override
    public String[] triggerCron() {
        // return new String[]{"0 0/5 * * * ?"};
        return new String[]{"0 0/5 * * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {

    }

    @Override
    public String desTrigger() {
        return "每天00:05分执行一次";
    }
}
```

画面 9:
```java
package com.heima.article.job;

import com.heima.common.quartz.AbstractJob;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class AppHotArticleQuartz extends AbstractJob {

    @Override
    public String[] triggerCron() {
        // return new String[]{"0 0/5 * * * ?"};
        return new String[]{"0 0/5 * * * ?"};
    }

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {

    }

    @Override
    public String desTrigger() {
        return "每天00:05分执行一次";
    }
}
```

画面 10:
```sql
CREATE TABLE CRAWLER_QRTZ_SIMPLE_TRIGGERS (
    SCHED_NAME VARCHAR(120) NOT NULL,
    TRIGGER_NAME VARCHAR(200) NOT NULL,
    TRIGGER_GROUP VARCHAR(200) NOT NULL,
    STR_PROP_1 VARCHAR(512) DEFAULT NULL,
    STR_PROP_2 VARCHAR(512) DEFAULT NULL,
    STR_PROP_3 VARCHAR(512) DEFAULT NULL,
    LONG_PROP_1 BIGINT DEFAULT NULL,
    LONG_PROP_2 BIGINT DEFAULT NULL,
    DECIMAL_PROP_1 NUMERIC(13, 4) DEFAULT NULL,
    DECIMAL_PROP_2 NUMERIC(13, 4) DEFAULT NULL,
    INT_PROP_1 INT DEFAULT NULL,
    INT_PROP_2 INT DEFAULT NULL,
    LONG_PROP_3 BIGINT DEFAULT NULL,
    DECIMAL_PROP_3 NUMERIC(13, 4) DEFAULT NULL,
    INT_PROP_3 INT DEFAULT NULL,
    LONG_PROP_4 BIGINT DEFAULT NULL,
    DECIMAL_PROP_4 NUMERIC(13, 4) DEFAULT NULL,
    INT_PROP_4 INT DEFAULT NULL,
    LONG_PROP_5 BIGINT DEFAULT NULL,
    DECIMAL_PROP_5 NUMERIC(13, 4) DEFAULT NULL,
    INT_PROP_5 INT DEFAULT NULL,
    LONG_PROP_6 BIGINT DEFAULT NULL,
    DECIMAL_PROP_6 NUMERIC(13, 4) DEFAULT NULL,
    INT_PROP_6 INT DEFAULT NULL,
    LONG_PROP_7 BIGINT DEFAULT NULL,
    DECIMAL_PROP_7 NUMERIC(13, 4) DEFAULT NULL,
    INT_PROP_7 INT DEFAULT NULL,
    LONG_PROP_8 BIGINT DEFAULT NULL,
    DECIMAL_PROP_8 NUMERIC(13, 4) DEFAULT NULL,
    INT_PROP_8 INT DEFAULT NULL,
    LONG_PROP_9 BIGINT DEFAULT NULL,
    DECIMAL_PROP_9 NUMERIC(13, 4) DEFAULT NULL,
    INT_PROP_9

