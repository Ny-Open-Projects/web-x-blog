# 13.回复陌生人问题之实现服务接口并且整合测试

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\13.回复陌生人问题之实现服务接口并且整合测试_【海量资源尽在 666java.com】.mp4
- 时长 6分57秒（音频 418s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来实现我们的接口服务然后呢我们就可以整合到我们的APP呢去做一个测试和开发了那么接下来呢我们首先来找到我们的一个today best这个Controller然后呢去编写这个方法那么我们就先来拷贝一下它然后呢找到我们这个Controller那么我们在我们的这个server这个工程里面呢我们来找一下就是在这个位置啊那我们找到
[00:29] 这个下面有一个叫做today best Controller然后呢我们去丢到这来然后呢我们需要去来看一下就是我们需要去接收的是一个我们的一个请求的一个map然后呢我们去拿到UID和replay然后呢我们去调用我们的best Service中的一个replayqson这样的一个这样的一个方法然后呢我们把这个方法呢给它去创建出来那么就是用户然后呢做一个回复
[00:59] 那么这个方法的一个实现呢我们主要呢是需要去调用我们的SSO的一个这个接口那我们就不做一个编写了那我们就直接把这个拷贝过来吧好那我们来看一下这个里面的一个内容的一个编写那么首先呢我们来看一下那么拿到当前的用户然后呢我们去做一个用户信息的一个查询然后构造我们的一个消息构造一个消息那么这几个呢是
[01:27] 我们需要去发送的一个消息的一个内容那么是不是我们刚刚在我们的这个测试用力中啊那么我们是不是就已经看过这样的一个消息了那么我们这样我们使用我们的这个JSON啊JSON VIEW吧然后呢JSON VIEW那么我去把它呢打开来看一下啊那么其实我们需要有这么几个内容去作为我们的一个消息体
[01:51] 那么是不是有一个UID然后还有是要注意UID是一个字符创然后还有就是我们那个Name还有就是我们的一个问题还有就是我们的一个答案然后设置这么几个内容然后我们去把它去转成一个我们的一个JSON那么这个Mapper是不我们现在没有我们来定义一个Mapper上面定义一下叫StaticFanel然后ObjectMapper
[02:20] 然后呢定义一个map等于new一个object map好嘞好那么有了这个map之后啊那么接下来呢我们就能够去使用它去做一个转化了然后呢这还有一个url是吧这个url呢是sso url那我们还得去这么来玩一下那么去再再再吧设置一个实际啊叫sso url然后呢我们来设置一个这个value
[02:46] 然后去设置一个$然后大括号然后我们来找到我们的一个找到我们的一个就是URL那么就是它来拷贝一下然后我们去回到这个Service中然后我们把它丢到这个位置来好那我们就可以使用这个SSO的URL了那我们就在这吧使用这个race.sso url做一个拼接
[03:12] 然后呢我们来啊设置我们的请求头然后呢设置我们的一个请求的一个这个type就是一个表单啊一个form表单的一个提交然后呢我们需要设置两个参数一个呢就是target一个就是message这个呢是不是刚刚我们在我们的这个环信啊这个就是在我们sso里面啊我们来看一下是不是在我们这个sso里面的Controller中啊其实我们是不是就指定了这样的一个啊这样的一个这个
[03:40] 参数来看一下那我们把这个呢就给它去掉去掉那么是不是需要有这么几个参数啊对吧一个呢就是target一个是message一个呢就是这个typetype呢是可以不用去传递啊那么传递这俩就可以了所以说在这个位置我们传递了两个这个参数然后呢向这个地址呢去发起一个请求然后呢设置一个http的一个additive然后呢我们再去通过这个rest啊template去发起一个请求
[04:09] 那我们现在还没有这个对象呢我们再把它注进来啊那我们继续注注一个叫rest template然后呢把它呢注进来做一个注入好那么这样的话呢我们就有了这个rest template然后有它之后呢就可以去发起请求了最后呢去响应200如果200呢就成功了啊那么我们再回到这个里面来那就成功了哎OK
[04:33] 好那么接下来呢我们就把我们这个服务呢都跑起来然后呢我们去整合到我们的一个APP里面我们来测试一下看它是否是OK的啊那么这面呢我来启动一下我的服务好的那么现在呢我们就已经把服务呢都已经啊重新启动了并且呢我们把模拟器呢也跑起来了然后呢我们去登录一下啊那么我们还是使用这个就是我们第一个这个用户020266868啊
[05:02] 然后我们去获取验证码然后去发送123456然后我们去进入到我们的首页那么进入到首页之后就会看到有这样的一些页面然后我们就是今日家人怎么没有了可能是他请求超时了我们再来一次我们再次打开我们的APP应用
[05:29] 然后呢我们就直接进入我们的一个主界面我们来看一下它的一个这个效果这回呢就OK了对吧然后呢我们点击我们的一个今日佳人点进去然后呢就会进入到这个页面然后呢我们点击这个聊一下这个关键点就来了那么我们是不是要去喜欢什么颜色呢我写一个red就是红色然后呢我们点击这个聊一下来看一下效果
[05:56] 他呢就会去是不是请求我们的刚刚所写的这个接口对吧好那我们来看一下这个效果走哎OK那么可以看到是不是他说这个消息啊已发送给对方了那就意味着什么呢我们是不是已经成功的把这个消息就发送给了环信了那么到这呢其实我们这个就是回复啊陌生人的这个问题呢这功能是不是也就啊搞定了好那么下面呢我们来看一下我们的这个接口呃那么
[06:25] 我们实现的是我们的这个在我们的today best Controller中编写的这个接口然后呢下面这个是Service主要呢是在调用sso系统所提供的一个接口进行去请求然后呢最终的一个测试呢就是这样的一个测试了那么最终可以看到什么呢消息已经发送给对方了ok好那么这个呢就是我们啊所讲的我们这个聊一下这个功能啊
[06:53] 好那么关于我们这个聊一下的功能呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现“今日最佳”功能的后端服务接口，包括控制器层的请求处理和业务层的逻辑实现，涉及用户信息查询、推荐评分、消息发送等核心功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Typora 文档中“4.6.3. 实现服务接口”章节，聚焦于 `TodayBestController` 中的 `@PostMapping("strangerQuestions")` 方法，用于接收陌生人提问请求。
画面 2: 在 IntelliJ IDEA 中展示 `TodayBestController.java` 文件，代码与画面 1 一致，显示了控制器层的请求处理逻辑。
画面 3: 展示 `TodayBestService.java` 文件中 `replyQuestion` 方法的实现，核心是通过 `RestTemplate` 向 `/user/huanxin/messages` 发送 POST 请求。
画面 4: 在 `TodayBestService.java` 中，代码聚焦于 `replyQuestion` 方法，构建了包含用户 ID、昵称和回复内容的 `Map<String, Object>`。
画面 5: 展示了 `JSON Viewer` 工具，用于查看 `replyQuestion` 方法中构建的 JSON 数据结构。
画面 6: 在 `TodayBestService.java` 中，展示了 `@Autowired` 注解注入的 `UserInfoService`、`RecommendUserService` 和 `QuestionService`。
画面 7: 展示了 `TodayBestService` 类中 `@Value` 注解配置的 `defaultRecommendUsers` 字符串和 `MAPPER` 对象的初始化。
画面 8: 展示了 `queryTodayBest` 方法的实现，其中调用 `recommendUserService.queryScore` 获取用户评分，并设置默认值 98。
画面 9: 展示了 `HuanXinController.java` 中的 `sendMsg` 方法，用于向“传智播客研究院”发送消息。
画面 10: 在 `TodayBestService.java` 中，展示了 `@Value("${tanhua.sso.url}")` 注解配置的 SSO 服务地址。
画面 11: 展示了 Genymotion 模拟器界面，显示“探花交友 - 传智播客研究院”应用的登录或配置页面。
画面 12: 展示了 Genymotion 模拟器界面，显示“探花交友”应用的“推荐”页面。
画面 13: 展示了 `TodayBestController.java` 中 `replyQuestion` 方法的完整代码，包括异常处理和返回状态。
画面 14: 展示了 Typora 文档中“4.6.4. 测试”章节，显示了“探花交友”应用的用户主页界面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@PostMapping("strangerQuestions")
public ResponseEntity<Void> replyQuestion(@RequestBody Map<String, Object> param) {
    try {
        Long userId = Long.valueOf(param.get("userId").toString());
        String reply = param.get("reply").toString();
        Boolean result = this.todayBestService.replyQuestion(userId, reply);
        if (result) {
            return ResponseEntity.ok(null);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 2:
```java
@PostMapping("strangerQuestions")
public ResponseEntity<Void> replyQuestion(@RequestBody Map<String, Object> param) {
    try {
        Long userId = Long.valueOf(param.get("userId").toString());
        String reply = param.get("reply").toString();
        Boolean result = this.todayBestService.replyQuestion(userId, reply);
        if (result) {
            return ResponseEntity.ok(null);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 3:
```java
String targetUrl = this.url + "/user/huanxin/messages";
HttpHeaders headers = new HttpHeaders();
headers.setContentType(MediaType.APPLICATION_FORM_URL_ENCODED);
MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
params.add("target", userId.toString());
params.add("msg", msgStr);
HttpEntity<MultiValueMap<String, String>> httpEntity = new HttpEntity<>(params, headers);
ResponseEntity<Void> responseEntity = this.restTemplate.postForEntity(targetUrl, httpEntity, Void.class);
return responseEntity.getStatusCodeValue() == 200;
```

画面 4:
```java
public Boolean replyQuestion(Long userId, String reply) {
    User user = UserThreadLocal.get();
    UserInfo userInfo = this.userInfoService.queryUserInfoById(user.getId());
    // 构造消息内容
    Map<String, Object> msg = new HashMap<>();
    msg.put("userId", user.getId().toString());
    msg.put("nickname", this.queryQuestion(userId));
    msg.put("reply", reply);
    try {
        String msgStr = MAPPER.writeValueAsString(msg);
        String targetUrl = this.url + "/user/huanxin/messages";
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URL_ENCODED);
        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("target", userId.toString());
        params.add("msg", msgStr);
        HttpEntity<MultiValueMap<String, String>> httpEntity = new HttpEntity<>(params, headers);
        ResponseEntity<Void> responseEntity = this.restTemplate.postForEntity(targetUrl, httpEntity, Void.class);
        return responseEntity.getStatusCodeValue() == 200;
    } catch (Exception e) {
        e.printStackTrace();
    }
    return false;
}
```

画面 5:
```json
{
  "userId": "1",
  "nickname": "探花",
  "reply": "你好"
}
```

画面 6:
```java
@Autowired
private UserInfoService userInfoService;
@Autowired
private RecommendUserService recommendUserService;
@Value("2")
private Long defaultUserId;
@Value("2,3,4,5,6")
private String defaultRecommendUsers;
@Autowired
private QuestionService questionService;
```

画面 7:
```java
@Value("2,3,4,5,6,7,8,9,10,11,12,13")
private String defaultRecommendUsers;
@Autowired
private QuestionService questionService;
private static final ObjectMapper MAPPER = new ObjectMapper();
```

画面 8:
```java
public TodayBest queryTodayBest(Long userId) {
    User user = UserThreadLocal.get();
    TodayBest todayBest = new TodayBest();
    UserInfo userInfo = this.userInfoService.queryUserInfoById(userId);
    todayBest.setId(userId);
    todayBest.setAge(userInfo.getAge());
    todayBest.setAvatar(userInfo.getLogo());
    todayBest.setGender(userInfo.getSex().name().toLowerCase());
    todayBest.setNickName(userInfo.getNickName());
    todayBest.setTags(StringUtil.split(userInfo.getTags(), ','));
    double score = this.recommendUserService.queryScore(userId, user.getId());
    if (score == 0) {
        score = 98; // 默认分值
    }
    todayBest.setRateValue(Double.valueOf(score).longValue());
    return todayBest;
}
```

画面 9:
```java
@PostMapping("messages")
public ResponseEntity<Void> sendMsg(@RequestParam("target") String target,
                                   @RequestParam("msg") String mq,
                                   @RequestParam(value = "type", defaultValue = "txt") String type) {
    try {
        Boolean result = this.huanXinService.sendMsg(target, mq, type);
        if (result) {
            return ResponseEntity.ok(null);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
    }
}
```

画面 10:
```java
@Value("${tanhua.sso.url}")
private String ssoUrl;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

