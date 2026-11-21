# 画面线理解：06.环信用户系统集成之获取管理员权限（说明）

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\06.环信用户系统集成之获取管理员权限（说明）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 03:06, 03:38, 03:39, 04:04, 04:05, 04:22, 04:25, 04:40, 04:42, 04:44, 04:46, 04:50, 04:52, 04:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:07:25

1) 这一组画面整体在讲什么（一句话）：
讲解如何通过 REST API 获取管理员权限的 token，包括请求头、请求体、响应体格式及示例。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了获取 token 的 HTTP 请求地址：POST /{org_name}/{app_name}/token
- 请求头：Content-Type: application/json
- 请求体：grant_type: client_credentials, client_id: App的client_id, 可在app详情页找到, client_secret: App的client_secret, 可在app详情页找到
- 响应体：access_token, expires_in, application

画面 2:
- 展示了响应体的详细说明：access_token（有效的token字符串）、expires_in（token有效时间，以秒为单位）、application（当前App的UUID值）

画面 3:
- 展示了请求示例：curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{ "grant_type": "client_credentials", "client_id": "XA061-A80D4Ecl2111ZJW-Eng", "client_secret": "YX6EVungHx0d87ImWtInk6G1X001Fc" }' "http://al.easemob.com/easemob-demo/testapp/token"

画面 4:
- 展示了可能返回的结果示例（200状态码）：access_token、expires_in、application
- 展示了可能返回的错误示例（400状态码）：error_description: "client_id does not match", error: "invalid_grant"

画面 5:
- 展示了请求示例：curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{ "grant_type": "client_credentials", "client_id": "XA061-A80D4Ecl2111ZJW-Eng", "client_secret": "YX6EVungHx0d87ImWtInk6G1X001Fc" }' "http://al.easemob.com/easemob-demo/testapp/token"

画面 6:
- 展示了可能返回的结果示例（200状态码）：access_token、expires_in、application
- 展示了可能返回的错误示例（400状态码）：error_description: "client_id does not match", error: "invalid_grant"

画面 7:
- 展示了请求示例：curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{ "grant_type": "client_credentials", "client_id": "XA061-A80D4Ecl2111ZJW-Eng", "client_secret": "YX6EVungHx0d87ImWtInk6G1X001Fc" }' "http://al.easemob.com/easemob-demo/testapp/token"

画面 8:
- 展示了可能返回的结果示例（200状态码）：access_token、expires_in、application
- 展示了可能返回的错误示例（400状态码）：error_description: "client_id does not match", error: "invalid_grant"

画面 9:
- 展示了文档内容：4.4. 获取管理员权限
- 文档说明：环境提供的 REST API 需要权限才能访问，权限通过发送 HTTP 请求时携带 token 来体现，下面描述获取 token 的方式。
- 重要提醒：获取 token 的服务器会返回 token 有效期，具体值参考接口返回的 expires_in 字段。
- client_id 和 client_secret 可以在环境管理后台的 APP 详情页面看到。

画面 10:
- 展示了文档内容：4.4. 获取管理员权限
- 文档说明：环境提供的 REST API 需要权限才能访问，权限通过发送 HTTP 请求时携带 token 来体现，下面描述获取 token 的方式。
- 重要提醒：获取 token 的服务器会返回 token 有效期，具体值参考接口返回的 expires_in 字段。
- client_id 和 client_secret 可以在环境管理后台的 APP 详情页面看到。

画面 11:
- 展示了文档内容：4.4. 获取管理员权限
- 文档说明：环境提供的 REST API 需要权限才能访问，权限通过发送 HTTP 请求时携带 token 来体现，下面描述获取 token 的方式。
- 重要提醒：获取 token 的服务器会返回 token 有效期，具体值参考接口返回的 expires_in 字段。
- client_id 和 client_secret 可以在环境管理后台的 APP 详情页面看到。

画面 12:
- 展示了文档内容：4.4. 获取管理员权限
- 文档说明：环境提供的 REST API 需要权限才能访问，权限通过发送 HTTP 请求时携带 token 来体现，下面描述获取 token 的方式。
- 重要提醒：获取 token 的服务器会返回 token 有效期，具体值参考接口返回的 expires_in 字段。
- client_id 和 client_secret 可以在环境管理后台的 APP 详情页面看到。

画面 13:
- 展示了请求示例：curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{ "grant_type": "client_credentials", "client_id": "XA061-A80D4Ecl2111ZJW-Eng", "client_secret": "YX6EVungHx0d87ImWtInk6G1X001Fc" }' "http://al.easemob.com/easemob-demo/testapp/token"

画面 14:
- 展示了请求示例：curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{ "grant_type": "client_credentials", "client_id": "XA061-A80D4Ecl2111ZJW-Eng", "client_secret": "YX6EVungHx0d87ImWtInk6G1X001Fc" }' "http://al.easemob.com/easemob-demo/testapp/token"

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
- HTTP Request: POST /{org_name}/{app_name}/token
- Request Headers:
  - 参数: Content-Type
  - 说明: application/json
- Request Body:
  - 参数: grant_type
  - 说明: client_credentials
  - 参数: client_id
  - 说明: App的client_id, 可在app详情页找到
  - 参数: client_secret
  - 说明: App的client_secret, 可在app详情页找到

画面 2:
- Response Body:
  - 参数: access_token
  - 说明: 有效的token字符串
  - 参数: expires_in
  - 说明: token 有效时间，以秒为单位，在有效期内不需要重复获取
  - 参数: application
  - 说明: 当前 App 的 UUID 值

画面 3:
- 请求示例:
  curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{
  "grant_type": "client_credentials",
  "client_id": "XA061-A80D4Ecl2111ZJW-Eng",
  "client_secret": "YX6EVungHx0d87ImWtInk6G1X001Fc"
  }' "http://al.easemob.com/easemob-demo/testapp/token"

画面 4:
- 可能返回的结果示例（200状态码）:
  {
  "access_token": "N9eTzHsudUc1e11KMPgr17lIaAAAAAAAAAAAAAAAAAAAAA4C7aT4XgP81aX0XW8KX0Cqg0000FkdC-gfPggFTLhhyKbWpE1808e0r13F3V6a0o2516oZ2S0eW",
  "expires_in": 518400,
  "application": "8be824f8-a978-11e8-b697-5d5905f58402"
  }
- 可能返回的错误示例（400状态码）:
  {
  "error_description": "client_id does not match",
  "error": "invalid_grant"
  }

画面 5:
- 请求示例:
  curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d '{
  "grant_type": "client_credentials",
  "client_id": "XA061-A80D4Ecl2111ZJW-Eng",
