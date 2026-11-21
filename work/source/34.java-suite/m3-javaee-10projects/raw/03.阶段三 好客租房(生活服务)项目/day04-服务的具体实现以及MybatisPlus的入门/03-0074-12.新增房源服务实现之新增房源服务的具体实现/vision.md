# 画面线理解：12.新增房源服务实现之新增房源服务的具体实现

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\12.新增房源服务实现之新增房源服务的具体实现【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 02:14, 03:21, 04:59, 07:11, 09:02, 10:17, 12:01, 14:38, 15:53, 17:37, 19:22, 20:23, 22:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:46:51

1) 这一组画面整体在讲如何使用 Spring Boot + MyBatis-Plus + Dubbo 构建一个房屋资源管理服务的提供者（Provider）。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，当前选中 `HouseResources.java`，该类是实体类，包含 `@TableField` 和 `@TableName` 注解，定义了数据库表 `tb_house_resources`。
画面2：在 IDE 中打开 `ApiHouseResourcesService.java`，显示了接口定义，同时弹出 PDF 文档预览，显示了课程内容目录。
画面3：展示 `application.properties` 配置文件，配置了 Spring Boot 应用名、数据源、Dubbo 服务名、协议、端口、ZooKeeper 注册中心地址。
画面4：PDF 文档中显示“4.7.2. 编写HouseResourcesMapper接口”，并展示了 `HouseResourcesMapper` 接口的代码，继承自 `BaseMapper<HouseResources>`。
画面5：PDF 文档中显示“4.7.3. 编写service”，并展示了 `HouseResourcesService` 接口的代码，定义了 `saveHouseResources` 方法。
画面6：在 IDE 中展示 `BaseService` 类中 `queryPageListByWhere` 方法的实现，用于分页查询。
画面7：在 IDE 中右键点击 `HouseResourcesServiceImpl` 类，弹出创建类的菜单，准备创建实现类。
画面8：在 IDE 中展示 `HouseResourcesServiceImpl` 类的代码，包含 `@Transactional` 注解，并显示了 `super.save` 方法的自动补全。
画面9：在 IDE 中展示 `HouseResourcesServiceImpl` 类的代码，添加了对 `title` 字段的非空校验逻辑。
画面10：在 IDE 中展示 `ApiHouseResourcesService` 接口的代码，使用 `@Service` 注解，并显示了 `@Autowired` 注解的自动补全。
画面11：在 IDE 中展示 `DubboProvider.java` 的代码，使用 `@SpringBootApplication` 注解，并配置了 `WebApplicationType.NONE`。
画面12：在终端中执行 `java -jar` 命令启动服务，输出了 Dubbo 服务的映射信息。
画面13：在 IDE 中展示 `DubboProvider.java` 的代码，显示了启动时的警告信息，提示 `@Configuration` 类不能被所有 `BeanPostProcessor` 处理。
画面14：PDF 文档中显示“4.9. 进行测试”，并展示了测试界面，显示了服务已注册到注册中心。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1：
```java
package cn.itcast.haoke.dubbo.server.pojo;
import ...
/**
 * 房源表
 * @author itcast
 */
@Data
@Accessors(chain = true)
@TableName("tb_house_resources")
public class HouseResources extends BasePojo {
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;
    /* 房源标题 */
    private String title;
    /* 房源id */
}
```

画面3：
```properties
# Spring Boot application name
spring.application.name = itcast-haoke-manage-dubbo-server-house-resources

# 数据库
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://172.16.55.185:3306/haoke?useUnicode=true&characterEncoding=utf8&autoReconnect=true
spring.datasource.username=root
spring.datasource.password=root

# 服务的扫描包
dubbo.basePackages = cn.itcast.haoke.dubbo.server.api

# 应用名称
dubbo.application.name = dubbo-provider-house-resources

# 协议以及端口
dubbo.protocol.name = dubbo
dubbo.protocol.port = 20881

# zk注册中心
dubbo.registry.address = zookeeper://172.16.55.185:2181
dubbo.registry.client = zkclient
```

