# day06-11-开户第一阶段-功能实现7

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-11-开户第一阶段-功能实现7_【海量资源尽在 666java.com】.mp4
- 时长 13分57秒（音频 837s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把这个存款代理微服务工程当中的数据访问层这个代码编写了一下这个比较简单那这个搞定完之后呢咱接下来自然就该搞定哪一层啊对药草那药草跟之前一样也是一个接口一个实现类那咱先去找到哪个包啊Service 包Service 包里边这两个Service是直接提供给大家去使用的我们现在创建一个新的Service
[00:29] 一个接口啊叫depository record是不是Service这是一个接口啊业务层的接口那这里边目前只需要定义一个方法就行了就是开户还是叫createconsumer啊这儿是不是就是从用户中心传过来的数据用户中心是不是用户中心是不是要传给存款代理服啊那用户中心当时他封装的类型是不是就是consumer request的嘛所以这边也得是什么呀consumer request然后这儿是不是我们说MP是不是对
[01:03] 右层也进行了封装了这是继承什么呀对继承MP的那个那个类或者说那个接口不应该是类是接口那这个呢大家也比较熟悉我就直接粘过来了实现类的代码咱一会儿重点编写一下这是什么呀右层的接口也有啊接口有了之后呢咱接下来重点是要编写它的实现类这类名呢咱还是跟讲义保持一致粘过来然后呢首先呢你要注意这是不是要加一些
[01:42] 什么呀对要加一些注解Service还要搞继承还要搞什么呀实现这个套路大家应该到现在应该记者都很熟悉了Service这边呢我们先干什么呀先来个继承吧继承mp提供的叫Service impr对吧s e r v i c e i m p r 第一个是范形是那个啥解口对吧叫depository record的map在这
[02:14] 第二个就是那个实体类了对应表的那个实体类就要depositoryrecord就这是吧然后还要实现刚才的那个自定义的接口那就叫depositoryrecordservice搞定那这报错很正常因为咱是不是要重写它里边的一个方法就是开户的这个方法咱先来一个空实现先不让他报错好
[02:47] 那咱们接下来重点是不是就编写这里边的代码那我们看一下这个实际图这还是给大家强调你在编写代码的时候一定要重点去看这个实际图那这里边展示了什么呀存管代理服务这边重点要实现两个功能那一个是加密返回数据对吧就是一定要返回嘛然后还有一个就是保存这个什么呀交易记录那其实说白就是几个功能对两个功能那第一个功能我们先保存吧好吧就是保存交
[03:20] 记录这俩时代前时代后倒无所谓啊第二个呢就是签名签名其实就是加密的意思并什么呀返回嘛得返回给谁啊你上网来嘛因为这个数据是用户中心传给从专案代理从专案代理这边其实主要是做加密加密完之后你还得干什么返回用户中心用户中心再返回给谁啊前端嘛这个第一级就搞定了是不是所以说呢在这个右层呢我们其实主要重点是编写
[03:58] 这两块的啊那咱先一个一个来吧先说第一块功能就是保存交易记录那这个这个相来说会简单一些啊这个比较简单保存交易记录那咋保存呢那就是直接什么呀save呗那我们关键是要看看这个交易记录如何进行什么呀封装如何进行封装呃这个交易记录这个对象的话他是这样就这个对象我们可以看看他的圆满
[04:29] 你会发现这里边其实我们需要操作的属性非常多是不是非常非常多呃所以说呢这个保存功能啊实现的时候可能代码会稍微有点多咱要不这样咱把保存交易记录这个代码咱单独抽取出来放到一个方法里边我就不在边写要不然整个这个方法写完这个代码会看着比较多咱抽一下我们起个名字就叫就叫什么呀savesave d p o s i
[05:00] t o t o r ydepositoryrecorder i c o r d对不对然后我们把代码都放到这个方案里面那咱们下面是个单独需要再定义一个方法private就叫这名了那我们要想这个方法有没有参数有没有反位值那一定得有参数啊而且也得有什么呀反位值啊对不对那么这个反位值不就是它吗那传进来的参数呢那传进来啥参数就看你
[05:36] 这个要往这个对象里边保存的时候要保存哪些数据了对不对那咱要保存的数据其实是不是跟用户中心那边传过来的是不是有一定的关系是不是那咱怎么办那你也可以在这儿传餐的时候把它一个一个取出来再扔进来你也可以把它直接扔进来咱这样咱这样行咱直接这么写直接就把它给干什么呀传进来得了是不是那我这儿是不是需要加这么一个餐
[06:07] 说这可以吧哎我把它扔给这个方法然后在这个方法里边呢需要啥注意从这里边取呗全之后呢你该保存保存就OK了那咱接下来保存的话是不是直接就拗这个对象就行直接等于拗对就拗它拗完之后无非就是往里边放值呗就给属性负值呗都需要负乃安值呢那倒是挺多的啊
[06:43] 比如说这个流水号set request number流水号就需要从这里边取就行了get对吧还需要什么呢还需要请求类型set request什么呀type那么这个request type是个啥玩意儿呢这个request type大家注意了request type呢我们需要
[07:11] 这是一个一个不是说你想给什么值就给什么值呢我们需要通过一个美举这个美举对象呢我们应该是直接提问给大家我们去这里边找一找美举对象应该是这个谁呀他比较长应该是叫应该是这depository request type code我们得给他粘进来是不是我们看他是放到哪个包里边的quoman
[07:43] 火曼包火曼包在这里放这里边他这里边已经有了是吧已经有了那你好办了已经有我们就直接拿用或者我们先看一看这里面你看有什么就他把交易说白了就是把交易分成了几种类型又有跟标的有关这还没搞到呢投标的审核标的的咱应该用哪一个咱应该用这个什么咱是咱现在这个交易属于什么开户将来还有什么充值提现对吧等等等等
[08:15] 那咱这呢就是取这个枚举对象就行了那我们怎么写那就是depositorydpositori单词老长了啊然后后边是什么呀request iq点我们应该挑刚才说的什么呀叫开户对就是他啊就是这个值然后我们要点一下get code对这相当于是交易类型啊或者请求类型都行
[08:48] 然后还有什么呀他这边还有很多东西都要存depository.还有一个叫叫这个啊什么实体类型啊set应该是object吧obj type还需要知道你这个呃操作的时候这个这个操作实体类到底是个什么东西啊操作实体类那这个应该怎么写呢我们直接就写死了直接我们操作的这个实体类是什么呀
[09:20] 我们操作的是用户吗用户就是什么consumer那这个东西我们去表里边瞅一瞅看他这里边有没有一些解释说明啊就这个表这个表你看看这里边有有有这就其实就是给这个字段复制了一要我实体类型咱这个要实体类型就是考虑了用户开会用户开户说这我们就直接给了一个字符串就是考虑了
[09:47] 然后再往下还有哪些这个属性的值需要给呢我们接着往下走还有就是一个idconsumer的idset object id对刚才是类型嘛现在是什么呀id这个id是哪个id啊这个id的话就是我们说的啊客户的这个id就用户的id那就是我们从consumer request里边直接取这个什么呀给他id就行
[10:18] 这个ID是啥意思呢这个ID呢你就要跟前面用户中心里边的代码要关联起来了用户中心呢咱当时在我给你找一找啊在这个业务应该是业务层我们找一找业务层吧你找一下哪啊找一下看这你看这是不是往里边存的ID吗咱在这个地方是不是取的那个ID吗稍等我把这个关掉
[10:49] 咱刚才在这取得不就是id吗那这个id表什么意思你看这这不就是consumer的那个id吗是不是consumer dto他的就是用户的id所以这个前后代码就有关联了然后还要存什么东西还要存本次这个交易的时间本次交易的时间是哪个字段呢叫setcreate date有没有就这个
[11:19] 就当前时间买当前时间我们这么写啊locallocaldatetime.now吧这个其实就获取当前时间这是什么呀开户的交易时间对吧然后呢就是那个同步的状态同步的状态呢我们应该是有一个叫statusdepositorysetsetrequeststatus
[11:52] 这个呢在我们的实际图里边是有所体现的状态应该是什么为同步为同步的意思咱之前其实说过因为咱整个开户的话咱现在这走的是第一阶段嘛后边整个开户完成了之后这个状态要改成什么呀一同步的其实就是区分这个什么呀这个整个开户有没有完完全全的这个走完或者完全的成功那这个曲子我们还是从那个那个叫
[12:20] status code吧对这里边来取它应该是为什么呀应该是未同步对吧out将来我们的改成另外相对应的一个值就行了这个状态我们保存完之后其实该给的数据就给的差不多了啊啊一个是流水号这个什么呀交易的类想我们这是开户吗然后呢我们这个操作的是consumer就是用户
[12:54] 这是一个类型然后这是用户的ID对吧然后这是当前的交易时间这是一个初始的一个状态未吞没的一个状态那么该给的值都给过之后接下来是不是就该调到哪个方法来保存哪个方法那放在以前我们要保存应该是怎么保存是不是应该是save是不是那我们这样试一下我们直接就用save进行保存有save方法吗有没有当然有这不是save方法
[13:23] 然后呢直接把这个对象给他干什么呀扔过来就OK了是吗这就完了吧是不是我们直接save因为我们以前说MP对业务层进行封装了那这为什么还报错呀他说没有返回值那大家想一下我们这只是做个保存的话咱这需要返回东西吗应该不需要吧用不着对吧我们这改一下改成void不需要那然后呢大家看咱们的第几步就搞定了第一步对不对业务层的第一步就是保存交易记录就搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在开户业务中，通过定义并实现 RepositoryRecordService 接口及其方法，完成交易记录的持久化和状态更新。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Mapper 包中新建 DepositoryRecordMapper 接口，定义其继承自 BaseMapper<DepositoryRecord>；同时在同包中新建 DepositoryRecordMapper.xml 文件，配置其 namespace 为 cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper。
画面 2: 展示了多个窗口，包括 PPT、WPS 图片、日志文件等，同时在 IDE 中显示了 DepositoryRecordServiceImpl 类的开头部分，定义了 createConsumer 方法。
画面 3: 展示了开户业务流程图，图中包含“前端/App”、“用户中心”、“容器代理服务”、“存管系统”和“开卡银行”五个模块，以及它们之间的交互流程。
画面 4: 在 IDE 中显示了 DepositoryRecordServiceImpl 类的完整结构，其中 extends ServiceImpl<DepositoryRecordMapper, DepositoryRecord>。
画面 5: 在 IDE 中显示了 DepositoryRecord 类的定义，包含私有字段 requestStatus、confirmDate 和 responseData，以及构造函数。
画面 6: 在 IDE 中显示了 createConsumer 方法的实现，调用 saveDepositoryRecord 方法。
画面 7: 在 IDE 中显示了 saveDepositoryRecord 方法的实现，创建 DepositoryRecord 对象并设置 requestNo 和 requestType。
画面 8: 在 IDE 中显示了 DepositoryRequestTypeCode 类的定义，包含多个常量如 TRADING、PULL_LOAN、MODIFY_STATUS 等。
画面 9: 在 IDE 中显示了 saveDepositoryRecord 方法中，设置 requestType 为 CONSUMER_CREATE。
画面 10: 在 IDE 中显示了 saveDepositoryRecord 方法中，设置 objectType 为 "Consumer"。
画面 11: 在 IDE 中显示了 ConsumerServiceImpl 类中，对银行卡状态进行校验，并设置 consumerRequest 的相关属性。
画面 12: 在 IDE 中显示了 saveDepositoryRecord 方法中，设置 objectTo 为 "Consumer"。
画面 13: 在 IDE 中显示了 saveDepositoryRecord 方法中，设置 requestStatus 为 STATUS_OUT。
画面 14: 在 IDE 中显示了 saveDepositoryRecord 方法中，调用 save 方法保存记录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 存管交易记录表 Mapper 接口
 */
