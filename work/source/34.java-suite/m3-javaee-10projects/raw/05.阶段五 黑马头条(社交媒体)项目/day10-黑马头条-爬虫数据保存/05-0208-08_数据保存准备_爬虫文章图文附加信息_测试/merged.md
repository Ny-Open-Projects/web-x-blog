# 08_数据保存准备_爬虫文章图文附加信息_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\08_数据保存准备_爬虫文章图文附加信息_测试【海量资源尽在 666java.com】.mp4
- 时长 4分39秒（音频 279s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去干嘛呢又来去测试一下啊把它呢拷贝一下然后在当前测试内容这儿拟出一个class叫test咱们这样啊咱们可以从之前的中的之前的这个中啊拷一下啊写了有没有什么没有什么技术含量啊然后考完之后呢这时候呢你要去注入谁啊注入当前的calleradditional Service是吧caller newsadditional Service好就是他
[00:31] 然后是读源注入一下咱们也测一个方法,或者两个方法public void test测试哪个呢?
[00:43] 咱们看一下啊没有一个保存,咱们就不测了,咱们就测个查询吧测一个这样的查询,还是测这样的查询测两个吧,一个是currylist,一个是curryur,好吧好,第二个呢,是咱们要去再去测另外一个啊
[01:09] 这个相当于测了好几个是吧C是加一个test然后下面这个也加test啊那加上之后呢这时候你可以调用方法了啊然后是.qrlist它需要有这么一个东西那咱们就直接去new出来一个啊叫clnewsadditional等于new一个clnewsadditional
[01:48] 然后这里边咱们要去传一些参数set什么呢比如说咱们要set一个URL吧好吧就是咱们要去查询某一个URL啊这URL呢咱们就这样啊咱们就去拷贝一个嗯嗯它是一个搜创是吧加上之后呢咱们就可以直接查了啊查完之后它应该返回的是一个列表是吧我们就可以打印一下啊CR News当然嗯连这个东西打印完之后呢这个东西咱们就做完了啊
[02:25] 这么之后咱们就可以在这钻点或者在这打钻点行咱们就可以去看一眼走执行稍等把这个往上拉一拉看一看看看有没有报错看看能不能查出来应该是能够查出来当前7108这一条数据好来了来了之后你可以看一眼这里边是有一条数据你看这个是不是7108没问题吧OK没问题行我就停了
[03:16] 然后下面还有一个就是检查当前的是否存在是吧怎么可以再去测一次啊Q不是CRNEWSMAP是吧COLOR啊COLOR AUDITION NEWS AUDITION SERVICE.2CHECK这个呢咱们也用当前的源吧好吧用它啊简单点它反而是个本是吧我们就去打一下当前这个这个就行什么意思
[03:55] 行那咱们就直接打印啊提八个一遍吧在这这先等一等看一看啊应该返回一个处是吧好稍等嗯看一看啊没有报测就行啊没有报测嗯也到这了是吧你看这是个处是吧没问题啊那行那这个咱们就算是测完了啊那这个介绍呢咱们也写完了下面呢咱们就来去写这个爬虫这个文章图文评论信息表啊好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写并测试一个用于查询和检查新闻附加信息的 Service 层代码，并通过控制台输出结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了项目结构，选中了 `CrawlerNewsAdditionalServiceImpl.java` 文件。
- 代码内容：`import java.util.ArrayList; import java.util.Date; import java.util.List; @Service @SuppressWarnings("all") public class CrawlerNewsAdditionalServiceImpl implements CrawlerNewsAdditionalService { @Autowired private CNewsAdditionalMapper cNewsAdditionalMapper; @Override public void saveAdditional(CNewsAdditional cNewsAdditional) { cNewsAdditionalMapper.insertSelective(cNewsAdditional); } @Override public List<CNewsAdditional> queryListByHeadDate(Date currentData) { return cNewsAdditionals; } }`

画面 2：
- 展示了测试类 `CrawlerNewsAdditionalServiceTest.java` 的开头部分。
- 代码内容：`package com.heima.crawler.Service; import org.junit.runner.RunWith; import org.springframework.boot.test.context.SpringBootTest; import org.springframework.test.context.junit4.SpringRunner; public class CrawlerNewsAdditionalServiceTest { private `

