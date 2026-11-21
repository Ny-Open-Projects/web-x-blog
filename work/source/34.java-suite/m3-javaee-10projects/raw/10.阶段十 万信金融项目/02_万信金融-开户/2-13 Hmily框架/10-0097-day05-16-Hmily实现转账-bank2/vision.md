# 画面线理解：day05-16-Hmily实现转账-bank2

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-13 Hmily框架
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-13 Hmily框架\day05-16-Hmily实现转账-bank2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:28, 00:45, 01:48, 02:35, 03:12, 04:04, 04:19, 04:49, 05:13, 05:42, 06:29, 06:48, 07:15, 08:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:07:58

1) 这一组画面整体在讲如何使用 TCC（Try-Confirm-Cancel）模式实现分布式事务，通过代码和架构图展示事务管理器协调两个服务（A账户和B账户）的事务操作。

2) 按时间顺序列出每张画面的要点：
画面1：展示 BankHmilyServer 启动类，配置了 @EnableDiscoveryClient、@EnableFeignClients，并指定 basePackages 包扫描路径。
画面2：展示 application.yml 配置文件，包含 druid 数据源配置、hmyl 配置、以及 ribbon 超时设置。
画面3：展示 DatabaseConfiguration.java，其中通过 @Autowired 注入 Environment，并从配置中读取 hmyl 相关属性设置到 HmilyTransactionBootstrap。
画面4：展示 AccountInfoServiceImpl.java，其中定义了 updateAccountBalance 方法，用于更新账户余额。
画面5：展示 Bank2Controller.java，其中定义了 @RequestMapping("/transfer") 的 transfer 方法，用于调用 AccountInfoService。
画面6：展示 AccountInfoServiceImpl.java，其中定义了 updateAccountBalance 方法，用于更新账户余额。
画面7：展示 AccountInfoServiceImpl.java，其中定义了 confirmMethod 和 cancelMethod 方法，分别用于确认和取消事务。
画面8：展示 AccountInfoServiceImpl.java，其中定义了 confirmMethod 方法，用于确认事务。
画面9：展示 AccountInfoServiceImpl.java，其中定义了 confirmMethod 方法，用于确认事务。
画面10：展示 AccountInfoServiceImpl.java，其中定义了 confirmMethod 方法，用于确认事务。
画面11：展示项目结构，选中了 hmily-demo-bank2 目录。
画面12：展示 Bank2HmilyServer 启动类，配置了 @SpringBootApplication、@EnableDiscoveryClient、@ComponentScan，并指定 basePackages 包扫描路径。
画面13：展示 PPT 页面，架构图显示事务管理器协调 A 账户和 B 账户的事务操作，包括 try、confirm、cancel 三个阶段。
画面14：展示 PPT 页面，文字说明 TCC 模式需要每个分支事务实现 Try、Confirm、Cancel 三个操作，以及 TCC 的不足之处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.mongo.MongoAutoConfiguration;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication(exclude = MongoAutoConfiguration.class)
@EnableDiscoveryClient
@EnableFeignClients(basePackages = {"cn.itcast.wanxint.hmyl.demo.bank1","org.dromara.hmyl"})
@ComponentScan({"cn.itcast.wanxint.hmyl.demo.bank1","org.dromara.hmyl"})
public class BankHmilyServer {
    public static void main(String[] args) {
        SpringApplication.run(BankHmilyServer.class, args);
    }
}
```

画面2：
```yaml
password: 123
type: com.alibaba.druid.pool.DruidDataSource
driver-class-name: com.mysql.cj.jdbc.Driver

hmyl:
  serializer: kryo #序列化工具
  retryMax: 30 #最大重试次数
  repositorySupport: db #持久化方式
  started: false #事务参与方

hmilyDbConfig:
  driverClassName: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:3306/bank?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai
  username: root
  password: 123

ribbon:
  ConnectTimeout: 600 #设置连接超时时间 default 5000
  ReadTimeout: 600 #设置读取超时时间 default 5000
```

画面3：
```java
@Autowired
private Environment env;

