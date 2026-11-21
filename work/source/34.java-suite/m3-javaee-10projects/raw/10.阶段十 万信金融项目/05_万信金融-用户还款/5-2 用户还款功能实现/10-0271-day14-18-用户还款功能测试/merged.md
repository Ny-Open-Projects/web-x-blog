# day14-18-用户还款功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-18-用户还款功能测试_【海量资源尽在 666java.com】.mp4
- 时长 7分43秒（音频 463s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好截止到目前呢我们已经把用户还款整个这一块的业务呢全部开发完毕了我们一共是分成了四个阶段啊那当然呢前两个阶段我们当时开发完之后是不是就进行了功能测试所以咱接下来的话重点是要对第三阶段啊就是2.1 2.2对吧还有第四阶段2.3一直到什么呀2.9啊这一块呢要进行功能测试
[00:30] 那咱从哪开始啊那我们是不是要看看这个都需要启动哪些服务哪些系统对不对那我们一看这个图呢一目了然对不对三个啊重点要启动的就是还款服务存款代理服务还有什么呀银行存款系统那这些呢我已经全部启动过了啊那咱既然是从前端发请求开始吗哎这里边我们要给大家说明一下啊咱们这个用户还款业务它本身是跟前端没有关系的
[01:00] 我们将来这个触发的入口是不是通过定时任务对不对咱们前面说过啊但是定时任务呢咱目前还没有开发所以说呢咱是不是在还款服务的Controller当中加了一个一个测试的一个入口对不对来我们打开让大家再回顾一下啊Controller大家看在哪就这是不是这只是测试用的啊将来我们把定时任务给他开发出来之后呢我们就主要是通过定时任务啊进行这个用户还款
[01:31] 这个业务的一个出发了那咱目前测试还得往这干什么发请求啊还得用它呃那咱就打开这个浏览器啊我们看看有没有历史记录啊没有是不是look host咱是53080吧我记得是53080吗哎呦大家看一下对不对你看啊这是咱以前测试的这个历史记录啊那我是往这敲回车对吧你敲回车他就发了一个请求请求是不是就到这个什么地方来
[02:03] 到这了对不对然后这呢就触发什么呀咱们图当中是不是还是从接口一开始嘛就第一阶段开始对不对然后第二阶段然后第三阶段然后第四阶段当然我们说过前两个阶段咱都已经测试过了所以说咱这次重点要观察的是第三阶段和第四阶段的效果那我们要观察啥呢你看第四阶段很明显你是不是要看看这几个更新操作有没有成功对不对然后呢你还要观察第四阶段你看这
[02:31] 这个保存的这个什么交易记录这个状态是不是保存了对吧这个有没有改成这个什么一同步这是我们通过几个关键的地方就可以观察出来这个效果那另外呢要提醒大家一定要注意你是不是还要启动Rocket的MQ是不是千万不要忘了因为我们这你看是不是要通过Rocket的MQ来进行这个协调协调这个分布式事务对不对咱当时写代码的时候都写过这个什么发送消息接收消息
[03:04] 这些代码啊随着说k的mq你也得记得启动呃那咱接下来的话我是不是就该在这干什么呀发请求了对不对我敲一下回车就行了啊走好前段这应该看不到啥我们主要是看控制台看看首先看看有没有报错啊呃我们看看这是什么呀repayment Service就还款服务这边应该是没有报错这也打印出来还款预处理成功对吧下面也是搜购语音呢都产生了一堆啊
[03:34] 然后我们看看这个存款代理服务这边这边也没有报错啊思考语句也都生成了那咱直接去表里边这个呃瞅一瞅刚才我们说的那那那些什么东西啊比如说这几个更新是不是有没有成功这是哪些表啊还款明细对吧你挑几个瞅着我就行了啊因为它是一个事物嘛要么都成功要么都失败嘛呃这个是我看啊它是第一个是什么呀还款明细啊还款明细应该是这个对不对
[04:07] 这是还款明细啊他说要改成什么呀改成已收是不是哪个字段要改成已收啊我们看看这里边应该是没有状态的啊这里边应该没有状态我们看他再换一个吧换一个这个什么还款计划这个咱应该是很清楚的还款计划咱前面是改过的啊还款计划呢这次要改成什么呀已还款还款计划还款计划是这个好我们看数据呃我们瞅瞅这个哪个字段呢
[04:40] 这个字感对不对1是不是应该是repayment status对吧repayment status我们找找啊repayment status你看这个咱当时测试的时候不是拿这个测试了2019年11月11号吗你看这对吧然后还有啥还有什么实收明细实收明细改成已收实收明细实收明细应该是这个吧这里边有状态吗
[05:15] 我这边应该也没有状态啊没有状态我们看看这个计划里面计划里面有没有状态啊这有状态对不对是这啊receivable status应该改成一是不是那我们找一找呗呃他是哪个字段啊receivable statusreceivable status找找啊在这你看这个是不是已经改成一了啊然后还有哪啊还有这个这个啊这个对吧
[05:49] 还有这个应该没了啊五个投资人吗还有印象吗当时我们在测试这个呃投标啊买标放款的时候我们那个标底是不是一共有五个人投资吗所以说你看这个记录当中现在有五个投资人他是不是相当于是已经收到钱了对不对就这意思啊这个状态已经改成一了所以这块是没有问题了然后我们再瞅瞅这个阶段四这一块的这个什么呀呃有没有保存交易记录他的状态有没有改成什么呀以同步是不是
[06:18] 这个应该去哪个表交易记录啊交易记录应该是在这个库里边这是不是呃我们看看应该是哪条记录啊应该是这条记录你看repayment对不对这是还款了吗然后你看这个状态是不是已经改成一了啊这没问题吧啊这也没问题交易交易记录也保存了状态也改成一了啊
[06:47] 然后呢这个大家下去你有时间你还可以做做RocketMQ相关的这个测试你比如说这个嗯我们之前在讲RocketMQ的时候是不是测试过这个15回查有印象吧我们故意怎么着啊不返回给RocketMQ任何消息对不对啊你还可以测试测试这个什么呀消息重视啊让这个第四阶段故意让他出个问题
[07:12] 看看能不能进行消息从事这块呢我就不再给大家测试了因为在前面我们的实现转账啊在实现满标放款的时候呢都详细的给大家做个测试大家有兴趣的话有时间的话你可以参考前面的这个套路都一样啊你就是让他报个错就行了啊然后观察观察控制台对不对看看他有没有这个效果有没有出来就行了这是目前吧咱们就把什么呀用户还款整个这块的业务呢就全部测试通过

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个还款服务的业务流程，包括前端触发、服务层处理、数据库操作及状态变更，并通过 Apollo 配置中心管理配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示一个序列图，描述“还款服务”与“支付代理服务”、“清算中心”之间的交互流程，包括生成计划、保存记录、更新状态等步骤。
画面 2: 展示 IDE 中的 `RepaymentServiceImpl.java` 文件，其中 `invokeConfirmRepayment` 方法调用 `depositoryAgentAgent.confirmRepayment`，并处理返回码为 `RETURN_CODE_00000` 的情况。
画面 3: 展示 Apollo 配置中心的 Web 界面，显示多个服务模块，如 `depository-agent-Service`、`transaction-Service`、`repayment-Service` 等。
画面 4: 展示序列图，流程与画面 1 类似，但细节略有不同，如“保存交易记录”状态为“未同步”。
画面 5: 展示 IDE 中的 `RepaymentController.java` 文件，包含 `@PostMapping("/start-repayment")` 和 `@ApiOperation("测试用户还款")` 注解的 `testExecuteRepayment` 方法。
画面 6: 展示 IDE 中的 `RepaymentService.java` 文件，`testExecuteRepayment` 方法调用 `repaymentService.executeRepayment(date)`，并显示了数据库操作日志。
画面 7: 展示序列图，流程与画面 1 类似，但“更新交易记录”状态为“已同步”。
画面 8: 展示数据库管理工具中 `repayment_detail` 表的结构，包含字段如 `ID`、`REPAYMENT_PLAN_ID`、`AMOUNT`、`REPAYMENT_DATE`、`STATUS`。
画面 9: 展示数据库管理工具中 `repayment_plan` 表的结构，包含字段如 `ID`、`CUSTOMER_ID`、`PROJECT_ID`、`PRINCIPAL`、`AMOUNT`、`REPAYMENT_STATUS`、`CREATE_DATE`。
画面 10: 展示数据库管理工具中 `receivable_detail` 表的结构，包含字段如 `ID`、`RECEIVABLE_ID`、`AMOUNT`、`RECEIVABLE_DATE`。
画面 11: 展示数据库管理工具中 `repayment_detail` 表的数据，包含多行记录，显示 `ID`、`CUSTOMER_ID`、`TENDER_ID`、`REPAYMENT_ID`、`NUMBER_OF_PERIODS`、`INTEREST`、`AMOUNT` 等字段。
画面 12: 展示数据库管理工具中 `repayment_detail` 表的数据，显示 `NUMBER_OF_PERIODS`、`AMOUNT`、`SHOULD_RECEIVABLE_DATE`、`RECEIVABLE_STATUS`、`CREATE_DATE`、`COMMISSION` 等字段。
画面 13: 展示数据库管理工具中 `depository_agent` 表的数据，包含字段如 `ID`、`REQUEST_ID`、`REQUEST_TYPE`、`OBJECT_TYPE`、`OBJECT_ID`、`CREATE_DATE`。
画面 14: 展示序列图，流程与画面 1 类似，但“更新交易记录”状态为“已同步”，并显示“更新还款交易状态为‘已还款’”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
// 更新还款计划，已还款
repaymentPlan.setPaymentStatus("1");
int rows = planMapper.updateById(repaymentPlan);
return rows > 0;
```
```java
public void invokeConfirmRepayment(RepaymentPlan repaymentPlan, RepaymentRequest repaymentRequest) {
    RestResponse<String> repaymentResponse = depositoryAgentAgent.confirmRepayment(repaymentRequest);
    if (!repaymentResponse.getSuccess() || !repaymentResponse.getResult().equals(DepositoryReturnCode.RETURN_CODE_00000)) {
        throw new RuntimeException("还款失败");
    }
}
```
画面 5:
```java
@PostMapping("/start-repayment")
public RestResponse<String> startRepayment(@RequestBody ProjectWithTendersDTO project) {
    String result = repaymentService.startRepayment(project);
    return RestResponse.success(result);
}
```
```java
@ApiOperation("测试用户还款")
public void testExecuteRepayment(@PathVariable String date) {
    repaymentService.executeRepayment(date);
}
```
画面 6:
```java
Time: 0 ms ID: cn.ictest.wanxingzp.depository.Mapper.DepositoryRecordMapper.selectOne
Execute SQL: SELECT ID,REQUEST_NO,REQUEST_TYPE,OBJECT_TYPE,OBJECT_ID,CREATE_DATE,REQUEST_STATUS,CONFIRM_DATE,RESPONSE_DATA FROM depository_record WHERE ID = 1
Time: 2 ms ID: cn.ictest.wanxingzp.depository.Mapper.DepositoryRecordMapper.insert
Execute SQL: INSERT INTO depository_record (ID,REQUEST_NO,REQUEST_TYPE,OBJECT_TYPE,OBJECT_ID,CREATE_DATE,REQUEST_STATUS,CONFIRM_DATE,RESPONSE_DATA) VALUES (1,1,1,1,1,1,1,1,1)
Time: 2 ms ID: cn.ictest.wanxingzp.depository.Mapper.DepositoryRecordMapper.selectOne
Execute SQL: SELECT ID,REQUEST_NO,REQUEST_TYPE,OBJECT_TYPE,OBJECT_ID,CREATE_DATE,REQUEST_STATUS,CONFIRM_DATE,RESPONSE_DATA FROM depository_record WHERE ID = 1
Time: 2 ms ID: cn.ictest.wanxingzp.depository.Mapper.DepositoryRecordMapper.updateById
Execute SQL: UPDATE depository_record SET REQUEST_NO='1',REQUEST_TYPE='1',OBJECT_TYPE='1',OBJECT_ID='1',CREATE_DATE='1',REQUEST_STATUS='1',CONFIRM_DATE='1',RESPONSE_DATA='1' WHERE ID=1
```
画面 8:
```sql
CREATE TABLE repayment_detail (
    ID BIGINT(20) NOT NULL COMMENT '主键',
    REPAYMENT_PLAN_ID BIGINT(20) COMMENT '还款计划ID',
    AMOUNT DECIMAL(10,2) COMMENT '金额',
    REPAYMENT_DATE DATETIME COMMENT '还款日期',
    STATUS TINYINT(4) COMMENT '状态'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
画面 9:
```sql
CREATE TABLE repayment_plan (
    ID BIGINT(20) NOT NULL COMMENT '主键',
    CUSTOMER_ID BIGINT(20) COMMENT '客户ID',
    PROJECT_ID VARCHAR(50) COMMENT '项目ID',
    NUMBER_OF_PERIODS INT(11) COMMENT '期数',
    PRINCIPAL DECIMAL(10,2) COMMENT '本金',
    AMOUNT DECIMAL(10,2) COMMENT '金额',
    REPAYMENT_STATUS VARCHAR(50) COMMENT '还款状态',
    CREATE_DATE DATETIME COMMENT '创建时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
画面 10:
```sql
CREATE TABLE receivable_detail (
    ID BIGINT(20) NOT NULL COMMENT '主键',
    RECEIVABLE_ID BIGINT(20) COMMENT '应收ID',
    AMOUNT DECIMAL(10,2) COMMENT '金额',
    RECEIVABLE_DATE DATETIME COMMENT '应收日期'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
画面 13:
```sql
CREATE TABLE depository_agent (
    ID BIGINT(20) NOT NULL COMMENT '主键',
    REQUEST_ID BIGINT(20) COMMENT '请求ID',
    REQUEST_TYPE VARCHAR(50) COMMENT '请求类型',
    OBJECT_TYPE VARCHAR(50) COMMENT '对象类型',
    OBJECT_ID VARCHAR(50) COMMENT '对象ID',
    CREATE_DATE DATETIME COMMENT '创建时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1、4、7、14: 展示序列图，包含三个主要参与者：“还款服务”、“支付代理服务”、“清算中心”。流程如下：
- 还款服务 → 支付代理服务：1.1 生成还款计划，状态为“未同步”；1.2 保存交易记录，状态为“未同步”；1.3 当前交易状态为“未同步”；1.4 通过转换生成签名及摘要；1.5 更新交易记录，状态为“已同步”；1.6 更新交易记录，状态为“已同步”。
- 支付代理服务 → 清算中心：1.7 清算中心返回“已成功”。
- 清算中心 → 还款服务：1.8 更新交易记录，状态为“已同步”。
画面 3: 展示 Apollo 配置中心的 Web 界面，包含多个服务模块，如 `depository-agent-Service`、`transaction-Service`、`repayment-Service` 等。
画面 8、9、10、11、12、13: 展示数据库管理工具中的表结构和数据，包含字段和索引信息。

