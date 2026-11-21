# day03-1-校验手机号和验证码-接口定义

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-1-校验手机号和验证码-接口定义_【海量资源尽在 666java.com】.mp4
- 时长 6分40秒（音频 400s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好 截至到目前的话我们就把MyBetis Plus整个这一块的内容呢全部学完了这也为咱接下来实现校验手机号和验证码这个功能打下了基础那咱们接下来就开始动手去实现注册当中的这是第几步啊第几步啊这属于对 第二步就是校验手机号和短信验证码咱大概回顾一下它的需求
[00:29] 它的需求是这个样子的咱看看这个这个这个图片啊就说呢当用户收到短信验证码之后呢他会在这输入手机号在这输入那个验证码对吧然后给你登录然后呢这个时候呢前端就会把手机号啊还有验证码一起发送到我们的服务器端服务器端要干什么要对手机号和验证码进行校验啊建手机号是要判断这个手机号
[00:57] 是不是已经存在就是说他想知道你是新用户还是老用户然后呢判断建议码他是看看你这个验证码对不对的这是我们既然要实现的功能啊具体来说呢我们对应到这个时序图里边的话他应该就是从7到到几啊对到10吧相当于啊7到10就是把手机号还有验证码哎发给谁啊发给统一账户为服统一账户为服他这边会判断手机号
[01:27] 然后呢再去找谁啊找验证码服务去判断验证码对不对啊然后返回结果返回结果对不对目前实现的是七八九十这块的功能啊这个需求呢我们给大家明确一下明确完之后呢咱跟以前一样先定义什么呀对先定义接口啊就是教验手机号和验证码的这个接口接口都是定义在什么地方啊接口都是定义在什么地方
[01:57] 对接口全部都是定义在万信P2P-API这个工程当中的啊这个千万不要忘记了那咱找到idea啊打开这个API这个工程嗯还是找这个可抗的API这个接口对不对再增加一个方法这个方法是干嘛的呢咱刚才说了是不是用来校验手机号和验证码我们起了一个名字叫check目标
[02:28] 然后你看这里边一共有几个参数三个参数返回值呢还是封装成rest对response那么这里边其实封装的是应该是一个数字吧一个一个一个什么校验是否通过的一个结果那我们重点是要看这三个参数分别表示什么意思咱直接拿过来咱一起分析分析我不是校验要见手机号和这个什么验证码吗怎么传过来三个参数
[03:00] 为什么传进来三个参数呢对不对这个不知道大家有没有印象啊咱们前面呢是这样子咱们前面在第一步的时候啊就是这儿就是一到六的时候大家当时测试的时候我们是不是通过普通漫威保死二个星测试大家知道这个第一步在测试的时候验证码是不是发到用户的手机上那返回给前端的是一个焦点标识那个焦点标识你还有印象长什么样吗那个焦点标识那个焦点标识长这个样子
[03:32] 是一个sms的冒号sms的冒号后面就是一堆乱七八糟的一堆这叫建议标识那你看看我们这次在实验建议标识号验证码的时候我们一共给了三个参数其中第一个参数你应该能猜到就是那个手机号最后一个参数你应该也能猜到就是他填的这个什么呀对他填的这个验证码中间那个参数是干嘛中间这个参数其实就是这个建议标识
[04:02] 那为什么要传这个东西呢对不对前头为什么要把这个东西传回去呢因为他校验这个什么呀验证码对不对的时候要用那为什么要用呢这时候大家注意啊嗯这个谁啊这个短信验证码为服务这边他在发送短信的时候注意他在发送短信的时候他会把这个验证码往redis当中也存一份redis啊存一份存的时候怎么存呢把它当为key就是当为键
[04:32] 把那个验证码作为什么呀值这是一对嘛它存到redis里边那为什么要这么存呢就是将来校验的时候要用啊校验的时候呢它是不是把这个校验标识就是这个key发过去它给你这个key是不是可以从redis里边取出来那个正确的验证码然后跟你传过去的这个验证码做相当判断它就知道你这个验证码是正确的还是错误的明白什么意思吧
[04:58] 啊所以一定要知道为什么要有这三个参数这个非常非常重要这是什么呀我们把接口定义好接口定义好之后呢我们跟之前一样顺手呢把control了里边的这个方法来一个空时线啊先放了那你看这边他是不是都已经这个报错了对不对我们找一找这个谁呀Controller然后呢把这个方法呢给他生成一下
[05:29] 就是这个方法对吧当然呢大家也知道这个方案上面是不是要加一堆注解咱看看讲义吧这个swag的注解啊supermvc的注解啊等等这些东西我就不再编写了啊我就直接给他拿过来用这个大家注念其实你看这儿就行看这个你得知道这三个参考是怎么传过去的怎么传过去的是不是通过这个RESTful的风格对吧在路径当中直接传过去
[06:07] 那你脱正方式传的话你的这个参数前面都得加什么注解帕斯瓦博这个注解这个很容易忘啊很容易忘我这个地方你一定要注意你看我这是不是还都没加了这些全部都要加上然后呢这就是一个控制线将来我们功能全部搞定完之后呢这儿再完善这个这个代码就行了啊这是我们把什么呀把教验手机号和验证码功能的这个接口给他定义好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现手机号验证码登录功能，包括定义接口、编写控制器和实现服务层逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了用户服务类 UserServiceImpl 中的 save 方法，其中调用了 usermapper.insert(...) 方法。
画面 2: 显示了一个登录界面的 PNG 图片，包含“请输入手机号”、“请输入验证码”和“登录”按钮，底部有“万信金融”标志。
画面 3: 与画面 2 内容相同，是登录界面的 PNG 图片。
画面 4: 展示了测试用例执行成功，控制台输出了 SQL 插入语句和测试通过信息。
画面 5: 展示了项目结构，选中了 AccountAPI.java 文件。
画面 6: 展示了 PPT 内容，说明在统一账号服务中定义校验手机号接口，包括校验验证码是否正确、校验手机号是否存在，并指出在 wanning2p-api 工程中的 AccountAPI 接口里定义 checkMobile 方法。
画面 7: 展示了 AccountAPI.java 文件，其中定义了 getSMSCode 和 checkMobile 方法。
画面 8: 与画面 2 内容相同，是登录界面的 PNG 图片。
画面 9: 展示了一个流程图，描述了用户登录的完整流程，包括“浏览器/App”、“用户中心服务”、“OAM 认证服务”、“统一账户”和“短信服务”之间的交互。
画面 10: 展示了项目结构，选中了 AccountController.java 文件。
画面 11: 展示了 AccountController.java 文件，其中定义了 getSMSCode 方法和 checkMobile 方法的框架。
画面 12: 展示了 AccountController.java 文件，其中定义了 checkMobile 方法的注解和路径映射。
画面 13: 展示了 PPT 内容，说明在 wanning2p-account-Service 工程中的 AccountController 类里实现 checkMobile 方法，并指向了 4.5.3 功能实现章节。
画面 14: 展示了 AccountController.java 文件，其中定义了 checkMobile 方法的完整注解和方法体。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class UserServiceImpl {
    @Autowired
    private UserMapper usermapper;
    public void save(){
        usermapper.insert(...);
    }
}
```

画面 4:
```sql
INSERT INTO tb_user (NAME, PASSWORD, AGE, EMAIL) VALUES (?, ?, ?, ?)
```

画面 5:
```java
package cn.ictast.wanning2p.api;
import cn.ictast.wanning2p.common.domain.RestResponse;
public interface AccountAPI {
    RestResponse getSMSCode(String mobile);
    RestResponse<Integer> checkMobile(String mobile, String key, String code);
}
```

画面 7:
```java
RestResponse getSMSCode(String mobile);
RestResponse<Integer> checkMobile(String mobile, String key, String code);
```

画面 11:
```java
@Override
@ApiOperation("获取手机验证码")
@ApiImplicitParams({
    @ApiImplicitParam(name = "mobile", value = "手机号", dataType = "String")
})
@GetMapping("/sms/{mobile}")
public RestResponse getSMSCode(@PathVariable String mobile) { return null; }