public HmilyTransactionBootstrap hmilyTransactionBootstrap(HmilyInitService hmilyInitService) {
    HmilyTransactionBootstrap hmilyTransactionBootstrap = new HmilyTransactionBootstrap(hmilyInitService);
    hmilyTransactionBootstrap.setRetryMax(env.getProperty("org.dromara.hmyl.retryMax"));
    hmilyTransactionBootstrap.setSerializer(env.getProperty("org.dromara.hmyl.serializer"));
    hmilyTransactionBootstrap.setRepositorySupport(env.getProperty("org.dromara.hmyl.repositorySupport"));
    HmilyDbConfig hmilyDbConfig = new HmilyDbConfig();
    hmilyDbConfig.setDriverClassName(env.getProperty("org.dromara.hmyl.hmilyDbConfig.driverClassName"));
    hmilyDbConfig.setUsername(env.getProperty("org.dromara.hmyl.hmilyDbConfig.username"));
    hmilyDbConfig.setPassword(env.getProperty("org.dromara.hmyl.hmilyDbConfig.password"));
    hmilyTransactionBootstrap.setHmilyDbConfig(hmilyDbConfig);
    return hmilyTransactionBootstrap;
}
```

画面4：
```java
@Service
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Hmily(confirmMethod = "confirmMethod", cancelMethod = "cancelMethod")
    public Boolean updateAccountBalance(String accountNo, Double amount) {
        System.out.println("******** Bank2 Service Begin ...");
        try {
            accountInfoDao.updateAccountBalance(accountNo, amount);
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e.getMessage());
        }
        return true;
    }
}
```

画面5：
```java
@RestController
public class Bank2Controller {
    @Autowired
    AccountInfoService accountInfoService;

    @RequestMapping("/transfer")
    public Boolean transfer(@RequestParam("amount") Double amount) {
        this.accountInfoService.updateAccountBalance("2", amount);
        return true;
    }
}
```

画面6：
```java
@Service
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Hmily(confirmMethod = "confirmMethod", cancelMethod = "cancelMethod")
    public Boolean updateAccountBalance(String accountNo, Double amount) {
        System.out.println("******** Bank2 Service Begin ...");
        try {
            accountInfoDao.updateAccountBalance(accountNo, amount);
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e.getMessage());
        }
        return true;
    }
}
```

画面7：
```java
@Service
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Hmily(confirmMethod = "confirmMethod", cancelMethod = "cancelMethod")
    public Boolean updateAccountBalance(String accountNo, Double amount) {
        System.out.println("******** Bank2 Service Begin ...");
        try {
            accountInfoDao.updateAccountBalance(accountNo, amount);
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e.getMessage());
        }
        return true;
    }

    public Boolean confirmMethod(String accountNo, Double amount) {
        System.out.println("******** Bank2 Service commit ...");
        return true;
    }

    public Boolean cancelMethod(String accountNo, Double amount) {
        accountInfoDao.updateAccountBalance(accountNo, amount - 1);
        System.out.println("******** Bank2 Service rollback...");
        return true;
    }
}
```

画面8：
```java
@Service
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Hmily(confirmMethod = "confirmMethod", cancelMethod = "cancelMethod")
    public Boolean updateAccountBalance(String accountNo, Double amount) {
        System.out.println("******** Bank2 Service Begin ...");
        try {
            accountInfoDao.updateAccountBalance(accountNo, amount);
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e.getMessage());
        }
        return true;
    }

    public Boolean confirmMethod(String accountNo, Double amount) {
        System.out.println("******** Bank2 Service commit ...");
        return true;
    }

    public Boolean cancelMethod(String accountNo, Double amount) {
        accountInfoDao.updateAccountBalance(accountNo, amount - 1);
        System.out.println("******** Bank2 Service rollback...");
        return true;
    }
}
```

画面9：
```java
@Service
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Hmily(confirmMethod = "confirmMethod", cancelMethod = "cancelMethod")
    public Boolean updateAccountBalance(String accountNo, Double amount) {
        System.out.println("******** Bank2 Service Begin ...");
        try {
            accountInfoDao.updateAccountBalance(accountNo, amount);
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException(e.getMessage());
        }
        return true;
    }

    public Boolean confirmMethod(String accountNo, Double amount) {
        System.out.println("******** Bank2 Service commit ...");
        return true;
    }

    public Boolean cancelMethod(String accountNo, Double amount) {
        accountInfoDao.updateAccountBalance(accountNo, amount - 1);
        System.out.println("******** Bank2 Service rollback...");
        return true;
    }
}
```

画面10：
```java
@Service
public class AccountInfoServiceImpl implements AccountInfoService {

    @Autowired
    private AccountInfoDao accountInfoDao;

    @Hmily(confirmMethod = "confirmMethod", cancelMethod = "cancelMethod")
    public Boolean updateAccount
