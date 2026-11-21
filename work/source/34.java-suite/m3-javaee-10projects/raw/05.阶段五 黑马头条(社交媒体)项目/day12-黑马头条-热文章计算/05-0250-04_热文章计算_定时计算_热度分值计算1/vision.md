# 画面线理解：04_热文章计算_定时计算_热度分值计算1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day12-黑马头条-热文章计算
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day12-黑马头条-热文章计算\04_热文章计算_定时计算_热度分值计算1【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:18, 01:18, 03:06, 04:56, 06:05, 07:54, 08:58, 09:36, 10:08, 10:44, 11:43, 12:59, 13:37, 14:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 15:33:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 Service 层调用 Mapper 层，实现对文章热度的计算与持久化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了项目结构，重点在 `src/main/resources/mappers/` 目录下的 `ApBehaviorMapper.xml` 文件。
- 该 XML 文件中包含两个 `<select>` 标签，用于根据用户 ID 或设备 ID 查询行为记录。
- 第一个 `<if>` 标签条件为 `test="userId=null and equipmentId=null"`，用于查询所有记录。
- 第二个 `<select>` 标签用于查询所有记录。
- XML 文件内容：
  ```xml
  <!--根据id从sp_behavior_entry表中查询-->
  <select id="selectById" resultType="com.heima.model.ApBehaviorEntry">
      select * from sp_behavior_entry a where a.entry_id=#{userId} and type=1 limit 1
  </select>

  <!--查询所有-->
  <select id="selectAllEntry" resultMap="BaseResultMap">
      select * from sp_behavior_entry
  </select>
  ```

画面 2：
- 展示了 `ApArticleServiceImpl.java` 文件的开头部分，包含包声明和类定义。
- 代码结构为 `public class ApArticleServiceImpl implements ApArticleService {`。

画面 3：
- 展示了 `ApArticleServiceImpl.java` 文件中 `computeHotArticle` 方法的实现。
- 该方法调用 `apArticleMapper.loadArticleForHot(lastDay)` 获取文章列表。
- 代码：
  ```java
  @Autowired
  private ApArticleMapper apArticleMapper;

  @Override
  public void computeHotArticle() {
      //查询一天内新发布的文章
      List<Article> articleList = apArticleMapper.loadArticleForHot(lastDay);
      //计算文章热度（阅读量、评论、点赞、收藏）
      //存在文章中的频道
      //给每一个用户保存一份热点文章
      //存在文章中的图片（暂时不做）
  }
  ```

画面 4：
- 展示了 `computeHotArticle` 方法的完整实现。
- 代码：
  ```java
  List<Article> articleList = apArticleMapper.loadArticleForHot(lastDay);
  List<ApHotArticles> hotArticlesList = computeHotArticle(articleList);
  //存在文章中的频道
  //给每一个用户保存一份热点文章
  //存在文章中的图片（暂时不做）
  ```

画面 5：
- 展示了 `computeHotArticle` 方法的完整实现。
- 代码：
  ```java
  public List<ApHotArticles> computeHotArticle(List<Article> aparticles) {
      return null;
  }
  ```

画面 6：
- 展示了 `computeHotArticle` 方法的完整实现。
- 代码：
  ```java
  public List<ApHotArticles> computeHotArticle(List<Article> aparticles) {
      List<ApHotArticles> hotArticlesList = new ArrayList<>();
      ApHotArticles hot = null;
      for (Article aparticle : aparticles) {
          hot = initHotBaseArticle(aparticle);
      }
      return hotArticlesList;
  }
  ```

画面 7：
- 展示了 `initHotBaseArticle` 方法的实现。
- 代码：
  ```java
  private ApHotArticles initHotBaseArticle(Article aparticle) {
      ApHotArticles hot = new ApHotArticles();
      hot.setEntryId(0);
      hot.setTagId(aparticle.getChannelId());
      hot.setTagName(aparticle.getChannelName());
      hot.setScore(0);
      hot.setArticleId(aparticle.getId());
      hot.setProvinceId(aparticle.getProvinceId());
      return hot;
  }
  ```

