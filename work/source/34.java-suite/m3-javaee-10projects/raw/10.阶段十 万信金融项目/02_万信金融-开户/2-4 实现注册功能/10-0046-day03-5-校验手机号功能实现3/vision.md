# 画面线理解：day03-5-校验手机号功能实现3

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-5-校验手机号功能实现3_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:01, 00:34, 01:22, 01:55, 03:00, 03:56, 05:22, 06:19, 07:07, 08:25, 09:36, 12:13, 13:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:30:53

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 MyBatis-Plus 实现手机号和验证码的校验功能，包括配置、接口定义、服务实现和控制器编写。

2) 按时间顺序列出每张画面的要点：
画面1：展示 PDF 文档中关于修改 Apollo 配置和 Mapper 接口的说明，以及 MyBatis-Plus 的依赖配置。
画面2：展示 AccountService 接口定义，包含 getSMSCode 方法。
画面3：在 AccountService 接口中添加 extends RuntimeException。
画面4：在 AccountServiceImpl 类中定义 getSMSCode 方法，调用 SmsService。
画面5：在 AccountService 接口中添加 checkMobile 方法。
画面6：在 AccountServiceImpl 类中实现 checkMobile 方法，调用 smsService.verifySmsCode。
画面7：在 AccountServiceImpl 类中完成 checkMobile 方法的实现，使用 QueryWrapper 进行数据库查询。
画面8：展示 PDF 文档中 MyBatis-Plus 的 Wrapper 类结构，重点是 AbstractLambdaWrapper。
画面9：展示数据库表 p2p_account 的创建语句，包含字段定义和字符集设置。
画面10：在 AccountServiceImpl 类中使用 QueryWrapper 进行条件查询。
画面11：在 AccountServiceImpl 类中使用 LambdaQueryWrapper 进行条件查询。
画面12：在 AccountServiceImpl 类中使用 LambdaQueryWrapper 进行条件查询，使用 getMobile 方法。
画面13：在 AccountController 类中定义 checkMobile 方法，使用 @PathVariable 注解接收参数并调用 service 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<dependency>
    <groupId>com.baidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
</dependency>
```
画面2：
```java
package cn.itcast.wanxing2p.account.service;

import cn.itcast.wanxing2p.common.domain.RestResponse;

public interface AccountService {
    RestResponse getSMSCode(String mobile);
}
```
画面3：
```java
public interface AccountService extends RuntimeException {
    RestResponse getSMSCode(String mobile);
}
```
画面4：
```java
@Service
public class AccountServiceImpl extends AccountService {
    @Autowired
    private SmsService smsService;

    @Override
    public RestResponse getSMSCode(String mobile) {
        return smsService.getSMSCode(mobile);
    }
}
```
画面5：
```java
public interface AccountService extends AccountService {
    RestResponse getSMSCode(String mobile);
    Integer checkMobile(String mobile, String key, String code);
}
```
画面6：
```java
@Service
public class AccountServiceImpl extends ServiceImpl<AccountMapper, Account> implements AccountService {
    @Autowired
    private SmsService smsService;

    @Override
    public RestResponse getSMSCode(String mobile) {
        return smsService.getSMSCode(mobile);
    }

    @Override
    public Integer checkMobile(String mobile, String key, String code) {
        smsService.verifySmsCode(key, code);
    }
}
```
画面7：
```java
@Override
public Integer checkMobile(String mobile, String key, String code) {
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.eq("mobile", mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
```
画面8：
```java
Wrapper(com.baidou.mybatplus.core.condition)
    AbstractWrapper(com.baidou.mybatplus.core.condition)
    AbstractLambdaWrapper(com.baidou.mybatplus.core.condition)
    LambdaQueryChainWrapper(com.baidou.mybatplus.core.condition)
    QueryWrapper(com.baidou.mybatplus.core.condition)
    UpdateWrapper(com.baidou.mybatplus.core.condition)
```
画面9：
```sql
CREATE TABLE `t_user` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `user_name` VARCHAR(20) NOT NULL COMMENT '用户名',
  `password` VARCHAR(20) NOT NULL COMMENT '密码',
  `name` VARCHAR(30) NOT NULL COMMENT '姓名',
  `age` INT(11) DEFAULT NULL COMMENT '年龄',
  `email` VARCHAR(50) DEFAULT NULL COMMENT '邮箱',
  `create_time` DATETIME DEFAULT NULL COMMENT '创建时间',
  `update_time` DATETIME DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
```
画面10：
```java
@Override
public Integer checkMobile(String mobile, String key, String code) {
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.eq("mobile", mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
```
画面11：
```java
@Override
public Integer checkMobile(String mobile, String key, String code) {
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.lambda().eq(Wrapper::getMobile, mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
```
画面12：
```java
@Override
public Integer checkMobile(String mobile, String key, String code) {
    QueryWrapper<Account> wrapper = new QueryWrapper<>();
    wrapper.lambda().eq(Account::getMobile, mobile);
    int count = count(wrapper);
    return count > 0 ? 1 : 0;
}
```
画面13：
```java
@GetMapping("/checkMobile")
public RestResponse checkMobile(@PathVariable String mobile, @PathVariable String key, @PathVariable String code) {
    return accountService.checkMobile(mobile, key, code);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：PPT 标题为“5.1 比较操作”，下方列出比较操作符：eq（等于）、ne（不等于）、gt（大于）、ge（大于等于）、lt（小于）、le（小于等于）。
画面9：无 PPT 标题，仅展示 SQL 语句。

5) 不要评价画面美观，不要输出与课程无关的内容。
