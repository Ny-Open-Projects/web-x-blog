# 画面线理解：day04-15-认证(登录)功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-8 实现认证功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-8 实现认证功能\day04-15-认证(登录)功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:45, 06:40, 09:33, 10:59, 13:31, 14:25, 15:18, 16:15, 17:45, 19:45, 21:26, 22:12, 23:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:51:06

1) 这一组画面整体在讲什么（一句话）：
讲解如何在 UAA 工程中实现自定义的用户认证处理器，通过重写 authentication 方法调用账户服务完成登录认证，并处理异常和返回用户信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 2: 在 IDE 中打开 `IntegrationUserDetailsAuthenticationHandler.java` 文件，高亮显示 `public UnifiedUserDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token)` 方法。
画面 3: 展示 PPT 页面，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 4: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，光标位于 `token` 变量上，显示其类型为 `UsernamePasswordAuthenticationToken`。
画面 5: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `public static boolean isBlank(String str)` 方法，并有注释说明空白字符定义。
画面 6: 在 IDE 中，`AccountController.java` 文件中，光标位于 `AccountController` 类上。
画面 7: 在 IDE 中，`AccountController.java` 文件中，光标位于 `AccountController` 类上。
画面 8: 在 IDE 中，`AccountController.java` 文件中，光标位于 `AccountController` 类上。
画面 9: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `public UnifiedUserDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token)` 方法。
画面 10: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，光标位于 `AccountAgent.login(accountLoginDTO)` 方法调用处。
画面 11: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `throw new BadCredentialsException("登录失败");` 语句。
画面 12: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));` 语句。
画面 13: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，光标位于 `AccountLoginDTO` 类的 `setMobile()` 方法上。
画面 14: 在 IDE 中，`IntegrationUserDetailsAuthenticationHandler.java` 文件中，高亮显示 `UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));` 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
public class IntegrationUserDetailsAuthenticationHandler {
    // 认证处理
    @Param domain 用户域，如前端用户、后端用户等
    @Param authenticationType 认证类型，如密码认证、短信认证等
    @Param token
    @Return
    public UnifiedUserDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token) {
        return null;
    }
    private UnifiedUserDetails getUserDetails(String username) {
        Map<String, UnifiedUserDetails> userDetailsMap = new HashMap<>();
        userDetailsMap.put("admin", new UnifiedUserDetails("admin", "111111", AuthorityUtils.createAuthorityList("ROLE_ADMIN")));
        userDetailsMap.put("zufan", new UnifiedUserDetails("zufan", "111111", AuthorityUtils.createAuthorityList("ROLE_ADMIN")));
        return userDetailsMap.get(username);
    }
}
```

画面 4:
```java
public class IntegrationUserDetailsAuthenticationHandler {
    // 认证处理
    @Param domain 用户域，如前端用户、后端用户等
    @Param authenticationType 认证类型，如密码认证、短信认证等
    @Param token
    @Return
    public UnifiedUserDetails authentication(String domain, String authenticationType, UsernamePasswordAuthenticationToken token) {
        // 从客户端获取数据
        String username = token.getPrincipal();
        if (StringUtils.isBlank(username)) {
            throw new BadCredentialsException("用户名为空");
        }
        if (token.getCredentials() == null) {
            throw new BadCredentialsException("密码为空");
        }
        // 2. 调用统一账户服务，进行账户密码校验
        AccountLoginDTO accountLoginDTO = new AccountLoginDTO();
        accountLoginDTO.setDomain(domain);
        accountLoginDTO.setUsername(username);
        accountLoginDTO.setPassword(token.getCredentials().toString());
        AccountAgent accountAgent = (AccountAgent) ApplicationContextHolder.getBean(AccountAgent.class);
        RestResponse<AccountDTO> restResponse = accountAgent.login(accountLoginDTO);
        // 3. 异常处理
        if (restResponse.getCode() != 0) {
            throw new BadCredentialsException("登录失败");
        }
        // 4. 登录成功，把用户数据封装到UnifiedUserDetails对象中
        UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), token.getCredentials().toString(), AuthorityUtils.createAuthorityList("ROLE_ADMIN"));
        unifiedUserDetails.setMobile(restResponse.getResult().getMobile());
        return unifiedUserDetails;
    }
}
```

画面 5:
```java
public static boolean isBlank(String str) {
    return str == null || str.trim().length() == 0;
}
```

画面 6:
```java
// 2. 调用统一账户服务，进行账户密码校验
AccountLoginDTO accountLoginDTO = new AccountLoginDTO();
accountLoginDTO.setDomain(domain);
accountLoginDTO.setUsername(username);
accountLoginDTO.setPassword(presentedPassword);
AccountAgent accountAgent = (AccountAgent) ApplicationContextHolder.getBean(AccountAgent.class);
RestResponse<AccountDTO> restResponse = accountAgent.login(accountLoginDTO);
// 3. 异常处理
if (restResponse.getCode() != 0) {
    throw new BadCredentialsException("登录失败");
}
// 4. 登录成功，把用户数据封装到UnifiedUserDetails对象中
UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));
unifiedUserDetails.setMobile(restResponse.getResult().getMobile());
return unifiedUserDetails;
```

画面 10:
```java
// 2. 调用统一账户服务，进行账户密码校验
AccountLoginDTO accountLoginDTO = new AccountLoginDTO();
accountLoginDTO.setDomain(domain);
accountLoginDTO.setUsername(username);
accountLoginDTO.setPassword(presentedPassword);
AccountAgent accountAgent = (AccountAgent) ApplicationContextHolder.getBean(AccountAgent.class);
RestResponse<AccountDTO> restResponse = accountAgent.login(accountLoginDTO);
// 3. 异常处理
if (restResponse.getCode() != 0) {
    throw new BadCredentialsException("登录失败");
}
// 4. 登录成功，把用户数据封装到UnifiedUserDetails对象中
UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));
unifiedUserDetails.setMobile(restResponse.getResult().getMobile());
return unifiedUserDetails;
```

画面 12:
```java
// 4. 登录成功，把用户数据封装到UnifiedUserDetails对象中
UnifiedUserDetails unifiedUserDetails = new UnifiedUserDetails(restResponse.getResult().getUsername(), presentedPassword, AuthorityUtils.createAuthorityList("ROLE_ADMIN"));
unifiedUserDetails.setMobile(restResponse.getResult().getMobile());
return unifiedUserDetails;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 3: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 6: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 9: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 10: PPT 标题为“UAA服务架构篇”，内容为“2. 注意检查启动类上的注解”和“3. 在UAA工程的domain包中找到IntegrationUserDetailsAuthenticationHandler类，并实现其中的authentication方法”。
画面 11: PPT
