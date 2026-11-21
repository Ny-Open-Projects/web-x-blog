# 16.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\16.课程总结_【海量资源尽在 666java.com】.mp4
- 时长 1分52秒（音频 112s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢做一下总结那么今天呢我们主要呢是来实现我们碳化交友这个项目的一些功能啊主要呢集中在首页啊这个功能那么我们实现了我们首页的这个好友的推荐啊好友推荐呢主要有分为两块的实现第一呢我们去实现它的一个默认的推荐的列表那么就是当我们查询不到列表的时候呢就给它展现我们这个默认值
[00:26] 然后还有就是我们去实现了我们的一个好友推荐那么这个是我们是基于Spark的MLib去做一个智能的一个推荐那么这个是我们今天的重点学习内容那么也希望大家能够去能够独立的完成这块的代码的编写以及这块的一些程序的设计然后我们实现了我们首页中的谁看过我的功能
[00:50] 以及什么呢我们的家人信息就是我们点击家人信息之后呢去展现他的详情其实呢我们不仅是说点击这个家人今日家人查看详情那我们点击下面的这个推荐列表也可以去查看这个详情的啊是一样的然后呢下面呢我们又实现了这个聊一下这个功能这个呢我们主要呢是需要去设置问题以及我们提交答案那么提交答案呢是要发送消息给我们的
[01:18] 这个环信这个平台然后呢给对方去发送消息那么对方在接收到消息之后呢如果点击啊这个聊一下那么就会成为这个好友了那么这个逻辑在前面我们已经实现过了啊我们现在已经是完成了一个消息这样的一个发送然后呢我们最后是不是实现了我们的一个地理位置的一个这个上报那么主要呢是用于我们后面的这个搜附近啊功能的一个实现啊OK
[01:43] 好那么关于我们今天课程的一个总结呢我们就讲到这那么今天呢主要呢我们在实现功能ok

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解“首页好友推荐”、“谁看过我”、“今日最佳”、“聊一下”等社交推荐功能的实现，包括配置、服务层代码、Spark推荐算法和接口定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 课程内容大纲：1. 首页好友推荐（含1.1默认推荐列表、1.2好友管理）、2. 谁看过我、3. 今日最佳、4. 聊一下、5. 地理位置。
- 1.1.1 配置默认推荐的用户：展示配置文件内容。
  #application.properties
  tanhua.sso.default.recommend.users=2,3,4,5,6,7,8,9,10,11,12,13
- 1.1.2 修改查询逻辑：展示TodayBestService类的代码片段，包含注释“查询推荐用户列表”和方法queryRecommendUserList。

画面2：
- 1.1.2 修改查询逻辑：展示TodayBestService类的代码片段，包含注释“查询推荐用户列表”和方法queryRecommendUserList。
  //查询推荐用户列表
  @Param("token")
  @Param("userId")
  @Param("date")
  @Return
  public PageResult queryRecommendUserList(RecommendUserQueryParam queryParam,
          String token) {
          //获取当前的技术用户
          User user = this.userService.queryUserByToken(token);
          if (null == user) {
          return null;
          }

画面3：
- 1.2 好友管理：展示代码片段，包含查询条件构建和用户信息处理。
  if (StringUtils.isNotEmpty(queryParam.getCity())) {
          queryWrapper.eq("city", queryParam.getCity());
          }
          if (queryParam.getAge() != null) {
          queryWrapper.ge("age", queryParam.getAge());
          }
          List<UserInfo> userInfos = this.userInfoService.queryList(queryWrapper);
          List<TodayBest> todayBests = new ArrayList<>();
          for (UserInfo userInfo : userInfos) {
          TodayBest todayBest = new TodayBest();
          todayBest.setUserId(userInfo.getUserId());
          todayBest.setAvatar(userInfo.getLogo());
          todayBest.setGender(userInfo.getSex().name().toLowerCase());
          todayBest.setNickName(userInfo.getNickName());
          todayBest.setTags(StringUtils.split(userInfo.getTags(), ','));
          //设置用户记录
          for (RecommendUser record : records) {
          record.getUserId().longValue() == userInfo.getUserId().longValue();
          }

画面4：
- 2.1 编写pojo：展示SparkUserRecommend类的代码片段，包含Spark配置和SparkSession创建。
  import org.joda.time.DateTime;
  import scala.Tuple2;
  import java.io.InputStream;
  import java.math.BigDecimal;
  import java.util.Arrays;
  import java.util.List;
  import java.util.Properties;
  public class SparkUserRecommend {
          public static void main(String[] args) throws Exception {
          //读取外部配置文件
          InputStream inputStream =
          SparkUserRecommend.class.getClassLoader().getResourceAsStream("app.properties");
          Properties properties = new Properties();
          properties.load(inputStream);
          //构建Spark配置
          SparkConf sparkConf = new SparkConf()
          .setAppName("SparkUserRecommend")
          .setMaster("local[1]")
          .set("Spark.mongodb.output.uri", properties.getProperty("Spark.mongodb.output.uri"));
          //构建Spark上下文环境
          SparkSession sparkSession =
          SparkSession.builder().config(sparkConf).getOrCreate();

画面5：
- 2.3 实现接口：展示接口定义代码，包含包名和导入的类。
  package com.tanhua.dubbo.server.api;
  import com.alibaba.dubbo.config.annotation.Service;
  import com.tanhua.dubbo.server.pojo.RecommendUser;
  import com.tanhua.dubbo.server.pojo.Visitors;
  import org.springframework.beans.factory.annotation.Autowired;

画面6：
- 3.2 TodayBestController：展示控制器代码片段和接口文档。
  //查询今日最佳
  @Param("userId")
  @Return
  @GetMapping("/id/{personalInfo}")
  public PageResult queryTodayBest(@PathVariable("userId") Long userId) {
          //查询今日最佳用户
          List<TodayBest> todayBests = this.todayBestService.queryTodayBest(userId);
          return new PageResult(0, todayBests);
          }

画面7：
- 4 聊一下：展示“聊一下”功能的接口文档，包含Mock接口和请求参数。
  聊一下功能包含了2个接口：
  • 查询对方设置的问题
  • 提交答案
  • 提交答案后要发送消息给对方
  mock接口：https://mock.boxuegu.com/project/164/interface/api/77937
  接口路径：GET /question
  Mock接口：http://mock.boxuegu.com/mock/2/api/question
  请求参数：
  Headers:
  Content-Type application/json
  Authorization eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTU2NzQwNzQwMjIsImlhdCI6MTU2NzQwNzQwMjIsInN1YiI6ImFkbWluIn0.1k0d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d744d74

