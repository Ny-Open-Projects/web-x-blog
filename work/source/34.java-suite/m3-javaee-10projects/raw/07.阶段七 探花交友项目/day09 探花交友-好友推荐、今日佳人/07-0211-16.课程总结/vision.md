# 画面线理解：16.课程总结

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\16.课程总结_【海量资源尽在 666java.com】.mp4
- 抽帧：7 帧 @ 00:14, 00:22, 00:27, 00:48, 00:51, 01:08, 01:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:20:30

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
          .set("spark.mongodb.output.uri", properties.getProperty("spark.mongodb.output.uri"));
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
