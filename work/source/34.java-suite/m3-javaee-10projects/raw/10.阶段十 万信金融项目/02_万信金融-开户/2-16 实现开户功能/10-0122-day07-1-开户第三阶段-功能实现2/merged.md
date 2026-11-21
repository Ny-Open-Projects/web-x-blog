# day07-1-开户第三阶段-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day07-1-开户第三阶段-功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 13分57秒（音频 837s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好前面呢我们把这个depository notify Controller呢给创新好了那在这个类当中呢我们实现了一个方法啊我们要实现一个方法就这个方法发明比较长啊这个方法的作用主要是用来接收什么呀对银行存款系统那边啊开户回调的一个什么呀一个结果
[00:27] 那在这个方案里边呢我们一共要实现三块功能啊大家看一下第一块呢就是更新数据第二块呢是发送消息给用户中心第三块呢返回结果比较简单一行代码就搞定了咱就不再说了那咱接下来的话按照顺序啊先实现第一块功能就是更新数据那咱先明确一下需求吧咱更新的是什么数据哪一块的数据那咱需要看图说话对吧
[01:00] 这个图就是开户业务流程图哪一块呢是不是3.2这一块对吧更新交易记录更新什么呀更新状态啊从原来的这个什么呀你看这儿未同步要改成什么呀对已同步那咱对应的数据库咱找一找对应的数据库还有表大家看就是这个表啊Depository Record就这个表那么具体我们要更新的字段大家注意看的是这个字段
[01:31] 这个字段request什么status那这个字段的取值呢有三个大家注意了啊零呢就表示什么呀未同步这是一开始的那个值对吧处理值零那一呢就表示已同步已同步的意思就是银行存管系统那边已经干什么呀对处理成功了那么他还有可能有一个值就是二二呢就表示银行存管系统那边干什么呀处理失败处理失败他会返回二啊处理成功会返回什么呀
[02:01] 一啊所以说呢我们要修改的这个字段的值呢就是这个字段的值大家一定要注意的那同时呢我们还要修改这个字段值就confirm啊confirm date这个字段值呢我们要修改成当前的这个什么呀对日期时间好那咱接下来开始实现这个功能怎么实现呢呃这个功能呢我们一定是要放在什么呀Service就是放在业务层实现然后再
[02:33] 这儿进行什么呀进行调用就行了还是老的套路啊那咱就找到这个什么呀对找到这个Service右层是吧还是一个接口一个什么呀实现类啊咱先找个接口那我们在这儿是要新增一个什么呀一个方法然后在实现类当中去实现这个方案就行了那咱看一眼讲义啊看这儿你看他说了是不是在这个接口当中右层的接口当中是不是新增一个什么方法叫modify
[03:03] request什么呀cetus这个见名之意是被修改状态了那这个方案名呢我们要跟讲义保持一致那咱接下来就要重点分析一下这个方法哎他要不要参数要不要什么呀反应值对不对咱一个一个来吧先说要不要反应值啊我们需要一个反应值什么类型的呢这个是不是用来表示这个什么呀修改数据库的某个字段对吧我们最终呢要要返回一个值就是修改成功还是什么呀
[03:34] 失败啊大家看一下什么类型啊对布尔类型的一个返回值需要大家注意的一个修改操作嘛我们最终是需要知道结果的啊修改的结果那这个方案要不要参数呢那肯定需要什么呀需要参数的需要几个参数呢刚才我们说了嘛呃我们主要是修改这个什么呀对修改这个状态的这个状态这个值我们是得有对吧你是改成一还是改成二是不是然后还有啥呢
[04:06] 有同学说老师还有这个时间这个时间就不需要通过参数来传了啊这个时间我们说了是不是当前时间就行了啊那还需要一个什么参数啊还需要这个request number其实说白了就是这个表里边的这个主件啊因为我们现在是在进行什么呀修改操作修改你修改了肯定是表当中某一行的值啊或者表当中某一行的这个字段的这个值是不是那我怎么定位这一行啊那肯定得知道这个什么呀request number
[04:35] 我得知道这个值比如说你传过来这么一个request number那我将来修改来是不是就是这个值你发现什么意思吧我们一共需要几个几个值啊几个参数啊两个啊一个是request number一个就是这个什么呀一个这个状态值我们看对不对呢我们看这个讲义大家看一下是不是一个request number一个这个什么呀对状态值啊一共两个参数好我们拿过来我们把上面这个
[05:07] 这个什么呀这个注释我们也一块给他拿过来用我们稍微调整一下这个格式啊这是我们在什么呀业务层的接口里边干什么呀对定义好了一个方法这是发明啊两个参数还有一个什么呀一个返回值那咱接下来就需要打开实现类在这里边干什么实现这个方案你看实现类是不是已经报错了对不对然后呢咱把这个方法呢给它生成出来好咱看一下在这个位置
[06:02] 那咱接下来是不是就应该在这个方案里边具体去实现什么功能啊对根据这个什么呀request number去修改表当中的哪个字段的值啊对request status这个字段的值以及这个什么呀对confirm什么呀data我们一共修改两个字段的值条件又是什么条件
[06:26] 对就是这个request number那这个其实说白了就是一个表的一个什么修改操作这个功能简单吧是不是很简单咱以前应该是用用什么来实现过这个这个类似的这个功能啊是不是MP对吧mybattlesplus啊用MP实现这个功能是非常简单的那咱接下来先回顾一下以前啊以前咱这块代码啊就是用MP实现数据库修改这种代码是怎么写
[06:57] 呃那大家看一下这个图啊你看我们在前面哪个地方你看1.3这个地方我们前面在这儿是不是应该就用过这个什么呀对用mp实现过这个什么呀更新功能那咱找一找以前的代码啊这个应该是在用户中心是不是用户中心咱找一找用户中心用户这是用户中心对吧他应该也是写在什么业务层这是实现类吧实现类啊咱找一找这个代码你看这儿在这儿是在这儿吧
[07:29] 你看当时咱是怎么实现了咱是不是用了一个对象叫update什么呀Warp对吧它是专门用来实现什么呀对数据库的一个什么修改大家看一下这个应该是条件吧是不是这个应该是条件然后呢这个呢就是什么呀具体要修改的这个什么呀这个指这里边我们是不是都用到了什么东西啊Lambda什么呀表达式这个大家应该还有印象那我们吧
[07:59] 这个条件呢还有还有这个修改的值呢都封装到了这个updatewarp对象里边之后把这个对象扔给什么方法对MP的update的方法那么他就完成了这个什么呀完成了这个数据的修改或者数据的更新这是咱以前的一种写法那么今天的话我们准备给大家介绍一种新的写法什么写法呢咱看看讲义啊这种写法呢比刚才那种写法要更简洁一些但是实际上啊
[08:29] 实际上是本质上是一样的但是于法更简洁大家看这因为这个大家能看出来这个是什么东西这个其实是不是就是那个update的方法你看update这是不是小果号一直到到哪到这结束了是不是那它其实对应的就是这个update的方法就是这个update然后这个update的方法我们说它是不是要的要一个什么东西一个update varp一个对象你看咱这个对象是new出来的对不对那你看咱今天的这个写法是怎么写
[09:00] 你看在这个小五号里边我有没有去new一个什么呀new一个什么什么什么呀update warp这个对象没有而是怎么写的呀你看我调用了一个warp这样一个类它的一个方法叫lambda什么呀update对不对那么这个方法呢我们一会儿在编写的时候你要注意看一下你看它的返回值是不是这种类型的一会儿写的时候你看一看然后你看接下来这个方案是不是都一样点EQ点set是不是
[09:30] 这里边是不是也是什么呀Lambda表示的写法所以说呢这个EQ方法还有set方法其实跟我们原来的这个写法都是什么呀都是一样的或者简单来说的话我们今天的这个写法从表面来看啊就这块代码我选了这块代码相当于以前的这块代码就是稍微简洁了一点啊你看以前是不是我在调EQ啊还有set方法的时候每次调的时候是不是都得写这块东西看出来没有
[10:03] 是不是重复的代码对不对那我们今天的这种写法你看没有那些重复的代码啊所以从这个写法来说呢它会更加简洁一些那咱接下来一起把这块代码呢编写一下是不是应该去哪去这儿对不对呃我们直接是不是要调用这个什么呀对updata方法大家看一下你看这个方法里边是不是要一个什么呀对updata warp这么一个什么呀
[10:34] 对这么一个对象但是这次呢咱这个对象啊咱不打算溜了啊咱准备这么写咱用一个类叫叫什么呀叫WRAPPAS这个其实就是一个工具类吧它有一个方法叫什么呀刚才让大家看叫什么名字叫Lambda什么呀Update你看它的返回值类型是一个什么呀Lambda Update什么呀Warp
[11:04] 那么你在调这个方案的时候呢大家注意我们在这需要干什么呀需要设置一个范形在这个地方这个写法还是有点特殊的那咱要修改的这个范形或者这个类型是不是就是那个什么呀那个depository record是吧也就是他需要加一个范形那么大家看一下我们重点研究这个方案大家再瞅一眼这个方法的返回值类型是一个什么呀你看是一个什么呀
[11:35] 对是一个蓝色的啊lambda update warp你看咱们以前的这个代码做一个对比你看这看到没有你看我们以前的这个写法在这调lambda的时候返回直的这个类型是不是也是lambda update warp对吧所以刚才说了嘛咱今天的这个写法相当于是跟这块代码是不是作用是一样但是你不用重复的去编写这块代码啊只是我们通过对比大家需要明白那接下来这个写法跟之前一样嘛
[12:05] 对接下来写法跟之前一样你就是调用这个什么EQ设置条件调用set来干什么设置要更新的这个什么这个值这个代码跟之前一样我就不再过多给大家说了大家看一下我们的条件就是这个谁对request number我们刚才说了就这个根据request number来修改这两个字段的这个值是不是所以说你看我们接下来调用set的方法一个是设置这个什么对这个状态
[12:35] 一个是设置这个什么其实就是当前的这个什么时间这个状态这个值将来到底是从哪来的从这儿来的给大家说从这儿来从这儿从这儿来那将来我们说了这个银行存款系统那边是不是要毁掉咱这个方法呢那它毁掉的时候就会往这个地方传什么传数据这里边就包含有那个什么呀那个状态就是那个那个一还是二那个值那
[13:04] 这边又毁掉它是不是在这儿将来就掉在这个右层吗最终就通过这儿就扔进来了那所以说接下来这个代码呢我就不再给大家编写了因为跟之前都是什么样一样的好我就直接拿过来了好我们看一下这儿还报着错了对不对为啥报错呢因为我们这儿少写一个什么呀对这个方法最终的这个结果是不二类型的我们要作为反转值干什么呀返回啊那这样子的话我们就把什么呀
[13:43] 就把业务层的这个代码就写完了写完之后呢我们将来是不是要在这儿把业务层的对象注进来然后在这儿就可以进行这个方法的什么呀调用

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个存款通知服务的代码实现，包括控制器接收请求、服务层修改状态、更新用户信息及银行卡信息等核心逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 `DepositoryNotifyController` 中的 `@RequestMapping` 和 `@RequestParam` 注解，用于接收请求参数并映射到方法。
画面2：聚焦于 `return "OK";` 语句，表示请求处理成功。
画面3：展示 PPT 内容，讲解 `DepositoryRecordService` 接口中的 `modifyRequestStatus` 方法及其实现。
画面4：展示数据库表 `depository_record` 的数据，包含请求ID、类型、项目ID、创建日期等字段。
画面5：展示 `DepositoryRecordServiceImpl` 中的 `modifyRequestStatus` 方法，包含 `update` 方法调用。
画面6：展示 `DepositoryRecordServiceImpl` 中的 `saveDepositoryRecord` 方法，用于创建新的存款记录。
画面7：展示 `ConsumerServiceImpl` 中的 `update` 方法，用于更新用户信息。
画面8：展示 `ConsumerServiceImpl` 中的 `update` 方法，设置用户手机号、姓名、证件号等。
画面9：再次展示 PPT 内容，讲解 `DepositoryRecordService` 接口中的 `modifyRequestStatus` 方法及其实现。
画面10：展示 `ConsumerServiceImpl` 中的 `update` 方法，设置用户证件号。
画面11：展示 `DepositoryRecordServiceImpl` 中的 `modifyRequestStatus` 方法，包含 `update` 方法调用。
画面12：再次展示数据库表 `depository_record` 的数据。
画面13：展示 `DepositoryNotifyController` 中的 `return "OK";` 语句。
画面14：再次展示 `DepositoryNotifyController` 中的 `return "OK";` 语句。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@ApiOperation(value = "需求的存管接口名",
        notes = "平台编号，平台与存管系统签约时获取。",
        required = true, dataType = "String", paramType = "query"),
