# day03-10-用户中心保存信息-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-10-用户中心保存信息-定义接口_【海量资源尽在 666java.com】.mp4
- 时长 6分26秒（音频 386s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 刚才呢我们已经在统一账户微服这边是不是实现了保存功能对吧这个过程不是很复杂主要是用MP是不是就是里边涉及到DODTO这几个实体内的一个转换啊这是需要大家注意的那这边这个功能实验完之后咱们接下来该实现哪一边了呀是不是用户中心就是consumer这边对吧这边也要进行什么呀信息的一个保存而且它保存的同时是不是还要调用谁呀
[00:30] 对统一账户这里边还有一个远程调用那咱接下来就去用户中心这边那么先干嘛套路都一样嘛还是先定义对接口好咱先把这些打开都先给它关掉然后呢要挪地方了啊换换地方了要换到哪呢换到consumer这边了还是先定义接口哎接口是在这里边定义吗哎不是对了我们想起来应该还是去哪啊
[01:01] API这边API这边是不是consumer是不是还从来都没有定义过什么呀接口大家想是不是好像是对不对所以说呢咱既然找到这个子包consumer这个子包点右键然后我们需要新定义一个接口其他名字就叫consumerAPI它是一个接口将来consumer这个wifu里边所有的接口所有的方法全部定义到这里
[01:45] 好我们这个接口已经打开打开之后呢我们在这里边就要先加一些注释吧好吧这个就属于什么呀对这是用户中心API用户中心接口API那咱现在要实现的什么功能啊是不是注册或者叫保存用户的信息对不对那咱接下来就要在这呢干什么呀对定义一个方法
[02:26] 跟这个统一账户中心那边是不是差不多这边呢我们就是也叫REGIST也起这个名字没有发没有发题写顺手这是接口那大家还是想同样的一个问题这里边我们需要参数吗需要参数吗需要对不对其实跟统一账户那边一样但是这个参数类型可变了这边是用户中心嘛
[02:57] 所以这边我们会传过来一个consumer的一个DTO这个DTO应该还不存在的我们看一看我们也是需要找一找公共内公共内里边有一个consumer register DTO你看咱刚才用的是不是acoumter register DTO对不对现在换成consumer register DTO套路都一样这个我们也是需要在这模仿的上面建一个子包叫modl把它扔进去就行
[03:30] modl然后呢给他粘过来这就有了这里边的字段基本上差不多有些是不用的时候再说这个DTO其实就是用来封装前端贴过来的那些注册信息的对不对那这儿呢我就写上consumerconsumerregister什么呀DTO好这是参数有了参数有了之后需要返回值吗
[04:09] 需要吗当然需要呀他给前端返回东西嘛那我们这返回的仍然是rest什么responserestresponserestresponse这个地方犯行我们就不再指定了将来给他返回一个成功失败就OK了这是接口里边的方法吧我们基本上定义完了然后呢再把这个注释给他补充一下我们一般都是在接口里边加上注释
[04:44] 那这功能是实现啥的呀是不是就是用户注册对吧那其实就是保存用户信息用户注册或者保存用户信息好我们就加这么点注释吧这个介绍定义好之后呢咱跟之前的套路基本上也是一样的顺手把扛出了里边的这个方法来个空实现
[05:22] 那这就要去哪了呀去consumer里边我们要找一找Controller找到这个类这个类我们是不是还需要改造一下这个类是不是还没有实现那个接口呢对不对这是咱以前测试的时候用的那就是来实现一下啊叫consumer API是吧consumer API对没错好然后呢他肯定会报错嘛
[05:57] 咱接下来就是把那个方法的空时线给他加上去就行好这是空时空时线正这就行了啊咱还是跟之前一样一会呢把右层的代码实现完之后在这补一下就行了那其实到目前呢咱们是在这是哪个中心啊用户中心这个微服务把这个接口已经全部定义好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在消费者服务中定义接口契约、创建DTO类，并在Controller中实现接口以调用账户服务的注册功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示账户服务的AccountController.java文件，其中包含两个方法：一个用于校验手机验证码，另一个用于用户注册，注册方法接收AccountRegisterDTO对象并调用accountService的register方法。
画面2：与画面1相同，无新内容。
画面3：在IDEA中右键点击项目目录，弹出“New”菜单，准备创建新文件。
画面4：在“New”菜单中选择“Class”，并输入类名“ConsumerAPI”，准备创建一个类。
画面5：展示文件资源管理器，显示了课程视频和相关资料的压缩包。
画面6：在IDEA中右键点击“consumer”包，选择“New” -> “Interface”，准备创建一个接口。
画面7：弹出“Copy”对话框，准备将ConsumerRegisterDTO.java复制到consumer包下的model目录。
画面8：展示ConsumerRegisterDTO.java文件，定义了用户注册信息的DTO类，包含用户名、手机号、密码、角色和验证码等字段。
画面9：展示ConsumerAPI.java文件，定义了用户中心接口，目前为空。
画面10：在ConsumerAPI.java中输入“register”，IDE提示自动补全方法签名。
画面11：在ConsumerAPI.java中输入“Rest”，IDE提示自动补全RestTemplate相关类。
画面12：展示ConsumerController.java文件，定义了两个测试方法：hello和hi，分别用于测试接口。
画面13：在ConsumerController.java中，将Controller类实现ConsumerAPI接口。
画面14：展示ConsumerController.java文件，Controller类已实现ConsumerAPI接口，包含hello和hi两个方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Override
@GetMapping("/mobiles/{mobile}/key/{key}/code/{code}")
public RestResponse<Integer> checkMobile(@PathVariable String mobile,
        @PathVariable String key,
        @PathVariable String code) {
    return RestResponse.success(accountService.checkMobile(mobile, key, code));
}

@Override
@ApiOperation(value = "用户注册", notes = "账户注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/accounts")
public RestResponse<AccountDTO> register(@RequestBody AccountRegisterDTO accountRegisterDTO) {
    return RestResponse.success(accountService.register(accountRegisterDTO));
}
```

画面8：
```java
@ApiModelProperty(value = "ConsumerRegisterDTO", description = "用户注册信息")
public class ConsumerRegisterDTO {

    @ApiModelProperty("用户名")
    private String username;

    @ApiModelProperty("手机号")
    private String mobile;

    @ApiModelProperty("密码")
    private String password;

    @ApiModelProperty("用户角色,0借款人,1投资人")
    private String role;

    @ApiModelProperty("验证码key")
    private String key;
}
```

画面9：
```java
package cn.ictcast.wanning2p.api.consumer;

/**
 * 用户中心接口API
 */
public interface ConsumerAPI {

}
```

画面10：
```java
public interface ConsumerAPI {
    register(ConsumerRegisterDTO);
}
```

画面11：
```java
public interface ConsumerAPI {
    RestTemplate register(ConsumerRegisterDTO consumerRegisterDTO);
}
```

画面12：
```java
@RestController
@Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
public class ConsumerController {

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello() { return "hello"; }

    @ApiOperation("测试hi")
    @PostMapping(path = "/hi")
    @ApiImplicitParam(name = "姓名", value = "姓名", required = true, dataType = "String")
    public String hi(String name) { return "hi, " + name; }
}
```

画面13：
```java
@RestController
@Api(value = "用户服务的Controller", tags = "Consumer", description = "用户服务API")
public class ConsumerController implements ConsumerAPI {

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello() { return "hello"; }

    @ApiOperation("测试hi")
    @PostMapping(path = "/hi")
    @ApiImplicitParam(name = "姓名", value = "姓名", required = true, dataType = "String")
    public String hi(String name) { return "hi, " + name; }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

