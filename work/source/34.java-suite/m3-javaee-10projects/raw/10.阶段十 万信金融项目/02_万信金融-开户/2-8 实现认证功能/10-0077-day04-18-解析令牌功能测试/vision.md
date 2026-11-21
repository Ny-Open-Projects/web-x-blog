# 画面线理解：day04-18-解析令牌功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-18-解析令牌功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:37, 00:49, 00:58, 01:12, 01:37, 01:54, 02:11, 02:28, 02:50, 03:01, 03:16, 03:23, 03:39, 04:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:52:49

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Postman 发起请求，调用 UAA 服务的 /oauth/check_token 接口，解析并验证访问令牌（Access Token），并展示返回的用户身份和权限信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“4.3.2 解析令牌”章节，说明访问路径为 POST http://localhost:53020/uaa/oauth/check_token，请求参数为 token，响应内容包含 code 和 msg 字段。
画面 2: 展示 PDF 文档中“4.3.2 解析令牌”章节的响应内容示例，包含 user_name、mobile、active、client_authorities 等字段，并显示“ROLE_TEST”。
画面 3: 展示 IDEA 编辑器中 UAAController.java 文件的代码，其中 @RequestMapping 注解定义了 /oauth/check_token 路径，方法接收 token 参数并进行验证。
画面 4: 展示 IDEA 编辑器中 UAAController.java 文件的代码，与画面 3 相同，但高亮了 @RequestMapping 注解。
画面 5: 展示 Postman 中弹出的“SAVE REQUEST”对话框，用于保存当前请求。
画面 6: 展示 PDF 文档中“4.3.2 解析令牌”章节，说明 msg: 操作结果，success 表示成功，jwt: 身份令牌，主要用于一次性 token，从而回避重复请求攻击。
画面 7: 展示 Postman 的工作区，显示多个打开的窗口，包括 Postman、wanningzp_apollo、UAA服务集成配置、SQLyog、ApolloPortal、adminService、configService。
画面 8: 展示 Postman 中创建的“解析令牌”请求，设置访问路径为 http://localhost:53020/uaa/oauth/check_token。
画面 9: 展示 Postman 中“解析令牌”请求的响应结果，返回了 access_token、refresh_token、expires_in、code、msg 等字段。
画面 10: 展示 SQLyog 数据库管理工具界面，显示多个打开的窗口，包括 SQLyog、Postman、wanningzp_apollo、UAA服务集成配置、ApolloPortal、adminService、configService。
画面 11: 展示 SQLyog 数据库管理工具界面，显示多个打开的窗口，包括 SQLyog、Postman、wanningzp_apollo、UAA服务集成配置、ApolloPortal、adminService、configService，鼠标指针在“资料”文件夹上。
画面 12: 展示 Postman 中“解析令牌”请求的响应结果，返回了 tenant_id、msg、code、user_name、mobile、client_authorities、client_id、scope 等字段，其中 client_authorities 包含 ROLE_API、ROLE_CONSUMER、ROLE_ADMIN。
画面 13: 展示 Postman 中“解析令牌”请求的响应结果，返回了 tenant_id、msg、code、user_name、mobile、client_authorities、client_id、scope 等字段，其中 client_authorities 包含 ROLE_API、ROLE_CONSUMER、ROLE_ADMIN。
画面 14: 展示 Postman 中“解析令牌”请求的响应结果，返回了 tenant_id、msg、code、user_name、mobile、client_authorities、client_id、scope 等字段，其中 client_authorities 包含 ROLE_API、ROLE_CONSUMER、ROLE_ADMIN。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
@RequestMapping(value = "/oauth/check_token", method = RequestMethod.POST)
public Map<String, ?> checkToken(@RequestParam("token") String value) {
    OAuth2AccessToken token = tokenServices.readAccessToken(value);
    if (token == null) {
        throw new InvalidTokenException("Token was not recognised");
    }
    if (token.isExpired()) {
        throw new InvalidTokenException("Token has expired");
    }
    OAuthAuthentication authentication = tokenServices.loadAuthentication(token.getValue());
    Map<String, ?> rst = accessTokenConverter.convertAccessToken(token, authentication);
    return rst;
}
```

画面 12:
```json
{
    "tenant_id": null,
    "msg": "success",
    "code": 0,
    "user_name": "admin",
    "mobile": "15178791011",
    "client_authorities": [
        "ROLE_API",
        "ROLE_CONSUMER",
        "ROLE_ADMIN"
    ],
    "client_id": "wanning-pzp-web-admin",
    "aud": [
        "wanning-resource"
    ],
    "scope": []
}
```

画面 13:
```json
{
    "tenant_id": null,
    "msg": "success",
    "code": 0,
    "user_name": "admin",
    "mobile": "15178791011",
    "client_authorities": [
        "ROLE_API",
        "ROLE_CONSUMER",
        "ROLE_ADMIN"
    ],
    "client_id": "wanning-pzp-web-admin",
    "aud": [
        "wanning-resource"
    ],
    "scope": []
}
```

画面 14:
```json
{
    "tenant_id": null,
    "msg": "success",
    "code": 0,
    "user_name": "admin",
    "mobile": "15178791011",
    "client_authorities": [
        "ROLE_API",
        "ROLE_CONSUMER",
        "ROLE_ADMIN"
    ],
    "client_id": "wanning-pzp-web-admin",
    "aud": [
        "wanning-resource"
    ],
    "scope": []
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“4.3.2 解析令牌”，内容包括功能说明、访问路径、请求参数、响应内容。
画面 2: PPT 标题为“4.3.2 解析令牌”，内容包括响应内容示例，包含 user_name、mobile、active、client_authorities 等字段。
画面 6: PPT 标题为“4.3.2 解析令牌”，内容包括 msg: 操作结果，success 表示成功，jwt: 身份令牌，主要用于一次性 token，从而回避重复请求攻击。
画面 7: 无 PPT 标题，展示 Postman 工作区，包含多个打开的窗口。
画面 8: 无 PPT 标题，展示 Postman 中创建的“解析令牌”请求。
画面 9: 无 PPT 标题，展示 Postman 中“解析令牌”请求的响应结果。
画面 10: 无 PPT 标题，展示 SQLyog 数据库管理工具界面。
画面 11: 无 PPT 标题，展示 SQLyog 数据库管理工具界面。
画面 12: 无 PPT 标题，展示 Postman 中“解析令牌”请求的响应结果。
画面 13: 无 PPT 标题，展示 Postman 中“解析令牌”请求的响应结果。
画面 14: 无 PPT 标题，展示 Postman 中“解析令牌”请求的响应结果。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
