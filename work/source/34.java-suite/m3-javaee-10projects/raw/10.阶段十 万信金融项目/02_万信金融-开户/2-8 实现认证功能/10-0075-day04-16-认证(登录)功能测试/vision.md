# 画面线理解：day04-16-认证(登录)功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-16-认证(登录)功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:34, 01:21, 02:08, 02:48, 03:48, 04:02, 04:19, 05:11, 05:58, 06:34, 07:08, 07:38, 08:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:51:42

1) 这一组画面整体在讲什么（一句话）：
演示 UAA 服务中用户登录（生成令牌）和解析令牌的流程，涉及前端请求、后端控制器代码、数据库查询及 Postman 测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“4.3.2 解析令牌”章节，说明访问路径为 POST http://localhost:53020/uaa/oauth/check_token，请求参数为 token，响应内容为 JSON 格式，包含 code、msg、user_name、mobile、active 字段。
画面 2: 在 IntelliJ IDEA 中，终端显示 GatewayServer 和 UAAService 的日志，包含服务启动和实例注册信息。
画面 3: 在 IntelliJ IDEA 中，终端显示 UAAService 的日志，包含服务启动和实例注册信息。
画面 4: 在 IntelliJ IDEA 中，终端显示 UAAService 的日志，包含服务启动和实例注册信息。
画面 5: 在 IntelliJ IDEA 中，终端显示 UAAService 的日志，包含服务启动和实例注册信息。
画面 6: 在 IntelliJ IDEA 中，展示 UAAController.java 文件，包含 @RequestMapping("/login")、@RequestMapping("/confirm_access")、@RequestMapping("/oauth_error") 方法。
画面 7: 在 IntelliJ IDEA 中，展示 UAAController.java 文件，包含 @Autowired 注入的 tokenService 和 accessTokenConverter，以及 @RequestMapping(value = "/oauth/check_token", method = RequestMethod.POST) 方法。
画面 8: 展示 PDF 文档中“4.3.1 登录（生成令牌）”章节，说明访问路径为 POST http://localhost:53020/uaa/oauth/token，请求参数包括 grant_type、client_id、client_secret、username、password、domain、authenticationType。
画面 9: 在 Postman 中，设置 POST 请求的 Body，包含 grant_type、client_id、client_secret、username、password、domain、authenticationType 字段。
画面 10: 在 Postman 中，设置 POST 请求的 Body，包含 grant_type、client_id、client_secret、username、password、domain、authenticationType 字段。
画面 11: 在 SQLyog 中，查询 pzp_account 数据库的 account 表，显示 ID、USERNAME、MOBILE、PASSWORD、GATE、STATUS、DOMAIN 字段的数据。
画面 12: 在 Postman 中，设置 POST 请求的 Body，包含 grant_type、client_id、client_secret、username、password、domain、authenticationType 字段。
画面 13: 展示 PDF 文档中“4.3.1 登录（生成令牌）”章节，说明访问路径为 POST http://localhost:53020/uaa/oauth/token，请求参数包括 grant_type、client_id、client_secret、username、password、domain、authenticationType。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6:
```java
private static final Logger LOG = LoggerFactory.getLogger(UAAController.class);

@RequestMapping(value = "/login")
public String loginModel(model) {
    LOG.info("Go to login, IP: {}", WebUtil2p.getIp());
    return "login";
}

@RequestMapping("/confirm_access")
public String confirmAccess() { return "/oauth_approval"; }

@RequestMapping("/oauth_error")
public String oauthError() { return "/oauth_error"; }
```

画面 7:
```java
@Autowired
private AuthorizationServerTokenServices tokenService;

@Autowired
private AccessTokenConverter accessTokenConverter;

@RequestMapping(value = "/oauth/check_token", method = RequestMethod.POST)
@RequestBody
public void checkToken() {
```

画面 11:
```sql
SELECT * FROM account;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8:
标题：4.3.1 登录（生成令牌）
内容：
功能说明：用户登录时生成并返回令牌，该令牌用于访问 P2P 平台内保护资源。
访问路径：POST http://localhost:53020/uaa/oauth/token
请求参数：
- grant_type: 授权类型，可以是 authorization_code, implicit, client_credentials, password
- client_id: 接入客户端 id
- client_secret: 接入客户端密钥
- username: 登录用户名
- password: 登录密码
- domain: 用户域，如移动端用户（扩展协议）
- authenticationType: 认证类型，如密码认证，短信认证，二维码认证（扩展协议）

画面 13:
标题：4.3.1 登录（生成令牌）
内容：
功能说明：用户登录时生成并返回令牌，该令牌用于访问 P2P 平台内保护资源。
访问路径：POST http://localhost:53020/uaa/oauth/token
请求参数：
- grant_type: 授权类型，可以是 authorization_code, implicit, client_credentials, password
- client_id: 接入客户端 id
- client_secret: 接入客户端密钥
- username: 登录用户名
- password: 登录密码
- domain: 用户域，如移动端用户（扩展协议）
- authenticationType: 认证类型，如密码认证，短信认证，二维码认证（扩展协议）

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