画面4：
```java
package cn.itcast.haoke.dubbo.server.mapper;
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import com.baidou.mybatplus.core.mapper.BaseMapper;
public interface HouseResourcesMapper extends BaseMapper<HouseResources> {
}
```

画面5：
```java
package cn.itcast.haoke.dubbo.server.service;
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
public interface HouseResourcesService {
    @Param("record")
    int saveHouseResources(HouseResources houseResources);
}
```

画面6：
```java
public List<T> queryListByWhere(T record) {
    return this.mapper.selectList(new QueryWrapper<>(record));
}

public IPage<T> queryPageListByWhere(T record, Integer page, Integer rows) {
    return this.mapper.selectPage(new Page<>(page, rows), new QueryWrapper<>(record));
}
```

画面8：
```java
package cn.itcast.haoke.dubbo.server.service.impl;
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.service.HouseResourcesService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
public class HouseResourcesServiceImpl extends BaseServiceImpl implements HouseResourcesService {
    @Override
    public int saveHouseResources(HouseResources houseResources) {
        return super.save(houseResources);
    }
}
```

画面9：
```java
@Override
public int saveHouseResources(HouseResources houseResources) {
    // 添加校验或者其他的逻辑
    if (StringUtils.isBlank(houseResources.getTitle())) {
        // 不符合要求
        return -1;
    }
    return super.save(houseResources);
}
```

画面10：
```java
package cn.itcast.haoke.dubbo.server;
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import com.alibaba.dubbo.config.annotation.Service;
@Service(version = "1.0.0")
public class ApiHouseResourcesService {
    private Map<String, Object> map = new HashMap<>();
    private List<Handler> handlers = new ArrayList<>();
    private Handler handler;
    private Handler hierarchyBoundsAdapter;
    private HierarchyBoundsListener hierarchyBoundsListener;
}
```

画面11：
```java
package cn.itcast.haoke.dubbo.server;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
@SpringBootApplication
public class DubboProvider {
    public static void main(String[] args) {
        new SpringApplicationBuilder(DubboProvider.class)
            .web(WebApplicationType.NONE) // 非 Web 应用
            .run(args);
    }
}
```

画面12：
```bash
2018-11-16 00:58:54.362  INFO 33434 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/api/env/rules],methods=[GET]}" onto public java.util.List<org.apache.dubbo.admin.dto.BalancingDTO> org.apache.dubbo.admin.controller.LoadBalanceController.getBalancingList()
2018-11-16 00:58:54.365  INFO 33434 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/api/env/rules],methods=[DELETE]}" onto public boolean org.apache.dubbo.admin.controller.LoadBalanceController.deleteLoadBalance()
2018-11-16 00:58:54.365  INFO 33434 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/api/env/rules],methods=[POST]}" onto public boolean org.apache.dubbo.admin.controller.LoadBalanceController.overridesController.enableRoute()
2018-11-16 00:58:54.365  INFO 33434 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/api/env/rules],methods=[PUT]}" onto public boolean org.apache.dubbo.admin.controller.LoadBalanceController.updateRoute()
```

画面13：
```java
package cn.itcast.haoke.dubbo.server;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
@SpringBootApplication
public class DubboProvider {
    public static void main(String[] args) {
        new SpringApplicationBuilder(DubboProvider.class)
            .web(WebApplicationType.NONE) // 非 Web 应用
            .run(args);
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2：PDF 文档标题为“讲义.pdf”，内容目录包括“4.3.1. itcast-haoke-manage-dubbo-server-house-resources-dubbo-interface”、“4.4. 编写BasePojo文件”、“4.5. 使用MyBatisPlus的CodeGenerator生成代码文件”、“4.6. 定义新增的dubbo服务”、“4.7. 编写application.properties文件”。
画面4：PDF 文档标题为“4.7.2. 编写HouseResourcesMapper接口”，内容包括 `HouseResourcesMapper` 接口的代码。
画面5：PDF 文档标题为“4.7.3. 编写service”，内容包括 `HouseResourcesService