public interface DepositoryRecordMapper extends BaseMapper<DepositoryRecord> {

}
```
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper">
</Mapper>
```
画面 4:
```java
package cn.itcast.wanxing2p.depository.Service;

import cn.itcast.wanxing2p.depository.entity.DepositoryRecord;
import cn.itcast.wanxing2p.depository.Mapper.DepositoryRecordMapper;
import org.springframework.stereotype.Service;

@Service
public class DepositoryRecordServiceImpl extends ServiceImpl<DepositoryRecordMapper, DepositoryRecord> {

}
```
画面 5:
```java
private Integer requestStatus;
// 消息确认时间
@TableField("CONFIRM_DATE")
private LocalDateTime confirmDate;
// 返回数据
@TableField("RESPONSE_DATA")
private String responseData;

public DepositoryRecord() {

}

public DepositoryRecord(String requestNo, String requestType, String objectType, Long objectId) {
    this.requestNo = requestNo;
    this.requestType = requestType;
    this.objectType = objectType;
    this.objectId = objectId;
}
```
画面 6:
```java
@Override
public GatewayRequest createConsumer(ConsumerRequest consumerRequest) {
    //1.保存交易记录
    saveDepositoryRecord(consumerRequest);
    //2.签名（加密）数据并返回
}
```
画面 7:
```java
private DepositoryRecord saveDepositoryRecord(ConsumerRequest consumerRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setRequestNo(consumerRequest.getRequestNo());
    depositoryRecord.setRequestType(consumerRequest.getRequestType());
}
```
画面 8:
```java
/**
 * 用户投标
 */
TRADING("TRADING", "用户投标"),
/**
 * 审核标满放款
 */
PULL_LOAN("FULL_LOAN", "审核标满放款"),
/**
 * 修改标的的状态
 */
MODIFY_STATUS("MODIFY_STATUS", "修改标的的状态"),
CONSUMER_CREATE("CONSUMER_CREATE", "开户"),
RECHARGE("RECHARGE", "充值"),
WITHDRAW("WITHDRAW", "提现");

private String code;
private String desc;
```
画面 9:
```java
depositoryRecord.setRequestType(DepositoryRequestTypeCode.CONSUMER_CREATE);
```
画面 10:
```java
depositoryRecord.setObjectType("Consumer");
```
画面 11:
```java
//3.更新用户的信息
consumerRequest.setUserName(bankCardDTO.getCardNo());
consumerRequest.setUserId(bankCardDTO.getCardNo());
consumerRequest.setRequestNo(CodeGenUtil.getCode(ConsumerRequest.CODE_REQUEST_PREFIX));
consumerRequest.setUserName(bankCardDTO.getCardNo());
consumerRequest.setUserId(bankCardDTO.getCardNo());
consumerRequest.setRequestNo(CodeGenUtil.getCode(ConsumerRequest.CODE_REQUEST_PREFIX));
//更新用户信息
UpdateWrapper<Consumer> updateWrapper = new UpdateWrapper<>();
updateWrapper.lambda().set(Consumer::updateUserName, consumerRequest.getUserName());
updateWrapper.lambda().set(Consumer::updateUserId, consumerRequest.getUserId());
updateWrapper.lambda().set(Consumer::updateRequestNo, consumerRequest.getRequestNo());
updateWrapper.lambda().set(Consumer::updateCardNo, consumerRequest.getCardNo());
updateWrapper.lambda().set(Consumer::updateStatus, consumerRequest.getStatus());
updateWrapper.lambda().set(Consumer::updateCreateTime, consumerRequest.getCreateTime());
updateWrapper.lambda().set(Consumer::updateUpdateTime, consumerRequest.getUpdateTime());
updateWrapper.lambda().set(Consumer::updateRemark, consumerRequest.getRemark());
updateWrapper.lambda().set(Consumer::updateVersion, consumerRequest.getVersion());
updateWrapper.lambda().set(Consumer::updateStatus, consumerRequest.getStatus());
updateWrapper.lambda().set(Consumer::updateUpdateTime, consumerRequest.getUpdateTime());
updateWrapper.lambda().set(Consumer::updateRemark, consumerRequest.getRemark());
updateWrapper.lambda().set(Consumer::updateVersion, consumerRequest.getVersion());
```
画面 12:
```java
depositoryRecord.setObjectTo("Consumer");
```
画面 13:
```java
depositoryRecord.setRequestStatus(StatusCode.STATUS_OUT);
```
画面 14:
```java
depositoryRecord.setCreateTime(LocalDateTime.now());
save(depositoryRecord);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 标题为“开户业务流程图”，流程图包含五个模块：“前端/App”、“用户中心”、“容器代理服务”、“存管系统”和“开卡银行”，它们之间的交互流程如下：
- “前端/App”指向“用户中心”，执行“1.1生成开户请求数据”。
- “用户中心”指向“容器代理服务”，执行“1.2准备开户所需基础数据”。
- “容器代理服务”指向“存管系统”，执行“1.4通过短信生成交易及数据”。
- “存管系统”指向“开卡银行”，执行“2.4验证请求”。
- “开卡银行”指向“存管系统”，执行“2.7保存交易记录”。
- “存管系统”指向“用户中心”，执行“2.6返回开户信息”。
- “用户中心”指向“前端/App”，执行“1.7返回开户请求数据”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

