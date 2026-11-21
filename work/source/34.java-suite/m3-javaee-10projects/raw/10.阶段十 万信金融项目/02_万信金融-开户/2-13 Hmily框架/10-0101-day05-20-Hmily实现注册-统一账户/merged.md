# day05-20-Hmily实现注册-统一账户

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-20-Hmily实现注册-统一账户_【海量资源尽在 666java.com】.mp4
- 时长 5分44秒（音频 344s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 事务发起方这边代码咱们搞定之后呢接下来紧接着咱要搞定哪一方啊对事务参与方事务参与方呢咱前面分析的就是统一账户中心啊可抗的Service这边其实要做的事跟呃事务发起方那边很多地方都是对一样的而且呢事务参与方一般他要比事务发起方要还要少一些啊少什么呀
[00:28] 那参议方这边没有什么呀非养生掉肉吗对不对咱看一看讲义都需要做哪些事首先是把还是搞定配置吧对不对我看到Service这边你要加上什么呀他们里相关的配置那咱还得去Apollo当中去Apollo当中呢我们要找到哪个是这个对吧统一账号服务我们也要把还没那个配置给他关联进来关联公共的那次选择那个谁呢还没对提交
[00:59] 然后呢我们回到这个项目当中我们展开看一下这里边你要注意的就是你要想一想这里边对于事务的参与方来说这里边的配置有没有需要改想想啊就这几个大家看一看有没有需要改的事务参与方有没有需要修改覆盖的有吧这个是不是就需要修改覆盖啊对我们说了这个触表是它是事务参与是事务的发行方而我们这边现在是事务的什么呀
[01:29] 餐饮房这应该改成什么呀然后再看看别的地方有没有需要改的别的就没有了这个数据库我们可以用同一个日志可以让他存到一个库里边这无所谓关键就是这个所以我们点击这要覆盖一下对吧把这个处给它改成对然后点击什么呀对提交然后还要干什么发布对没错这是配置咱就搞定了
[02:02] 那将来如果说在P2P项目当中别的地方也要用到Harmony那是不是都是这么来操作的对不对那接下来跟刚才一样我们需要在Configure包当中是不是新增一个那个配置类是不是那我们还是去资料里边找到这个配置类Ctrl C这次我们是不是要粘到Account这家了找到这个Configure包Ctrl V粘过来看一眼没有报错就OK了
[02:34] 再往下启动内上是不是要加这个扫描项了是不是我能复制一下找到account的它的启动内在这个地方加进来就可以了那一定要注意检查这个路径检查这个路径看看跟你这边的是否什么样对照这个是需要大家特别细心的一件事情启动内搞定之后接下来是不是修改注册的那个代码
[03:10] 因为咱们当时也实现了这个Alcantara这边是不是也实现了有保存这个功能就是保存账号的信息你看这里边原来的代码里边原来代码这儿看不到对吧那咱一会再说这里边也是找到原来注册的方法上面是不是要加Hemily注解同时再增加Confirm这个代码还有什么Cancel这个代码都差不多那咱接下来找一找谁Alcantara这边的Service对不对
[03:40] 都在业务层找到他找到原来的注册你看这就是注册你看这里边他也走了一个什么呀sale方法所以说这样呢我还是需要加上at还没注解这里边要配置两个方法一个叫conform发明一会再补啊还有一个叫cancel对啊这里边做的就是保存嘛
[04:10] 然后这两个方法相来说也比较简单啊我们给他先粘过来就不再时间关系就不再敲了啊粘过来之后稍微改一下吧这个呃这里边这个log呢我们也是在这加上了一个34g就ok了好咱接下来大概看一下这两个方法吧嗯然后呢大家注意一下啊这块东西咱暂时用不到先不用管他现在删了呃这两个方法代码也非常简单大家看一眼
[04:57] confirm里边我们目前仍然是什么事都不需要做然后cancel这边要注意了cancel这边要做的事其实跟注册这边做的事是不是相反这边保存那这就要做什么删除其实这就是一个回滚操作因为出问题了出问题你刚才保存的数据在这就要被删除掉回滚一下所以说这是down remove方法删除了刚才保存的信息这是需要大家注意的然后我们把
[05:26] 这两个方法的名字加到这里就OK了加到这里啊配置一下好这样就搞定了那这边代码咱应该也整完了吧对不对整完一会咱进行功能测试就OK了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 Apollo 配置中心配置 Hmily 事务管理器，并修改账户服务代码以支持事务的确认与取消操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PPT 页面，内容为“4.3.2 事务参与方：account-Service”，并列出需要执行的步骤，包括修改 Apollo 中的配置、修改 config 包中的 Hmily 配置类、以及在启动类上添加扫描包注解。
画面 2: 浏览器访问 Apollo 配置中心的空白页面，URL 为 localhost:8070/config.html#/appid=account-Service。
画面 3: Apollo 配置中心界面，显示了多个配置项，包括 micro_service.spring-boot-http、micro_service.spring-Eureka、micro_service.spring-hystrix、micro_service.spring-ribbon、micro_service.spring-boot-druid。
画面 4: Apollo 配置中心的公共配置页面，显示了多个 Hmily 相关的配置项，包括 org.dromara.hmily.sotilber、org.dromara.hmily.retry、org.dromara.hmily.repositorySupport、org.dromara.hmily.started、org.dromara.hmily.h2.jdbc.Driver、org.dromara.hmily.h2.jdbc.config.url、org.dromara.hmily.h2.jdbc.config.username、org.dromara.hmily.h2.jdbc.config.password。
画面 5: IntelliJ IDEA 中打开的项目结构，显示了 wanning2p_apollo 项目下的多个模块，包括 wanning2p-account-Service、wanning2p-api、wanning2p-common、wanning2p-consumer-Service、wanning2p-discover-server、wanning2p-gateway-server、wanning2p-uaa-Service。
画面 6: IntelliJ IDEA 中打开的项目结构，显示了 wanning2p-account-Service 模块下的 src/main/java 和 src/main/resources 目录结构。
画面 7: 展示了课程 PPT 页面，内容为“4.3.2 事务参与方：account-Service”，并列出需要执行的步骤，包括修改 Apollo 中的配置、修改 config 包中的 Hmily 配置类、以及在启动类上添加扫描包注解。
画面 8: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 register 方法的代码，包括设置用户名、密码、手机号、是否启用、域名等属性，并调用 save 方法保存账户。
画面 9: 展示了课程 PPT 页面，内容为“4.4 功能测试”，并列出用户中心服务和统一账户服务执行成功，统一账户服务执行失败，用户中心服务回滚成功。
画面 10: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 confirmRegister 方法的代码，包括更新账户状态为“IN”，并调用 save 方法保存账户。
画面 11: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 cancelRegister 方法的代码，包括删除账户。
画面 12: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 register 方法的代码，包括设置用户名、密码、手机号、是否启用、域名等属性，并调用 save 方法保存账户。
画面 13: IntelliJ IDEA 中打开的 AccountServiceImpl.java 文件，显示了 register 方法的代码，包括设置用户名、密码、手机号、是否启用、域名等属性，并调用 save 方法保存账户。
画面 14: 展示了课程 PPT 页面，内容为“4.4 功能测试”，并列出用户中心服务和统一账户服务执行成功，统一账户服务执行失败，用户中心服务回滚成功。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
(1) 在 Apollo 中，为 account-Service 项目关联 micro_service.spring-cloud-hmily 名称空间，并修改 org.dromara.hmily.started=false。
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
画面 1: PPT 标题为“4.3.2 事务参与方：account-Service”，并列出需要执行的步骤。
画面 7: PPT 标题为“4.3.2 事务参与方：account-Service”，并列出需要执行的步骤。
画面 9: PPT 标题为“4.4 功能测试”，并列出用户中心服务和统一账户服务执行成功，统一账户服务执行失败，用户中心服务回滚成功。
画面 14: PPT 标题为“4.4 功能测试”，并列出用户中心服务和统一账户服务执行成功，统一账户服务执行失败，用户中心服务回滚成功。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

