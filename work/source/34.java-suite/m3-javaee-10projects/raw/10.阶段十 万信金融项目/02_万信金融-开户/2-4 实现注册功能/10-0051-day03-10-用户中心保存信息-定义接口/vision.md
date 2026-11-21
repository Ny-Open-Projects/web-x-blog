# 画面线理解：day03-10-用户中心保存信息-定义接口

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-10-用户中心保存信息-定义接口_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:39, 00:45, 01:20, 01:28, 03:03, 03:25, 03:37, 03:42, 03:49, 04:02, 04:23, 05:31, 05:53, 06:07
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:33:55

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