画面 8：
- 展示了 `initHotBaseArticle` 方法的实现。
- 代码：
  ```java
  private ApHotArticles initHotBaseArticle(Article aparticle) {
      ApHotArticles hot = new ApHotArticles();
      hot.setEntryId(0);
      hot.setTagId(aparticle.getChannelId());
      hot.setTagName(aparticle.getChannelName());
      hot.setScore(0);
      hot.setArticleId(aparticle.getId());
      hot.setProvinceId(aparticle.getProvinceId());
      hot.setCityId(aparticle.getCityId());
      return hot;
  }
  ```

画面 9：
- 展示了 `initHotBaseArticle` 方法的实现。
- 代码：
  ```java
  private ApHotArticles initHotBaseArticle(Article aparticle) {
      ApHotArticles hot = new ApHotArticles();
      hot.setEntryId(0);
      hot.setTagId(aparticle.getChannelId());
      hot.setTagName(aparticle.getChannelName());
      hot.setScore(0);
      hot.setArticleId(aparticle.getId());
      hot.setProvinceId(aparticle.getProvinceId());
      hot.setCityId(aparticle.getCityId());
      hot.setCollection(aparticle.getCollection());
      return hot;
  }
  ```

画面 10：
- 展示了 `initHotBaseArticle` 方法的实现。
- 代码：
  ```java
  private ApHotArticles initHotBaseArticle(Article aparticle) {
      ApHotArticles hot = new ApHotArticles();
      hot.setEntryId(0);
      hot.setTagId(aparticle.getChannelId());
      hot.setTagName(aparticle.getChannelName());
      hot.setScore(0);
      hot.setArticleId(aparticle.getId());
      hot.setProvinceId(aparticle.getProvinceId());
      hot.setCityId(aparticle.getCityId());
      hot.setCollection(aparticle.getCollection());
      hot.setComment(aparticle.getComment());
      return hot;
  }
  ```

画面 11：
- 展示了 `initHotBaseArticle` 方法的实现。
- 代码：
  ```java
  private ApHotArticles initHotBaseArticle(Article aparticle) {
      ApHotArticles hot = new ApHotArticles();
      hot.setEntryId(0);
      hot.setTagId(aparticle.getChannelId());
      hot.setTagName(aparticle.getChannelName());
      hot.setScore(0);
      hot.setArticleId(aparticle.getId());
      hot.setProvinceId(aparticle.getProvinceId());
      hot.setCityId(aparticle.getCityId());
      hot.setCollection(aparticle.getCollection());
      hot.setComment(aparticle.getComment());
      hot.setLike(aparticle.getLike());
      return hot;
  }
  ```

画面 12：
- 展示了 `initHotBaseArticle` 方法的实现。
- 代码：
  ```java
  private ApHotArticles initHotBaseArticle(Article aparticle) {
      ApHotArticles hot = new ApHotArticles();
      hot.setEntryId(0);
      hot.setTagId(aparticle.getChannelId());
      hot.setTagName(aparticle.getChannelName());
      hot.setScore(0);
      hot.setArticleId(aparticle.getId());
      hot.setProvinceId(aparticle.getProvinceId());
      hot.setCityId(aparticle.getCityId());
      hot.setCollection(aparticle.getCollection());
      hot.setComment(aparticle.getComment());
      hot.setLike(aparticle.getLike());
      hot.setPublishTime(aparticle.getPublishTime());
      return hot;
  }
  ```

画面 13：
- 展示了 `computeScore` 方法的实现。
- 代码：
  ```java
  private Integer computeScore(Article aparticle) {
      Integer score = 0;
      if (aparticle.getLikes() != null) {
          score += aparticle.getLikes();
      }
      if (aparticle.getCollection() != null) {
          score += aparticle.getCollection();
      }
      if (aparticle.getComment() != null) {
          score += aparticle.getComment();
      }
      return score;
  }
  ```

画面 14：
- 展示了 `computeScore` 方法的实现。
- 代码：
  ```java
  private Integer computeScore(Article aparticle) {
      Integer score = 0;
      if (aparticle.getLikes() != null) {
          score += aparticle.getLikes();
      }
      if (aparticle.getCollection() != null) {
          score += aparticle.getCollection();
      }
      if (aparticle.getComment() != null) {
          score += aparticle.getComment();
      }
      return score;
  }
  ```
