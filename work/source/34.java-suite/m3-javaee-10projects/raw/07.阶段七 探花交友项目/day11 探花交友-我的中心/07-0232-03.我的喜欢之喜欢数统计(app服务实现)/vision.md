# 画面线理解：03.我的喜欢之喜欢数统计（app服务实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\03.我的喜欢之喜欢数统计（app服务实现）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:02, 01:21, 01:55, 02:35, 03:00, 03:28, 03:59, 04:28, 06:25, 07:09, 08:00, 08:19, 08:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 21:37:29

1) 这一组画面整体在讲什么（一句话）：
演示一个“互相关注、喜欢、粉丝”统计接口的前后端实现，包括Mock接口定义、单元测试、服务层逻辑和前端调用验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 界面：Mock服务接口管理页面。
- 接口基本信息：
  接口名称：互相关注、喜欢、粉丝、统计
  状态：已发布
  接口地址：GET /users/counts
  Mock地址：https://mock.boxegu.com/mock/164/interface/api/64715
- 请求参数：
  Headers：
    Content-Type: application/json
    Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiaWF0IjoxNTQxNjQwNzU1LCJleHAiOjE1NDE2NDMzNTV9.6KwEhEhB3TYD2qrrW11rXQGfuk

画面2：
- 界面：IntelliJ IDEA中TestUserLikeApiImpl.java的单元测试代码。
- 代码：
  public void testSave() {
      this.userLikeApi.saveUserLike(userId: 11, likeUserId: 21);
      this.userLikeApi.saveUserLike(userId: 11, likeUserId: 31);
      this.userLikeApi.saveUserLike(userId: 11, likeUserId: 15);
      this.userLikeApi.saveUserLike(userId: 41, likeUserId: 11);
      this.userLikeApi.saveUserLike(userId: 51, likeUserId: 11);
  }
  @Test
  public void testQueryCounts() {
      System.out.println(this.userLikeApi.queryEachLikeCount(userId: 11));
  }
- 测试结果：testQueryCounts 通过，耗时401ms，输出为2、4、1。

画面3：
- 界面：IntelliJ IDEA中CountVo.java的VO类定义。
- 代码：
  package com.tanhua.server.vo;
  import ...
  @Data
  @NoArgsConstructor
  @AllArgsConstructor
  public class CountsVo {
      private Long eachLoveCount; // 互相关注
      private Long loveCount; // 喜欢
      private Long fanCount; // 粉丝
  }

画面4：
- 界面：IntelliJ IDEA中UsersController.java的Controller层代码。
- 代码：
  @GetMapping("/counts")
  public ResponseEntity<CountsVo> queryCounts() {
      try {
          CountsVo countsVo = this.userService.queryCounts();
          return ResponseEntity.ok(countsVo);
      } catch (Exception e) {
          e.printStackTrace();
      }
      return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
  }

画面5：
- 界面：IntelliJ IDEA中UsersService.java的Service层代码。
- 代码：
  @Autowired
  private UserInfoService userInfoService;
  private UserLikeApi userLikeApi;
  public UserInfoVo queryUserInfo(String userId, String huanxinID) {
      User user = UserThreadLocal.get();
      Long userId = user.getId();
      if (StringUtils.isNotBlank(userId)) {
          userId = Long.valueOf(userId);
      } else if (StringUtils.isNotBlank(huanxinID)) {
          userId = Long.valueOf(huanxinID);
      }
      UserInfo userInfo = this.userInfoService.queryUserInfoById(userId);
      if (null == userInfo) {
          return null;
      }
      UserInfoVo userInfoVo = new UserInfoVo();
      userInfoVo.setAge(user.getAge() != null ? user.getAge().toString() : null);
      userInfoVo.setAvatar(user.getAvatar());
      return this.userInfoService.updateUserInfoByUserId(userInfo);
  }

画面6：
- 界面：IntelliJ IDEA中UsersService.java的代码，光标在queryCounts方法中。
- 代码：
  public CountsVo queryCounts() {
      User user = UserThreadLocal.get();
      CountsVo countsVo = new CountsVo();
      this.userLikeApi.queryEachLikeCount(user.getId());
      return null;
  }

画面7：
- 界面：IntelliJ IDEA中UsersService.java的代码，光标在queryCounts方法中。
- 代码：
  public CountsVo queryCounts() {
      User user = UserThreadLocal.get();
      CountsVo countsVo = new CountsVo();
      countsVo.setEachLoveCount(this.userLikeApi.queryEachLikeCount(user.getId()));
      countsVo.setLoveCount(this.userLikeApi.queryLikeCount(user.getId()));
      countsVo.setFanCount(this.userLikeApi.queryFanCount(user.getId()));
      return countsVo;
  }

画面8：
- 界面：Advanced REST Client中发送GET请求。
- 请求头：
  Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiaWF0IjoxNTQxNjQwNzU1LCJleHAiOjE1NDE2NDMzNTV9.6KwEhEhB3TYD2qrrW11rXQGfuk
- 响应头：
  Server: nginx/1.7.3
  Date: Sat, 02 Nov 2019 12:04:53 GMT
  Content-Type: application/json;charset=UTF-8
  Transfer-Encoding: chunked
  Connection: keep-alive

画面9：
- 界面：手机模拟器界面，显示“孤独无处安放”的图片。
- 操作：点击“发布”按钮。

画面10：
- 界面：手机模拟器界面，显示“孤独无处安放”的图片。
- 操作：点击“发布”按钮。

画面11：
- 界面：IntelliJ IDEA中，手机模拟器界面显示“互相关注、喜欢、粉丝”页面。
- 代码：
  package com.tanhua.server.vo;
  import ...
  @Data
  @NoArgsConstructor
  @AllArgsConstructor
  public class CountsVo {
      private Long eachLoveCount; // 互相关注
      private Long loveCount; // 喜欢
      private Long fanCount; // 粉丝
  }

画面12：
- 界面：IntelliJ IDEA中，手机模拟器界面显示“互相关注、喜欢、粉丝”页面。
- 代码：
  package com.tanhua.server.vo;
  import ...
  @Data
  @NoArgsConstructor
  @AllArgsConstructor
  public class CountsVo {
      private Long eachLoveCount; // 互相关注
      private Long loveCount; // 喜欢
      private Long fanCount; // 粉丝
  }

画面13：
- 界面：IntelliJ IDEA中，手机模拟器界面显示“互相关注、喜欢、粉丝”页面。
- 代码：
  package com.tanhua.server.vo;
  import ...
  @Data
  @NoArgsConstructor
  @AllArgsConstructor
  public class CountsVo {
      private Long eachLoveCount; // 互相关注
      private Long loveCount; // 喜欢
      private Long fanCount; // 粉丝
  }

画面14：
- 界面：Typora编辑器中，显示“1.4.4. mock接口”章节。
- 代码：
  http://172.16.10.11:8080/users/counts
  GET
  Headers:
  Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiaWF0IjoxNTQxNjQwNzU1LCJleHAiOjE1NDE2NDMzNTV9.6KwEhEhB3TYD2qrrW11rXQGfuk
