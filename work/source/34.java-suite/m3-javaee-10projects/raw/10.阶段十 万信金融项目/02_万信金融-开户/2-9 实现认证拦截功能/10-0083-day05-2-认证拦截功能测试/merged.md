# day05-2-认证拦截功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-9 实现认证拦截功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-9 实现认证拦截功能\day05-2-认证拦截功能测试_【海量资源尽在 666java.com】.mp4
- 时长 6分23秒（音频 384s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好刚才呢我们把一些准备工作做了一下就是为了测试这个什么功能对认证拦截功能我们做了一个准备工作就是在什么呀Controller当中consumer Controller当中定义了一个方法注意这个方法我们模拟的是它是什么呀说保护的资源什么意思呢就是这个方法的请求路径是什么呀M打头的那么M打头的这种
[00:28] 资源访问的时候呢就要求扣端或者接入方必须具有一定的权限否则网关是不会放行的就是会被拒绝无情的拒绝对不对那我们要想访问M.2的这种资源需要具备什么样的权限呢那这个你得看表看书就看表你看这里边我们应该是要求具备什么样肉向先耳的面为什么是它呢是因为咱前面啊大家看讲义
[00:57] 前面我们应该是在这个地方吧这你看这你看这个M大头的这是M大头吧你看他这就要求必须具有什么呀Row下载线什么呀Admin这个权限所以说大家在进行测试的时候一定要注意一个细节就是你很多测试的数据啊要查一查数据或查一查表要跟里边的东西进行关联或者进行对应而谁具有这个权限呢Row Admin呢那只有谁啊只有这个什么呀这个什么呀WebGang
[01:27] 而我们前面在登录的时候其实就是拿着这条数据在进行什么测试的咱一会可以再看一下那咱接下来就进行测试吧怎么测试那无非就是通过Postman对不对通过Postman往哪发请求那就往这发请求当然我们这次发请求的时候是比较过网关往这发请求对不对
[01:50] 那么网关呢会自动对什么呀令牌呀对那个接入方的权限进行交易这样通过的话这个请求是不是才会转发到这这个过程是不是就是我们之前说的就是这个图里边什么呀567对不对这三个不是其实我们现在就在测这一块测这一块南极亚来的话就打开postman我们需要建一个请求这个请求咱放到用户中心吧
[02:18] 因为毕竟咱这个方法是不是在consumer这边是吧那我就新建一个请求起个名字就叫什么呀认证拦截认证拦截测试吧给它保存到对用户中心保存这就是这个啊然后呢我们补充一下这个请求地址这个请求地址的话你是不是就照到这复制过去就行了get请求conclude stay
[02:53] 对吧然后呢我们需要把前面的补充一下一定要注意啊我们这是过网关测试网关是不是这个53010嘛对不对Ctrl C然后这边Ctrl V这就完了吗没完啊我们需要加上Consumer是吧这这个Consumer是那个Consumer微幅的基本反而录音嘛然后才是M打头然后53010是不是这个呃网关的那个端口号码
[03:23] 所以我们现在是通过postman发请求往哪发往网关发所有的请求都要过网关那么网关呢会对令牌以及接入方的权限进行交易既然通过的话请求就会往这转发而且他在往这转发的时候是不是会带有那个什么数据用户的一些数据对不对这个功能是不是咱前面在这个过滤器里面已经实现了用软件就测试一下那往这发请求的时候要不要带一些参数啊那肯定得带啊那我们前面说了嘛
[03:52] 你以后登录完之后发请求是不是都要携带一个什么样令牌吗有没有令牌呢你寸步难行是不是因此我们要加参数这个参数不是拨在里边的是在parameter直接设置就行了因为咱这是get请求get请求你传参数问号这种形式就直接传了这个参数名你一定要注意不能随便乱写这是有规定的我们看一看讲义这里边规定的参数名是叫access下环线什么token
[04:24] 看这对吧这不能随便乱写啊我们接下来加参数ACCESS下滑线TOKEN轻轻点别拼错了啊然后这个这个令牌咱从哪来啊令牌这个令牌估计都已经过期了吧咱重新登一下然后再拿到一个令牌可以吧咱重新登一下啊哎你看这你看这咱之前登录的时候是不是就拿着这个什么webadmin做测试了对不对
[04:55] 所以这些数据啊前后啊一定跟表里边的数据要保持一致要对应上啊那咱就重新send一下吧重新登录一下好我们又重新拿了一个新的另一盘好我Ctrl CCtrl C然后这边呢就Ctrl V好大家看一下我现在给你测试的是不是正确的另一盘我是不是粘过来没有改吧对吧没有动它这是正确的另一盘啊那这时候我直接send一下好咱看一下0就表示什么呀正常
[05:28] 然后这就是我们拿到的什么呀用户相关的一些数据吗你比如这里面是不是有他的手机号是不是还有客户端的 id等等等等相关的一些信息有一些信息我一空因为咱暂时用不到后边用到的时候咱再加到时候再说那咱接下来再做一个测试就是什么呀林凡是错误的错误的林凡还不简单你这里边随便干掉一点东西就行了这个林凡就错了对不对那接下来咱再试呢看会怎么着
[05:58] 你看401吧401不就是未授权吗那你就你就拿不到那个什么呀拿不到那个用户的信息或者说这个请求这个请求就不会被网关网站进行什么呀转发就是被拒绝了啊被拒绝所以你看目前呢咱们这个认证拦截这个功能咱也搞定了也测试通过

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

