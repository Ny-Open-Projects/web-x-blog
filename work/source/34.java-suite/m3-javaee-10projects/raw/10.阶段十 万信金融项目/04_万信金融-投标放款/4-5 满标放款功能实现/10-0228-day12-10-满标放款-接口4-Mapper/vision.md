# 画面线理解：day12-10-满标放款-接口4-Mapper

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-10-满标放款-接口4-Mapper_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:34, 01:04, 01:31, 02:01, 02:29, 02:50, 03:13, 03:50, 04:09, 04:27, 04:45, 05:05, 05:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:52:00

1) 这一组画面整体在讲什么（一句话）：
讲解万能金融平台还款服务中“启动还款接口”的业务流程与对应的 MyBatis 数据访问层（Mapper）接口及配置文件的开发实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款服务启动还款接口的时序图，包含多个步骤，如保存交易记录、调用接口、修改状态、生成还款计划等。
画面2：展示PPT内容，讲解“3.2.5 还款服务启动还款接口(接口④)”中的“还款方式”，包括月利率、每月还款额、第n月利息的计算公式。
画面3：PPT页面，继续讲解“3.2.5.2 功能实现”部分，指出在mapper包中定义PlanMapper接口。
画面4：IDE界面，显示在项目中创建新文件的菜单，准备创建新的Java类或接口。
画面5：展示多个窗口，包括PPT、IDE、数据库工具等，说明开发环境。
画面6：IDE界面，显示RepaymentPlan.java文件，其中定义了还款计划实体类。
画面7：IDE界面，显示PlanMapper.java文件，定义了PlanMapper接口。
画面8：IDE界面，显示创建新类的对话框，准备创建ReceiveablePlanMapper接口。
画面9：PPT页面，继续讲解“3.2.5.2 功能实现”，列出需要创建的三个部分：定义PlanMapper接口、新建PlanMapper.xml配置文件、定义ReceiveablePlanMapper接口。
画面10：IDE界面，显示创建ReceiveablePlanMapper接口的对话框。
画面11：IDE界面，显示ReceiveablePlan.java文件，定义了还款计划实体类的属性。
画面12：IDE界面，显示ReceiveablePlanMapper.java文件，定义了ReceiveablePlanMapper接口。
画面13：IDE界面，显示ReceiveablePlanMapper.xml文件，其中包含MyBatis的XML配置。
画面14：PPT页面，再次展示“3.2.5.2 功能实现”的内容，强调在mapper包中定义PlanMapper接口和新建PlanMapper.xml配置文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
月利率 = 借款年利率 / 12
每月还款额 = 借款本金 × [月利率 × (1 + 月利率) ^ 借款月数] / [(1 + 月利率) ^ 借款月数 - 1]
第n月利息 = 本金 × 月利率 × (1 + 月利率) ^ (n - 1) - [ (1 + 月利率) ^ (n - 1) - 1 ] × 月利率

画面3：
```java
/**
 * 还款计划：针对借款人的 保存到表中
 * 借款人还款计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {
```

画面6：
```java
package cn.itcast.wanxing2p.repayment.entity;

import java.io.Serializable;

/**
 * 借款人还款计划
 */
@TableName("repayment_plan")
public class RepaymentPlan implements Serializable {
    private static final long serialVersionUID = 1L;

    // 三链
    @TableId("ID")
    private Long id;

    // 投标人用户标识
    @TableField("CONSUMER_ID")
    private Long consumerId;

    // 投标人用户编码
    @TableField("USER_NO")
    private String userNo;
```

画面7：
```java
package cn.itcast.wanxing2p.repayment.mapper;

import cn.itcast.wanxing2p.repayment.entity.RepaymentPlan;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

/**
 * 借款人还款计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {
```

画面9：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.wanxing2p.repayment.mapper.PlanMapper">
```

画面11：
```java
package cn.itcast.wanxing2p.repayment.entity;

import java.io.Serializable;

/**
 * 借款人还款计划
 */
@TableName("repayment_plan")
public class RepaymentPlan implements Serializable {
    private static final long serialVersionUID = 1L;

    // 三链
    @TableId("ID")
    private Long id;

    // 投标人用户标识
    @TableField("CONSUMER_ID")
    private Long consumerId;

    // 投标人用户编码
    @TableField("USER_NO")
    private String userNo;
```

画面12：
```java
package cn.itcast.wanxing2p.repayment.mapper;

import cn.itcast.wanxing2p.repayment.entity.ReceivablePlan;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

/**
 * 借款人应收款 Mapper 接口
 */
public interface ReceivablePlanMapper extends BaseMapper<ReceivablePlan> {
```

画面13：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="cn.itcast.wanxing2p.repayment.mapper.ReceivablePlanMapper">
    <resultMap id="BaseResultMap" type="cn.itcast.wanxing2p.repayment.entity.ReceivablePlan">
        <id column="id" property="id" />
        <result column="consumer_id" property="consumerId" />
        <result column="user_no" property="userNo" />
        <result column="amount" property="amount" />
        <result column="status" property="status" />
        <result column="create_time" property="createTime" />
        <result column="update_time" property="updateTime" />
    </resultMap>
</mapper>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.1 还款方式”，内容包括还款方式的计算公式。
画面3：PPT标题为“3.2.5.2 功能实现”，内容包括“数据访问层”部分，列出三个步骤。
画面9：PPT标题为“3.2.5.2 功能实现”，内容包括“数据访问层”部分，列出三个步骤。
画面14：PPT标题为“3.2.5.2 功能实现”，内容包括“数据访问层”部分，列出三个步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
