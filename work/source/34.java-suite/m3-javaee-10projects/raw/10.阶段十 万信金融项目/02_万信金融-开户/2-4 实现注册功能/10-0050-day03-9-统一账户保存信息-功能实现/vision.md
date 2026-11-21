# 画面线理解：day03-9-统一账户保存信息-功能实现

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-9-统一账户保存信息-功能实现_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:35, 02:52, 03:49, 04:46, 05:12, 07:08, 07:37, 09:07, 10:07, 12:11, 13:12, 13:58, 15:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:33:22

1) 这一组画面整体在讲什么（一句话）：
实现账户注册功能，包括定义接口、编写服务层代码、处理密码加密、以及控制器层的请求映射。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在AccountService接口中定义register方法，使用AccountDTO作为参数。
画面2：在AccountServiceImpl类中实现register方法，通过MyBatis-Plus实现数据保存。
画面3：展示Account实体类中定义的字段，包括手机号、密码、盐值等。
画面4：在AccountServiceImpl中，通过AccountMapper将AccountDTO转换为Account实体。
画面5：在AccountServiceImpl中，使用AccountMapper将AccountDTO转换为Account实体。
画面6：在AccountServiceImpl中，使用AccountMapper将AccountDTO转换为Account实体。
画面7：在AccountServiceImpl中，使用AccountMapper将AccountDTO转换为Account实体。
画面8：在AccountServiceImpl中，使用AccountMapper将AccountDTO转换为Account实体。
画面9：展示PasswordUtil类中生成随机盐值和加密密码的代码。
画面10：在AccountServiceImpl中，调用PasswordUtil生成密码。
画面11：在AccountServiceImpl中，调用PasswordUtil生成密码。
画面12：在AccountServiceImpl中，将Account实体转换为AccountDTO。
画面13：在AccountController中，调用AccountService的register方法。
画面14：在AccountController中，定义register方法，接收AccountRegisterDTO并返回RestResponse。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 账户注册
 * @param registerDTO 注册信息
 * @return
 */
AccountDTO register(AccountRegisterDTO registerDTO);
```

画面2：
```java
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AccountServiceImpl extends ServiceImpl<AccountMapper, Account> implements AccountService {
    private SmsService smsService;

    public RestResponse getSMSCode(String mobile) {
        return smsService.getSMSCode(mobile);
    }

    public Integer checkMobile(String mobile, String key, String code) {
        smsService.verifySmsCode(key, code);
        QueryWrapper<Account> wrapper = new QueryWrapper<>();
        wrapper.eq("mobile", mobile);
        int count = count(wrapper);
        return count;
    }
}
```

画面3：
```java
@TableName("account")
public class Account {
    @TableField("MOBILE")
    private String mobile;

    @TableField("PASSWORD")
    private String password;

    @TableField("SALT")
    private String salt;

    // 密码状态
}
```

画面4：
```java
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUserName(accountRegisterDTO.getUserName());
    account.setPassword(accountRegisterDTO.getPassword());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setDomain("e");
    save(account);
    return null;
}
```

画面5：
```java
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUserName(accountRegisterDTO.getUserName());
    account.setPassword(accountRegisterDTO.getPassword());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setDomain("e");
    save(account);
    return null;
}
```

画面6：
```java
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUserName(accountRegisterDTO.getUserName());
    account.setPassword(accountRegisterDTO.getPassword());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setDomain("e");
    save(account);
    return null;
}
```

画面7：
```java
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AccountServiceImpl extends ServiceImpl<AccountMapper, Account> implements AccountService {
    private SmsService smsService;

    @Override
    public RestResponse getSMSCode(String mobile) {
        return smsService.getSMSCode(mobile);
    }

    @Override
    public Integer checkMobile(String mobile, String key, String code) {
        smsService.verifySmsCode(key, code);
        QueryWrapper<Account> wrapper = new QueryWrapper<>();
        wrapper.eq("mobile", mobile);
        int count = count(wrapper);
        return count;
    }
}
```

画面8：
```java
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUserName(accountRegisterDTO.getUserName());
    account.setPassword(accountRegisterDTO.getPassword());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setDomain("e");
    save(account);
    return null;
}
```

画面9：
```java
public static String generate(String password) {
    Random r = new Random();
    StringBuilder sb = new StringBuilder(capacity: 16);
    sb.append(r.nextInt(99999999)).append(r.nextInt(99999999));
    int len = sb.length();
    if (len < 16) {
        for (int i = 0; i < 16 - len; i++) {
            sb.append("0");
        }
    }
    String salt = sb.toString();
    password = md5Hex(password + salt);
    char[] cs = new char[48];
    for (int i = 0; i < 48; i += 3) {
        cs[i] = password.charAt(i / 3 * 2);
        cs[i + 1] = password.charAt(i / 3 * 2 + 1);
        cs[i + 2] = salt.charAt(i / 3);
    }
    return new String(cs);
}
```

画面10：
```java
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUserName(accountRegisterDTO.getUserName());
    account.setPassword(accountRegisterDTO.getPassword());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setDomain("e");
    save(account);
    return null;
}
```

画面11：
```java
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUserName(accountRegisterDTO.getUserName());
    account.setPassword(accountRegisterDTO.getPassword());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setDomain("e");
    save(account);
    return null;
}
```

画面12：
```java
private AccountDTO convertAccountEntityToDTO(Account entity) {
    if (entity == null) {
        return null;
    }
    AccountDTO dto = new AccountDTO();
    BeanUtils.copyProperties(entity, dto);
    return dto;
}
```

画面13：
```java
@Override
public AccountDTO register(AccountRegisterDTO accountRegisterDTO) {
    Account account = new Account();
    account.setUserName(accountRegisterDTO.getUserName());
    account.setPassword(accountRegisterDTO.getPassword());
    account.setMobile(accountRegisterDTO.getMobile());
    account.setDomain("e");
    save(account);
    return null;
}
```

画面14：
```java
@Override
@RequestMapping("/mobiles")
public RestResponse register(@RequestBody AccountRegisterDTO accountRegisterDTO) {
    return RestResponse.success(AccountService.register(accountRegisterDTO));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