@ApiOperation(value = "对reqData参数的签名",
        required = true, dataType = "String", paramType = "query"),
@ApiOperation(value = "业务数据报文，json格式",
        required = true, dataType = "String", paramType = "query"),
)
@RequestMapping(value = "/gateway", method = RequestMethod.GET, params = "serviceName=PERSONAL_REGISTER")
public String receivedepositoryCreateConsumerResult(@RequestParam("serviceName") String serviceName,
        @RequestParam("platformNo") String platformNo,
        @RequestParam("signature") String signature,
        @RequestParam("reqData") String reqData) {
    //1.更易读
    //2.发送消息给用户中心
    //3.返回结果
    return "OK";
}
```

画面3：
```java
2. 在DepositoryRecordService接口中新增modifyRequestStatus方法：
/**
 * 根据请求流水号更新请求状态
 * @param requestNo
 * @param requestStatus
 * @return
 */
Boolean modifyRequestStatus(String requestNo, Integer requestStatus);

在DepositoryRecordServiceImpl类中实现modifyRequestStatus方法：
@Override
public Boolean modifyRequestStatus(String requestNo, Integer requestStatus) {
    return update(Wrappers.<DepositoryRecord>lambdaUpdate()
            .eq(DepositoryRecord::getRequestNo, requestNo)
            .set(DepositoryRecord::getRequestStatus, requestStatus)
            .set(DepositoryRecord::getConfirmDate, LocalDateTime.now()));
}

