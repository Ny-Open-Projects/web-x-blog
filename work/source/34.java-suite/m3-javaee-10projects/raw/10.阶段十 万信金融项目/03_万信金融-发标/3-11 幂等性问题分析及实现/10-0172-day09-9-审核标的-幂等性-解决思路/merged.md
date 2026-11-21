# day09-9-审核标的-幂等性-解决思路

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-11 幂等性问题分析及实现
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-11 幂等性问题分析及实现\day09-9-审核标的-幂等性-解决思路_【海量资源尽在 666java.com】.mp4
- 时长 9分23秒（音频 564s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才呢我们结合这个图以及这个实际图一起分析了一下审核标的业务当中存在了什么呀对密等性的这个问题那具体来说呢我们是就是结合这个案例啊我们是要解决两个问题很具体的两个问题哪两个问题啊我们在这再明确一下第一个呢就是数据重复保存的问题对吧我们刚才说了前两次进行嘛对不对
[00:29] 有可能会往数据库里边保存重复的这个什么交易记录好第二个问题就是短时间内的重复点击和重复什么呀请求的问题比如说在三秒之内咔咔点了三次他是不是就发过来三个请求啊对不对三个请求过来那我们这里边你肯定不能说你发过来几次请求我就整个全部执行一遍你三个请求过来我只能让其中一个
[00:58] 这个去执行就行了其他两个群众我就不搭理你就行所以我们具体来说其实是要解决这两个问题那咋解决咱刚才说是不是要实现密等性对不对那咱审核标的这一块针对这两个问题怎么去实现密等性呢咱进来分析分析啊看看这个讲义讲义里边是这么说的我们首先是要根据request number先查一下交易记录给大家想一想咱们前面在实现这个审核标的功能的时候这一块是不是上来就干什么就保存是不是你看咱这个实际图
[01:28] 是上来就保存我不会干什么先查一下我就直接就进行保存了那咱考虑到这个密等性这个问题我们这次呢就不再直接保存了而是先根据这个什么呀request number先查一查交易记录然后呢我们分三种情况区别对待或者说分三种情况分别进行什么呀处理哪三种情况呢咱一个一个分析一下第一种情况大家注意听第一种情况呢就是说这个请求过来之后呢
[01:56] 我们是不是先查那个交易记录是否存在一查不存在这说明啥一查不存在证明这个之前的请求基本上是不是就没有成功过了是不是他是不是连这个保存交易记录这一步都还没执行成功那一旦我们这个请求过来发现交易记录不存在那你说我们接下来该干啥很简单交易记录都不存在我们就要干什么保存交易记录是不是这是第一种情况也是最简单的一种情况
[02:25] 交易记录一查不存在那就保存交易记录当然数据的状态一开始肯定是什么呀会同步这是第一种情况那么第二种情况就是一个请求过来按照这个流程开始走走走那他过来之后是不是也是要先根据require number进行查询那这次查出的结果如果是交易记录已经存在而且数据的状态是什么呀已同步这说明啥注意听我查出来结果是交易记录存在而且数据状态是已同步这说明说明之前某一次请求已经罢
[02:55] 2.3 2.4 2.5 2.6 2.7以及2.8整个这一块核心的业务业务全部干什么呀执行完了然后你这次请求过来之后一查才发现结果记录已经存在而且状态都已经是一同步了那你说我这次接下来该怎么办这次请求该怎么办那你能怎么办你这次请求过来之后发现结果记录已经存在状态都已经是一同的证明是不是之前的这个请求已经把核心业务处理完了那你说你该怎么办你啥也别干了直接把这个
[03:26] 这个结果返回就行了是不是你什么都不要干直接返回这个比如说同步成功啊对吧这个结果就完事其他啥都不应该干只是第二种情况先来说也比较好理解那么接下来就剩最后一种情况最后一种情况呢其实主要是解决这个问题就是短时间内客户重复的点一按钮然后造成短时间内重复的发送了什么这就是什么呀请求我们要解决这个问题那这个问题咋解决呢这个问题呢主要就是我们要结合什么呀redis利用它的这个
[03:59] 原子性自称原子性自增这这个一个特性吧我们让这个短时间内发过来这个多次请求让他们去争夺一下这个执行权就是说呢多个请求只让其中一个能干什么呀往下执行那其他的请求我们就直接返回什么呀这个业务正在处理你就不要错这个热闹然后直接就返回来就是你扣到那边
[04:27] 短时间内点了十次请求到我这边最终也就什么样一个请求能往下执行其他请求全部就相当于是挡住了呗就是直接给你返回一个业务正在处理中就完事那具体怎么利用这个redis的原子性呢咱一会编码的时候再说这是呢我们把咱们审核标的这个业务当中密等性的问题怎么去实现我们大概做了一个分析接下来的话咱们就开始编码去
[04:56] 实现这个密等性那么在这个depositoryrecordserviceimpr这个类当中我们会单独定一个方法针对这三种情况对吧然后呢在这个方案里边实现一下这个功能那咱先找一找这个谁啊找一找这个类对不对在存款代理服务这边我们找到这个什么呀实现类对不对在这里边的话我们准备是不是单独干什么呀
[05:28] 对定义一个方法就在这吧private啊然后呢我们来咱参考一下讲义吧我们的名字啥都要跟讲义保持一致我连同这个注释呢一块拿过来咱一起看一看哎这个方案是不是专门实现这个密等性的啊那咱看一看吧这个方法的名字就不再说了啊其啥名都行我们看这个参数这个参数传过来的是不是就是一个什么呀交易记录depository什么呀require
[06:08] 因为我刚才说了我们是不是要要干什么呀要分三种情况进行判断对吧之前我们是不是先拗好一个depositoryrecord的对象然后接下来就直接保存了对不对现在不是现在你拗好一个depositoryrecord对象之后先整理这个方法来实现密等性然后再继续往下走啊所以说呢这儿呢要传过来一个这个交易记录啊但是呢在这里边呢我们要先做密等性的一个实现
[06:36] 然后整个密等性这个实现完之后呢我们会返回这个一些信息嘛然后封装成这个depository based response最终的封装成DTO对象返回这俩对象咱之前是见过的啊你要是不熟悉的话你可以这个点进去看看这里边都封装了什么信息还有那些信息嘛状态码描述信息交易状态流水号然后呢它是一个范形吧我们又放到这个DTO对象里边这里边就包含这个什么业务数据还有什么呀
[07:09] 签名这个到时候用的时候再说吧你看我们都往里边封装了哪些数据这里边你目前最主要关心的就是这个参数就是还是我刚才说了以前我们溜了一个这个交易记录对象之后接下来直接就保存了现在不是现在是传的这个方法要实现这个什么密等线那刚才我们也说了这里边分几种情况对我们这里边整体是要分成三种情况的我们把这三种情况先用注释给他写一写
[07:39] 那当然了首先呢在分这三种情况之前我们是不是得先根据什么呀request number进行什么呀查询对吧然后根据这个结果我们分了几种情况三种情况第一种情况呢就是交易什么呀记录不存在这种是不是最简单了对吧你就保存就行了第二种情况呢就是什么呀交易交易记录已经
[08:12] 存在并且呢状态是什么呀对一同步那最后一种情况呢就是什么呀对重复点击重复请求然后呢利用什么呀对redis的原子线争夺什么呀争夺执行权
[08:52] 就是刚才我们说的嘛你不管发过来多少个请求我最终只会让其中一个去执行剩下呢我就直接返回来了这是我们大概分成这三种情况前两种相当于说简单一些最后一个稍微复杂一些其实呢第一种呢就是请求一开始的这个情况第二种呢其实是请求基本上执行完的情况第三种呢相当于是这个请求执行到什么中间这一块中间这一块的这个情况
[09:20] 我们大概是分了这三种情况

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过“幂等性”设计解决分布式系统中因网络问题或重复请求导致的业务数据不一致问题。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个架构图，包含“交易中心服务”向三个“存管代理服务”（A、B、C）发起请求，每个代理服务再连接到“DB”，并标注“第1次请求”、“第2次请求”、“第3次请求”。
画面2：展示一个弹窗，内容为“如果sql查询语句不带条件，可以吗？不行，如何解决重复量问题？”，并给出一个示例，说明如何通过logstash和MODIFY_DATE字段解决。
画面3：展示架构图，内容与画面1相同，但“交易中心服务”下方标注“前端”。
画面4：展示架构图，内容与画面1相同。
画面5：展示文档内容，说明“幂等性”的定义，并引出“3.6.2 功能实现”部分，描述当交易中心服务请求存管代理服务时，需先获取requestNo并记录，然后分三种情况处理。
画面6：展示一个时序图，描述“调数据/APP”、“交易中心”、“存管代理服务”、“标的待签服务”、“银行存管系统”之间的交互流程。
画面7：展示时序图，内容与画面6相同。
画面8：展示文档内容，说明“幂等性”的定义，并引出“3.6.2 功能实现”部分。
画面9：展示代码，显示“DepositoryRecordServiceImpl”类中的“saveDepositoryRecord”方法，用于保存交易记录。
画面10：展示代码，显示“DepositoryRecordServiceImpl”类中的“handleTdempotent”方法，用于处理幂等性。
画面11：展示代码，显示“DepositoryRecordServiceImpl”类中的“handleTdempotent”方法，光标位于方法定义处。
画面12：展示“DepositoryBaseResponse”类的代码，包含“respCode”、“respMsg”、“status”、“requestNo”等字段。
画面13：展示“DepositoryResponseDTO”类的代码，包含“respData”、“signature”等字段。
画面14：展示“DepositoryRecordServiceImpl”类中的“handleTdempotent”方法，光标位于方法定义处，注释说明“1. 交易记录不存在”、“2. 交易记录存在，并且状态为‘已同步’”、“3. 重复点击，重复请求，利用redis原子性，当务以行权”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面5：
在DepositoryRecordServiceImpl类中单定义一个方法实现幂等性：
/**
 * 实现幂等性
 * @param depositoryRecord
 * @return
 */
