# day12-10-满标放款-接口4-Mapper

- 阶段：10.阶段十 万信金融项目
- 章节：04_万信金融-投标放款/4-5 满标放款功能实现
- 源文件：10.阶段十 万信金融项目\04_万信金融-投标放款\4-5 满标放款功能实现\day12-10-满标放款-接口4-Mapper_【海量资源尽在 666java.com】.mp4
- 时长 5分31秒（音频 331s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 了解了接口是要实现的这两个功能之后呢咱接下来就要编码动手去实现这两个功能那首先呢我们要从数据访问层开始大家注意了我们这个功能是不是主要是在哪实现的呀还款微服这是不是咱新增加了一个微服工厂对不对所以说我们要从哪从数据访问层开始因为咱前面说了嘛这个还款计划应声明信是不是要保存到什么呀表里边啊所以说这呢涉及到什么呀
[00:30] 数据库操作所以说咱需要从数据防范层开始那当然了由于我们采用了这个什么呀mybattlesplus所以说呢这个数据防范层呢编写起来是比较简单的啊大家大概看一下讲义吧我们是不是第一个要定义什么呀买法接口然后呢再新建跟他对应的什么呀对映射配置文件啊当然了我们需要定义两份啊一个是针对什么呀
[00:57] 针对还款计划的这个什么呀数据方案层一个是针对什么呀应收明细的吧我们刚才说了咱有两个功能吧一个是生成还款计划一个是生成应收明细这是对应的两张表嘛刚才让大家看了一下那咱接下来就开始一个一个来吧我们找到这个什么呀还款微服这个工厂我们找到呢这个Mapper包这是一个空包然后呢我们开始定义点右键
[01:30] 新建一个Mapper接口那我们跟讲义保持一致吧第一个接口叫PlanMapper指的就是那个什么还款计划啊你看好了叫PlanMapper这是一个接口Mapper接口那咱跟讲义保持一致吧把那些诸事啥的我们都考过来这个呢就是什么呀生成借款人还款计划的这个Mapper接口那我们的这个Mapper接口要干什么呀要继承谁的接口啊
[02:08] 对继承mybattispass的这个接口叫base Mapper大家应该还有印象那么在继承它的时候是不是要设置这个什么呀范形这个范形就叫repayment plan那么这个实体类呢其实对应的就是这个表对不对我们可以去这个实体类当中瞅一眼来看一下这里边的这个属性是不是跟刚才那个表里边字段都是什么呀一一对应的这个就不再说了啊因为刚才我们熟悉过这个表
[02:40] 这是跟这个表对应的实体类这是这个麦克接口是不是咱这样就定义完了对不对那我问大家一个问题啊这个接口是空的吗这个接口里面一个方案都没有吗可不是啊因为它继承了mybattispass的什么呀base map那这个接口里面是定义了最基本的什么自身感察的方法啊所以这需要大家注意的那接口有了之后呢接口有了之后咱接下来是不是就应该去干什么呀对新建一个相对应的映射配置文件叫planmap.xml
[03:11] 就在这儿新建一个咱之前是配了一个模板对吧这个名字呢我们也是叫什么呀对来麦克OK然后这里边是不是只需要把刚才麦克解口的这个路径放到这就行了啊cnditcast点在点点谁呀点retainment对吧点map点哎这是哪一块呢就搞定了
[03:42] 这是还款计划啊这个功能对应的数据访问层的接口和应设配有文件就搞定了那咱接下来去编写什么呀对应收明细啊就是投资人应收明细的Mapper接口和应设配有文件那这个接口的名字叫Receive Plan什么呀Mapper咱接下来创建一下比较简单同样的话它也要继承Base Mapper然后是不是也要指定一个
[04:16] 这个范型它的名字叫Receive Plan那么这个实体类对应的就是这个表是吧刚才跟大家看过了那咱也可以进去看它里边的这个属性吧它里边的这个属性跟表里边的这些字段也是什么呀对一一对应的具体用到时候再说这是接口就有了然后呢我们再新建一个跟它相对应的映射配置文件我们找一找在这儿
[04:46] 那名字呢我们还是叫这个什么呀还是叫这个名字然后呢这儿呢改成接口的路径就行了应该是这个对吧好这就把什么搞定了呀把应收明细这个功能对应的数据访问层的map接口和什么呀对硬设配有链就搞定了那这是整个数据访问层吧咱就全部编写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解万能金融平台还款服务中“启动还款接口”的业务流程与对应的 MyBatis 数据访问层（Mapper）接口及配置文件的开发实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示还款服务启动还款接口的时序图，包含多个步骤，如保存交易记录、调用接口、修改状态、生成还款计划等。
画面2：展示PPT内容，讲解“3.2.5 还款服务启动还款接口(接口④)”中的“还款方式”，包括月利率、每月还款额、第n月利息的计算公式。
画面3：PPT页面，继续讲解“3.2.5.2 功能实现”部分，指出在Mapper包中定义PlanMapper接口。
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
画面14：PPT页面，再次展示“3.2.5.2 功能实现”的内容，强调在Mapper包中定义PlanMapper接口和新建PlanMapper.xml配置文件。

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
package cn.itcast.wanxing2p.repayment.Mapper;

import cn.itcast.wanxing2p.repayment.entity.RepaymentPlan;
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;

/**
 * 借款人还款计划 Mapper 接口
 */
public interface PlanMapper extends BaseMapper<RepaymentPlan> {
```

画面9：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.itcast.wanxing2p.repayment.Mapper.PlanMapper">
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
package cn.itcast.wanxing2p.repayment.Mapper;

import cn.itcast.wanxing2p.repayment.entity.ReceivablePlan;
import com.baomidou.mybatisplus.core.Mapper.BaseMapper;

/**
 * 借款人应收款 Mapper 接口
 */
public interface ReceivablePlanMapper extends BaseMapper<ReceivablePlan> {
```

画面13：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.itcast.wanxing2p.repayment.Mapper.ReceivablePlanMapper">
    <resultMap id="BaseResultMap" type="cn.itcast.wanxing2p.repayment.entity.ReceivablePlan">
        <id column="id" property="id" />
        <result column="consumer_id" property="consumerId" />
        <result column="user_no" property="userNo" />
        <result column="amount" property="amount" />
        <result column="status" property="status" />
        <result column="create_time" property="createTime" />
        <result column="update_time" property="updateTime" />
    </resultMap>
</Mapper>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT标题为“3.2.5 还款服务启动还款接口(接口④)”，子标题“3.2.5.1 还款方式”，内容包括还款方式的计算公式。
画面3：PPT标题为“3.2.5.2 功能实现”，内容包括“数据访问层”部分，列出三个步骤。
画面9：PPT标题为“3.2.5.2 功能实现”，内容包括“数据访问层”部分，列出三个步骤。
画面14：PPT标题为“3.2.5.2 功能实现”，内容包括“数据访问层”部分，列出三个步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

