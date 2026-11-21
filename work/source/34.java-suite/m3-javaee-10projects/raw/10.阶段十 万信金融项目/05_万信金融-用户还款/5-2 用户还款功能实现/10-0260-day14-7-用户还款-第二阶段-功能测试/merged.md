# day14-7-用户还款-第二阶段-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-2 用户还款功能实现
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-2 用户还款功能实现\day14-7-用户还款-第二阶段-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 4分44秒（音频 285s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好前面呢我们把用户还款业务当中第二阶段的代码全部搞定了啊就是图当中1.3到1.10对吧而且这块功能搞定完之后呢咱把业务出发入口里边那个代码也完善了那咱接下来其实就可以进行功能测试了那大家看一下我们要测试第二阶段的这个功能我们是不是需要把还款服务以及存款代理服务都
[00:32] 启动起来当然呢还包括谁呀对银行存系统啊所以说这三块都需要启动那我这边的话该启动的都已经启动过了啊大家看一看是不是哎我这边这个充气一下怎么报错这个还款服务我们看一下是不是没问题对不对这还在没问题啊那我们把这个存款代理服务银行存款系统我也启动成功了
[01:02] 我们看这个存管代理服务得把它给启动一下稍等片刻啊就应该是启动完了那该启动的都已经启动过了那咱接下来怎么进行测试呢咋进行测试呢大家想一下我们是不是还得从入口开始啊这个入口是不是还是这个谁啊control这儿是吧来从这开始你还是得在浏览器里边就是这这儿对吧干什么呀发请求往这发请求啊然后他调右层的这个入口吗
[01:41] 在这个入口里边咱前面是不是这块代码是不是测试这个第一阶段接口一接口二的对不对然后这一走这个代码是不是就开始出发咱第二阶段这个代码的运行了是不是那在这里边你看他是不是构造了请求数据然后开始往什么呀存款代理服务那边发请求吗是不是开始走1.3对吧然后一直1.4 1.5一直到什么呀说这个大家得知道怎么回事啊那咱怎么观察这个效果呢
[02:13] 你要观察这个效果的话你看首先你看你要检查检查从来带你服务这边你比如说这个保存交易记录有没有成功他这个状态对吧最终的状态应该是改成什么呀一同步吧然后我们还可以看这个这个他成功的话应该会返回处是不是返回处的话我想想我们要想看到这个返回处我是不是在这打印个东西就行对不对那如果处理成功这就是出吗
[02:45] 这儿是出的话这条这个语句应该会打印到控制台吗对不对那我这就写一个这样一个字符串啊就预还款处理成功可以吧那我就需要把这个谁给重启一下这是还款服务加一点代码重启完的话咱就开始进行测试这都启动过稍等一下好这边的话基本上就启动完了吧
[03:36] 好启动完了启动完之后咱是吧还是从这开始好走这边前端是没啥反应的我们去控制台看看你看控制台是不是的确打印出来什么还款预备处理成功然后咱看看存款代理服务这边应该会出现一些什么搜索语句先是保存交易记录然后是不是要更新它的什么状态对吧那咱去表里边瞅一瞅表里边存款代理服务应该是在这
[04:09] 咱应该在下边吧看这儿就这你看repayment对不对这是我们业务的类型或者请求的类型嘛是不是你看这里边是咱发过去的数据你看看签名啊对不对还有你看这是返回的数据嘛成功嘛对不对我们在这个空间台也看到然后他那个交易记录的状态你看这儿是不是最终也是一吗是表示什么意思对一同步
[04:38] 那这个咱们第二阶段这个代码呢咱就测试完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个还款服务在调用存管代理服务时，如何通过代码逻辑处理还款请求、与数据库交互并最终在数据库中记录还款结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示IDE中RepaymentServiceImpl.java文件，其中包含selectDueRepayment和executeRepayment方法，以及一个返回-1的else分支。项目结构中可见entity、Mapper、Service等包。
画面2：终端日志显示服务启动失败，提示无法找到meta server地址，配置同步失败，需重试。
画面3：终端日志显示服务启动过程中的Bean初始化信息，包括Spring框架、Jackson、RocketMQ等组件的加载。
画面4：终端日志显示服务启动成功，Eureka注册成功，配置中心（Apollo）动态配置已启用。
画面5：浏览器访问localhost:53080/repayment/execute-repayment/2019-11-11，页面为空白。
画面6：IDE中展示executeRepayment方法中预处理逻辑，包含prepayment方法调用和if判断。
画面7：展示一个流程图，描述还款服务、存管代理服务和存管系统之间的交互流程，包括生成还款计划、预处理、提交交易记录等步骤。
画面8：IDE中展示executeRepayment方法中预处理成功后的代码，包含System.out.println语句。
画面9：终端日志显示服务已连接到目标VM，地址为127.0.0.1:54274。
画面10：终端日志显示服务启动成功，Bean初始化完成。
画面11：终端日志显示动态配置属性翻转，从depository切换到deposit。
画面12：终端日志显示执行SQL语句，包括SELECT、INSERT、UPDATE操作。
画面13：数据库管理工具中显示depository_record表的数据，包含REQUEST_ID、REQUEST_TYPE、CREATE_DATE、REQUEST_STATUS等字段。
画面14：数据库管理工具中显示depository_record表的数据，包含REQUEST_ID、REQUEST_TYPE、CREATE_DATE、REQUEST_STATUS等字段，其中一条记录的REQUEST_STATUS为“SUCCESS”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
}else{
    return "-1";
}

return DepositoryReturnCode.RETURN_CODE_00000.getCode();

@Override
public List<RepaymentPlan> selectDueRepayment(String date) { return planMapper.selectDueRepayment(date); }

@Override
public RepaymentDetail saveRepaymentDetail(RepaymentPlan repaymentPlan) {
    RepaymentDetail repaymentDetail = repaymentDetailMapper.selectOne(Wrappers.<RepaymentDetail>query().eq(RepaymentDetail::getRepaymentPlanId, repaymentPlan.getRepaymentPlanId()));
    if(repaymentDetail == null){
        repaymentDetail = new RepaymentDetail();
        repaymentDetail.setRepaymentPlanId(repaymentPlan.getRepaymentPlanId());
    }
    repaymentDetail.setRepaymentPlanId(repaymentPlan.getRepaymentPlanId());
    repaymentDetail.setRepaymentPlan(repaymentPlan);
    repaymentDetail.setRepaymentDetailId(repaymentPlan.getRepaymentDetailId());
    repaymentDetail.setRepaymentDetailStatus(RepaymentDetailStatusEnum.SUCCESS.getCode());
    repaymentDetail.setRepaymentDetailType(RepaymentDetailTypeEnum.REPAYMENT.getCode());
    repaymentDetail.setRepaymentDetailCreateTime(new Date());
    repaymentDetail.setRepaymentDetailUpdateTime(new Date());
    repaymentDetail.setRepaymentDetailCreateUserId(repaymentPlan.getRepaymentPlanCreateUserId());
    repaymentDetail.setRepaymentDetailUpdateUserId(repaymentPlan.getRepaymentPlanUpdateUserId());
    repaymentDetail.setRepaymentDetailCreateUserName(repaymentPlan.getRepaymentPlanCreateUserName());
    repaymentDetail.setRepaymentDetailUpdateUserName(repaymentPlan.getRepaymentPlanUpdateUserName());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail.setRepaymentDetailUpdateIp(repaymentPlan.getRepaymentPlanUpdateIp());
    repaymentDetail.setRepaymentDetailCreateIp(repaymentPlan.getRepaymentPlanCreateIp());
    repaymentDetail