private depositoryResponseTO depositoryBaseResponse handleTdempotent(DepositoryRecord depositoryRecord) {
    //根据requestNo查询
    String requestNo = depositoryRecord.getRequestNo();
    DepositoryRecordDTO depositoryRecordDTO = getbyRequestNo(requestNo);
}

画面9：
private ProjectRequestDataDTO convertProjectDTOToObjectRequestDataDTO(ProjectDTO projectDTO, String requestNo) {
    if (projectDTO == null) {
        return null;
    }
    ProjectRequestDataDTO requestDataDTO = new ProjectRequestDataDTO();
    BeanUtils.copyProperties(projectDTO, requestDataDTO);
    requestDataDTO.setRequestNo(requestNo);
    return requestDataDTO;
}

画面10：
private void saveDepositoryRecord(ConsumerRequest consumerRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setRequestNo(consumerRequest.getRequestNo());
    depositoryRecord.setRequestType(ConsumerRequest.CONSUMER_CREATE.getCode());
    depositoryRecord.setObjectType(ConsumerRequest.CONSUMER.getCode());
    depositoryRecord.setObjectID(consumerRequest.getObjectId());
    depositoryRecord.setCreateTime(LocalDateTime.now());
    depositoryRecord.setRequestStatus(StatusCode.STATUS_OUT.getCode());
    save(depositoryRecord);
}

