# 画面线理解：16_app文章详情_文章关系接口_controller代码编写及测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\16_app文章详情_文章关系接口_controller代码编写及测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:53, 01:12, 01:39, 02:16, 02:46, 03:21, 03:57, 04:09, 04:34, 05:05, 06:40, 06:52, 07:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 13:16:42

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过 Controller 层调用 Service 层，实现文章信息加载和用户行为（点赞、收藏、关注）的接口，并通过单元测试验证其功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 `AppArticleInfoServiceImpl` 类中的 `loadArticleBehavior` 方法，用于处理用户对文章的行为（点赞、收藏、关注）。
- 代码片段：
  ```java
  //5. 通过authorId(appId)获取userId
  ApAuthor apauthor = apAuthorMapper.selectById(dto.getAuthorId());
  //查看关注关系，根据当前登录人的user_id与作者的user_id判断，如果有数据，说明已经关注，没有则说明没有关注
  if(user!=null && apauthor!=null && apauthor.getUserId()!=null) {
      ApUserFollow apUserFollow=null;
      if(apUserFollowMapper.selectFollowId(QuartzUtils.groupId(user), apauthor.getUserId())!=null) {
          isFollow=true;
      }
  }
  Map<String, Object> data = new HashMap<>();
  data.put("isfollow", isFollow);
  data.put("islike", isLike);
  data.put("isunlike", isUnlike);
  data.put("iscollection", isCollection);
  return ResponseResult.okResult(data);
  ```

画面 2：
- 展示了 `ArticleInfoControllerApi` 接口，定义了 `loadArticleInfo` 方法。
- 代码片段：
  ```java
  package com.heima.article.apis;
  import com.heima.model.article.dtos.ArticleInfoDto;
  import com.heima.model.common.dtos.ResponseResult;
  public interface ArticleInfoControllerApi {
      ResponseResult loadArticleInfo(ArticleInfoDto dto);
  }
  ```

画面 3：
- 展示了 `ArticleInfoController` 类，实现了 `ArticleInfoControllerApi` 接口。
- 代码片段：
  ```java
  @RestController
  @RequestMapping("/api/v1/article")
  public class ArticleInfoController implements ArticleInfoControllerApi {
      @Autowired
      private AppArticleInfoService appArticleInfoService;
      @Override
      @PostMapping("/load_article_info")
      public ResponseResult loadArticleInfo(@RequestBody ArticleInfoDto dto) {
          return appArticleInfoService.getArticleInfo(dto.getArticleId());
      }
      @Override
      public ResponseResult loadArticleBehavior(ArticleInfoDto dto) {
          return appArticleInfoService.loadArticleBehavior(dto);
      }
  }
  ```

画面 4：
- 展示了 `ArticleInfoControllerTest` 类中的 `testLoadArticleInfo` 方法，用于测试 `loadArticleInfo` 接口。
- 代码片段：
  ```java
  @Test
  public void testLoadArticleInfo() throws Exception {
      ArticleInfoDto dto = new ArticleInfoDto();
      dto.setArticleId(1L);
      dto.setUserId(1L);
      dto.setEquipmentId(1L);
      dto.setChannelId(1L);
      dto.setArticleId(1L);
      MvcRequestBuilder builder = MockMvcRequestBuilders.post("/api/v1/article/load_article_info")
              .contentType(MediaType.APPLICATION_JSON_VALUE).content(mapper.writeValueAsString(dto));
      mvc.perform(builder).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print());
  }
  ```

画面 5：
- 展示了 `ArticleInfoController` 类中的 `loadArticleBehavior` 方法，用于处理用户行为。
- 代码片段：
  ```java
  @Override
  @PostMapping("/load_article_behavior")
  public ResponseResult loadArticleBehavior(@RequestBody ArticleInfoDto dto) {
      return appArticleInfoService.loadArticleBehavior(dto);
  }
  ```

