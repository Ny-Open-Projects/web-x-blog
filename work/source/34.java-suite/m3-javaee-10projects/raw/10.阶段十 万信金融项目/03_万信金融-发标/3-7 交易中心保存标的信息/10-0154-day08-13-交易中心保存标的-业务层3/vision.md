# 画面线理解：day08-13-交易中心保存标的-业务层3

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-13-交易中心保存标的-业务层3_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:28, 01:09, 01:31, 02:15, 02:47, 03:18, 03:53, 05:07, 07:41, 08:57, 09:31, 10:06, 10:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:52:15

1) 这一组画面整体在讲如何在 Java 项目中通过 Service 层将前端传入的 ProjectDTO 转换为数据库实体 Project，并设置其属性、调用配置服务获取参数、构造查询条件并最终保存到数据库。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 代码：在 ProjectServiceImpl.java 中，设置 ProjectDTO 的属性，如项目编号、状态、创建时间、还款方式、类型等，并调用 convertProjectDTOToEntity 方法转换，最后调用 save(project) 保存。
- 代码片段：
  ```java
  projectDTO.setProjectNo(CodePrefixCode.CODE_PROJECT_PREFIX);
  projectDTO.setProjectStatus(ProjectCode.COLLECTING.getCode());
  projectDTO.setStatusCode(StatusCode.STATUS_OUT.getCode());
  projectDTO.setCreateDate(LocalDateTime.now());
  projectDTO.setRepaymentWay(RepaymentWayCode.FIXED_REPAYMENT.getCode());
  projectDTO.setType("NEW");
  Project project = convertProjectDTOToEntity(projectDTO);
  save(project);
  ```

画面 2:
- 代码：展示 Project 实体类中定义的字段，如 projectNo、name、description、type，每个字段上都有 @TableField 注解指定数据库列名。

画面 3:
- 界面：Apollo 配置中心页面，显示了多个已发布的配置项，其中包含分库分表策略，如 PROJECT_ID 的分片策略。

画面 4:
- 代码：ConfigService.java 中定义了获取配置项的方法，如 getAnnualRate() 和 getMinInvestmentAmount()，用于获取年化利率和最小投资金额。

画面 5:
- 代码：ProjectServiceImpl.java 中导入了多个包，包括实体类、Mapper、Service、ConfigService 等。

画面 6:
- 代码：在 ProjectServiceImpl.java 中，调用 ConfigService 获取配置，设置 ProjectDTO 的属性，如年化利率、委托转让等。

画面 7:
- 代码：在 ProjectServiceImpl.java 中，设置 ProjectDTO 的属性，如年化利率、委托转让等，并调用 save(project) 保存。

画面 8:
- 界面：DBeaver 数据库管理工具，显示了 pgy_transaction_0 数据库中的 pgy_transaction_2 表，表结构包含 ID、CONSUMER_ID、PROJECT_NO、NAME、DESCRIPTION、TYPE、PERIOD、ANNUAL_RATE、BORROWER_ANNUAL_RATE、COMMISSION_ANNUAL_RATE 等字段。

画面 9:
- 界面：DBeaver 数据库管理工具，显示了 pgy_transaction_0 数据库中的 pgy_transaction_2 表，表结构包含 ID、CONSUMER_ID、PROJECT_NO、NAME、DESCRIPTION、TYPE、PERIOD、ANNUAL_RATE、BORROWER_ANNUAL_RATE、COMMISSION_ANNUAL_RATE 等字段。

画面 10:
- 代码：在 ProjectServiceImpl.java 中，根据消费者性别设置项目名称，如“女士”或“先生”，并构造查询条件。

画面 11:
- 代码：在 ProjectServiceImpl.java 中，使用 QueryWrapper 构造查询条件，设置项目 ID 等条件，并调用 save(project) 保存。

画面 12:
- 代码：在 ProjectServiceImpl.java 中，调用 convertProjectDTOToEntity 方法转换 ProjectDTO 为 Project 实体，并设置其属性。

画面 13:
- 代码：在 ProjectServiceImpl.java 中，设置 ProjectDTO 的属性，如年化利率、委托转让等，并调用 save(project) 保存。

画面 14:
- 代码：在 ProjectServiceImpl.java 中，设置 ProjectDTO 的属性，如年化利率、委托转让等，并调用 save(project) 保存。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```java
projectDTO.setProjectNo(CodePrefixCode.CODE_PROJECT_PREFIX);
projectDTO.setProjectStatus(ProjectCode.COLLECTING.getCode());
projectDTO.setStatusCode(StatusCode.STATUS_OUT.getCode());
projectDTO.setCreateDate(LocalDateTime.now());
projectDTO.setRepaymentWay(RepaymentWayCode.FIXED_REPAYMENT.getCode());
projectDTO.setType("NEW");
Project project = convertProjectDTOToEntity(projectDTO);
save(project);
```

画面 2:
```java
@TableField("PROJECT_NO")
private String projectNo;

@TableField("NAME")
private String name;

@TableField("DESCRIPTION")
private String description;

@TableField("TYPE")
private String type;
```

画面 3:
- 配置项：
  - `spring.shardingsphere.sharding.tables.project.tenant_id`：`PROJECT_ID`
  - `spring.shardingsphere.sharding.tables.tender.tenant_id`：`PROJECT_ID % 2`

画面 4:
```java
public BigDecimal getAnnualRate() {
    return getBorrowerAnnualRate().subtract(getCommissionAnnualRate());
}

public BigDecimal getMinInvestmentAmount() {
    return new BigDecimal(config.getProperty("mini.investment.amount", "100.0"));
}
```

画面 5:
```java
import cn.cesta.wanxingp.transaction.entity.Project;
import cn.cesta.wanxingp.transaction.mapper.ProjectMapper;
import com.baidubce.bcejava.common.domain.ConsumerDTO;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common.domain.ConsumerId;
import com.baidubce.bcejava.common
