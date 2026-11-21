# 11.环信用户系统集成之注册环信用户（测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\11.环信用户系统集成之注册环信用户（测试）_【海量资源尽在 666java.com】.mp4
- 时长 3分53秒（音频 234s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们就把我们注册环信用户的这个逻辑呢去添加到我们之前的逻辑中啊那么在我们之前的注册逻辑呢是在这个位置就是有个叫做User Service下面Login这个里面如果发现我们的手机号被注册的话那么就去注册一个用户那么显然呢我们应该在这个里面就添加逻辑了那么我们在这呢我们就把谁呢把我们这个就叫环信啊
[00:27] 环信Service呢去注入进来把它呢注好嘞那么我们有了这个环信Service之后啊那么就在下面这个位置啊就是注册用户到环信啊平台好然后呢我们就要用this.环信Service.register拿到这个user.getid啊就可以了好那么来看一下这个user是不是去做了一个insert之后的一个这个user啊对吧哎呦ok
[00:57] 好嘞那么我们接下来呢就来测试一下啊那我们在这个位置去打一个断点那么把我们的这个SSO呢就跑起来那我们来测试一下好到这儿呢我们去执行一下debug好那么等待它的一个启动好那么现在呢就跑起来了那么我们来看一下我们的现在表中的数据啊那么我们有这样的一个就是手机号啊那么我们就给它来改成这个2吧去给它发送一个验证码啊
[01:25] 然后我们去做一个这个验证发送验证码那么这个是试一下是不是我们那个NGX没启我的NGX可能没启那么我们来启动一下这个NGX是在我的这个SERV的下面有个这个NGX那么应该是没有启动我们来看一下找一下这个NGXNGX没有那我们把这个NGX来启动一下
[01:54] 来一个start index好嘞然后呢我们去发起这个请求好嘞那么这个我们这个验证码就发出去了好那么接下来呢我们就去做一个登录就通过我们这个手机号去做一个登录走那么可以看到断点呢是不是就进入到我们刚刚所打断点的这个位置了对吧好那我们来一步一步跟踪一下走去获取验证码去做一个下面做这个做校验是不是相等相等
[02:24] 然后去设置为一日六为False然后去到我们数据库查取一下发现这个U的为空那么接下来就需要去注册了走注册走做音色的操作然后走走OK是不是就进入刚刚我们所写的逻辑了对吧走走走然后走走走
[02:48] 好那么下面我们这个就不看了啊然后呢最后呢就会拿到我们这个token啊这个token这个token呢是我们自己的token啊那我们来看一下这个数据有没有注册到我们的数据库表里面呢有那么他的这个ID呢是102那么接下来呢我们就进入到环信的控制台我们来刷新一下那么其实可以看到这个102啊是不是也就写入到这个环信的这个呃用户体系中了那么也就是说
[03:16] 那么我们现在呢只要我们每当我们注册一个新的用户的时候呢我们就会把这个信息呢去写入到环信那么写入到环信呢我们就可以通过这个用户的信息去登录到这个环信然后呢就可以进行这个接收和发送这个消息了就是这样的一个逻辑啊就是这样的一个逻辑了OK好那么这样的话呢我们其实已经就完成了一个环信用户体系的这样的一个注册了
[03:43] 那么到我们的一个测试注册已经是注册好了好嘞好那么关于我们环信用户注册我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个用户注册与登录功能的实现，包括在 UserService 中处理手机号注册、生成 JWT Token、调用环信服务注册用户，并通过调试和 REST 客户端验证流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserService.java 文件，其中定义了 @Service 注解的 UserService 类，包含 @Autowired 注入的 redisTemplate、userMapper、secret、MAPPER 和 rocketMQTemplate 等成员变量。
画面 2: 展示 UserService.java 中的 login 方法部分代码，逻辑是校验手机号是否已注册，若未注册则创建用户并插入数据库，然后生成 JWT Token。
画面 3: 展示 UserService.java 中的 login 方法，继续展示生成 JWT Token 的代码，使用 Jwts.builder() 设置 Claims、签名算法和密钥。
画面 4: 展示 UserService.java 中的 login 方法，重点在调用 this.huanXinService.register(user.getId()) 将用户注册到环信平台。
画面 5: 展示 MyApplication.java 文件，其中包含 @MapperScan 注解用于扫描 Mapper 接口，以及 @SpringBootApplication 注解。
画面 6: 展示文件资源管理器，显示 day05 目录下的多个视频文件。
画面 7: 展示 Advanced REST Client 的“Headers”设置面板，其中“User-Agent”字段被设置为 "iPhone"。
画面 8: 展示 Advanced REST Client 的历史记录，包含多个 HTTP 请求，其中包含 POST /user/login 请求，请求体为 application/json 格式。
画面 9: 展示 UserService.java 中的 login 方法，调试器断点位于 if (!StringUtils.equals(value, code)) 判断处，变量 value 为 "123456"，code 为 "17602026962"。
画面 10: 展示 UserService.java 中的 login 方法，调试器断点位于 if (null == user) 判断处，变量 user 为 null。
画面 11: 展示 HuanXinService.java 文件，其中定义了 register 方法，调用 huanXinConfig 获取环信服务 URL 和组织名，调用 huanXinTokenService 获取 Token，并设置 HTTP 请求头。
画面 12: 展示 UserService.java 中的 login 方法，调试器断点位于 claims.put("id", user.getId()); 之后，变量 user 的 id 为 1。
画面 13: 展示浏览器空白页面，地址栏为 https://console.easemob.com/app-detail/user。
画面 14: 展示 Typora 编辑器中的 day05.md 文件，其中包含“加入到登录逻辑中”的代码片段，重点是 this.huanXinService.register(user.getId()); 这行代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.sso.Service;

