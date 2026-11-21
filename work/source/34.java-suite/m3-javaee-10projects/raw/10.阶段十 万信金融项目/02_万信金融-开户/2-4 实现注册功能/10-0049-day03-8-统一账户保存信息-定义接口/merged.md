# day03-8-统一账户保存信息-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-8-统一账户保存信息-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 10分22秒（音频 622s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把保存用户信息这一块的需求还有流程啊给大家说了一下接下来是不是该动动小手实现功能的时候了对不对那咱从哪开始呢大家还得看一下这个流程图这个图因为这里边咱们说了是不是有两个微服务都要进行这个保存我要先开发哪个微服务呢这个我个人是这样想你想从任何一个地方开始都可以
[00:31] 前提是只要你的需求你的流程你都搞清楚了我觉得从哪开始是无所谓的那我这里呢是先搞统一账户这边然后再搞用户中心这边然后再让用户中心去演成调用什么呀统一账户我是按照这个流程的你也可以按这个也可以不按这个刚才说了只要你需求清楚了流程也清楚了其实你从哪开始都是可以的那咱就先整统一账户为服务了这边从哪开始
[01:01] 想想咱之前开发任何一个功能的时候都是从哪开始对先定义什么呀接口没错看这儿统一账号对吧微服务实现保存功能先干什么呀对定义接口去哪定义接口啊还有印象吗咱们所有的接口都在哪放着来对在什么呀在哪在哪里说在API这个工程里边对不对好咱展开
[01:30] 那么大家注意这个包呢这个结构呢我们发生了一点变化可能跟之前不太一样因为考虑到API这个工程呢是存放所有的什么样的接口比如我存放ArkHunt这个微幅的接口将来又存放什么呀Consumer微幅的接口将来还有别的这个微幅的接口对不对所以我在API这个包下面又建了子包然后ArkHunt里边是专门存放它的接口将来Consumer这个包里边存放就Consumer的什么呀接口
[01:59] 那我建议你呢也按照这种结构给他再重新做一个调整那好咱找到这个接口然后在这里边是不是需要新定义一个什么呀方法来实现这个保存功能好先加注释吧功能呢其实最终实现的就是什么呀注册对吧注册具体来说这一步是保存信息是吧那咱先给方法起个名字吧
[02:36] 就叫注册版就叫R1GISTR这个单词比较常用大家得记住啊那然后呢大家想一想第一个问题跟之前一样第一个问题需要参数吗对不对需要参数吗大家想保存信息啊保存信息这个信息应该是从哪来的是不是应该是前端发请求带过来那这种情况下一般是不是咱都需要有一个参数来封装接收前端
[03:08] 传过来这个信息对吧而且注册的时候呢前端发过来信息有可能不止一个呀所以我们这儿呢建议你用一个什么呀实体类那用哪个实体类呢这个也不需要大家编写了我们给大家提前准备好了直接拿过来用就行公共类里边啊哪个呢大家看名字应该是这个吧这个长得比较像是不是accountregisterdto.j这个呢看名字就是用来封装什么呀这个注册
[03:39] 这个信息的对不对注册时候用户提交过来的信息呢那它考到哪呢考到哪你得看一眼啊看看它这里边这个包嘛对不对你看API工程里边的accountmodel哦它应该是在下面又新建了一个子包专门存放实体类的这咱就看明白了那咱就在应该是这吧点右键再新建一个什么呀子包然后叫MO
[04:11] DEL然后呢咱就把这个哥们给他Ctrl C然后然后在这是吧Ctrl V粘过来就能用了对就这样啊这玩东西的话比较简单你自己打开只手就行了这里边大家能看到传过来也就三样东西用户名手机号和密码对不对具体怎么用咱一会再说实验功能时候再说
[04:45] 反正呢他就是用来接收什么呀封装前端传过来的这些数据的注册的数据用户的数据好那我这就写了啊这就应该写什么呀一个参数吧ACC好我们找一找就是他了我就不再敲了啊就是他这是参数那返回值呢返回值得有吧对我们前面说了他一定会有返回值而且都是什么类型啊对rest response没错
[05:20] 那它的一般都是有什么有范形的我们这也需要给大家指定一个范形这个范形呢用什么呢我们也是给大家提供好的一个类叫Count DTO是它我先给你粘过来咱再看里边都是什么东西它也是它是放到哪它同样也是放到这个位置了对不对那好那咱就也给它粘过来Ctrl C然后也是这这个位置Ctrl V
[05:54] 让我们大家看一看啊这里边呢跟刚才这个register DTO相比是不是多了一些东西对不对有什么主件用户名手机号还有什么账户状态好它是属于哪种用户C端就是普通客户还是这个企业客户啊对不对B端的客户啊所以说我们返回的时候呢返回的数据会多一些啊因为有些这个值呢是默认的比如这个账号状态你刚注册了一定是正常的一个状态对不对
[06:22] 所以说呢他返回的时候呢数据会多一些所以我们准备呢把他作为这个返回给前端的一个一个范形去使用给他放到这就行不能自动识别是吧卡了我这应该卡了一下啊好识别过来反应有点慢这是咱定义好的这个方法然后呢咱把这个注视呢给他补一下吧有一个参数叫at反应比较慢par
[06:58] AM这是用来干什么呀对是用来封装注册信息这个返回值呢我就一个return了跟上面一样了agr1提完好就这样吧这是接口啊咱就定义好定义好之后呢咱像以前一样顺手把这个什么呀control料里边这个方法先来用空实现吧好吧account src找一找因为咱这个接口前面说过都是表现层的嘛
[07:34] 所以你看他打开应该正常应该会要报错的吧不报错吧报错了对不对好我们来一个空实现就OK了实现一下OK去最下面瞅一眼啊是这个吧对不对这是咱刚才定义的这个方法嗯那咱在这呢按照惯例把该加的一些什么呀注解都给他加上比如说smile mvc的注解还有swag的注解咱现在写代码基本上形成这个固定的套路了对不对咱先把这个
[08:13] 请求路径先定一定吧这个是注册注册的话咱得用post的请求所以说这呢我就加一个at什么呀post mapping对不对然后路径呢咱一会儿指定一个路径就行post mapping然后这个路径的话我们给一个什么路径呢这个每次啊凡是碰到这种起名字的都很纠结对吧不知道该起啥名字这个地方有一个细节需要大家注意了有个细节需要大家注意哪个细节呢
[08:45] 大家看这个图看这个流程图的话大家知道统一账号这块这个功能是不是被谁去远程调用的呀是被用户中心远程调用的也就是说呢这个接口它是不是不暴露给谁啊前端那么之前呢咱们提醒过大家让大家好好看那个什么呀编码规范对吧编码规范里边对这一点是有规定的什么规定呢如果是不暴露给前端的它这种这个请求地址呢是以什么开头的呀对是以L开头的
[09:19] 这是咱这边的一个规定咱这个项目当中的一个规定啊我这个一定要注意了后边咱就起个名字吧就是ACC OUNTS就起这样一个名字罢了啊就这么一个路径就提醒大家注意啊一定是L打头的啊这是因为咱那个规范或者那个手册里边咱进行规定了我这个呢是你一定要注意的然后呢接下来呢咱把那个SWAG的注解加一下SWAG注解后边我就不在意点一让你敲了啊
[09:48] 因为前面都给大家敲过了而且这个东西呢说实话没啥技术含量就是一个体力活啊我就从讲义里边直接给大家粘了咱不浪费这个时间啊就这个地方从这开始粘了啊这个东西大家应该都比较熟悉了就粘到这个地方好了那到目前为止呢咱就在这是哪个微服啊统一账户微服这边把接口给什么呀定音好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲用户注册流程的架构设计与对应的 Java 代码实现，包括接口定义、数据传输对象（DTO）设计、控制器层代码以及系统各模块间的交互时序。

