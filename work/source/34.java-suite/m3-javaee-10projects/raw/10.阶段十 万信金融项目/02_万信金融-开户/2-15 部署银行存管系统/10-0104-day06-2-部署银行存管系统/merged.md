# day06-2-部署银行存管系统

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-15 部署银行存管系统
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-15 部署银行存管系统\day06-2-部署银行存管系统_【海量资源尽在 666java.com】.mp4
- 时长 10分45秒（音频 645s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们整体了解了一下开户这个业务的需求分析以及他执行的一个详细的一个流程对吧这里呢我们再次给大家强调一下这个时序图就这个图啊非常非常重要那么这个图里边呢具体显示了咱开户这个业务都涉及到哪些系统哪些微服务以及他们这个之间的关系包括这个很详细的一些什么呀对运行的一个步骤
[00:30] 所以这个图至关重要那么大家在开发过程当中呢一定要注意去参考这个图那咱接下来的话要做一个准备工作啊什么准备工作呢大家看这儿这个地方我们说咱这个开户过程当中呢是不是涉及到一个银行那边的系统比如这个存款系统是吧那么这个银行存款系统呢不归咱管也不需要咱开发是不是它是银行那边的系统也部署运行在银行那边
[00:58] 但是呢咱在开发P2P的时候是不是要要用它要访问它对吧要调用它这边的接口然后一起呢完成这个开户这个功能所以说呢接下来我们要做的一个准备工作呢就是在咱们自己的电脑上把这个银行存款系统给它部署好给它运行起来这个系统是我们直接停为大家我刚才说了这个东西是银行那边的也不需要人开发嘛我们就直接停为大家那我们就是说直接去资料文件夹里边
[01:29] 这里边有个银行存款系统这里边有我的文件PDF文件直接呢就是参考这个进行部署运行就行那这呢我已经打开了你看银行存款系统部署指南对吧首先我们要做的第一件事就是出入化数据库啊银行存款系统它肯定也有数据库嘛它也要操作管理一堆数据所以咱先把这个数据库环境先搞定这呢直接有一个脚本我们一运行就完事很简单在这
[02:00] 我们把它直接拽到这个这个速费样里边你也不用管这里边代码我们直接运行就行那稍等片刻啊这里边的话你看他是不是创建了一个数据库吗对不对然后这里边也有一堆表一堆一堆的表这里边呢都是银行那边的用到的一些表但是呢我们的P2P这个平台要去也要去使用啊要去交互所以我们稍等片刻啊他正在创建数据库创建表
[02:34] 好已经执行完了没有错误对吧你看这没有错误然后呢我们刷新一下刷新一下哪个库啊这个啊p2pbankdeposit就是他我们看一下表你看这里边是有一堆的表对吧有银行卡呀银行的账号等等各种各样的信息啊这是数据库这块我们就搞定搞定了这往下走吧往下走就是这个项目了我刚才说了嘛这个
[03:09] 这是银行那边的我们也不用开发现成的我们直接用iDare打开把它给启动一下就行了这个项目呢在这就旁边这我们在iDare里边呢我们直接是open就行了openopen就是对就是它直接打开新开一个窗口吧呃然后呢这就是我们说的这个银行存管系统啊这边呢你最好的这个时候呢是第一次打开的时候呢要保证呃你的电脑联网
[03:42] 他可能要根据你的碰文件来下载一些jar 包啊然后你稍等片刻之后你要看这里边有没有报错要把这个没问的环境问题给他解决一下那这个我们就打开打开之后里边代码你也不用管我说这个我们只是拿着去用而已将来我们去调用他的接口就行了那接下来咱就要尝试运行一下这里边我们要起一下这个项目但是需要配他的什么呀启动参数大家看这个启动参数大家应该很熟悉吧
[04:12] 它是要从Apollo里边去读取配置对吧那么银行存款系统对应的这个配置我们在第一章的时候也已经生成过了就放到Apollo里边都已经有你看这边Apollo我也已经打开了大家瞅一眼就这儿就这儿第一章的时候都已经搞过了生成过你看这里边是不是啥配置都有对不对具体的配置咱就不再看了将来用到的时候再说那我们就配这个启动参数就行了
[04:44] 在这儿是吧然后粘过来端口号55010那这个跑完之后咱是不是就可以运行了啊把这个项目给跑一下好接下来他已经启动了啊这里边他要死瓶环境对吧加载Apollo的配置啊你看他也用到了mybattlesplus是不是往下走走哎这边已经启动成功了没有报错啊55010这个端口号
[05:20] 那这是启动成功不代表里边的功能就没问题对不对那咱接下来呢也考虑到这一点这呢给大家提供了一个测试类大家可以跑一下测试一下它的基本功能在这个测试包里边我们找一下这个测试类我们可以跑一下在哪呢再找一找测试包就这个啊bank cardservice test咱看看这里边它大概实现了什么功能啊
[05:52] 这是Gunet的运行环境对吧这是注入了一个业务层业务层要调到层对不对然后我们看这应该是看名字应该是一个增删改查当中的一个增加就是保存的一个操作是吧循环了100次你看最终关键代码是不是在这对不对调业务层的方法然后我们跟踪一下业务层的方案里边他这是先做了一个查询看看它存在不存在大概的意思对吧
[06:24] 不存在的话就走最终还是走到什么呀save你看他这个保存的可不止一个表你看这是bank user这是bank什么呀card那我们猜测我们根据名字猜测应该是将来往这个表里边会差了100条数据对吧还有谁呀bank user对吧这个表里边也会差了100条数据大概的代码咱是能看懂的这无非就是这个数据库操作
[06:52] 是循环了100次啊这其实就是准备了一些这个测试数据那咱接下来就直接跑一下吧测试一下他这个测试他要重新加载这个死不用环境对吧所以会稍微慢一些这里边还要读取Apollo的配置了你看这儿所以都会慢一些啊我们稍等片刻我们正常情况下应该在控制台能看到一些打印信息吗是不是呃你看他这里边本身这就有打印而且呢我们的搜寄语
[07:35] MP嘛生成的似乎语句他应该也会打印到控制台上我们一会重点观察一下有点慢是吧好接下来应该开始跑了啊MyBettisMP这个好机友已经出来了接下来是100次循环嘛对不对好开始了啊100次循环0对吧应该是没有出问题的这不是语句都打印出来的吗咱不再看控制台了咱直接去哪去表里边瞅呗Bankcard这数据有了吧
[08:18] 对不对看看啊是100条吗100对不对还有谁啊Bank谁啊Uder没问题吧对不对他这个数据都是随机的啊你不用管他随机的等一会拿来用一用就行呃那咱目前的话这个银行存款系统咱也不说好也跑起来了是不是将来你开发这个开入功能的时候呢就可以去访问他调用他这里边功能那具体怎么调用呢那这边就涉及到这么一个问题就说我们大家一定要明白就是说这个银行存款系统啊
[08:49] 是人家开发好的对吧银行那边的东西但是我们要去用但是由于不是我们开发的我们对它里边东西熟悉吗不熟悉吧对不对我们我们要要调用它的一个什么东西我们也不清楚啊它那要什么参数啊它反而给我们什么东西啊它里边都有哪些功能我们不清楚所以说这儿呢我们还给大家提供了另外一个文档就这个银行存款系统的这个什么呀接口说明这儿呢我也打开了大家过一遍
[09:19] 让他告诉你说银行存在系统里边这个接口有三种对不对然后这里边都都是每种接口都是长什么样都是什么规定然后下面你往下看这个他就开始介绍他这个银行存完系统里边对吧都有哪些功能每功能对应的接口是长什么样的这里边他需要你提供哪些参数他返回给你哪些数据这边都有详细的介绍充值功能的对不对这下面还有什么提现功能等等等等
[09:49] 那这个文档呢是咱开发过程当中要去用的而且这个文档非常非常重要这个大家刻下一定要认认真真地看一下或者说呢你具体要调哪个功能的时候你要认认真真地看一下那这个呢其实我们在企业能开发的时候也是一样你在企业当中开发的时候也会碰到这种情况就是说你要去调用第三方的对吧一个系统那这个东西呢不需要你开发人家开发好所以说这个时候呢人家也会给你提供类似这样的一个文档
[10:19] 需要你进行什么呀查阅的说这个文档非常非常重要那咱具体用到的时候呢我们也是到时候再查这个文档照着这个文档按照这个里边的要求去给他传数据去获取他返回的什么呀数据那这是目前吧咱把银行存款系统这一块也部署好了里边呢也有一个接口文档咱将来开发时候去用就行了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲银行存管系统的开发与部署，包括架构设计、数据库初始化、服务启动、接口测试及配置管理。

2) 按时间顺序列出每张画面的要点：
画面1：展示系统架构图，包含“浏览器APP”、“用户中心”、“存管代理服务”、“存管系统”、“开户银行”等模块，以及各模块间的数据流向（如1.1生成开户请求数据、1.3准备开户参数、1.4生成交易记录等）。
画面2：在P2P项目中打开并查看SQL文件`wanxindepository-init.sql`，内容为创建`bank_card_detail`和`bank_user`表的语句。
画面3：在IntelliJ IDEA中打开项目`wanxindepository`，弹出“Open File or Project”对话框，显示项目文件夹结构。
画面4：在Apollo配置中心网页界面，展示“wanxindepository”项目及其关联服务（如consumer-Service、account-Service等）。
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

