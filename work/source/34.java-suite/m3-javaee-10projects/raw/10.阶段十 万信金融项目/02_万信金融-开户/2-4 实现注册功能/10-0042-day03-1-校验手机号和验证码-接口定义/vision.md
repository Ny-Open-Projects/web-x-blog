# 画面线理解：day03-1-校验手机号和验证码-接口定义

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-1-校验手机号和验证码-接口定义_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:35, 01:08, 01:53, 02:15, 02:20, 03:10, 03:54, 04:15, 05:19, 05:28, 05:51, 06:01, 06:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:27:45

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
画面 13: 展示了 PPT 内容，说明在 wanning2p-account-service 工程中的 AccountController 类里实现 checkMobile 方法，并指向了 4.5.3 功能实现章节。
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