2) 按时间顺序列出每张画面的要点：
画面1：展示用户注册流程的时序图，包含“网关/API”、“用户中心服务”、“OAUTH认证服务”、“统一用户”、“验证网服务”五个模块，通过编号箭头展示交互步骤。
画面2：展示IDEA中`AccountAPI.java`接口定义，包含`getSMSCode`方法。
画面3：IDEA项目结构视图，聚焦于`AccountAPI`接口。
画面4：IDEA中`AccountAPI.java`，光标位于`register()`方法定义处。
画面5：文件资源管理器中显示多个项目文件夹和文件，包括`wanningzp_apollo`、`SQLyog Professional 8.4...`、`Apollo配置中心 - Google...`等。
画面6：IDEA中`AccountRegisterDTO.java`类定义，包含`@ApiModel`注解和`@ApiModelProperty`字段注解。
画面7：IDEA中`AccountAPI.java`，光标位于`register()`方法定义处。
画面8：文件资源管理器中显示多个Java文件，包括`Account.java`、`AccountDTO.java`、`AccountRegisterDTO.java`等。
画面9：IDEA中`AccountDTO.java`类定义，包含`@ApiModel`注解和`@ApiModelProperty`字段注解。
画面10：IDEA中`AccountDTO.java`，光标位于`domain`字段定义处。
画面11：IDEA中`AccountDTO.java`，光标位于`status`字段定义处。
画面12：IDEA中`AccountController.java`控制器类，包含`@GetMapping`注解的`getSMSCode`和`checkMobile`方法。
画面13：展示用户注册流程的时序图，与画面1内容相同。
画面14：文件资源管理器中显示多个项目文件夹和文件，包括`wanningzp_apollo`、`SQLyog Professional 8.4...`、`Apollo配置中心 - Google...`等。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```java
package cn.itcast.wanningzp.api;

import cn.itcast.wanningzp.common.domain.RestResponse;

/**
 * 获取短信验证码
 * @param mobile 手机号
 * @return
 */
RestResponse getSMSCode(String mobile);

/**
 * 校验手机号和验证码
 * @param mobile 手机号
 * @param key 校验标识
 * @param code 验证码
 * @return
 */
RestResponse<Integer> checkMobile(String mobile, String key, String code);
```

