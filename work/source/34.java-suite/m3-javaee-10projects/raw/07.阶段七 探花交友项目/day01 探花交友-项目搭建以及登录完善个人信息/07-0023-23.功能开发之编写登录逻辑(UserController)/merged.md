# 23.功能开发之编写登录逻辑（UserController）

- 阶段：07.阶段七 探花交友项目
- 章节：day01 探花交友-项目搭建以及登录完善个人信息
- 源文件：07.阶段七 探花交友项目\day01 探花交友-项目搭建以及登录完善个人信息\23.功能开发之编写登录逻辑（UserController）_【海量资源尽在 666java.com】.mp4
- 时长 10分34秒（音频 635s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们将完善之前我们所写的这个Controller的逻辑啊那么在这个login这个位置呢我们其实就拿到谁了拿到这个token了对吧那么拿到token之后呢我们需要去做一下什么呢判断那么如果如果这个token啊is notis not什么empty那么如果这个token不为空的话
[00:29] 那么就代表什么他登录成功了对不对那么登录成功了我们就需要拿到他里面包含的两个这个数据然后呢根据我们前面所看到的接口要这个格式呢给他去做一个返回那么我们在这个位置呢就来给他写一下啊那么我们怎么来玩呢我们需要通过这个stream有tios.split对之前的这个拿到这个token呢
[00:57] 去做一个这个分割字符分割吧那么用数杠去做一个分割那么分割之后呢我们拿到一个这个数组去做一个接收那么我们可以看到我们第一个啊叫bole is new它等于什么呢是不是就s应该叫bole.value of ss0然后呢
[01:26] 还有一个呢下面一个是不是就是我们真正的一个token的对吧那么这叫token吧str这个就不需要这样来写了就sse这样的话就可以了好然后呢下面呢我们就可以去做一个return了对不对return那么这个还不行啊那我们还是要做一个分装啊那么因为我们return的时候我来看一下啊return的时候呢有个叫做response
[01:57] edit点什么呢ok那么ok中的需要传什么呢传我们的一个对象对吧传我们一个这个object对象那么我们来看一下那么这个对象呢我们就这样来写吧写一个map对象吧来个stream然后呢来一个object叫做result等于new一个hcmap那么第一个呢我们就给他去设置一个谁呢设置一个这个isnew
[02:28] 一只new然后呢一只new那第二个呢就是这个token还有什么呢token str好那么我们把它呢丢到这来这个是不是就是到这啊这个我们处理的逻辑呢就是登录成功了啊登录成功那么如果没有登录成功的话逻辑是不是会走到
[02:52] 下面这个位置来啊那我们就返回500就可以了那么500呢在之前我们是不是已经写过这个逻辑了那么我把这个来拷贝一下吧把它靠一下靠到这个位置来然后呢我们再去return一下它好那么到这好嘞那么这个是不是就是我们这样的逻辑啊大了我们可以这么来操作一下就是我们把前面做一个揣开的处理对吧如果有异常的话那么我们就最后呢走到这响应这个500啊就可以了
[03:27] 好嘞那么我们这个应该改一下就是叫做登录啊登录失败好那么到这里呢我们这个是不是已经就搞定了对吧那么接下来呢我们是不是就可以来测试一下了那么我们呃把我们的服务呢重启一下然后呢通过我们的restclan的工具呢去做一个这个启动啊好那么我们还是去debug启动吧把它debug哎这个错了这个应该是我们选择它啊选择错了把它就停掉
[04:01] 然后呢我们进入到这个里面吧然后呢去debug启动一下好我们来等待它的一个启动好那么现在呢就启动起来了那么启动起来之后呢我们在这个U的Ctrl中呢我们去打一个断点OK然后呢我们去打开我们的这个哎不对打开我们这个工具啊打开我们的工具然后呢我们去测试一下那么我们来看一下
[04:28] 之前呢我应该有测试过这样的一个例子啊来找一下他啊那么你比如说我们去做这样的一个登录的一个处理对吧那么发送请求呢是这样的一个请求好那么他的请求参数类型呢是阶层类型然后点击这个发送好那么可以看到断点是不是已经来了对吧然后呢往下面走走走拿到这两个这个参数然后呢我们是不是要进入到这个里面来啊打个断点然后呢通过走
[04:58] 然后呢我们往下面走走是不是去初始化我们redis的这个template然后呢发现验证码是没有了对吧那肯定返回呢那么最后呢是不是就会响应的就是这个登录失败啊那么我们接下来呢我们就先来去获取一下这个验证码然后呢我们再去做一个输入啊这样的一个逻辑啊好那我们先到之前有这样的一个验证码先去获取这个验证码走
[05:28] 那么验证码就获取到了然后我们再去做一个登录那么验证码我看一下我的手机手机验证码是813436这样的一个逻辑了走好然后往下面走走走走走走教练发现验证码是不为空的然后继续往下面走然后验证码又是相同的可以看到
[05:58] 都是这个813436然后呢往下面再去看一下他这个已经注册了就是未注册然后呢去查询发现这个user是文档然后呢我们去new一个user然后呢去设置一些这个参数做一个insert是不是就已经已经查询成功了对吧那我们可以来检查一下我们的数据库是否是已经有了数据呢找一下我们这个NavKit打开来看一下
[06:28] 那么我们在其他里面本机的下面有一个叫麦炭花里面悠着那么其实可以看到是不是已经插入一条数据了然后呢我们继续往下面走这个逻辑走走走走让他去生成这个token这个token已经就生成了可以来看一下啊是这样的一个支付创会有一项就是这样的一个支付创然后呢我们将把它呢存储到我们的redis中
[06:58] 去做一个存储没有问题然后呢去发送这个消息看有没有问题发送消息也没有问题最后呢去做一个返回OK来看一下响应啊最后呢是不是就告诉我们这个再次登录的话登录的话是不是就是这个EASY NEW等于CHU然后呢这个是不是就是我们GWT所生成的这个token那么如果我们再次点击登录的话会怎么样的通过通过那么你会发现这个EASY NEW是不是变成了FOOSE
[07:27] 对吧而这个呢是不是又重新又生成了哎OK好嘞好那么这个呢其实就是我们的一个登录逻辑啊那么接下来呢我们就整合到我们的前端呢我们来做一个测试那么我们打开它来看一下然后呢我们直接去点击这个注册大家最好在点之前呢先确认一下这个服务的一个地址那么这个是我的地址是没有问题的返回然后点击登录
[07:55] 那么我就输入一个1就我刚才的这个手机号吧然后呢点击这个获取验证码已经获取到那么我来看一下验证码是多少6653589589我就先输出我输成这个8逻辑来了通过通过那么断点我都不要了我们看一下它有什么提醒吗没有提醒吗
[08:29] 把这个断点都去掉啊然后来看一下哎登录失败对吧登录失败那么如果我来输一个最后这个尾号输成什么呢9哎这个有点不太好输我要把它前面这个先去掉哎这个去不掉呃就是重新输一下啊这个叫呃653然后呢589589哎65
[09:04] 653653少了个56535然后呢89哎OK那么这样的话呢是不是就登录进来了那么我们这个用户呢他已经就直接进入我们的这个主页了对吧虽然我们主页现在还没有东西啊他已经进入主页了那么为什么没有进入完善用户信息这个位置呢原因我们返回的这个用户呢他是什么呢他是16HFORCE啊那么可以再来测试一个这个帮户啊
[09:33] 比如说我再来拿我的另外一个手机号我们来测一下那么我这个位置去输入我的另外一个然后呢点击获取来看一下我的这个手机验证码现在还没到稍微等一下好验证码呢已经来了就是358954954好那么
[10:02] 我这个用户呢他呢就是一个新用户他就会去进入到我们这个完善这个个人资料的这个界面中啊当然我这个逻辑现在还没有去实现对吧但是我们可以看到我们现在登录这个逻辑他是不是已经就OK了那么其实可以看到这个用户呢是不是就已经插入进来了OK好嘞好那么到这里呢我们是不是就已经完成了用户的这个登录的这个操作啊哎呀OK好嘞
[10:30] 好那么关于这个用户的一个登录逻辑呢就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的用户登录验证系统，包含控制器、服务层、Redis 令牌生成、JWT 令牌生成及前端调用测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 UserController.java 文件，其中定义了 @PostMapping("/loginVerification") 方法，接收手机号和验证码，调用 userService.login 方法。
- 代码片段：
  ```java
  @RequestMapping("user")
  @RestController
  public class UserController {
      @Autowired
      private UserService userService;
      @PostMapping("loginVerification")
      public ResponseEntity<Object> login(@RequestBody Map<String,String> param) {
          String mobile = param.get("phone");
          String code = param.get("verificationCode");
          String token = this.userService.login(mobile, code);
      }
  ```

