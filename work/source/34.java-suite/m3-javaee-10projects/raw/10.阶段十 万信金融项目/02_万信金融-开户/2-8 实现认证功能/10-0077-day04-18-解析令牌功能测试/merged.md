# day04-18-解析令牌功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-18-解析令牌功能测试_【海量资源尽在 666java.com】.mp4
- 时长 4分18秒（音频 257s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好刚才呢我们通过Postman进行了登录功能的一个测试我们也顺利的把期待已久的这个令牌给拿到手了这不就长这样长得有点丑吗就长这样啊反正呢它是加密后的就长这样那有的学员就以为呢老师那我也分不清这啥玩意儿对不对这东西到底是真的令牌还是假的令牌呢那我们接下来就要解析一下这个令牌以验明真身对不对那什么叫解析令牌呢
[00:31] 那就是把这个令牌里边存的原始内容给它读取出来嘛那就可以验明真身了嘛是不是那么怎么解析呢也很简单啊我们朝这发一个请求然后发请求的时候把这个令牌给干什么呀对传过去让它解析就行了然后返回的内容就是那些对里边存的原始数据那这个请求地址呢对应的就是咱Controller当中的某个方法你看这是咱的ua Controller里边有这么一个方法
[01:00] 他的请求地址就是欧奥索什么呀check下滑线什么呀token跟这一样吗一样吧当然了这个代码大家不用写这当然不用写也是直接提供给大家了你看他是不是要求你传进来一个令牌吗进来之后你看他有这个方法去解析或者说读取这个令牌的内容他最终是不是返回一个map吗返回map之后呢加了这个注解不就变成Jason返回给钱端了吗是不是啊这个代码大概咱也能看懂
[01:31] 那咱接下来在postman里边进行测试吧那我需要是不是再建一个请求这个就叫什么呀解析令牌解析令牌我们还是保存到统一认证中心保存然后呢咱们把这个地址给它粘过来吧而且是post的请求对不对好我们这儿改一下post粘过来粘过来之后呢它是不是要一个参数是吧包在里边啊
[02:11] 这个参与名字咱看他是设置为token了见名之义那这个令牌不就是刚才咱生成的这个令牌吗给它粘过去就行粘的时候给大家强调一定要细心啊多一个子少一个子都不行必须要细心啊control c然后这边粘到这儿对吧control v然后直接点击什么呀send 发送请求就行好这边没有问题对吧已经正常返回了反而内容你大家看一眼吧里边
[02:41] 你看这些是不是那个响应的状态信息成功了是不是然后呢你看登录名是不是耳的密码因为咱刚才这登录的时候你看登录的时候咱不就是用耳的密码来登录的吗是不是说就是原始信息返回了吗这个手机上手机上你可以去表里边这笔查手机号1911吗是不是这是他的客户端的一些权限这些都是从这个表里边查出来的从这个表后边这个信息是在这个表里这些权限
[03:14] 这三个对不对你看然后这个可克兰台的这克兰的AV不就是这吗是不是这边都有都有这是那个什么呀那个有效期吗对不对全线的咱目前由于没有涉及到所以说就这是空的空权限啊后边用的时候再说你看这大概呢就是把我们这个令牌里边存出的原始信息是不是解析出来读取出来是不是这就是解析令牌
[03:47] 那另外呢我们也可以给他加一个什么呀过网关的一个测试啊这呢我就不再新建请求了我在这只能给大家测试了啊那无非就是这改成什么呀对1是不是53020改成53020其他不用动我们直接点一send好大家看还是没问题吧对没有问题啊这是过网关的测试呢我们也进行了一下也没有问题那目前的话我们这个解析令牌的这个功能测试也全部搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

