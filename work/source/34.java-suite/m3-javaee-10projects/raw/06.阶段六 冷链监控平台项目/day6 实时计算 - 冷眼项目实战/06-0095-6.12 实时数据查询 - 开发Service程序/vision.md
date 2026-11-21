# 画面线理解：6.12 实时数据查询 - 开发Service程序

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.12 实时数据查询 - 开发Service程序_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:08, 02:02, 02:43, 03:28, 04:59, 06:26, 07:37, 09:07, 09:48, 10:17, 11:35, 13:07, 13:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:36:46

1) 这一组画面整体在讲如何在 Spring Boot 项目中，通过定义接口和实现类，使用 MyBatis-Plus 的 QueryWrapper 来构建动态分页查询条件。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示项目结构和启动类 MonitorApplication，其中包含 @SpringBootApplication 和 @EnableDiscoveryClient 注解。
画面 2: 定义服务接口 MessageService，继承自 IService。
画面 3: 在 MessageService 接口中添加方法 queryMessageRealtime，参数为 Map<String, Object>。
画面 4: 创建实现类 MessageServiceImpl。
画面 5: 在 MessageServiceImpl 中声明继承关系，并引入 MyBatis-Plus 的 ServiceImpl 和实体类。
画面 6: 在 MessageServiceImpl 中重写 queryMessageRealtime 方法，使用 Page 和 QueryWrapper。
画面 7: 在 queryMessageRealtime 方法中，使用 QueryWrapper 的构造函数创建对象。
画面 8: 在 queryMessageRealtime 方法中，从参数中提取 page 和 size，并设置到 Page 对象。
画面 9: 在 queryMessageRealtime 方法中，使用 Ctrl+Shift+空格 自动补全 QueryWrapper 的方法。
画面 10: 在 queryMessageRealtime 方法中，定义私有方法 getMessageCondition。
画面 11: 在 getMessageCondition 方法中，使用 QueryWrapper 的 eq 方法设置条件。
画面 12: 在 getMessageCondition 方法中，对参数 company_id 进行非空判断。
画面 13: 在 getMessageCondition 方法中，使用 QueryWrapper 的 eq 方法设置 company_id 条件。
画面 14: 在 getMessageCondition 方法中，完成条件设置并返回 QueryWrapper。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```java
package com.ithema;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class MonitorApplication {
    public static void main(String[] args) {
        SpringApplication.run(MonitorApplication.class, args);
    }
}
```

画面 2:
```java
package com.ithema.com.ithema.cold.monitor.service;
import com.baidou.mybatplus.extension.service.IService;
public interface MessageService extends IService {
}
```

画面 3:
```java
package com.ithema.com.ithema.cold.monitor.service;
import com.baidou.mybatplus.extension.service.IService;
import com.ithema.cold.common.netty.MessageEntity;
public interface MessageService extends IService<MessageEntity> {
    IPage queryMessageRealtime(Map<String, Object> params);
}
```

画面 4:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
public class MessageServiceImpl {
}
```

画面 5:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.service.MessageService;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
}
```

画面 6:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        return this;
    }
}
```

画面 7:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        return this.page(new Page<MessageEntity>(1, 10), queryWrapper);
    }
}
```

画面 8:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
}
```

画面 9:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
}
```

画面 10:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
    private QueryWrapper getMessageCondition(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        return queryWrapper;
    }
}
```

画面 11:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
    private QueryWrapper getMessageCondition(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        String companyId = params.get("companyId") == null ? params.get("companyId").toString().trim() : "";
        return queryWrapper;
    }
}
```

画面 12:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty.MessageEntity;
import com.ithema.cold.monitor.service.MessageService;
import java.util.Map;
public class MessageServiceImpl extends ServiceImpl<MessageDao, MessageEntity> implements MessageService {
    @Override
    public IPage queryMessageRealtime(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        int page = Integer.valueOf(params.get("page").toString());
        int size = Integer.valueOf(params.get("pageSize").toString());
        return this.page(new Page<MessageEntity>(page, size), queryWrapper);
    }
    private QueryWrapper getMessageCondition(Map<String, Object> params) {
        QueryWrapper queryWrapper = new QueryWrapper();
        String companyId = params.get("companyId") == null ? params.get("companyId").toString().trim() : "";
        if (companyId != null && !"".equals(companyId)) {
            queryWrapper.eq("company_id", companyId);
        }
        return queryWrapper;
    }
}
```

画面 13:
```java
package com.ithema.com.ithema.cold.monitor.service.impl;
import com.baidou.mybatplus.core.metadata.IPage;
import com.baidou.mybatplus.extension.service.impl.ServiceImpl;
import com.ithema.cold.common.netty
