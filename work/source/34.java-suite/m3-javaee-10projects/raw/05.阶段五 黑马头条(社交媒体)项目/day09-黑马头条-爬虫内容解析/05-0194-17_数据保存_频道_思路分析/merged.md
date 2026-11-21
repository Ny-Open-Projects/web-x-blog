# 17_数据保存_频道_思路分析

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\17_数据保存_频道_思路分析【海量资源尽在 666java.com】.mp4
- 时长 4分25秒（音频 266s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们下面就继续往下讲咱们之前就是已经把这个东西就是把咱们前面的整合已经做完了整合其实还没有完全做完是吧只是做了两部分一个是下载一个是解析对吧但是后期的话咱们还要再去新增一些内容但新增内容之后咱们首先得要先做一步就是要一个数据保存的准备
[00:30] 那这个呢咱们最终啊其实爬出爬去完文章之后呢解析解析完之后呢咱们肯定是要存到数据库中对吧所以说呢那这个数据库怎么存呢所以说咱们现在啊目前的话呢首先得先去准备一些这种保存数据库的一些业务啊那比如说啊咱们现在的是有一个频道啊还有一个IP的离持当然这个还不够啊还不够啊还有啥呢还有一些文章的保存是吧那这个今天呢咱们并没有并做不完啊做不完
[01:00] 这时候咱们只是把这两块先做了把这两块先做了咱们首先先来看一下频道频道什么是频道其实咱们之前去保存文章的时候其实也说到过这个问题就是频道这个频道是这样咱们可以打开表这表其实有一个adad里边是有一些希望大家知道的比如说有adchannel这个就是频道当前文章到底是属于哪一个频道当然目前你要是爬取到某一条文章的话
[01:29] 它并不能对应一些频道它有啥呢标签有标签看到了吗那么一个思路是啥呢频道的思路咱们首先是通过当前的文章爬取爬取完之后拿到当前的标签有可能是多个有可能是多个有可能是一个也可能又没有好拿到标签之后首先咱们到咱们的数据库中去查询哪一个是频道的数据库比方说这个
[01:58] 先到这个表中去查看看有没有如果没有怎么办没有就插入没有就新增这是第一个如果一旦查到之后这时候咱们需要去通过当前这个label就是这个标签需要去查到当前对应什么频道那怎么查其实里边有一个叫adchannellabel看到吧它是一个中间表你又可以通过当前的标签
[02:26] 去查询谁查询当前的频道信息OK那做到这这事就算是做完了OK还是比较简单的相对来说比较简单就是说你首先是通过一文章解析之后拿到它的标签有可能是多个去数据库中去查如果说没有就插入一条数据然后最终通过当前这个什么当前这个频道的是标签是吧当前那个文章的标签去查询它的频道
[02:55] 频道ID看有没有好吧行最终咱们这个思路咱们这个频道这这模块咱们就讲那么多刚才我也去说了两个类是吧那两个类再说一下第一个就是两个表第一个表就是当前的label就是标签
[03:12] 然后第二个是缠斗怎么拿到缠斗是通过当前的中间表去获取缠斗当然刚才可能有同学也说了目前的话比如说有一个文章有可能会有多个这种标签多个标签是不是要对应多个这种频道是的没错但是一个文章咱们只会对应一个频道所以说咱们的一个思路处理的思路就是默认默认的是拿取一个比如说是属于mybuddies
[03:42] 那咱们就把它归类到mybattis这个频道下边就可以了那么默认是拿第一个好吧咱们下面也可以看一下这两个实体类其实也比较简单一个是label标签的id name type是吧类型还有个创建时间然后下面还有一个就是当前的这种channel label当前充电表是吧ID你看里边是你可以通过当前的label id拿到谁拿到当前的channel id
[04:10] 还有一个Ord,这个是为了排序咱们现在用不着这两个实体内的大家一定要熟悉一下还有这两个表大家也应该能够知道好吧行那这个思路思路跟这个表咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解一个爬虫项目中数据模型（实体类）、数据库表结构设计及 MyBatis 与 Spring 框架整合所需依赖的配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中 `mappers` 目录，准备编写数据访问层代码。
画面2：在文档中定位到“2.1 实体类”章节，展示 `CrawlerComponent` 类的代码，包含 `pageProcessor`、`pipelineList` 和 `scheduler` 等成员变量。
画面3：继续展示 `CrawlerComponent` 类，重点是 `@PostConstruct` 注解下的 `initProcessingFlow` 方法，其中对 `processFlowList` 进行排序，使用 `ProcessFlow` 的 `getPriority()` 方法比较优先级。
画面4：文档导航到“3.1.5 测试”章节，同时显示“3.2 ip代理池”下的“3.2.1 思路分析”和“3.2.2 实体类”标题，下方展示 `ClipPool` 类的定义。
画面5：文档导航到“3.1.1 思路分析”和“3.1.2 实体类”章节，展示 `AdLabel` 类的定义。
画面6：在 Navicat for MySQL 中查看 `ad_channel` 表的 DDL，展示表结构定义。
画面7：在 CSDN 网站上打开一篇关于“MyBatis和Spring整合”的文章，展示所需依赖包列表。
画面8：在 CSDN 网站上浏览“MyBatis和Spring整合”文章，页面未发生明显变化。
画面9：在 Navicat for MySQL 中查看 `ad_channel_label` 表的 DDL，展示表结构定义。
画面10：文档导航到“3.1.1 思路分析”和“3.1.2 实体类”章节，展示 `AdLabel` 类的定义。
画面11：在 Navicat for MySQL 中查看 `ad_channel_label` 表的 DDL，展示表结构定义。
画面12：在 CSDN 网站上浏览“MyBatis和Spring整合”文章，页面未发生明显变化。
画面13：文档导航到“3.1.3 Mapper接口定义”章节，展示 `AdLabelMapper` 接口的定义。
画面14：文档导航到“3.1.3 Mapper接口定义”章节，展示 `AdLabelMapper` 接口的定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
// 爬虫组件
public class CrawlerComponent implements Serializable {
    // 页面处理器
    private PageProcessor pageProcessor;
    // pipelineList 处理
    private List<Pipeline> pipelineList = new ArrayList<Pipeline>();
    // 主要组件
    private Scheduler scheduler;
    // 数据组件
}
```

画面3：
```java
private CrawlerNewsAdditionalService crawlerNewsAdditionalService;
// spring 启动时会执行此方法
* 对实现ProcessFlow接口的类按照getPriority()接口对实现类进行从小到大的排序
* 实现简单的优先级处理模式，一个模块处理一件事然后将后续任务递到下一个模块进行处理
*/
@PostConstruct
private void initProcessingFlow() {
    if (null != processFlowList && processFlowList.isEmpty()) {
        processFlowList.sort(new Comparator<ProcessFlow>() {
            public int compare(ProcessFlow p1, ProcessFlow p2) {
                if (p1.getPriority() > p2.getPriority()) {
                    return 1;
                } else if (p1.getPriority() < p2.getPriority()) {
                    return -1;
                }
                return 0;
            }
        });
    }
}
```

画面4：
```java
3.1.5 测试
3.2 ip代理池
3.2.1 思路分析
3.2.2 实体类
ClipPool类
com.heima.model.crawler.pojos ClipPool
@Data
public class ClipPool {
```

画面5：
```java
3.1.1 思路分析
    • 从文章解析中获取具体的标签labels，查询数据库如果没有则需要新建
    • 根据文章的labels去查找对应的质量信息
3.1.2 实体类
AdLabel类
com.heima.model.admin.pojos.AdLabel
@Data
public class AdLabel {
    private Integer id;
    private String name;
    private Boolean type;
    private Date createdTime;
}
```

画面6：
```sql
CREATE TABLE `ad_channel` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '频道名称',
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '频道描述',
  `status` tinyint(1) unsigned DEFAULT NULL COMMENT '是否默认频道',
  `code` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '频道编码',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='频道信息表';
```

画面7：
```text
1、MyBatis和Spring框架整合
1.1、导入所需的包
我所需要的是：
Cp00 0.5.2.jar
com.springsource.javax.servlet.jsp.jstl-1.2.0.jar
com.springsource.org.apache.commons.lang-2.6.0.jar
com.springsource.org.apache.commons.logging-1.2.0.jar
com.springsource.org.apache.commons.lang-2.6.0.jar
mybatis-spring-1.2.1.jar
mybatis-3.4.6.jar
mysql-connector-java-5.1.37.jar
```

画面9：
```sql
CREATE TABLE `ad_channel_label` (
  `Channel_Id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `Label_Id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '标签ID',
  `ord` int(5) unsigned NOT NULL DEFAULT '0' COMMENT '排序',
  PRIMARY KEY (`Channel_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=1111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='频道标签表';
```

画面13：
```java
AdLabelMapper
com.heima.model.mappers.admin.AdLabelMapper
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“2.1 实体类”，子标题“CrawlerComponent类”，下方展示代码。
画面3：PPT标题为“2.1 实体类”，子标题“ProcessingFlowManager”，下方展示代码。
画面4：PPT标题为“3.1.5 测试”，下方有“3.2 ip代理池”和“3.2.2 实体类”标题。
画面5：PPT标题为“3.1.1 思路分析”，下方有“3.1.2 实体类”标题。
画面6：无PPT标题，展示SQL语句。
画面7：PPT标题为“1、MyBatis和Spring框架整合”，子标题“1.1、导入所需的包”，下方列出所需依赖包。
画面9：无PPT标题，展示SQL语句。
画面10：PPT标题为“3.1.1 思路分析”，下方有“3.1.2 实体类”标题。
画面11：无PPT标题，展示SQL语句。
画面12：PPT标题为“1、MyBatis和Spring框架整合”，子标题“1.1、导入所需的包”，下方列出所需依赖包。
画面13：PPT标题为“3.1.3 Mapper接口定义”，下方展示 `AdLabelMapper` 接口定义。
画面14：PPT标题为“3.1.3 Mapper接口定义”，下方展示 `AdLabelMapper` 接口定义。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）