画面 6：
- 展示了 `ArticleInfoControllerTest` 类中的 `testLoadArticleBehavior` 方法，用于测试 `loadArticleBehavior` 接口。
- 代码片段：
  ```java
  @Test
  public void testLoadArticleBehavior() throws Exception {
      ArticleInfoDto dto = new ArticleInfoDto();
      dto.setArticleId(1L);
      dto.setUserId(1L);
      dto.setEquipmentId(1L);
      dto.setChannelId(1L);
      dto.setArticleId(1L);
      MvcRequestBuilder builder = MockMvcRequestBuilders.post("/api/v1/article/load_article_behavior")
              .contentType(MediaType.APPLICATION_JSON_VALUE).content(mapper.writeValueAsString(dto));
      mvc.perform(builder).andExpect(MockMvcResultMatchers.status().isOk()).andDo(MockMvcResultHandlers.print());
  }
  ```

画面 7：
- 展示了 MySQL 数据库中的 `ap_likes_behavior` 表的 DDL 语句。
- SQL 语句：
  ```sql
  CREATE TABLE `ap_likes_behavior` (
      `id` int(11) unsigned NOT NULL,
      `behavior_entry_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
      `entry_id` int(11) unsigned DEFAULT NULL COMMENT '文章ID',
      `operation` tinyint(1) DEFAULT NULL COMMENT '点赞行为',
      `created_time` datetime DEFAULT NULL COMMENT '创建时间',
      `burst` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
      `PRIMARY KEY (`id`) USING BTREE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='点赞行为表';
  ```

画面 8：
- 展示了 `ArticleInfoControllerTest` 类中的 `testLoadArticleBehavior` 方法的测试结果，显示测试通过。
- 控制台输出：
  ```
  "C:\Program Files\Java\jdk1.8.0_171\bin\java.exe"...
  Compilation completed successfully in 103 ms (moments ago)
  ```

画面 9：
- 展示了 `ArticleInfoControllerTest` 类中的 `testLoadArticleBehavior` 方法的测试结果，显示测试失败。
- 控制台输出：
  ```
  2019-09-17 10:38:12,376 [INFO] (Thread-3) log.springframework.scheduling.concurrent.ThreadPoolTaskExecutor [shutdown] [Starting some ExecutorService]
  2019-09-17 10:38:12,382 [INFO] (Thread-3) com.zaxxer.hikari.HikariDataSource [close] [HikariPool-1 - Shutdown initiated...]
  2019-09-17 10:38:12,382 [INFO] (Thread-3) com.zaxxer.hikari.HikariPool [logState] [HikariPool-1 - Before shutdown state: total=5, active=0, idle=5, waiting=0]
  2019-09-17 10:38:12,382 [INFO] (Thread-3) com.zaxxer.hikari.HikariPool [logState] [HikariPool-1 - After shutdown state: total=5, active=0, idle=5, waiting=0]
  ```

画面 10：
- 展示了 `ArticleInfoControllerTest` 类中的 `testLoadArticleBehavior` 方法的测试结果，显示测试失败。
- 控制台输出：
  ```
  2019-09-17 10:40:37,215 [INFO] (Thread-3) org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean [destroy] [Closing JPA EntityManagerFactory]
  2019-09-17 10:40:37,220 [INFO] (Thread-3) org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean [destroy] [Closing JPA EntityManagerFactory]
  2019-09-17 10:40:37,220 [INFO] (Thread-3) org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean [destroy] [Closing JPA EntityManagerFactory]
  2019-09-17 10:40:37,220 [INFO] (Thread-3) org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean [destroy] [Closing JPA EntityManagerFactory]
  ```

画面 11：
- 展示了 `ApLikesBehaviorMapper` 接口，用于查询用户点赞行为。
- 代码片段：
  ```java
  import com.heima.model.behavior.po.ApLikesBehavior;
  public interface ApLikesBehaviorMapper {
      ApLikesBehavior selectLastLike(String burst, Integer objectId, Integer entryId);
  }
  ```

画面 12：
- 展示了 `ApUserFollowMapper` 接口，用于查询用户关注关系。
- 代码片段：
  ```java
  package com.heima.model.mappers.app;
  import com.heima.model.user.po.ApUserFollow;
  import org.apache.ibatis.annotations.Param;
  public interface ApUserFollowMapper {
      ApUserFollow selectFollowId(@Param("burst") String burst, @Param("userId") Long userId);
  }
  ```

画面 13：
- 展示了 `ApUserFollowMapper` 接口，用于查询用户关注关系。
- 代码片段：
  ```java
  package com.he