画面 2：
- 在 UserController.java 中，添加了对 token 的判断逻辑，如果 token 不为空，则进行字符串分割。
- 代码片段：
  ```java
  if(StringUtils.isNotEmpty(token)) {
      String[] ss = StringUtils.split(token, separatorChar: '|');
  ```

画面 3：
- 在 UserController.java 中，尝试将 token 分割后的字符串数组赋值给 tokenStr，但编译器提示类型不匹配。
- 代码片段：
  ```java
  String tokenStr = ss[1];
  return ResponseEntity.ok();
  ```
- 编译错误提示：
  ```
  Incompatible types.
  Required: org.springframework.http.ResponseEntity
  Found: org.springframework.http.ResponseEntity.BodyBuilder
  ```

画面 4：
- 展示 SmsController.java 文件，其中定义了 @PostMapping("/login") 方法，用于发送验证码。
- 代码片段：
  ```java
  @PostMapping("login")
  public ResponseEntity<Object> sendCheckCode(@RequestBody Map<String,Object> param) {
      String phone = String.valueOf(param.get("erCode"));
      String code = this.smsService.sendCheckCode(phone);
      int code = ((Integer)(sendCheckCode.get("code"))).intValue();
      if (code == 3) {
          return ResponseEntity.ok(null);
      } else if (code != 1) {
          String msg = sendCheckCode.get("msg").toString();
          builder.errCode("000001").errMessage(msg);
      }
      return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(null);
  ```