import ...

@Service
public class UserService {
    private static final Logger LOGGER = LoggerFactory.getLogger(UserService.class);
    @Autowired
    private RedisTemplate<String, String> redisTemplate;
    @Autowired
    private UserMapper userMapper;
    @Value("${jwt.secret}")
    private String secret;
    private static final ObjectMapper MAPPER = new ObjectMapper();
    @Autowired
    private RocketMQTemplate rocketMQTemplate;
}
```

画面 2:
```java
Boolean isNew = false; //默认已注册
//校验手机号是否已经注册，如果没有注册，需要注册一个账号，如果已经注册，直接登录
QueryWrapper<User> queryWrapper = new QueryWrapper<>();
queryWrapper.eq(column: "mobile", mobile);
User user = this.userMapper.selectOne(queryWrapper);
if (null == user) {
    // 该手机号未注册
    user = new User();
    user.setMobile(mobile);
    // 默认密码
    user.setPassword(DigestUtils.md5Hex(data: "123456"));
    this.userMapper.insert(user);
    isNew = true;
}
```

画面 3:
```java
Map<String, Object> claims = new HashMap<>();
claims.put("mobile", mobile);
claims.put("id", user.getId());

// 生成token
String token = Jwts.builder()
    .setClaims(claims) // 设置响应数据体
    .signWith(SignatureAlgorithm.HS256, secret) // 设置加密方法和密钥
    .compact();
```

画面 4:
```java
// 该手机号未注册，进行注册操作
User user = new User();
user.setMobile(mobile);
// 默认密码
user.setPassword(DigestUtils.md5Hex(data: "123456"));
this.userMapper.insert(user);
isNew = true;
// 注册用户到环信平台
this.huanXinService.register(user.getId());
```

画面 5:
```java
package com.tanhua.sso;

import ...

@MapperScan("com.tanhua.sso.Mapper") // 设置Mapper接口的扫描包
@SpringBootApplication
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

画面 9:
```java
public String login(String mobile, String code) {
    // 校验验证码是否正确
    String redisKey = "CHECK_CODE_" + mobile;
    String value = this.redisTemplate.opsForValue().get(redisKey);
    if (StringUtils.isEmpty(value)) {
        return null;
    }
    if (!StringUtils.equals(value, code)) {
        // 验证码输入错误
        return null;
    }
}
```

画面 11:
```java
public boolean register(Long userId) { userId: 102
    String url = this.huanXinConfig.getUrl() + "/"
        + this.huanXinConfig.getOrgName() + "/users";
    String token = this.huanXinTokenService.getToken();
    // 请求头信息
    HttpHeaders httpHeaders = new HttpHeaders();
    httpHeaders.add(headerName: "Content-Type", headerValue: "application/json");
    httpHeaders.add(headerName: "Authorization", headerValue: "Bearer " + token);
}
```

画面 14:
```markdown
加入到登录逻辑中：
if (selectUser == null) {
    // 该手机号未注册，进行注册操作
    User user = new User();
    user.setMobile(mobile);
    user.setPassword(DigestUtils.md5Hex(data: secret + "123456")); // 注意：此处代码与画面 2 不一致，画面 2 是 "123456"，画面 14 是 "secret + "123456""
    selectUser = user;
    isNew = true;
}
this.huanXinService.register(user.getId());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14: Typora 编辑器中的 day05.md 文件，包含标题“4.6、测试”，以及一个表格，表格内容为：
| 用户名 | 密码 | 手机号 | 邮箱 | 备注 |
|--------|------|--------|------|------|
| 用户1  | 123456 | 13800138000 | user1@example.com | 测试用户 |
| 用户2  | 123456 | 13800138001 | user2@example.com | 测试用户 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

