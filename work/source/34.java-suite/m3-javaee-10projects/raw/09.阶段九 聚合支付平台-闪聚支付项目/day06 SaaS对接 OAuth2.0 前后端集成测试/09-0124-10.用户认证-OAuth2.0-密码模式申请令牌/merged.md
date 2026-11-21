# 10.用户认证-OAuth2.0-密码模式申请令牌

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\10.用户认证-OAuth2.0-密码模式申请令牌【海量资源尽在 666java.com】.mp4
- 时长 11分37秒（音频 698s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面呢,我们来测试一下我们的统一认证接口。
[00:04] 在刚才我们分析,AUX 2.0有四种模式,授权码模式,密码模式,客户端模式和简化模式。
[00:11] 那么在我们散具支付平台,针对我们平台自己的账号呢,它的登录我们会采用密码模式。
[00:18] 所以这里边呢,我们只测试密码模式,其他几种模式呢,大家可以按照我们的什么接口的规范呢,自行进行测试。
[00:27] 那方法呢其实和密码模式类似啊我们来看那么密码模式呢是需要输入账号和密码对不对并且按照OAuth 2.0协议的标准这里边有几个参数是必须要有的一个是Ground Type授权类型根据刚才我们说的四种模式这四种模式各位
[00:48] 这四种模式第一种对应授权码模式对吧第二种对应的是简化模式第三种是客户端模式第四种就是密码模式所以我们用哪一种模式呢这个ground time你要输入哪个值好然后client id就是客户端的id然后呢是客户端密码这个呢咱们知道客户端最终是不是要由这个资源拥有者给他授权吧所以这个客户端呢
[01:17] 这四种模式呢它是都需要的那ID和密钥是提前需要告诉这个客户端你的ID是什么你的密钥是什么大家理解吗所以以后呢我们按照咱们这个统一认证因为咱们是不是接入了SaaS系统是吧SaaS系统呢在SaaS系统的这个数据库当中我们把客户端ID和密钥配好之后呢我们就可以用这个ID和密钥来向我们SaaS系统的这个认证服务来申请令牌了
[01:45] user name呢就不用说了就是我们说的账号对吧只不过user name呢各位我们是在我们本的项目的当中啊我们把它进行扩展了一下啊user name呢我们是用一个json这个数据啊那这就是一个账号那这个呢就是一个什么密码模式的这个password所以一会我们请求这样的一个东西还有password就是登录密码好响应的内容呢就是会响应具体的令牌了因为大家可以看到这个是不是就是令牌啊哎这就是令牌
[02:15] 那这个呢就是令牌的什么有效期好那么我们来看那现在我们是不是就可以怎么弄啊来测试一下吧当然这个令牌你拿到的时候呢我们还有一个接口呢还可以把这个令牌的内容给它解析出来各位你也知道这个令牌你没发现你看是看不懂的是不是最终这个令牌里边有什么内容呢我们可以通过这个解析令牌的接口把它解析出来好了那下面呢我们就开始来测试啊密码模式
[02:43] 那首先呢各位我们需要把我们项目原来我们对接的这个SaaS的三个服务呢给它起起来哪三个呀一个是网关一个是user还有一个是UAA其实作为这个认证的服务呢正是UAA那这个UAA呢它采用的技术呢是Special Security加OS 2.0
[03:11] 那么在我们的这个黑板成员官方网站也有相关的专题资料大家可以去自行学习当前呢我们主要是来和他的这个接口呢做对接我们呢使用他的接口OK那我们来看啊首先我们要测试接口因为他是一个http的接口对吧我们要打开post闷好那么这里边呢我们要做的事呢是不是就要进行什么建一个请求了对不对好看一下啊我们这儿呢就先创建一个文件夹
[03:41] 这个呢我们就叫做什么呀叫认证授权行吧好那么这里边呢就会是相关的认证授权相关的测试的信息了好那这个呢就是我们说的什么呀现在我们要测啥呀我们是不是要测密码模式我们最终要通过密码模式进行什么认证对不对所以我们就是密码模式认证的测试好然后选择刚才我们创建的认证授权
[04:12] 那么这个链接我们要填哪个呢那你要看了现在我们这个链接你看这就是它的链接是POST的对吧好这里边改成POST的至于这个56020指的是什么注意看啊找到SaaS系统的三个服务呢我们已经放到了我们的工程中了
[04:36] 所以它呢也是死门部的工程其实很多东西我们也是看得懂的啊来我们找到UAA就是我们说的认证服务那我们找到它的这个配置文件嗯你看56020是不是就是我们的UAA的这个端口地址呀好那现在URL知道了那现在我们要通过刚才我们说的接口的这个什么你看它的参数是不是要跟它请求了呀
[05:06] 那我们按照咱们刚才所说的这个要求来设置参数好吧第一个呢就是client id对吧client id和client meal那么我刚才说了嘛这个id和meal我们需要找到这个当初我们导入sas数据库的这个ua的数据库看到了吗那么你找到里边有一个叫做os下滑线client detail的这个表
[05:36] 这表里边有很多促使化的数据啊其中看好这儿是有一个叫针对商户平台我们给他分配了一个这个client id和什么和密钥这就是他的client id这就是他的密钥懂了吧所以这里边呢我们就来看一下一个一个来输入啊那这个呢是post的嘛所以这里边我们要来他就是client id段是不是就是这个叫merchandise-platform是吧
[06:07] 放进去然后Client ID的密钥呢所以这个参数啊你不要复制数据库这个啊这个是不正确的你尽量是跟刚才我说的这个接口的这个规范里边你看这个Client IDClient ID密钥对吧你在这复制啊所以这是Client ID密钥Client ID密钥它是什么呢看123456一定跟它对应起来啊然后呢接下来还有还有咋还有就是Ground TypeGround Type是啥呢
[06:36] 就是我们说的四种模式分别对应一个我们是密码模式要输入password这是OS2.0协议的标准嘛还有什么还有username对吧那这个username是不是就是我们说的账号啊那username各位我们说了嘛username在我们系统当中做了一个扩展呢
[07:00] 对吧做了一个扩展这个扩展的方式是啥呢在接口描述这边写的很清楚也就是你要把这个账号包裹在一个接身串当中但这个账号你要注意一定是我们系统中存在的账号那系统中存在什么账号呢当初我们说一个员工是不是就是对应一个用户的账号啊
[07:23] 对吧当初我们也测试了整个对接的流程那这里边TES01和02是不是就是我们的账号我们可以把这个TES02放进去这就是其中一个账号对吧好那接下来还有呢是不是就是密码呀密码密码的话当初我们输的什么密码你这呢就是什么密码对吧老师这是啥密码我也忘了随便输的瞎输的是吧那刚
[07:50] 当初我们进行商户注册的时候你可以看一下当初我们商户注册的这个信息嘛你看当初密码我们输的是多少呀123456对不对那所以说这里面呢我们要怎么弄啊输入123456这就是按照我们说的密码模式啊然后呢把这个参数呢都输全了输全了之后接下来我们是不是就可以来进行发送请求
[08:20] 然后最终呢他就可以得到什么可以得到令牌这个就是我们的什么访问令牌那么这个令牌的类型呢你看这里面是不是有一叫比尔对吧比尔啥意思你看这是OS2.0协议的也是他的标准要求我们知道啊当初我们在自治申请的时候我们是不是伪造了令牌你看定牌前面是不是都有一个比尔
[08:44] 对B2空格所以各位再回到刚才测试来这是令牌的类型是吧这个呢是刷新令牌就这令牌快过期了我可以用这个令牌呢对再申请一个令牌这是令牌的什么过期时间这是我们申请的这个令牌的一个什么它的权限范围这个呢是指的是这个令牌好长指的是对这个令牌的一个相当于简化的一个唯一的一个什么号所以我们平常用哪个令牌呢我们就用第一个
[09:12] 这就是我们的访问令牌懂了吧好那各位这个令牌就被我申请成功了那有人说老师这令牌到底这里头是啥东西呢我们是不是就可以通过解析令牌这个接口来看看这个令牌到底有啥对吧所以解析令牌的话你也可以再建一个request这叫什么解析令牌
[09:38] 而这个解析令牌的时候呢注意看你需要把令牌的信息要拿到因为你解析嘛你解析令牌是不是要拿到令牌的信息啊所以这里面呢我们还是pose的在这儿我们得有一个token然后呢把刚才密码模式拿到的这个令牌的信息注意考出来然后呢把它贴到这里头好长是吧然后呢
[10:07] 发送这时候就得到了解析令牌的里面的内容大家看到这内容是啥内容有时候看不懂但是其实我们之前说过这个令牌就是用户的身份信息对吧用户的身份信息你看这账号有了吧对吧账号你看手机号有了吧所以一般它的基本信息是不是都在里头了还有这一堆就是用户的权限懂了吧有时候老师这用户怎么都有权限了因为当初我们注册三户的时候我们是不是说了
[10:38] 我们给他一个默认权限对不对他下面的员工有一个默认权限所以这就是他的什么哎权限一堆的这个权限权限符号是吧好那么到这呢各位你基本上应该知道我们使用的是os2.0协议进行认证我们采用具体的是os2.0协议当中的密码模式来申请令牌是吧那这时候你拿到令牌了那各位我已经拿到真正的令牌了
[11:07] 那么我们再进行资质申请或者说其他的操作的时候那我咱们就要使用真正的令牌了大家理解了吗包括后边我们和前后端和前端集成了之后呀那么就可以使用我们这个SaaS系统提供的统一认证服务来完成用户的登录然后呢颁发一个正式的令牌对到这儿呢我们就完成了这个统一认证的测试好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

