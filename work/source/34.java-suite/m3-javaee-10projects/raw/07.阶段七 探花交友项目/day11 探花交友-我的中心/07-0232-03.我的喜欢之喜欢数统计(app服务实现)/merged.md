# 03.我的喜欢之喜欢数统计（app服务实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day11 探花交友-我的中心
- 源文件：07.阶段七 探花交友项目\day11 探花交友-我的中心\03.我的喜欢之喜欢数统计（app服务实现）_【海量资源尽在 666java.com】.mp4
- 时长 9分3秒（音频 543s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们的查询统计的数据那么首先呢我们先来看一下我们的Mock接口那么是在我们的这个位置那么就是我们去查询我们的这个相互喜欢啊喜欢以及这个粉丝的一个统计的一个数据啊一个展现然后呢这个呢是我们的一个Uris的一个Counts它的一个接口的一个地址
[00:26] 然后呢请求的参数是没有的就是通根据我们token啊做一个查询然后呢响应呢是返回一个阶层数据呃然后呢我们返回呢是有这么三个呃这样的一个呃数据啊一个就是我们的一个相互喜欢的一个数量还有就是我们的一个喜欢数量还有就是一个粉丝的一个数量啊那么我们需要返回这三个数据啊那么接下来呢我们就来实现这个接口
[00:52] 那么首先呢我们要根据我们Mock接口中的这个返回数据的一个结构啊那我们定义我们的一个VO就叫Counts一个VO那我们把这个VO呢来拷贝一下然后呢进入到哪里呢进入到我们的这个Server那么在这个Server啊找下面啊Server里面那我们来看一下是在这个下面呢我们找到有一个这个VO啊然后呢我们把它啊就拷贝过来嗯哎这个我们重新拷贝一下
[01:21] 好那么拷贝过来之后呢我们可以来看一下啊这个就是我们的counts为u然后呢有三个这个数量一个呢是相互喜欢数一个就是喜欢一个就是粉丝啊这样的一个数量啊那么接下来呢我们来看一下我们的接口的一个定义啊那么这个定义的这个方法呢是需要写到我们这个us
[01:41] 这个Controller下面啊因为它的路径呢是这样的一个路径那我们就统一都写到这个里面来然后呢我们把这个方法呢来拷贝一下然后呢找到我们这个Controller下面有个ususcontroller那么就写到这个最下面来好那我们来看一下这个方法啊那么最后这个方法的这个返回呢是一个这个contest.vo然后它是一个get一个请求然后呢通过一个ususervice呢去做一个这个查询
[02:08] 如果它不等于空呢就做一个return啊这个200好那么接下来呢我们就把它呢来做一个实现好那我们去创建一下我们的这个query count这个方法呃然后呢接下来呢我们首先呢是需要在我们的这个上面是不是去引入我们所写的这个服务呀对吧那么叫做user啊user这个like api那么把它呢引入进来呃然后呢这个位置用reference去做一个引入
[02:38] 然后呢这个Worsen版本呢就是1.0.0这样的一个版本那么接下来呢我们就通过这个API呢去做一个去做一个这个引路啊然后呢调用这个User-like API然后呢我们去做一个查询啊去做一个我们要查询这三个是吧那么这个是我们的一个相互喜欢那么这样我们先拿到
[03:05] 我们的一个Url这个对象等于UrlUrl3local.get这个方法然后呢拿到这个Url之后呢我们就拿到这个get id然后呢我们是需要去得到有三个啊这样的一些这个数据所以说我们就给他这样我们直接来去new一个这个VU这个对象吧那么直接去new一个他然后呢我们最后呢return呢就把这个对象的return回去然后呢我们就给他去做填充
[03:34] 然后呢set一个首先第一个呢就是我们的一个each love count就是我们的一个相互喜欢啊这样的一个数量然后呢ok搞定然后呢我们来看一下啊那么总共呢有三个那么还有呢就是love那么这个我就改成什么呢叫做query这个like count
[03:54] 然后呢这个set什么呢这个份然后呢这个叫query这个份count啊好那么这样的话呢我们是不是就设置完成了那么然后呢最后就可以把它呢就return回去了那么这样的话呢我们这个API呢就实现好了那么接下来呢我们把这个服务呢都跑起来那我们来测试一下
[04:14] 好,那么现在我们这个服务呢都已经跑起来了那么接下来呢我们就来去测试一下刚刚我已经完成了用户的一个登录了那么接下来呢我们就来测试一下这个接口然后呢走好,那么这样的话可以查看到这个结果这个数据啊那么其实呢我们可以看到这个跟我们在做单元测试的时候结果是不是一样的呀没有任何问题那么接下来呢我们就来整合到我们的这个APP中就拿我们的手机呢来测一下
[04:44] 那么之前我们的测试呢都是去启动一个模拟器那么这个呢是在我们开发过程中啊去使用这个就是我们开发移动端项目的时候的比较常用的一种方式啊当然了还有另外一种方式就是可以通过我们的手机的投屏这种方式呢去投屏到我们电脑上面来那我在这呢就简单的去说一下这个怎么去投屏啊
[05:06] 因为这个呢也是一种比较常见的一种方式然后呢我们需要去下载一个这个Apple Mirror这个软件啊大家可以自行去下载一下然后呢我们来打开它把它打开
[05:18] 打开之后呢就会有一个这个手机的这样的一个这个样式然后呢这个软件呢你免费呢是可以去使用的啊那么其实也没有必要去去升级它的VIP因为升级VIP呢是它功能虽然多了很多但是这个是需要去付费的啊那么其实我们对于我们去做开发而言呢我们做简单的
[05:40] 这个投屏就可以了那么这是第一个你需要把你手机上面的这个电脑上面这个软件的打开同样的在你的手机上面呢也是需要去安装一个这个软件然后呢点击上面会有一个投屏啊那么我就先做一个投屏然后呢去让大家来看一下这个效果那么现在大家看到的就是我手机上面那个投屏啊比如说呢我们到达哎返回到我这个桌面来然后呢我再打开这个软件啊就是
[06:09] 我们在这个位置啊有一个这个投屏大家可以看一下啊投屏然后呢去选择你这个电脑去做一个投屏就可以了然后呢这个时候呢你当你可以投屏之后你就可以把它关掉了然后呢就打开我们这个应用啊然后呢我们去做一个测试啊就可以了当然我们这个测就是免费版的它这个水印呢是一直存在的但是它不影响使用啊那么所以说呢我们就这个就无所谓了啊那我们就直接来去我直接在我手机上面去做操作啊
[06:39] 然后呢首先呢我们修改我们的这个服务器这个配置这个是没有问题的然后呢我们去来看一下我的这个登录一个用户就是通过我的这个用户去做一个登录然后呢我们点击过去验证码然后呢输入验证码这个跟我们模拟器是一模一样的然后呢就可以看到它就登录成功进入到我们的主页了然后呢是可能一开始会有一点慢吧那么我们尝试的就再去
[07:08] 再去这个重新来打开一下我们再来测一下然后呢然后我们再来测试一下他说上一次发送的验证码还没有还没有失效那我稍微等一会儿好那么我们接着继续刚刚的是网络有点问题我重启了一下这个路由器然后呢我们再来测试一下然后呢输入这个验证码就可以看到它正常能够登录进来
[07:39] 然后呢我们就点击我们的这个我的这个位置啊然后呢就会进入到我们的这个页面啊其实可以看到在我们的上面的这个位置啊那么是不是就把我们这个相关的一些这个数据呢是不是就已经啊显示出来了然后呢当然了我们可以去在前面大家应该还记得记住啊这个234这个数据啊那么你比如说呢我们在前面这个位置是不是有探花这个功能对吧
[08:04] 然后呢我们向右滑的话是不是就代表我们喜欢比如说这个是我这个用户向右滑哎向右滑喜欢然后呢喜欢啊喜欢喜欢然后呢喜欢啊我滑一点啊好那么然后呢我们就再回到我的这个功能中啊其实可以看到那么我这个喜欢数啊是不是就变成什么呢13了那么所以说明什么呢我们这个
[08:32] 这个效果啊是不是已经就OK了能够去显示出我们的一个这个数量对吧好嘞那么这样的话呢我们其实就完成了我们这样的一个功能的一个这个开发那么我们来看一下这个讲义啊这个是我们的Controller下面这个是Service下面这个是一个测试啊并且呢我们也整合到我们的这个APP中呢去做了一个演示啊好嘞好那么关于我们这个
[08:59] 统计数据的一个查询功能呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  Server: Nginx/1.7.3
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

