# 画面线理解：day05-17-Hmily实现转账-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-17-Hmily实现转账-功能测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:44, 02:04, 02:28, 03:53, 04:59, 05:28, 06:20, 06:57, 07:55, 08:20, 08:56, 09:34, 11:00, 12:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:08:28

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的分布式银行转账系统，重点展示服务间调用、数据库事务处理及异常处理机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：IDEA项目结构视图，选中“Scratches and Consoles”。
画面2：Bank2服务启动日志，显示服务注册成功。
画面3：IDEA调试界面，显示Bank2服务已启动。
画面4：Bank1服务的BankController.java文件，展示转账接口。
画面5：多窗口视图，包含SQLyog数据库工具和PDF文档。
画面6：SQLyog中bank2数据库的account_info表数据。
画面7：Bank2服务的AccountInfoServiceImpl.java文件，展示更新余额方法。
画面8：Bank2服务的AccountInfoServiceImpl.java文件，展示确认方法。
画面9：Bank2服务的AccountInfoServiceImpl.java文件，展示取消方法。
画面10：Bank2服务的启动日志，显示服务已启动。
画面11：Bank2服务的启动日志，显示SQL连接成功。
画面12：SQLyog中bank1数据库的account_info表数据。
画面13：Bank2服务的启动日志，显示服务准备就绪。
画面14：Bank2服务的AccountInfoServiceImpl.java文件，展示转账逻辑。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```java
@Autowired
AccountInfoService accountInfoService;

@RequestMapping("/transfer")
public String test(@RequestParam("amount") Double amount) {
    this.accountInfoService.updateAccountBalance("1", amount);
    return "bank1向bank2转账：" + amount;
}
```

画面7：
```java
public Boolean updateAccountBalance(String accountNo, Double amount) {
    try {
        accountInfoDao.updateAccountBalance(accountNo, amount);
    } catch (Exception e) {
        throw new RuntimeException(e.getMessage());
    }
    return true;
}

public Boolean confirmMethod(String accountNo, Double amount) {
    System.out.println("********* Bank2 Service commit...");
    return true;
}
```

画面8：
```java
public Boolean cancelMethod(String accountNo, Double amount) {
    accountInfoDao.updateAccountBalance(accountNo, amount + -1);
    System.out.println("********* Bank2 Service rollback...");
    return true;
}
```

画面9：
```java
@override
public AccountInfoService accountInfoDao;

public Boolean updateAccountBalance(String accountNo, Double amount) {
    try {
        accountInfoDao.updateAccountBalance(accountNo, amount);
    } catch (Exception e) {
        throw new RuntimeException(e.getMessage());
    }
    return true;
}

public Boolean confirmMethod(String accountNo, Double amount) {
    System.out.println("********* Bank2 Service commit...");
    return true;
}
```

画面13：
```java
2019-08-06 15:52:13.982 INFO 916 --- [self-recovery-30] .c.HmilyTransactionRecoveryScheduled : self recovery execute delayTime:60
********* Bank1 Service prepare...
```

画面14：
```java
public Boolean updateAccountBalance(String accountNo, Double amount) {
    accountInfoDao = null; // 模拟异常
    accountInfoDao.updateAccountBalance(accountNo, amount);
    throw new RuntimeException(e.getMessage());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
