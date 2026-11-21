# 画面线理解：11.环信用户系统集成之注册环信用户（测试）

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\11.环信用户系统集成之注册环信用户（测试）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:19, 00:36, 00:50, 01:06, 01:36, 01:49, 02:05, 02:19, 02:30, 02:39, 02:48, 03:07, 03:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:11:13

1) 这一组画面整体在讲什么（一句话）：
演示一个用户注册与登录功能的实现，包括在 UserService 中处理手机号注册、生成 JWT Token、调用环信服务注册用户，并通过调试和 REST 客户端验证流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserService.java 文件，其中定义了 @Service 注解的 UserService 类，包含 @Autowired 注入的 redisTemplate、userMapper、secret、MAPPER 和 rocketMQTemplate 等成员变量。
画面 2: 展示 UserService.java 中的 login 方法部分代码，逻辑是校验手机号是否已注册，若未注册则创建用户并插入数据库，然后生成 JWT Token。
画面 3: 展示 UserService.java 中的 login 方法，继续展示生成 JWT Token 的代码，使用 Jwts.builder() 设置 Claims、签名算法和密钥。
画面 4: 展示 UserService.java 中的 login 方法，重点在调用 this.huanXinService.register(user.getId()) 将用户注册到环信平台。
画面 5: 展示 MyApplication.java 文件，其中包含 @MapperScan 注解用于扫描 mapper 接口，以及 @SpringBootApplication 注解。
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
package com.tanhua.sso.service;

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

@MapperScan("com.tanhua.sso.mapper") // 设置mapper接口的扫描包
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