画面6：
```java
import io.Swagger.annotations.ApiModelProperty;
import lombok.Data;

@ApiModel(value = "AccountRegisterDTO", description = "账户注册信息")
public class AccountRegisterDTO {

    @ApiModelProperty("用户名")
    private String username;

    @ApiModelProperty("手机号")
    private String mobile;

    @ApiModelProperty("密码")
    private String password;
}
```

画面9：
```java
import io.Swagger.annotations.ApiModelProperty;
import lombok.Data;

@ApiModel(value = "AccountDTO", description = "账户信息")
public class AccountDTO {

    @ApiModelProperty("标识")
    private Long id;

    @ApiModelProperty("用户名")
    private String username;

    @ApiModelProperty("手机号")
    private String mobile;

    @ApiModelProperty("账号状态")
    private Integer status;

    @ApiModelProperty("域(c端用户; b端用户)")
    private String domain;
}
```

画面12：
```java
@Authorized
private AccountService accountService;

@GetMapping("/hello")
public String hello() { return "hello" }

@Override
@GetMapping("/获取手机验证码")
@ApiImplicitParam(name = "mobile", value = "手机号", dataType = "String")
public RestResponse getSMSCode(@PathVariable String mobile) { return accountService.getSMSCode(mobile); }

@Override
@GetMapping("/校验手机号和验证码")
@ApiImplicitParam(name = "mobile", value = "手机号", required = true, dataType = "String")
@ApiImplicitParam(name = "key", value = "校验标识", required = true, dataType = "String")
@ApiImplicitParam(name = "code", value = "验证码", required = true, dataType = "String")
@GetMapping("/mobiles/{mobile}/{key}/{code}")
public RestResponse checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：时序图结构：
- “网关/API” → “用户中心服务” → “OAUTH认证服务” → “统一用户” → “验证网服务”
- “统一用户” → “验证网服务”（步骤4）
- “验证网服务” → “统一用户”（步骤5）
- “统一用户” → “用户中心服务”（步骤6）
- “用户中心服务” → “统一用户”（步骤7）
- “统一用户” → “用户中心服务”（步骤8）
- “用户中心服务” → “统一用户”（步骤9）
- “统一用户” → “用户中心服务”（步骤10）
- “用户中心服务” → “统一用户”（步骤11）
- “统一用户” → “用户中心服务”（步骤12）
- “用户中心服务” → “统一用户”（步骤13）
- “统一用户” → “用户中心服务”（步骤14）
- “用户中心服务” → “统一用户”（步骤15）
- “统一用户” → “用户中心服务”（步骤16）
- “用户中心服务” → “统一用户”（步骤17）
- “统一用户” → “用户中心服务”（步骤18）
- “用户中心服务” → “统一用户”（步骤19）
- “统一用户” → “用户中心服务”（步骤20）

画面13：与画面1内容相同。

5) 无。

