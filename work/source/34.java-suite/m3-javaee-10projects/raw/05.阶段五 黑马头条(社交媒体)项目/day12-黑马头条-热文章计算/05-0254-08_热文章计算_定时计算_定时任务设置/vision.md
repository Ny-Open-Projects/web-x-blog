# 画面线理解：08_热文章计算_定时计算_定时任务设置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\08_热文章计算_定时计算_定时任务设置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 01:09, 01:22, 01:39, 01:49, 03:00, 03:16, 03:32, 04:01, 04:33, 05:01, 05:18, 05:55, 06:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:36:28

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