画面11：
private DepositoryResponseDTO DepositoryBaseResponse handleTdempotent(DepositoryRecord depositoryRecord) {
}

画面12：
public class DepositoryBaseResponse implements Serializable {
    @MyModelProperty("返回码")
    private String respCode;
    @MyModelProperty("描述信息")
    private String respMsg;
    @MyModelProperty("交易状态")
    private Integer status;
    @MyModelProperty("请求流水号")
    private String requestNo;
}

画面13：
@Data
public class DepositoryResponseDTO implements Serializable {
    /**
     * 业务数据报文，JSON格式
     */
    @MyModelProperty("业务数据报文，JSON格式")
    private RespData;
    /**
     * 签名
     */
    @MyModelProperty("签名数据")
    private String signature;
}

画面14：
private DepositoryResponseDTO DepositoryBaseResponse handleTdempotent(DepositoryRecord depositoryRecord) {
    //1. 交易记录不存在
    //2. 交易记录存在，并且状态为‘已同步’
    //3. 重复点击，重复请求，利用redis原子性，当务以行权
}

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：架构图，包含“DB”、“存管代理服务A”、“存管代理服务B”、“存管代理服务C”、“交易中心服务”，并标注“第1次请求”、“第2次请求”、“第3次请求”。
画面6：时序图，包含“调数据/APP”、“交易中心”、“存管代理服务”、“标的待签服务”、“银行存管系统”，并标注“1.1.借款人发标”、“1.3.发标成功,待审核”、“2.1.管理员审核通过”、“2.2.标的的信息同步”、“2.3.通过秘钥生成签名及数据”、“2.4.保存交易记录,状态为:未同步”、“2.5.标的的信息同步:直连接口”、“2.6.标的的信息保存”、“2.7.标的的信息同步成功”、“2.8.更新交易记录,状态为:已同步”、“2.9.标的的信息同步成功”、“2.10.建立标的索引”、“2.11.建立索引”、“2.12.索引建立成功”、“2.13.保存标的的信息,数据状态为:已发布”、“2.14.审核成功”。
画面5：文档标题“3.6.2 功能实现”，内容描述“当存管代理服务被交易中心请求时，首先获取该请求的requestNo并记录，然后分三种情况进行处理：1. 若交易记录不存在则新增记录，requestNo为唯一，新保存的数据的状态为“未同步”。2. 若交易记录存在并且数据状态为“未同步”，此阶段存在并发可能，利用redis原子性，争抢请求行权，若count大于1，说明已有线程在执行操作，直接返回“正在处理”。3. 若交易记录存在并且数据状态为“已同步”，直接返回处理结果。”
画面8：文档标题“3.6.2 功能实现”，内容与画面5相同。
画面14：代码注释“//1. 交易记录不存在”、“//2. 交易记录存在，并且状态为‘已同步’”、“//3. 重复点击，重复请求，利用redis原子性，当务以行权”。

