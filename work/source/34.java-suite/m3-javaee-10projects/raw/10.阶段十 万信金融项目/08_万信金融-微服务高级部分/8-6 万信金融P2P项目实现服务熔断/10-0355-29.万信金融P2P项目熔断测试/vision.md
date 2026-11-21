# 画面线理解：29.万信金融P2P项目熔断测试

- 阶段：10.阶段十 万信金融项目
- 章节：08_万信金融-微服务高级部分/8-6 万信金融P2P项目实现服务熔断
- 源文件：10.阶段十 万信金融项目\08_万信金融-微服务高级部分\8-6 万信金融P2P项目实现服务熔断\29.万信金融P2P项目熔断测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:45, 01:27, 01:53, 02:23, 02:50, 03:33, 03:54, 04:46, 05:08, 05:29, 05:44, 06:15, 07:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 09:22:17

1) 这一组画面整体在讲什么（一句话）：
演示 SpringCloud 微服务架构中用户登录功能的实现，包括代码逻辑、异常处理、服务调用流程及调试过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `AccountFallbackFactory` 类代码，用于处理 `AccountApiAgent` 服务调用失败时的降级逻辑。代码中包含日志记录和返回特定错误码的逻辑。
画面 2: 展示 Apollo 配置中心登录页面，用于配置服务。
画面 3: 展示用户登录流程的时序图，包含“用户中心服务”、“统一用户”、“验证服务”等组件间的交互。
画面 4: 展示 `AccountController` 中的 `register` 和 `login` 方法，用于处理用户注册和登录请求。
画面 5: 展示 Apollo 配置中心登录页面。
画面 6: 展示 `AccountController` 中的 `login` 方法，调试时显示 `accountLoginDTO` 对象的值。
画面 7: 展示 `CommonErrorCode` 类中的错误码定义，其中 `E_999995` 对应“统一账户服务被熔断”。
画面 8: 展示 `IntegrationUserDetailsAuthenticationHandler` 类中的 `authentication` 方法，用于处理用户认证。
画面 9: 展示 Apollo 配置中心登录页面，网络请求返回错误。
画面 10: 展示 `AccountController` 中的 `login` 方法，调试时显示日志信息。
画面 11: 展示 `AccountController` 中的 `login` 方法，调试时显示日志信息。
画面 12: 展示 `AccountController` 中的 `login` 方法，调试时显示日志信息。
画面 13: 展示 `IntegrationUserDetailsAuthenticationHandler` 类中的 `authentication` 方法，调试时显示 `accountLoginDTO` 对象的值。
画面 14: 展示用户登录流程的时序图，包含“用户中心服务”、“统一用户”、“验证服务”等组件间的交互。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@Component
@Slf4j
class AccountFallbackFactory implements FallbackFactory<AccountApiAgent> {
    @Override
    public AccountApiAgent create(Throwable cause) {
        return new AccountApiAgent() {
            @Override
            public RestResponse<AccountDTO> login(AccountLoginDTO accountLoginDTO) {
                //记录错误原因
                log.info("Fallback; reason was: ", cause);
                //降级返回
                return new RestResponse<>(CommonErrorCode.E_999995.getCode(),
                        CommonErrorCode.E_999995.getDesc());
            }
        };
    }
}
```

画面 4:
```java
@PostMapping(value = "/accounts/session")
@Override
public RestResponse<AccountDTO> login(@RequestBody AccountLoginDTO accountLoginDTO) {
    return RestResponse.success(accountService.login(accountLoginDTO));
}
```

画面 6:
```java
accountLoginDTO = AccountLoginDTO{username='15378791981', mobile='15378791981', password='15378791981', domain=''}
```

画面 7:
```java
E_100105(100.05, "ID格式不正确或超出Long存储范围"),
E_100106(100.06, "请求失败"),
E_999991(99991, "调用微服务-交易中心 被熔断"),
E_999992(99992, "调用微服务-一些服务 被熔断"),
E_999993(99993, "调用微服务-用户服务 被熔断"),
E_999994(99994, "调用微服务-资源服务 被熔断"),
E_999995(99995, "调用微服务-统一账户服务 被熔断"),
E_999996(99996, "调用微服务-存管代理服务 被熔断"),
```

画面 8:
```java
public UniRestDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token) {
    //从客户端获取
    String username = token.getName();
    if (StringUtils.isBlank(username)) {
        throw new BadCredentialsException("账户为空");
    }
    if (token.getCredentials() == null) {
        throw new BadCredentialsException("密码为空");
    }
    String presentedPassword = token.getCredentials().toString();
    //远程调用统一账户服务，进行用户密码校验
```

画面 13:
```java
accountLoginDTO = AccountLoginDTO{username='15378791981', mobile='15378791981', password='15378791981', domain=''}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3:
- 流程图标题：用户登录流程
- 组件：浏览器/App → 用户中心服务 → 统一用户 → 验证服务
- 交互：
  1. 用户输入手机号
  2. 获取验证码
  3. 获取短信验证码
  4. 发送短信
  5. 获取短信验证码
  6. 通过此次短信校验
  7. 校验手机号是否已注册
  8. 返回校验结果
  9. 返回校验结果
  10. 返回注册结果
  11. 未注册
  12. 发起注册请求
  13. 账户注册
  14. 保存注册信息
  15. 返回注册结果
  16. 用户登录
  17. 返回登录结果
  18. 登录成功
  19. 返回登录结果

画面 14:
- 流程图标题：用户登录流程
- 组件：浏览器/App → 用户中心服务 → 统一用户 → 验证服务
- 交互：
  1. 用户输入手机号
  2. 获取验证码
  3. 获取短信验证码
  4. 发送短信
  5. 获取短信验证码
  6. 通过此次短信校验
  7. 校验手机号是否已注册
  8. 返回校验结果
  9. 返回校验结果
  10. 返回注册结果
  11. 未注册
  12. 发起注册请求
  13. 账户注册
  14. 保存注册信息
  15. 返回注册结果
  16. 用户登录
  17. 返回登录结果
  18. 登录成功
  19. 返回登录结果

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