3. 新建message包，在该包中定义消息生产者：
```

画面5：
```java
package cn.icta.warning2p.depository.Service;
import cn.icta.warning2p.depository.entity.DepositoryRecord;
import cn.icta.warning2p.depository.Mapper.DepositoryRecordMapper;
import cn.icta.warning2p.depository.Service.DepositoryRecordService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;
@Service
@Transactional
public class DepositoryRecordServiceImpl implements DepositoryRecordService {
    @Autowired
    private ConfigService configService;
    @Autowired
    private DepositoryRecordMapper depositoryRecordMapper;
    @Override
    public GatewayRequest receivedepositoryCreateConsumerRequest(CommonRequest consumerRequest) {
        //1.修改请求状态
        String reqData = consumerRequest.getReqData();
        String sign = consumerRequest.getSignature();
        String platformNo = consumerRequest.getPlatformNo();
        String serviceNo = consumerRequest.getServiceNo();
        GatewayRequest gatewayRequest = new GatewayRequest();
        gatewayRequest.setReqData(reqData);
        gatewayRequest.setSignature(sign);
        gatewayRequest.setPlatformNo(platformNo);
        gatewayRequest.setServiceNo(serviceNo);
        gatewayRequest.setDepositUrl(configService.getDepositUrl() + "/gateway");
        return gatewayRequest;
    }
}
```

画面6：
```java
@Override
public Boolean modifyRequestStatus(String requestNo, Integer requestStatus) {
    update(Wrappers.<DepositoryRecord>lambdaUpdate()
            .eq(DepositoryRecord::getRequestNo, requestNo)
            .set(DepositoryRecord::getRequestStatus, requestStatus)
            .set(DepositoryRecord::getConfirmDate, LocalDateTime.now()));
}

