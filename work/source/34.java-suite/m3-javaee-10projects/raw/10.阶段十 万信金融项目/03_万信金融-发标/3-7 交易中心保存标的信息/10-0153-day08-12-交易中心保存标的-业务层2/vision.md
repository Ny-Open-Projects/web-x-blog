# 画面线理解：day08-12-交易中心保存标的-业务层2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-12-交易中心保存标的-业务层2_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:18, 02:34, 03:52, 04:28, 05:02, 05:48, 07:12, 08:37, 09:51, 10:50, 13:12, 13:51, 14:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:51:20

1) 这一组画面整体在讲如何在交易中心服务中通过 Feign 调用消费者服务，实现借款项目创建功能，并涉及数据库分库分表配置。

2) 按时间顺序列出每张画面的要点：
画面1：在交易中心服务中创建 Feign 远程调用消费者服务的接口定义。
画面2：在 service 包中新建 ProjectServiceImpl 类实现 createProject 方法，调用 ConsumerApiAgent。
画面3：展示 P2P 平台借款项目申请页面，用于演示业务场景。
画面4：在 ProjectServiceImpl 中调用 consumerApiAgent.getCurrConsumer() 获取借款人信息。
画面5：展示 ProjectDTO 类定义，包含借款人标识、项目编号、名称、描述等字段。
画面6：展示 ProjectDTO 类中 status、isAssignment、requestNo、remainingAmount、risk 等字段定义。
画面7：展示项目管理后台的多个窗口，包括数据库、代码编辑器和文件资源管理器。
画面8：展示 ProjectCode.java 中定义的项目状态常量，包括 COLLECTING、FULLY、REPAYING、FINISH。
画面9：展示 TransactionController 中的 @Api 注解和 createProject 方法，用于调用 ProjectService。
画面10：展示 Project 实体类，包含 ID、consumerId、userNo 等字段。
画面11：展示 Project 实体类中 annualRate、borrowerAnnualRate、commissionAnnualRate、repaymentWay 等字段。
画面12：展示 Apollo 配置中心的空白页面。
画面13：展示 Apollo 配置中心 application 的 properties 配置，包含数据库连接、分库分表策略等。
画面14：在 ProjectServiceImpl 中设置项目状态、创建时间、还款方式等属性，并调用 save 方法保存。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
@ApiOperation("获取登录用户信息")
@GetMapping("/i/currConsumer")
public RestResponse<ConsumerDTO> getCurrConsumer() {
    ConsumerDTO consumerDTO = consumerService
            .getMobileSecurityUtil().getMobile();
    return RestResponse.success(consumerDTO);
}
```
```java
// C服务代理
@FeignClient(value = "consumer-service")
public interface ConsumerApiAgent {
    @GetMapping("/i/currConsumer")
    public RestResponse<ConsumerDTO> getCurrConsumer();
}
```

画面2：
```java
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class ProjectServiceImpl extends ServiceImpl<ProjectMapper, Project> implements ProjectService {
    @Autowired
    private ConsumerApiAgent consumerApiAgent;
    @Override
    public ProjectDTO createProject(ProjectDTO project) {
        RestResponse<ConsumerDTO> consumerResponse = consumerApiAgent.getCurrConsumer();
        // ...
    }
}
```

画面4：
```java
RestResponse<ConsumerDTO> consumerResponse = consumerApiAgent.getCurrConsumer();
projectDTO.setConsumerId(consumerResponse.getData().getConsumerId());
projectDTO.setUserName(consumerResponse.getData().getUserName());
projectDTO.setMobile(consumerResponse.getData().getMobile());
projectDTO.setProjectNo(projectNo);
projectDTO.setName(name);
projectDTO.setDesc(desc);
```

画面5：
```java
private String projectNo;
private String name;
private String desc;
```

画面6：
```java
private Integer status;
private Integer isAssignment;
private String requestNo;
private BigDecimal remainingAmount;
private String risk = "B";
```

画面8：
```java
COLLECTING("募集期"),
FULLY("已满标"),
REPAYING("还款中"),
FINISH("已结标");
```

画面9：
```java
@Api(value = "交易中心服务", tags = "transaction")
@RestController
@RequestMapping("/transaction")
public class TransactionController {
    @Autowired
    private ProjectService projectService;
    @PostMapping("/createProject")
    public RestResponse<ProjectDTO> createProject(@RequestBody ProjectDTO projectDTO) {
        return projectService.createProject(projectDTO);
    }
}
```

画面10：
```java
@TableId("ID")
private Long id;
@TableField("CONSUMER_ID")
private Long consumerId;
@TableField("USER_NO")
private String userNo;
```

画面11：
```java
@TableField("ANNUAL_RATE")
private BigDecimal annualRate;
@TableField("BORROWER_ANNUAL_RATE")
private BigDecimal borrowerAnnualRate;
@TableField("COMMISSION_ANNUAL_RATE")
private BigDecimal commissionAnnualRate;
@TableField("REPAYMENT_WAY")
private String repaymentWay;
```

画面13：
```properties
spring.shardingsphere.datasource.names=ds0,ds1
spring.shardingsphere.datasource.ds0.jdbc-url=jdbc:mysql://localhost:3306/p2p_transaction?useUnicode=true&characterEncoding=utf8&allowMultiQueries=true&autoReconnect=true&failOverReadOnly=false&maxAllowedPacket=100M
spring.shardingsphere.datasource.ds0.username=root
spring.shardingsphere.datasource.ds0.password=123
spring.shardingsphere.datasource.ds1.jdbc-url=jdbc:mysql://localhost:3306/p2p_transaction?useUnicode=true&characterEncoding=utf8&allowMultiQueries=true&autoReconnect=true&failOverReadOnly=false&maxAllowedPacket=100M
spring.shardingsphere.datasource.ds1.username=root
spring.shardingsphere.datasource.ds1.password=123
spring.shardingsphere.sharding.tables.project.actual-data-nodes=ds$->{0..1}.project_$->{0..1}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID % 2}
spring.shardingsphere.sharding.tables.tender.actual-data-nodes=ds$->{0..1}.tender_$->{0..1}
spring.shardingsphere.sharding.tables.tender.table-strategy.inline.algorithm-expression=tender_$->{ID % 2}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID % 2}
spring.shardingsphere.sharding.tables.tender.table-strategy.inline.algorithm-expression=tender_$->{ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes=ds$->{0..1}.project_$->{0..1}
spring.shardingsphere.sharding.tables.tender.actual-data-nodes=ds$->{0..1}.tender_$->{0..1}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID % 2}
spring.shardingsphere.sharding.tables.tender.table-strategy.inline.algorithm-expression=tender_$->{ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes=ds$->{0..1}.project_$->{0..1}
spring.shardingsphere.sharding.tables.tender.actual-data-nodes=ds$->{0..1}.tender_$->{0..1}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID % 2}
spring.shardingsphere.sharding.tables.tender.table-strategy.inline.algorithm-expression=tender_$->{ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes=ds$->{0..1}.project_$->{0..1}
spring.shardingsphere.sharding.tables.tender.actual-data-nodes=ds$->{0..1}.tender_$->{0..1}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID % 2}
spring.shardingsphere.sharding.tables.tender.table-strategy.inline.algorithm-expression=tender_$->{ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes=ds$->{0..1}.project_$->{0..1}
spring.shardingsphere.sharding.tables.tender.actual-data-nodes=ds$->{0..1}.tender_$->{0..1}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID % 2}
spring.shardingsphere.sharding.tables.tender.table-strategy.inline.algorithm-expression=tender_$->{ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes=ds$->{0..1}.project_$->{0..1}
spring.shardingsphere.sharding.tables.tender.actual-data-nodes=ds$->{0..1}.tender_$->{0..1}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID % 2}
spring.shardingsphere.sharding.tables.tender.table-strategy.inline.algorithm-expression=tender_$->{ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes=ds$->{0..1}.project_$->{0..1}
spring.shardingsphere.sharding.tables.tender.actual-data-nodes=ds$->{0..1}.tender_$->{0..1}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID % 2}
spring.shardingsphere.sharding.tables.tender.table-strategy.inline.algorithm-expression=tender_$->{ID % 2}
spring.shardingsphere.sharding.tables.project.actual-data-nodes=ds$->{0..1}.project_$->{0..1}
spring.shardingsphere.sharding.tables.tender.actual-data-nodes=ds$->{0..1}.tender_$->{0..1}
spring.shardingsphere.sharding.tables.project.table-strategy.inline.algorithm-expression=project_$->{ID %
