# 画面线理解：15_数据迁移_业务代码编写_热点文章接口1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\15_数据迁移_业务代码编写_热点文章接口1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:57, 01:24, 01:49, 02:50, 03:39, 04:11, 04:31, 04:45, 05:14, 05:43, 06:02, 06:30, 06:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:09:08

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现一个热点文章同步服务，包括定义接口、编写实现类并注入相关依赖。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示接口定义文件，包含热点文章接口的注释和方法签名。
画面2：在 IDE 中右键点击项目，弹出菜单，准备进行重构或分析。
画面3：在 IDE 中打开 `ApHotArticleService.java` 文件，显示接口定义。
画面4：在 IDE 中，光标位于接口定义的 `insert` 方法后，准备编写实现。
画面5：在 IDE 中，光标位于接口定义的 `hotApArticleSync` 方法后，准备编写实现。
画面6：在 IDE 中，光标位于接口定义的 `selectExpireMonth` 方法后，准备编写实现。
画面7：在 IDE 中打开 `ApHotArticleServiceImpl.java` 文件，准备编写实现类。
画面8：在 IDE 中，光标位于实现类的 `@Service` 注解后，准备编写类定义。
画面9：在 IDE 中，光标位于实现类的 `private` 关键字后，准备声明字段。
画面10：在 IDE 中，光标位于实现类的 `private` 关键字后，准备声明字段。
画面11：在 IDE 中，光标位于实现类的 `private` 关键字后，准备声明字段。
画面12：在 IDE 中，光标位于实现类的 `selectList` 方法后，准备编写实现。
画面13：在 IDE 中，光标位于实现类的 `hotApArticleSync` 方法后，准备编写实现。
画面14：在 IDE 中，光标位于实现类的 `insert` 方法后，准备编写实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
}
log.info("同步数据到HBASE失败，articleId: {}, 状态:{}", articleId,
System.currentTimeMillis() - currentTimeMillis);
}
```

画面3：
```java
package com.heima.migration.service;

import com.heima.model.article.po.ApHotArticles;
import java.util.List;

public interface ApHotArticleService {
    List<ApHotArticles> selectList(ApHotArticles apHotArticles);
    void insert(ApHotArticles apHotArticles);
    /*
     * 热度级 HBase 同步
     * @param articleId
     */
    public void hotApArticleSync(Integer articleId);
    /*
     * 查询过期的频道
     * @return
     */
    public List<ApHotArticles> selectExpireMonth();
}
```

画面7：
```java
package com.heima.migration.service.impl;

public class ApHotArticleServiceImpl implements ApHotArticleService {
```

画面8：
```java
@Service
public class ApHotArticleServiceImpl implements ApHotArticleService {
```

画面9：
```java
@Service
@Log4j2
public class ApHotArticleServiceImpl implements ApHotArticleService {
```

画面10：
```java
@Service
@Log4j2
@SuppressWarnings("all")
public class ApHotArticleServiceImpl implements ApHotArticleService {
```

画面11：
```java
@Service
@Log4j2
@SuppressWarnings("all")
public class ApHotArticleServiceImpl implements ApHotArticleService {
    @Autowired
    private ApHotArticlesMapper apHotArticlesMapper;
```

画面12：
```java
@Service
@Log4j2
@SuppressWarnings("all")
public class ApHotArticleServiceImpl implements ApHotArticleService {
    @Autowired
    private ApHotArticlesMapper apHotArticlesMapper;
    @Autowired
    private MongoTemplate mongoTemplate;
    @Autowired
    private HBaseStorageClient hBaseStorageClient;
    @Autowired
    private ArticleQuantityService quantityService;
```

画面13：
```java
@Override
public List<ApHotArticles> selectList(ApHotArticles apHotArticles) {
    return apHotArticlesMapper.selectList(apHotArticles);
}
```

画面14：
```java
@Override
public void insert(ApHotArticles apHotArticles) {
    apHotArticlesMapper.insert(apHotArticles);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