private void saveDepositoryRecord(CommonRequest consumerRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setRequestNo(consumerRequest.getRequestNo());
    depositoryRecord.setRequestType(DepositoryRecordTypeCode.CONSUMER_CREATE.getCode());
    depositoryRecord.setObjectType(DepositoryRecordObjectTypeCode.CONSUMER.getCode());
    depositoryRecord.setObjectId(consumerRequest.getConsumerId());
    depositoryRecord.setCreateDatetime(LocalDateTime.now());
    depositoryRecord.setRequestStatus(DepositoryRecordStatusCode.STATUS_OUT.getCode());
    depositoryRecord.setConfirmDate(LocalDateTime.now());
    depositoryRecord.setConfirmDatetime(LocalDateTime.now());
    depositoryRecord.setConfirmUser(consumerRequest.getConfirmUser());
    depositoryRecord.setConfirmIp(consumerRequest.getConfirmIp());
    depositoryRecord.setConfirmTime(consumerRequest.getConfirmTime());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmRemark(consumerRequest.getConfirmRemark());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode.CONFIRMED.getCode());
    depositoryRecord.setConfirmType(DepositoryRecordConfirmTypeCode.CONFIRM_TYPE.getCode());
    depositoryRecord.setConfirmCode(consumerRequest.getConfirmCode());
    depositoryRecord.setConfirmData(consumerRequest.getConfirmData());
    depositoryRecord.setConfirmStatus(DepositoryRecordConfirmStatusCode

