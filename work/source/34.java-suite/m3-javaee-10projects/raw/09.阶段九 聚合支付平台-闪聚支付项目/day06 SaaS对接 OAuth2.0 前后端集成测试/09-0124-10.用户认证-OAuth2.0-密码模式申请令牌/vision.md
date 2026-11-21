# 画面线理解：10.用户认证-OAuth2.0-密码模式申请令牌

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\10.用户认证-OAuth2.0-密码模式申请令牌【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 02:21, 02:45, 03:39, 04:23, 05:00, 06:03, 06:32, 07:02, 07:44, 08:46, 09:52, 10:35, 11:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:39:44

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Postman 工具测试 OAuth2.0 密码模式认证接口，包括获取 token 和解析 token 的过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 课程目录显示当前章节为“2.4.1 认证接口说明”下的“2.4.1.1 登录”。
- 展示了 OAuth2.0 密码模式的请求参数和响应内容。
- 响应内容中的 `expires_in` 字段值为 `31535999`，表示有效期。

画面 2:
- 课程目录显示当前章节为“2.4.1 认证接口说明”下的“2.4.1.1 登录”。
- 展示了 OAuth2.0 密码模式的请求参数和响应内容。
- 响应内容中的 `expires_in` 字段值为 `31535999`，表示有效期。

画面 3:
- 课程目录显示当前章节为“2.4.2.2 密码模式认证”。
- 展示了用于测试的 POST 接口地址：`http://localhost:56202/uaa/oauth/token`。
- 展示了请求参数表，包含 `client_id`、`client_secret`、`grant_type`、`username`、`password` 等字段及其值。

画面 4:
- 展示了 Postman 工具中“添加文件夹”的弹窗界面。
- 弹窗包含“Name”、“Description”、“Authorization”、“Pre-request Scripts”、“Tests”等标签页。

画面 5:
- 展示了 Postman 工具中“密码模式认证”请求的“Authorization”选项卡。
- “TYPE”设置为“Inherit auth from parent”。
- 提示信息：“This request is not inheriting any authorization helper at the moment. Save it in a collection to use the parent's authorization helper.”

画面 6:
- 课程目录显示当前章节为“2.4.2.2 密码模式认证”。
- 展示了用于测试的 POST 接口地址：`http://localhost:56202/uaa/oauth/token`。
- 展示了请求参数表，包含 `client_id`、`client_secret`、`grant_type`、`username`、`password` 等字段及其值。

画面 7:
- 展示了数据库管理工具（如 Navicat）中“shanjupay_uaa”数据库的“auth_client_details”表。
- 表中包含 `client_id`、`client_secret`、`authorized_grant_types` 等字段。
- `client_id` 为 `merchant-platform`，`client_secret` 为 `123456`，`authorized_grant_types` 为 `client_credentials,password,authorization_code,implicit,refresh_token`。

画面 8:
- 课程目录显示当前章节为“2.4.1 认证接口说明”下的“2.4.1.1 登录”。
- 展示了 OAuth2.0 密码模式的请求参数和响应内容。
- 响应内容中的 `expires_in` 字段值为 `31535999`，表示有效期。

画面 9:
- 课程目录显示当前章节为“2.4.2.2 密码模式认证”。
- 展示了用于测试的 POST 接口地址：`http://localhost:56202/uaa/oauth/token`。
- 展示了请求参数表，包含 `client_id`、`client_secret`、`grant_type`、`username`、`password` 等字段及其值。
- 展示了请求的响应体，包含 `access_token`、`refresh_token`、`expires_in`、`scope`、`jti` 等字段。

画面 10:
- 展示了数据库管理工具（如 Navicat）中“shanjupay_uaa”数据库的“account”表。
- 表中包含 `id`、`username`、`password` 等字段。
- `username` 为 `admin`，`password` 为 `123456`。

画面 11:
- 展示了 Postman 工具中“密码模式认证”请求的“Body”选项卡。
- “Body”选项卡中显示了请求的 JSON 数据。
- JSON 数据包含 `access_token`、`refresh_token`、`expires_in`、`scope`、`jti` 等字段。

画面 12:
- 展示了 Postman 工具中“解析令牌”请求的“Body”选项卡。
- “Body”选项卡中显示了请求的“Form-data”格式。
- “Form-data”格式包含 `token` 字段。

画面 13:
- 展示了 Postman 工具中“解析令牌”请求的“Body”选项卡。
- “Body”选项卡中显示了请求的 JSON 数据。
- JSON 数据包含 `aud`、`payload` 等字段。
- `aud` 字段值为 `["shanjupay-resource"]`。
- `payload` 字段包含 `user_authorities` 数组，其中包含 `ROLE_ADMIN`、`ROLE_USER` 等权限。

画面 14:
- 课程目录显示当前章节为“2.4.1 认证接口说明”下的“2.4.1.2 解析令牌”。
- 展示了用于解析令牌的请求参数：`token`。
- 展示了响应内容，包含 `aud` 和 `payload` 字段。
- `aud` 字段值为 `["shanjupay-resource"]`。
- `payload` 字段包含 `user_authorities` 数组，其中包含 `ROLE_ADMIN`、`ROLE_USER` 等权限。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
访问路径：[授权服务地址]/oauth/token
请求参数：
• grant type：授权类型，可以是authorization_code,implicit,client_credentials,password
• client id：接入客户端id
• client secret：接入客户端密钥
• username：登录用户名，认证类型(如密码认证，短信认证，二维码认证等)
{"username":"admin","authenticationType":"password"}
• password：登录密码
响应内容：
{
"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
"token_type": "bearer",
"refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
"expires_in": 31535999, //有效期
"scope": "read",
"jti": "dfc6f30a-aade-4028-a43a-1487e64a2cfb"
}
```

画面 3:
```
POST http://localhost:56202/uaa/oauth/token
请求参数：
Key	Value	Description
client_id	merchant-platform
client_secret	123456
grant_type	password
username	{"username":"itcast03","authenticationType":"password"}
password	123456
```

画面 7:
```
client_id	merchant-platform
client_secret	123456
authorized_grant_types	client_credentials,password,authorization_code,implicit,refresh_token
```

画面 9:
```
POST http://localhost:56202/uaa/oauth/token
请求参数：
Key	Value	Description
client_id	merchant-platform
client_secret	123456
grant_type	password
username	{"username":"itcast03","authenticationType":"password"}
password	123456
```

画面 11:
```
{
"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
"token_type": "bearer",
"refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
"expires_in": 31535999,
"scope": "read",
"jti": "dfc6f30a-aade-4028-a43a-1487e64a2cfb"
}
```

画面 13:
```
{
"aud": [
"shanjupay-resource"
],
"payload": {
"user_authorities": [
"ROLE_ADMIN",
"ROLE_USER"
]
}
}
```

画面 14:
```
访问路径：[授权服务地址]/oauth/check_token
请求参数：
• token ："eyJhbGciOiJI...FJD/gHfdsog..."
响应内容：
{
"aud": [
"shanjupay-resource"
],
"payload": {
"user_authorities": [
"ROLE_ADMIN",
"ROLE_USER"
]
}
}
```

4) 出现的 P