画面 5：
- 在 UserController.java 中，完善了登录成功后的返回逻辑，将 token 信息封装进 Map 并返回。
- 代码片段：
  ```java
  if(StringUtils.isNotEmpty(token)) {
      String[] ss = StringUtils.split(token, separatorChar: '|');
      Boolean isNew = Boolean.valueOf(ss[0]);
      Map<String, Object> result = new HashMap<>();
      result.put("isNew", isNew);
      result.put("tokenStr", ss[1]);
      return ResponseEntity.ok(result);
  } catch (Exception e) {
      e.printStackTrace();
      ErrorResult.ErrorResultBuilder builder = ErrorResult.builder().errCode("000001").errMessage("登录失败");
      return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(builder.build());
  }
  ```

画面 6：
- 展示 MyApplication.java 文件，其中包含 Spring Boot 的主类，用于启动应用。
- 代码片段：
  ```java
  package com.tanhua.sso;
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;
  import org.springframework.context.annotation.ComponentScan;
  @ComponentScan("com.tanhua.sso.Mapper") // 设置 Mapper 接口的扫描包
  @SpringBootApplication
  public class MyApplication {
      public static void main(String[] args) {
          SpringApplication.run(MyApplication.class, args);
      }
  }
  ```

画面 7：
- 展示 UserService.java 文件，其中定义了 login 方法，用于处理登录逻辑。
- 代码片段：
  ```java
  public String login(String mobile, String code) {
      // 仅验证是否登录成功
      String redisKey = "CHECK_CODE" + mobile;
      String value = this.redisTemplate.opsForValue().get(redisKey);
      if (StringUtils.isEmpty(value)) {
          return null;
      }
  ```

画面 8：
- 在 UserController.java 中，调试器断点位于 login 方法的参数获取处。
- 代码片段：
  ```java
  String mobile = param.get("phone");
  String code = param.get("verificationCode");
  String token = this.userService.login(mobile, code);
  ```

画面 9：
- 在 UserService.java 中，调试器断点位于用户信息设置处。
- 代码片段：
  ```java
  user = new User();
  user.setMobile(mobile);
  user.setPassword(DigestUtils.md5Hex(data: "123456"));
  this.userMapper.insert(user);
  ```

画面 10：
- 在 UserService.java 中，调试器断点位于生成 JWT 令牌处。
- 代码片段：
  ```java
  String token = JwtUtils.builder()
      .subject("user")
      .claim("mobile", mobile)
      .claim("isNew", isNew)
      .expiresIn(Duration.ofMinutes(30))
      .build().signWith(SignatureAlgorithm.HS256, secret).compact();
  ```

画面 11：
- 在 UserController.java 中，调试器断点位于 login 方法的参数获取处。
- 代码片段：
  ```java
  String mobile = param.get("phone");
  String code = param.get("verificationCode");
  String token = this.userService.login(mobile, code);
  ```

画面 12：
- 展示 Advanced REST Client 发送 POST 请求到 /user/loginVerification 接口，请求体为 {"phone": "17602189189", "verificationCode": "113421"}。
- 响应状态码为 200，响应体为 {"token": "eyJhbGciOiJIUzI1NiJ9.eyJ..."}。

画面 13：
- 展示 Advanced REST Client 发送 POST 请求到 /user/loginVerification 接口，请求体为 {"phone": "17602189189", "verificationCode": "113421"}。
- 响应状态码为 200，响应体为 {"token": "eyJhbGciOiJIUzI1NiJ9.eyJ..."}。

画面 14：
- 展示 Typora 编辑器中的 day01 项目搭建及登录的个人笔记，其中包含 UserService 类的代码片段。
- 代码片段：
  ```java
  @Service
  public class UserService {
      @Autowired
      private UserMapper userMapper;
      @Autowired
      private RedisTemplate<String, String> redisTemplate;
      private static final ObjectMapper MAPPER = new ObjectMapper();
      @Autowired
      private RocketMQTemplate rocketMQTemplate;
      @Value("${jwt.secret}")
      private String secret;
  }
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
见上文第 2 点。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 或架构图/流程图。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

