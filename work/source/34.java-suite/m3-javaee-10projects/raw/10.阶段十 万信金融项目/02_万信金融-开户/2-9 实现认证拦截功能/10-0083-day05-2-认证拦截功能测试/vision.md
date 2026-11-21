# 画面线理解：day05-2-认证拦截功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-9 实现认证拦截功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-9 实现认证拦截功能\day05-2-认证拦截功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:57, 01:14, 01:41, 02:10, 02:23, 02:38, 02:59, 03:40, 03:45, 04:15, 04:26, 04:47, 05:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:57:49

1) 这一组画面整体在讲如何通过 Spring Security OAuth2 实现用户认证与授权，并通过 Postman 测试相关接口。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IDEA 中 `ConsumerController.java` 文件，其中包含 `@ApiImplicitParam` 注解定义的测试接口，以及 `@GetMapping` 注解的 `/m/consumers/test` 接口，用于测试认证拦截。
画面2：展示 PPT 内容，标题为“1.4.4 功能测试”，内容包括在 `ConsumerController` 中定义受保护资源方法的代码示例，以及使用 Postman 发起 GET 请求的说明。
画面3：展示 DBeaver 中 `oauth_client_details` 表的数据，其中包含客户端信息，如 `client_id` 为 `wannin-py-web-admin`，`authorized_grant_types` 包含 `password`、`authorization_code`、`implicit`、`refresh_token`。
画面4：展示 DBeaver 中 `oauth_client_details` 表的数据，其中包含客户端信息，如 `client_id` 为 `wannin-py-web`，`authorized_grant_types` 包含 `password`、`authorization_code`、`implicit`、`refresh_token`。
画面5：展示 Postman 中的 POST 请求，用于获取访问令牌，请求 URL 为 `http://localhost:53010/oauth/token`，请求体为 JSON 格式，包含 `grant_type`、`client_id`、`client_secret`、`username`、`password` 等字段。
画面6：展示 Postman 中的 POST 请求，用于获取访问令牌，请求 URL 为 `http://localhost:53010/oauth/token`，请求体为 JSON 格式，包含 `grant_type`、`client_id`、`client_secret`、`username`、`password` 等字段。
画面7：展示 Postman 中的 POST 请求，用于获取访问令牌，请求 URL 为 `http://localhost:53010/oauth/token`，请求体为 JSON 格式，包含 `grant_type`、`client_id`、`client_secret`、`username`、`password` 等字段。
画面8：展示 Postman 中的 GET 请求，用于测试受保护资源，请求 URL 为 `http://localhost:53010/consumer/m/consumers/test`，请求头中包含 `Authorization` 字段，值为 `Bearer <access_token>`。
画面9：展示 IDEA 中 `ConsumerController.java` 文件，其中包含 `@ApiImplicitParam` 注解定义的测试接口，以及 `@GetMapping` 注解的 `/m/consumers/test` 接口，用于测试认证拦截。
画面10：展示 Postman 中的 GET 请求，用于测试受保护资源，请求 URL 为 `http://localhost:53010/consumer/m/consumers/test`，请求头中包含 `Authorization` 字段，值为 `Bearer <access_token>`。
画面11：展示 PPT 内容，标题为“1.4.4 功能测试”，内容包括在 `ConsumerController` 中定义受保护资源方法的代码示例，以及使用 Postman 发起 GET 请求的说明。
画面12：展示 Postman 中的 GET 请求，用于测试受保护资源，请求 URL 为 `http://localhost:53010/consumer/m/consumers/test`，请求头中包含 `Authorization` 字段，值为 `Bearer <access_token>`。
画面13：展示 Postman 中的 POST 请求，用于获取访问令牌，请求 URL 为 `http://localhost:53010/oauth/token`，请求体为 JSON 格式，包含 `grant_type`、`client_id`、`client_secret`、`username`、`password` 等字段。
画面14：展示 Postman 中的 GET 请求，用于测试受保护资源，请求 URL 为 `http://localhost:53010/consumer/m/consumers/test`，请求头中包含 `Authorization` 字段，值为 `Bearer <access_token>`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
//获取Spring Security OAuth2认证信息对象
Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
if (authentication == null || !(authentication instanceof OAuth2Authentication)) {
    return null; //无token访问网关资源，直接返回null
}
//将当前登录的用户以及接入客户端的信息放入Map中
OAuth2Authentication oauthAuthentication = (OAuth2Authentication) authentication;
Map<String, String> jsonToken = new HashMap<>();
(oauthAuthentication.getOAuth2Request().getRequestParameters());
//43行：将token写入转发服务的request中，这样就能获取到响应
request.setParameterMap(jsonToken);
```

画面2：
```java
@ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "string")
@GetMapping(value = "/m/consumers/test")
public RestResponse<String> successResources(String jsonToken) {
    return RestResponse.success(EncryptUtil.decryptUTF8StringBase64(jsonToken));
}
```

画面3：
```sql
-- 表结构：oauth_client_details
-- 字段：client_id, client_secret, scope, authorized_grant_types, web_server_redirect_uri, authorities, access_token_validity, refresh_token_validity
```

画面4：
```sql
-- 表结构：oauth_client_details
-- 字段：client_id, client_secret, scope, authorized_grant_types, web_server_redirect_uri, authorities, access_token_validity, refresh_token_validity
```

画面5：
```json
{
  "grant_type": "password",
  "client_id": "wannin-py-web-admin",
  "client_secret": "123456",
  "username": "admin",
  "password": "123456"
}
```

画面6：
```json
{
  "grant_type": "password",
  "client_id": "wannin-py-web-admin",
  "client_secret": "123456",
  "username": "admin",
  "password": "123456"
}
```

画面7：
```json
{
  "grant_type": "password",
  "client_id": "wannin-py-web-admin",
  "client_secret": "123456",
  "username": "admin",
  "password": "123456"
}
```

画面8：
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YW5uaW5uLXBydXNlLW1hZG1pbiIsImV4cCI6MTU5NjYwNjM0MjQsImlhdCI6MTU5NjYwNjM0MjQsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c3RlciIsInN1YiI6InN1c
