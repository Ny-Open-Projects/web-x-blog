# 16_app文章详情_文章关系接口_controller代码编写及测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day03-黑马头条-app端文章详情
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day03-黑马头条-app端文章详情\16_app文章详情_文章关系接口_controller代码编写及测试【海量资源尽在 666java.com】.mp4
- 时长 7分20秒（音频 441s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去编写一下当前的API接口和当前的Controller啊那这接口呢咱们还是需要在当前的API S里边去定义啊打开它然后这里边呢是有一个叫做article info Controller在这里边去定义就可以了啊然后呢在这儿啊去加一个方法这方法呢其实咱们之前都写过啊还是response without回叫load
[00:31] article 然后是叫 behavior参数呢其实跟上面是一样都是 article 比如说咱们直接拷过来就可以了拷过来之后呢下面咱们就去写当前的什么东西啊当前的当前的 Controller 啊Controller 里边呢就是他这里边应该是再去重写另外一个方法啊Controller 啊不是他需要再去重写一个方法呗然后这时候呢咱们需要去注入谁啊
[01:08] 注入还是它是吧其实已经注入完了往下逃避不切这种咱们直接去调用当前的方法干什么呢点一个叫做load article pick up然后直接把当前的d o传过去完事了那这个Service这个Service跟control都已经写完了下面咱们就来去测试一下看看好不好使那关于测试直接其实跟咱们之前测的差不多打开这还是它
[01:39] 还是他这时候咱们可以去把它给粘贴一下好位一份是叫啥呢叫load article behavior是吧好在这个参数的其实也是他这个参数也是他稍等稍等好像少了点东西这个是不是没有加东西是吧这个咱们再加上什么request body然后这个是叫什么来着这个是啥这个是啥的话咱们还是看接口看接口
[02:11] 这可是叫load article behavior 是吧拷贝过来好拷贝过来之后呢咱们再去写这目前的测试啊这个测试在这呢啊这个测试访问的就是刚才咱们写的这个东西拷贝一下好把它放到这好放到这之后呢咱们现在要去设置参数了啊其实这里边这东西都不用动啊都不用动啊因为它这个也是dto但是这个参数好像是
[02:42] 并不是1是吧不仅仅只有1还有啥呢还有一个是当前的设备ID咱们也可以设这个1好吧1 1 L吗错了吗我看看intiger1没错呢好嗯不是get是set是吧说呢怎么回事set好设备ID
[03:11] 然后是dto.set当前的一个author也是这位一其实这一里边根本都是有数据的咱们可以查看一下现在设备ID设备ID是哪个是behaviour entry是吧打开设备ID是它是有值的然后再往下看它还有啥还有当年的authorauthor是哪个author的话就是它这是不是有个测试数据所以说你测试的时候都测试一就可以了当然你也可以自己加数据也没问题
[03:42] 好咱们可以去测一下看看好使不好使就可以了好点执行走稍等正在加载不出意外的情况下应该是能够查出来的出意外了再说真出意外了是吧好来看一看说我这块是有问题拍照目击拍照目击好像不太清楚是吧就这个咱们之前好像是写的时候有问题是吧咱们去写在那些mypro的时候直接拷过来拷过来之后参数太多了
[04:27] 所以说这个内容大家一定要注意写的时候咱们还去检查检查当时咱们去写了几个麦克风写了6个是吧写了5个是吧麦克风第一个咱们是有过的咱们再来去回顾一下第一个config咱们写完了content咱们也写完了article说完了author这个不用说是吧然后再往下看behind entry这个咱们也不用说因为咱们也说之前也写过collection这个东西咱们要去设置一下这个好像是设置完了是吧
[04:57] pairm都没问题然后下面是lags这个里边是不是忘了写了是吧pairm这会儿是没有什么技术含量大家一定要加一下你要分担的时候要跟你的参数对应上要不然的话到map文件里面找不着找不着的话它就报错所以说该加上的还得加上这还少一个pairm然后这里边就是往前的type
[05:33] 好这是一个这个没问题吧简单下type EntryID,OptionID,然后是verse没问题然后下面是这个好像是咱们之前讲过这个这个也没有是吧加上是param然后一个是叫EntryID然后第二个就是当前的什么ArticleID好这考过来到了就比较简单了是重复的工作然后下面还有一个这个加了是吧我这个加了很好
[06:07] 这个呢这个没加是吧以后再写的时候都要加上啊要不然的话他可能参数过多的话他真分辨不出来啊宝贝天天天天这个话还是挺简单的是吧你要一时干这点活的话是吧我感觉是吧嗯也不说了那这个啊这个咱们加完了啊加完之后呢咱们再去测一下好打开打开的测试啊直接点一下他也行点稍等那这次是不是绿色呀
[06:55] 然后看一下数据啊那数据是不是操作成功那这里边是first first first first那是不是这些数据都拿到了呀我看没问题啊那这个数据啊其实都已经拿到了啊那个没有报错说明就没有问题咱们后期咱们可以再找一些数据再去测啊咱们当前这个呃关注接口啊啊不是关注接口是想什么呢叫关系接口啊咱们先讲到这儿好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
              .contentType(MediaType.APPLICATION_JSON_VALUE).content(Mapper.writeValueAsString(dto));
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
              .contentType(MediaType.APPLICATION_JSON_VALUE).content(Mapper.writeValueAsString(dto));
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
  "C:\Program Files\Java\JDK 8.0_171\bin\java.exe"...
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