画面 3：
- 展示了测试类中定义的测试方法。
- 代码内容：`public List<CNewsAdditional> queryList(CNewsAdditional cNewsAdditional); // 根据条件查询 @param cNewsAdditional @return public boolean checkExist(String url); // 根据 url 判断是否存在 @param url @return`

画面 4：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { } public void testCheckExist() { } }`

画面 5：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { } public void testCheckExist() { } }`

画面 6：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { CNewsAdditional cNewsAdditional = new CNewsAdditional(); cNewsAdditional.setUrl("https://blog.csdn.net/weixin_43976602/article/details/96971651"); crawlerNewsAdditionalService.queryList(cNewsAdditional); } public void testCheckExist() { } }`

画面 7：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { CNewsAdditional cNewsAdditional = new CNewsAdditional(); cNewsAdditional.setUrl("https://blog.csdn.net/weixin_43976602/article/details/96971651"); List out = crawlerNewsAdditionalService.queryList(cNewsAdditional); System.out.println(out); } public void testCheckExist() { } }`

画面 8：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { CNewsAdditional cNewsAdditional = new CNewsAdditional(); cNewsAdditional.setUrl("https://blog.csdn.net/weixin_43976602/article/details/96971651"); List out = crawlerNewsAdditionalService.queryList(cNewsAdditional); System.out.println(out); } public void testCheckExist() { } }`

画面 9：
- 展示了数据库表 `t_news_additional` 的数据。
- 数据内容：`id news_id url read_count likes comment forward unlikes collection created_time count update`，其中一条记录为 `7108 25111 https://blog.csdn.net/weixin_43976602/article/details/96971651 29 0 (Null) 0 0 0 2019-06-21 20:54:16 1 0`

画面 10：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { CNewsAdditional cNewsAdditional = new CNewsAdditional(); cNewsAdditional.setUrl("https://blog.csdn.net/weixin_43976602/article/details/96971651"); List out = crawlerNewsAdditionalService.queryList(cNewsAdditional); System.out.println(out); } public void testCheckExist() { } }`

画面 11：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { CNewsAdditional cNewsAdditional = new CNewsAdditional(); cNewsAdditional.setUrl("https://blog.csdn.net/weixin_43976602/article/details/96971651"); List out = crawlerNewsAdditionalService.queryList(cNewsAdditional); System.out.println(out); } public void testCheckExist() { } }`

画面 12：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { CNewsAdditional cNewsAdditional = new CNewsAdditional(); cNewsAdditional.setUrl("https://blog.csdn.net/weixin_43976602/article/details/96971651"); List out = crawlerNewsAdditionalService.queryList(cNewsAdditional); System.out.println(out); } public void testCheckExist() { } }`

画面 13：
- 展示了测试类中定义的测试方法，并添加了 `@Autowired` 注解。
- 代码内容：`@SpringBootTest @RunWith(SpringRunner.class) public class CrawlerNewsAdditionalServiceTest { @Autowired private CrawlerNewsAdditionalService crawlerNewsAdditionalService; public void testQueryList() { CNewsAdditional cNewsAdditional = new CNewsAdditional(); cNewsAdditional.setUrl("https://blog.csdn.net/weixin_43976602/article/details/96971651"); List out = crawlerNewsAdditionalService.queryList(cNewsAdditional); System.out.println(out); } public void testCheckExist() { } }`

画面 14：
- 展示了文档 `day11.html` 中的目录结构。
- 文档内容：`1.1 需求分析 1.1.1 需求分析 1.1.2 实体类 1.1.3 Mapper接口定义 1.1.4 Service接口定义 1.1.5 测试 1.2 频道文章附加信息 1.2.1 实体类 1.2.2 Mapper接口定义 1.2.3 Service接口定义 1.2.4 测试 1.3 频道文章正文解析 1.3.1 需求分析 1.3.2 实体类 1.3.3 Mapper接口定义 1.3.4 Service接口定义 1.3.5 测试 1.4 频道文章 1.4.1 思路分析 1.4.2 攻略`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
无

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

