# 画面线理解：08_数据保存准备_爬虫文章图文附加信息_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day10-黑马头条-爬虫数据保存
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day10-黑马头条-爬虫数据保存\08_数据保存准备_爬虫文章图文附加信息_测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:23, 00:52, 01:23, 01:37, 01:55, 02:24, 02:48, 02:59, 03:23, 03:33, 03:54, 04:17, 04:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:04:32

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写并测试一个用于查询和检查新闻附加信息的 Service 层代码，并通过控制台输出结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了项目结构，选中了 `CrawlerNewsAdditionalServiceImpl.java` 文件。
- 代码内容：`import java.util.ArrayList; import java.util.Date; import java.util.List; @Service @SuppressWarnings("all") public class CrawlerNewsAdditionalServiceImpl implements CrawlerNewsAdditionalService { @Autowired private CNewsAdditionalMapper cNewsAdditionalMapper; @Override public void saveAdditional(CNewsAdditional cNewsAdditional) { cNewsAdditionalMapper.insertSelective(cNewsAdditional); } @Override public List<CNewsAdditional> queryListByHeadDate(Date currentData) { return cNewsAdditionals; } }`

画面 2：
- 展示了测试类 `CrawlerNewsAdditionalServiceTest.java` 的开头部分。
- 代码内容：`package com.heima.crawler.service; import org.junit.runner.RunWith; import org.springframework.boot.test.context.SpringBootTest; import org.springframework.test.context.junit4.SpringRunner; public class CrawlerNewsAdditionalServiceTest { private `

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
- 文档内容：`1.1 需求分析 1.1.1 需求分析 1.1.2 实体类 1.1.3 mapper接口定义 1.1.4 service接口定义 1.1.5 测试 1.2 频道文章附加信息 1.2.1 实体类 1.2.2 mapper接口定义 1.2.3 service接口定义 1.2.4 测试 1.3 频道文章正文解析 1.3.1 需求分析 1.3.2 实体类 1.3.3 mapper接口定义 1.3.4 service接口定义 1.3.5 测试 1.4 频道文章 1.4.1 思路分析 1.4.2 攻略`

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
无

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