@Override
@ApiOperation("校验手机号和验证码")
@ApiImplicitParams({
    @ApiImplicitParam(name = "mobile", value = "手机号", required = true, dataType = "String"),
    @ApiImplicitParam(name = "key", value = "校验标识", required = true, dataType = "String"),
    @ApiImplicitParam(name = "code", value = "验证码", required = true, dataType = "String")
})
@GetMapping(value = "/mobiles/{mobile}/{key}/{code}")
public RestResponse<Integer> checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {
    return null;
}
```

画面 13:
```java
@ApiOperation("校验手机号和验证码")
@ApiImplicitParams({
    @ApiImplicitParam(name = "mobile", value = "手机号", required = true, dataType = "String"),
    @ApiImplicitParam(name = "key", value = "校验标识", required = true, dataType = "String"),
    @ApiImplicitParam(name = "code", value = "验证码", required = true, dataType = "String")
})
@Override
public RestResponse<Integer> checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6:
标题: “4.4.2 功能实现”
内容:
在统一账号服务中定义校验手机号接口:
1. 校验验证码是否正确
2. 如果校验正确则校验手机号是否存在
在 wanning2p-api 工程中的 AccountAPI 接口里面定义 checkMobile 方法:

画面 9:
标题: “注册登录流程图”
结构:
- “浏览器/App” → “用户中心服务” → “OAM 认证服务” → “统一账户” → “短信服务”
- “统一账户” → “短信服务” → “统一账户”
- “统一账户” → “用户中心服务” → “浏览器/App”
- “短信服务” → “统一账户” → “用户中心服务” → “浏览器/App”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

