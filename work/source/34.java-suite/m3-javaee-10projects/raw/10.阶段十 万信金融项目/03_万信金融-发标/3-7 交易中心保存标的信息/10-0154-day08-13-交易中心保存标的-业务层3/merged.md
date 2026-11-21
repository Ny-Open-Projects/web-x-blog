# day08-13-交易中心保存标的-业务层3

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-13-交易中心保存标的-业务层3_【海量资源尽在 666java.com】.mp4
- 时长 10分40秒（音频 640s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那咱接下来还要接着写这块代码啊我们家还要干啥啊那我们说了这个project对象里面还有一些属性的值需要给是不是还有哪些属性的值需要给呢我大概给大家说一说就刚才这这个几个配到什么呀Apollo上的那些值就这些利率啊包括这个佣金啥的这些值都得给还有一个值还有一个挺麻烦的一个值啊就是就是这个标的的什么名字这还挺麻烦
[00:30] 为啥麻烦一会再说这是我们接下来还要给的几个值啊那咱接下来就要调用塞的方法开始给值啊那我们首先给阿博上那几个值啊那几个值呢我们主要是通过这个configure Service来获取到咱们前面是不是刚讲过这个东西可能一个serviceconfigure Service呢大家看一下他是不是专门用来干什么呀对用来从阿博上来获取这个值的啊他主要是通过configure对象
[01:00] 他有个方案叫get property这儿写的是不是就见的名字得到就是他对应的什么值这些就是件key后边得到这些就是什么值我们要得到就里边这几个值这些代码你不用想我们config Service直接给大家提供好你看这边获取的什么借款人的佣金投资人的佣金利率年化利率等等这些代码全部都已经写好
[01:28] 咱直接拿着用就可以了包括这个最小投标镜是不是你看这里边他都已经写好那咱接下来就开始直接调用他的什么对set方法开始取这些值然后进行存储就行了那咱就是project点都有谁set咱先set一个谁set这个包这个我们要取的值这是借款人的利率
[02:00] 净化利率应该是从卡飞格这个卡飞格Service咱是吧还没有注入是不是没有注入的话就注入一下那就是叫privateconfig Service然后我们就可以调用他的方法config Service.get跟他发明是一样的一个get一个set还有proproject.set还有谁
[02:37] 赛特咱应该还有一个投资人的这个一个利率年化利率对不对config Service.get就是他那其他我就不再挨个敲了啊这里边反正都是从这个config Service或者从阿卜罗上来取职的你看这还有一个平台佣金对吧还有阵营转让阵营转让其实咱现在还不涉及到呢不涉及到的话咱现在也该给一个处理值给一个处理值吧就是一个0
[03:15] 然后这是这一项转让啊这个不涉及到你就不用管他先给个处理指令然后接下来还有什么接下来其实就是那个什么呀接下来就是我们说的那个标底的名字我们说了呃非常麻烦啊为啥说麻烦呢大家看一下讲义很早的时候这个讲发表的时候你看看啊为啥说他麻烦你瞅瞅这个我们找一些这个标底的名字啊你就知道了你看这是一个标底信息吧是不是这是一个标底信息啊
[03:48] 那么照理让你看一下谁是标的的名字就这个就这个字段就这个谁啊内部啊对应的我们这个实体类当中就是这个内部这个标题的名称是啥其实就这好就谁谁谁第几次借款谁谁谁第几次借款谁谁谁第几次借款你觉得这个名字是不是我们得合成一下特别是里边哪些数据需要我们单独取一下这个人名谁谁谁你看这是董赵先生这是赵森先生对不对
[04:20] 然后第几次这个次数你也得查一下然后再拼成这么一个对字符串然后作为内幕属性的值去使用所以说它比较麻烦一些所以你看咱讲义里边具体是怎么实现的咱先看讲义的代码咱看一下这你看这你看这还涉及到先生女士呢你看这更麻烦啊这这这这这个你看先生女士一个就是这个谁啊
[04:51] 这个用户的真实性命还有就是第几次借款来这个代码一个一个来吧首先大家看一下我们这是得到了这是得到他的什么信息当前动用户的什么信息ad number应该是什么身份证号吧ad number来咱瞅瞅聊里边consumer啊瞅一瞅id number是这个吧这个是身份证号不是是那么身份证号里面我不知道大家知道不知道啊
[05:17] 身份证上里边包含有什么呀性别这个信息他还包含出生年日这个大家都知道啊他也包含性别系哪个是包含性别信息呢啊这是第几位这是这个你下去自己数一下吧你可以找到你的身份证找到你同桌的身份证对吧然后自己试一试啊看看他截取出来的这个那一位啊身份证上那一位然后他是怎么判断的除以二判断结果说啊如果除进的话就是女士啊出不进就是先生这个你可以自己试啊
[05:46] 这是判断性别的这个比较简单然后呢关键就是这个次数它是第几次借款这个次数我怎么去这个获取的我咋获取这里边其实你就查一下这个哪个表查一下project这个不就是发标存储那个标的信息了吗那如果说一个人借了十次那这里边consumer ID或者username这个应该会出现几次十次就是你借一次钱就是一行记录借一次钱就是一行记录或者发一次标就是一行记录
[06:17] 那你借十次钱就要发十次表是不是那这边就有几行记录就是十行记录那就相当于你是已经借了十次了那再借就是第十一次所以说我是不是根据consumerid或者有的number或者说这个谁谁啊就是用户的一些信息做一个count次数的一个统计是不是就可以是不是你看这里边我们就是做了一个查询啊你看查的就是哪个表project的表对吧然后给你给你consumerid啊你看给你consumerid就是这个
[06:48] 然后查什么查他的什么次数你看我们调的方法在哪我们调的方法在在在这你看看他对不对快warp不就是我们上面构造的什么条件我们的条件就是根据什么来查考试买的但是我们查的是什么出现的次数然后再加上一不就是本次这是第几次是不是我们第几次这就拿到手拿手之后就是
[07:18] 这个不就是那个当前动物用户的全名吧拼上刚才那个性别就先生女士再拼上第几次第几次接话然后这就全部搞定这个名字啊标题的名字就全部搞定这是比较麻烦的一个事情啊咱把这块代码我们就征过来这个代码倒是也不难啊它就是怎么着呢比较复杂比较多
[07:49] 好咱看一看这里边的名字我们应该是改一改它上面的话应该是这么子来改的当前登用户应该是这么来写的改一下就行这也是一样的这改一下他要的是ID对就这么来做的然后代码的格式你可以自己再调整一下因为我们从pdf粘过来的话它格式不太好用
[08:25] 这是这一块你看我们最终塞的内幕这个值是不是存进去存完之后你就可以干什么进行对save到这的话我们是该给的值就是属性里边该给的值那就全部都给过了给完之后我们就可以进行保存保存之后还有一个小的细节大家注意我们这大家看我们保存完之后是不是要把这个dto对象作为反制返回是不是作为反制返回的话你就直接返回我们在这就可以直接谁
[08:56] 看这个project的地球但是呢我希望呢返回到这个地球对象里面呢这个数据全更全一些怎么更全呢咱这个project的地球里面目前是不是没有ID没有这个内幕是不是啊啊他一开始没有了这个这个内幕是不是咱刚才刚合成的吗这个ID是不是你保存的时候他才生成的主线吗是不是所以说保存完之后呢我想在这个地球里面呢他的他的一些属性这个值我给他这个
[09:26] 怎么着啊得给他补上那这个ID是不是从project里边来得到然后还有呢就是这个谁啊刚才那个名字是不是点set什么呀sign name呗然后就是project.get什么呀对我们把一个相对完整的一个信息哎这为啥报错呀啊这应该是set
[10:01] 我们是希望把一个相对完整的一个DTO对象作为反日返回你看这个DTO我们刚才说了一开始它没几个指纹一开始就三个指纹后来我们又放进去这一堆然后呢又把这个名字啊包括保存之后的这个ID是不是也存进去然后最后把这个DTO对象作为反日返回那这是到目前为止吧咱们把什么呀什么功能就开发完了呀对吧
[10:27] 把这个保存啊标的信息的这个功能就开发完毕了要层代码的确比较多啊这个大家写的时候参考讲义一步一步来就行

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
import cn.cesta.wanxingp.transaction.Mapper.ProjectMapper;
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

