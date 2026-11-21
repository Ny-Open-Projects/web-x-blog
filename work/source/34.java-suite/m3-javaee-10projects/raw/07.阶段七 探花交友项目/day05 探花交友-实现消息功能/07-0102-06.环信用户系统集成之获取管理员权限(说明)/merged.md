# 06.环信用户系统集成之获取管理员权限（说明）

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\06.环信用户系统集成之获取管理员权限（说明）_【海量资源尽在 666java.com】.mp4
- 时长 4分59秒（音频 299s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下获取管理员的权限那么这个是什么意思啊就是说我们想要去访问这个环信所提供的一些rest接口的时候啊那我们必须呢要去携带一个这个token那么也就是说我们需要去拥有这个管理员这个权限去做这个操作啊他其实他的这个流程或者说逻辑啊
[00:26] 跟我们的这个碳化交易这个项目的这个登录逻辑是一样的就说比如说我们现在用户他想要去访问圈子中的一些数据那么他必须要携带一个这个token而这个token从哪来的呢是我们用户在登录之后呢就可以得到一个这个token那么我们在这的意义也是一样的就是说我们需要先在环信的这个平台呢
[00:51] 先去获取到这个token然后呢在请求我们目标API的时候啊携带这个token啊就可以了那么如果没有这个token的话那么我们这个API肯定是访问不了的啊OK好那么下面呢这个他的一个提醒就是说获取这个token服务器的会返回token的一个有效期具体的这个值呢参考返回的这个experting这个资段但是呢由于网络延迟等原因呢
[01:20] 它的系统不保证token在这个表示表示这个有效期是绝对有效的就说有可能它告诉我们说这个有效期是两天但是呢我们可能在使用了一天之后它就已经过期了这个是它不保证的所以说呢在我们的应用中呢在使用这个token的时候那我们就要注意了那么一旦我们这个token这个从有效变成无效了
[01:48] 那么我们就需要重新再做一个获取那么所以说你看如果发现token这个异常的话就要重新去获取这个token那么也就是说我们如果http请求的响应是401的那么就代表说没有权限访问对吧那么我就需要重新来获取我们这个token了那么另外需要注意的是不要频繁的向服务器发起获取token的一个请求
[02:15] 那么同一个这个账号发送请求超过一定频率的时候呢会被服务器分号切记切记那么这个是指什么意思呢就是说如果说没有这个限制的话那么有些人在使用这个环信API的时候呢他可能是这么玩的就是说每一次请求的时候我先获取管理员权限然后呢我再去请求目标的一个API这样的话就会导致环信的这个获取token这个服务的
[02:44] 这样的一个这个服务器它的压力就会变得非常大所以说它必须要有这样的一个限制来限制我们怎么呢你拿到token你可以把它存起来存起来之后呢你需要的时候就拿到去用就可以了并不需要每一次请求接口的时候都去获取这个token这个大家理解了吧好那么我们来看一下它的一些这个相关的一些请求那么它的这个http请求呢是地址是这样的一个地址
[03:12] 然后它的请求投信息然后这个是请求的一个body那么需要有三个参数get typeclient idclient secret那么这两个参数是固定然后这两个我们可以在我们的后台去找到相关的一些值只要你的应用创建成功那么就能够找到这两个值
[03:37] 然后响应的一个body就是有这个参数叫access token这个就是我们所需要拿到的token那么expert in这个是有效期然后下面这个是当前应用的一个uuid其实这个我们就用不着了那么当然我们现在一个应用如果是有多个应用的话这个还是有用的然后它下面给出一个请求的一个示例
[04:07] 他通过这个CURL做一个请求那么可以看到这个是他的一个请求的头然后呢这个也是投信息下面这个是请求的参数信息然后这个请求的一个地址发起的是一个post请求ok好那么我们是不是就可以通过我们restclient去做一个访问了那么如果是这个响应成功的话那么就会返回这个token那么关键是我们去拿到这个token
[04:33] OK好那么如果是400的话就是这client id或者是client一个secret的一个错误了好嘞好那么接下来我们就要去实现什么呢来获取管理员的权限了那么我们这个讲义中所写的内容呢就是拷贝的他的这个文档中内容啊所以呢是一样的啊好那么关于这个获取管理员权限的一个这个说明呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

