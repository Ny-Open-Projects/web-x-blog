# 画面线理解：day05-20-Hmily实现注册-统一账户

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-20-Hmily实现注册-统一账户_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:47, 01:02, 01:53, 02:19, 02:44, 03:08, 03:45, 04:17, 04:30, 04:46, 05:07, 05:26, 05:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:10:49

1) 这一组画面整体在讲什么（一句话）：
在 Apollo 配置中心配置 Hmily 事务管理器，并修改账户服务代码以支持事务的确认与取消操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PPT 页面，内容为“4.3.2 事务参与方：account-service”，并列出需要执行的步骤，包括修改 Apollo 中的配置、修改 config 包中的 Hmily 配置类、以及在启动类上添加扫描包注解。
画面 2: 浏览器访问 Apollo 配置中心的空白页面，URL 为 localhost:8070/config.html#/appid=account-service。
画面 3: Apollo 配置中心界面，显示了多个配置项，包括 micro_service.spring-boot-http、micro_service.spring-eureka、micro_service.spring-hystrix、micro_service.spring-ribbon、micro_service.spring-boot-druid。
画面 4: Apollo 配置中心的公共配置页面，显示了多个 Hmily 相关的配置项，包括 org.dromara.hmily.sotilber、org.dromara.hmily.retry、org.dromara.hmily.repositorySupport、org.dromara.hmily.started、org.dromara.hmily.h2.jdbc.Driver、org.dromara.hmily.h2.jdbc.config.url、org.dromara.hmily.h2.jdbc.config.username、org.dromara.hmily.h2.jdbc.config.password。
画面 5: IntelliJ IDEA 中打开的项目结构，显示了 wanning2p_apollo 项目下的多个模块，包括 wanning2p-account-service、wanning2p-api、wanning2p-common、wanning2p-consumer-service、wanning2p-discover-server、wanning2p-gateway-server、wanning2p-uaa-service。
画面 6: IntelliJ IDEA 中打开的项目结构，显示了 wanning2p-account-service 模块下的 src/main/java 和 src/main/resources 目录结构。
画面 7: 展示了课程 PPT 页面，内容为“4.3.2 事务参与方：account-service”，并列出需要执行的步骤，包括修改 Apollo 中的配置、修改 config 包中的 Hmily 配置类、以及在启动类上添加扫描包注解。
画面 8: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 register 方法的代码，包括设置用户名、密码、手机号、是否启用、域名等属性，并调用 save 方法保存账户。
画面 9: 展示了课程 PPT 页面，内容为“4.4 功能测试”，并列出用户中心服务和统一账户服务执行成功，统一账户服务执行失败，用户中心服务回滚成功。
画面 10: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 confirmRegister 方法的代码，包括更新账户状态为“IN”，并调用 save 方法保存账户。
画面 11: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 cancelRegister 方法的代码，包括删除账户。
画面 12: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 register 方法的代码，包括设置用户名、密码、手机号、是否启用、域名等属性，并调用 save 方法保存账户。
画面 13: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 register 方法的代码，包括设置用户名、密码、手机号、是否启用、域名等属性，并调用 save 方法保存账户。
画面 14: 展示了课程 PPT 页面，内容为“4.4 功能测试”，并列出用户中心服务和统一账户服务执行成功，统一账户服务执行失败，用户中心服务回滚成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
(1) 在 Apollo 中，为 account-service 项目关联 micro_service.spring-cloud-hmily 名称空间，并修改 org.dromara.hmily.started=false。
(3) 启动类上添加 org.dromara.hmily 的扫描项
@SpringBootApplication(scanBasePackages = {"org.dromara.hmily", "cn.ictcast.wanning2p.account"})
画面 7:
(4) 修改 AccountServiceImpl 代码，注册 Try, Confirm, Cancel
@Override
@Hmily(confirmMethod = "confirmRegister", cancelMethod = "cancelRegister")
public AccountDTO register(AccountRegisterDTO registerDTO) {
画面 8:
public RestResponse getSMSCode(String mobile) { return smsService.getSMSCode(mobile); }
@Override
public Integer checkMobile(String mobile, String code) {
    smsService.twiFCode(ber, code);
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.eq("mobile", mobile);
    wrapper.lambda().eq(Account::getMobile, mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
@Override
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUsername(accountRegisterDTO.getUsername());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setPassword(PasswordUtil.generate(accountRegisterDTO.getPassword()));
    if (smsEnable) {
        account.setPassword(PasswordUtil.generate(accountRegisterDTO.getMobile()));
    }
    account.setDomain("c");
    save(account);
    return convertAccountEntityToDTO(account);
}
画面 10:
public void confirmRegister(AccountRegisterDTO registerDTO) {
    log.info("execute confirmRegister");
    update(Wrappers.<Account>lambdaUpdate().eq(Account::getUsername, registerDTO.getUsername()).set(Account::getStatus, StatusCode.STATUS_IN.getCode()));
}
public void cancelRegister(AccountRegisterDTO registerDTO) {
    log.info("execute cancelRegister");
    remove(Wrappers.<Account>lambdaQuery().eq(Account::getUsername, registerDTO.getUsername()));
}
画面 12:
public void confirmRegister(AccountRegisterDTO registerDTO) {
    log.info("execute confirmRegister");
    update(Wrappers.<Account>lambdaUpdate().eq(Account::getUsername, registerDTO.getUsername()).set(Account::getStatus, StatusCode.STATUS_IN.getCode()));
}
public void cancelRegister(AccountRegisterDTO registerDTO) {
    log.info("execute cancelRegister");
    remove(Wrappers.<Account>lambdaQuery().eq(Account::getUsername, registerDTO.getUsername()));
}
画面 13:
public void confirmRegister(AccountRegisterDTO registerDTO) {
    log.info("execute confirmRegister");
    update(Wrappers.<Account>lambdaUpdate().eq(Account::getUsername, registerDTO.getUsername()).set(Account::getStatus, StatusCode.STATUS_IN.getCode()));
}
public void cancelRegister(AccountRegisterDTO registerDTO) {
    log.info("execute cancelRegister");
    remove(Wrappers.<Account>lambdaQuery().eq(Account::getUsername, registerDTO.getUsername()));
}
画面 14:
4.4 功能测试
- 用户中心服务和统一账户服务都执行成功。
- 统一账户服务执行失败，用户中心服务回滚成功。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“4.3.2 事务参与方：account-service”，并列出需要执行的步骤。
画面 7: PPT 标题为“4.3.2 事务参与方：account-service”，并列出需要执行的步骤。
画面 9: PPT 标题为“4.4 功能测试”，并列出用户中心服务和统一账户服务执行成功，统一账户服务执行失败，用户中心服务回滚成功。
画面 14: PPT 标题为“4.4 功能测试”，并列出用户中心服务和统一账户服务执行成功，统一账户服务执行失败，用户中心服务回滚成功。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
