# 画面线理解：day03-14-用户中心保存信息-Service-保存用户信息

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-14-用户中心保存信息-Service-保存用户信息_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 02:07, 02:56, 03:44, 05:17, 06:58, 07:57, 09:23, 10:31, 11:25, 12:46, 13:59, 15:05, 16:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:37:06

1) 这一组画面整体在讲什么（一句话）：
演示用户服务（Consumer Service）中用户注册功能的实现，包括服务层、控制器层的代码编写，以及数据库表结构设计。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 ConsumerServiceImpl.java 文件，其中 checkMobile 方法用于校验手机号，getBMobile 方法用于查询数据库，register 方法用于注册用户。
画面 2：在 register 方法中，添加了 if 判断，如果手机号已存在则抛出异常。
画面 3：在 register 方法中，抛出的异常类型从无参数改为带参数的 BusinessException。
画面 4：在 register 方法中，抛出的异常参数设置为 ConsumerErrorCode。
画面 5：在 register 方法中，使用 BeanUtils.copyProperties 将 DTO 数据复制到实体类 Consumer 中。
画面 6：在 register 方法中，使用 CodePrefixUtil 获取用户编号前缀，并设置到 Consumer 实体。
画面 7：在 register 方法中，使用 CodePrefixUtil 获取用户编号前缀，并设置到 Consumer 实体。
画面 8：切换到 wanningzp-common 模块，查看 CodePrefixCode 类，其中定义了 CODE_REQUEST_PREFIX 常量。
画面 9：展示数据库表 pzp_consumer 的结构，包含 ID、USERNAME、FULLNAME、MOBILE、ROLE、STATUS、REQUEST_ID 等字段。
画面 10：在 ConsumerController.java 中，定义了 @Autowired 注解的 ConsumerService 服务。
画面 11：在 ConsumerController.java 中，定义了 @RestController 注解的类，并添加了 @Api(tags = "Consumer", description = "用户服务API") 注解。
画面 12：再次展示数据库表 pzp_consumer 的结构。
画面 13：在 ConsumerController.java 中，定义了 @ApiOperation 注解的 register 方法，用于处理用户注册请求。
画面 14：在 ConsumerController.java 中，定义了 @ApiImplicitParam 注解的 register 方法，用于处理用户注册请求。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
import com.baidou.rybation.bus.core.conditions.query.QueryWrapper;
import com.baidou.rybation.bus.extension.service.impl.ServiceImpl;
import org.springframework.beans.BeanUtils;

public class ConsumerServiceImpl extends ServiceImpl<ConsumerMapper, Consumer> implements ConsumerService {

    @Override
    public Integer checkMobile(String mobile) {
        return getBMobile(mobile) != null ? 1 : 0;
    }

    private ConsumerDTO getBMobile(String mobile) {
        Consumer consumer = getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
        return convertConsumerEntityToDTO(consumer);
    }

    @Override
    public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    }
}
```

画面 2：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException();
    }
}
```

画面 3：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
}
```

画面 4：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
}
```

画面 5：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    save(consumer);
}
```

画面 6：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodePrefixUtil.getNo(CodePrefixUtil.CODE_REQUEST_PREFIX));
    save(consumer);
}
```

画面 7：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodePrefixUtil.getNo(CodePrefixUtil.CODE_REQUEST_PREFIX));
    save(consumer);
}
```

画面 8：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodePrefixUtil.getNo(CodePrefixUtil.CODE_REQUEST_PREFIX));
    save(consumer);
}
```

画面 9：
```sql
CREATE TABLE `pzp_consumer` (
  `ID` varchar(60) NOT NULL,
  `USERNAME` varchar(60) NOT NULL,
  `FULLNAME` varchar(60) NOT NULL,
  `MOBILE` varchar(60) NOT NULL,
  `ROLE` varchar(60) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `REQUEST_ID` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 10：
```java
@Autowired
private ConsumerService consumerService;
```

画面 11：
```java
@RestController
@Api(tags = "Consumer", description = "用户服务API")
public class ConsumerController implements ConsumerAPI {

    @Autowired
    private ConsumerService consumerService;

    @ApiOperation("测试hello")
    @GetMapping(path = "/hello")
    public String hello() {
        return "hello";
    }

    @ApiOperation("测试hi")
    @GetMapping(path = "/hi")
    @ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
    public String hi(String name) {
        return "hi," + name;
    }
}
```

画面 12：
```sql
CREATE TABLE `pzp_consumer` (
  `ID` varchar(60) NOT NULL,
  `USERNAME` varchar(60) NOT NULL,
  `FULLNAME` varchar(60) NOT NULL,
  `MOBILE` varchar(60) NOT NULL,
  `ROLE` varchar(60) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `REQUEST_ID` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

画面 13：
```java
@Override
public void register(ConsumerRegisterDTO consumerRegisterDTO) {
    if (checkMobile(consumerRegisterDTO.getMobile()) == 1) {
        throw new BusinessException(ConsumerErrorCode);
    }
    Consumer consumer = new Consumer();
    BeanUtils.copyProperties(consumerRegisterDTO, consumer);
    consumer.setUserName(CodePrefixUtil.getNo(CodePrefixUtil.CODE_REQUEST_PREFIX));
    save(consumer);
}
```

画面 14：
```java
@ApiOperation("用户注册")
@ApiImplicitParam(name = "AccountRegisterDTO", value = "注册信息", required = true, dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumer")
public RestResponse register(ConsumerRegisterDTO consumerRegisterDTO) {
    return RestResponse.success();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
