# 画面线理解：day06-2-部署银行存管系统

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-15 部署银行存管系统
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-15 部署银行存管系统\day06-2-部署银行存管系统_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:13, 02:17, 03:23, 04:25, 05:05, 05:46, 06:22, 07:07, 07:27, 07:52, 08:09, 09:23, 09:41, 10:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:13:13

1) 这一组画面整体在讲银行存管系统的开发与部署，包括架构设计、数据库初始化、服务启动、接口测试及配置管理。

2) 按时间顺序列出每张画面的要点：
画面1：展示系统架构图，包含“浏览器APP”、“用户中心”、“存管代理服务”、“存管系统”、“开户银行”等模块，以及各模块间的数据流向（如1.1生成开户请求数据、1.3准备开户参数、1.4生成交易记录等）。
画面2：在P2P项目中打开并查看SQL文件`wanxindepository-init.sql`，内容为创建`bank_card_detail`和`bank_user`表的语句。
画面3：在IntelliJ IDEA中打开项目`wanxindepository`，弹出“Open File or Project”对话框，显示项目文件夹结构。
画面4：在Apollo配置中心网页界面，展示“wanxindepository”项目及其关联服务（如consumer-service、account-service等）。
画面5：在IntelliJ IDEA终端中启动`wanxindepositoryServer`，日志显示Spring Boot启动成功，但未找到元数据服务器地址。
画面6：在IntelliJ IDEA中查看`BankCardServiceTest`测试类，代码中设置银行卡请求参数并调用`createBankCard`方法。
画面7：在IntelliJ IDEA中查看`BankCardServiceImpl.java`，展示`createBankCard`方法的实现，包括用户和银行卡信息的创建与保存。
画面8：在IntelliJ IDEA终端中运行测试，日志显示Spring Boot启动失败，因未设置环境变量。
画面9：在IntelliJ IDEA终端中运行测试，日志显示Apollo配置同步失败，无法连接元数据服务器。
画面10：在IntelliJ IDEA终端中运行测试，日志显示Spring Boot启动成功，开始加载配置。
画面11：在IntelliJ IDEA终端中运行测试，日志显示数据库插入操作成功，执行了`INSERT INTO bank_card`和`INSERT INTO bank_card_details`语句。
画面12：在Word文档中查看“银行存管系统接口说明”，内容包括“网关接口”部分，描述请求通过浏览器跳转到网关页面，以及请求参数格式约定。
画面13：在Word文档中查看“银行存管系统接口说明”，内容包括“网关接口”部分，展示请求参数表（如serviceName、platformNo、reqData等）和“异步通知（审核结果）”参数表（如userNo、status等）。
画面14：在Word文档中查看“银行存管系统部署指南”，内容包括“1. 初始化数据库”（执行`wanxindepository-init.sql`）、“2. 导入项目”（使用IDEA打开项目并下载jar）、“3. 设置启动参数并启动项目”（-Denv=dev -Dapollo.cluster=DEFAULT -Dserver.port=55010），并注明Apollo配置已在第一章生成。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2 SQL：
```sql
CREATE TABLE bank_card_detail (
  ID BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  BANK_CARD_ID BIGINT(20) DEFAULT NULL COMMENT '银行卡ID',
  CHANGE_TYPE TINYINT(4) DEFAULT NULL COMMENT '变动类型',
  MONEY DECIMAL(19,2) DEFAULT NULL COMMENT '变动金额',
  BALANCE DECIMAL(19,2) DEFAULT NULL COMMENT '当前余额',
  CREATE_DATE DATETIME DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='银行卡明细表';

DROP TABLE IF EXISTS `bank_user`;

CREATE TABLE bank_user (
  ID BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  FILLNAME VARCHAR(50) NOT NULL COMMENT '真实姓名',
  MOBILE VARCHAR(11) NOT NULL COMMENT '手机号',
  PASSWORD VARCHAR(32) NOT NULL COMMENT '密码',
  USER_TYPE TINYINT(4) NOT NULL COMMENT '用户类型',
  CREATE_DATE DATETIME DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';
```

画面6 Java代码：
```java
bankCardRequest.setFullName(ChineseNameGenerator.getInstance().generate());
bankCardRequest.setNumber(ChineseICardNumberGenerator.getInstance().generate());
bankCardRequest.setMobile(ChineseMobileNumberGenerator.getInstance().generateAll());
BankCard bankCard = BankCardNumberGenerator.getInstance().generateAll();
bankCardRequest.setBalance(new BigDecimal(100000));
bankCardRequest.setCardType(1);
bankCardRequest.setPassword("888888");
BankCard bankCard = BankCardNumberGenerator.getInstance().generateAll();
```

画面7 Java代码：
```java
@Override
@Transactional
public String createBankCard(BankCardRequest bankCardRequest) {
    BankUser bankUser = bankUserService.getBankCardRequest.getFullName(), bankCardRequest.getCardNumber());
    if (bankUser == null) {
        bankUser = new BankUser();
        BeanUtils.copyProperties(bankCardRequest, bankUser);
        bankUserService.save(bankUser);
    }
    BankCard bankCard = getByCardNumber(bankCardRequest.getCardNumber());
    if (bankCard != null) {
        throw new BusinessException(LocalReturnCode.E_20010);
    }
    bankCard = new BankCard();
    BeanUtils.copyProperties(bankCardRequest, bankCard);
    bankCard.setCardType(bankCardRequest.getCardType());
    save(bankCard);
    return bankCard.getCardNumber();
}
```

画面12 表格数据：
| 参数名称 | 必填 | 参数说明 |
|----------|------|----------|
| serviceName | Y | 端口名称 |
| platformNo | Y | 平台编号 |
| reqData | Y | 业务数据报文，JSON 格式 |

画面13 表格数据：
| 参数名称 | 必填 | 类型 | 长度 | 参数说明 |
|----------|------|------|------|----------|
| userNo | Y | S | 50 | 平台用户编号 |
| status | Y | E | 50 | 【交易状态】 |

画面14 配置：
```
-Denv=dev -Dapollo.cluster=DEFAULT -Dserver.port=55010
```

4) PPT标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：架构图，模块包括“浏览器APP”、“用户中心”、“存管代理服务”、“存管系统”、“开户银行”，数据流向如下：
- “浏览器APP” → “用户中心”（1.1生成开户请求数据）
- “用户中心” → “存管代理服务”（1.3准备开户参数）
- “存管代理服务” → “存管系统”（1.4生成交易记录）
- “存管系统” → “开户银行”（1.5保存交易记录）
- “开户银行” → “存管系统”（1.6返回开户结果）
- “存管系统” → “用户中心”（1.7返回开户数据）
- “用户中心” → “浏览器APP”（1.8返回开户结果）

画面12：表格数据（见上文）。
画面13：表格数据（见上文）。
画面14：部署指南（见上文）。

5) 无。
