# 画面线理解：day03-13-用户中心保存信息-Service-用户是否存在

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-13-用户中心保存信息-Service-用户是否存在_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:25, 02:29, 03:31, 04:38, 05:33, 07:15, 07:58, 08:42, 09:43, 10:19, 11:30, 12:00, 12:47, 13:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 05:36:16

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis-Plus 和 Lambda 表达式实现消费者服务的手机号校验与用户注册功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，聚焦于 `ConsumerMapper.xml` 文件，其内容为 MyBatis Mapper 配置，namespace 指向 `cn.itcast.wanxing2p.consumer.mapper.ConsumerMapper`。
画面 2: 展示 `ConsumerService.java` 接口，定义了 `checkMobile` 和 `register` 方法。
画面 3: 展示右键 `ConsumerService.java` 选择“Generate”生成实现类，提示将生成 `ConsumerServiceImpl`。
画面 4: 展示生成的 `ConsumerServiceImpl.java` 文件，其继承自 `ServiceImpl<ConsumerMapper, Consumer>` 并实现 `ConsumerService` 接口。
画面 5: 在 `ConsumerServiceImpl.java` 中，展示 `checkMobile` 方法的实现，当前返回 `null`。
画面 6: 在 `ConsumerServiceImpl.java` 中，将 `checkMobile` 方法改为私有方法，并添加了 `private` 修饰符。
画面 7: 展示 `ConsumerRegisterDTO` 类，其包含 `id`、`username`、`fullname`、`idNumber` 等字段，并使用 `@ApiModel` 和 `@ApiModelProperty` 注解。
画面 8: 在 `ConsumerServiceImpl.java` 中，展示 `getByMobile` 方法的 Lambda 表达式实现，使用 `QueryWrapper` 和 `lambda` 方法。
画面 9: 在 `ConsumerServiceImpl.java` 中，展示 `getByMobile` 方法的完整实现，使用 `QueryWrapper` 和 `lambda` 方法。
画面 10: 在 `ConsumerServiceImpl.java` 中，展示 `getByMobile` 方法的 Lambda 表达式实现，使用 `QueryWrapper` 和 `lambda` 方法。
画面 11: 展示一个 Word 文档，内容为“万方数据-消费者注册流程”，其中包含“检查手机号是否已注册”、“创建 Consumer 实体”、“保存 Consumer”等步骤。
画面 12: 屏幕空白，无内容。
画面 13: 展示 `ConsumerServiceImpl.java` 中 `convertConsumerEntityToDTO` 方法的实现，用于将实体转换为 DTO。
画面 14: 展示 `ConsumerServiceImpl.java` 中 `checkMobile` 方法的实现，当前返回 `null`，并展示 `getByMobile` 方法的 Lambda 表达式实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0.0/EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.wanxing2p.consumer.mapper.ConsumerMapper">
</mapper>
```

画面 2:
```java
package cn.itcast.wanxing2p.consumer.service;

public interface ConsumerService {
}
```

画面 4:
```java
package cn.itcast.wanxing2p.consumer.service;

import cn.itcast.wanxing2p.api.consumer.model.ConsumerRegisterDTO;
import cn.itcast.wanxing2p.consumer.entity.Consumer;
import cn.itcast.wanxing2p.consumer.mapper.ConsumerMapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;

public class ConsumerServiceImpl extends ServiceImpl<ConsumerMapper, Consumer> implements ConsumerService {
}
```

画面 5:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}
```

画面 6:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}

private getMobile(String mobile) {
}
```

画面 7:
```java
import ...

@Data
@ApiModel(value = "ConsumerDTO", description = "平台-端用户信息")
public class ConsumerDTO {

    @ApiModelProperty("用户id")
    private Long id;

    @ApiModelProperty("用户名")
    private String username;

    @ApiModelProperty("真实姓名")
    private String fullname;

    @ApiModelProperty("身份证号")
    private String idNumber;
}
```

画面 8:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}

private ConsumerDTO getMobile(String mobile) {
    return getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
}
```

画面 9:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}

private ConsumerDTO getMobile(String mobile) {
    return getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
}
```

画面 10:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}

private ConsumerDTO getMobile(String mobile) {
    return getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
}
```

画面 13:
```java
private ConsumerDTO convertConsumerEntityToDTO(Consumer entity) {
    if (entity == null) {
        return null;
    }
    ConsumerDTO dto = new ConsumerDTO();
    BeanUtils.copyProperties(entity, dto);
    return dto;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 11:
标题：“万方数据-消费者注册流程”
内容：
- 4.5.1 检查手机号是否已注册
- 4.5.2 生成用户信息
- 4.5.3 保存用户信息
- 4.5.4 返回结果
- 4.5.5 保存用户信息
- 4.5.6 保存用户信息
- 4.5.7 保存用户信息
- 4.5.8 保存用户信息
- 4.5.9 保存用户信息
- 4.5.10 保存用户信息
- 4.5.11 保存用户信息
- 4.5.12 保存用户信息
- 4.5.13 保存用户信息
- 4.5.14 保存用户信息
- 4.5.15 保存用户信息
- 4.5.16 保存用户信息
- 4.5.17 保存用户信息
- 4.5.18 保存用户信息
- 4.5.19 保存用户信息
- 4.5.20 保存用户信息
- 4.5.21 保存用户信息
- 4.5.22 保存用户信息
- 4.5.23 保存用户信息
- 4.5.24 保存用户信息
- 4.5.25 保存用户信息
- 4.5.26 保存用户信息
- 4.5.27 保存用户信息
- 4.5.28 保存用户信息
- 4.5.29 保存用户信息
- 4.5.30 保存用户信息
- 4.5.31 保存用户信息
- 4.5.32 保存用户信息
- 4.5.33 保存用户信息
- 4.5.34 保存用户信息
- 4.5.35 保存用户信息
- 4.5.36 保存用户信息
- 4.5.37 保存用户信息
- 4.5.38 保存用户信息
- 4.5.39 保存用户信息
- 4.5.40 保存用户信息
- 4.5.41 保存用户信息
- 4.5.42 保存用户信息
- 4.5.43 保存用户信息
- 4.5.44 保存用户信息
- 4.5.45 保存用户信息
- 4.5.46 保存用户信息
- 4.5.47 保存用户信息
- 4.5.48 保存用户信息
- 4.5.49 保存用户信息
- 4.5.50 保存用户信息
- 4.5.51 保存用户信息
- 4.5.52 保存用户信息
- 4.5.53 保存用户信息
- 4.5.54 保存用户信息
- 4.5.55 保存用户信息
- 4.5.56 保存用户信息
- 4.5.57 保存用户信息
- 4.5.58 保存用户信息
- 4.5.59 保存用户信息
- 4.5.60 保存用户信息
- 4.5.61 保存用户信息
- 4.5.62 保存用户信息
- 4.5.63 保存用户信息
- 4.5.64 保存用户信息
