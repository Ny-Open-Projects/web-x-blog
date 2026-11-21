# day06-3-开户第一阶段-定义接口1

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-3-开户第一阶段-定义接口1_【海量资源尽在 666java.com】.mp4
- 时长 13分56秒（音频 836s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把银行那边的这个什么呀存管系统已经布置好了也能启动了对吧那这就为咱接下来在P2P项目当中开发开户功能做好了准备是不是那咱接下来就回到P2P项目当中开始呢去实现我们的开户功能这个开户功能啊咱们前面
[00:28] 进行过需求分期大家看一下这个时序图还有这个图这个整体的这个时序图看下来是不是还是感觉开户这个业务非常的复杂对吧所以咱当时在做需求分析的时候给大家强调我们是不是分成三个阶段你还有印象吗咱讲义当时是不是也是给大家说了分成三个阶段你看这是不是第一阶段是生成开户数据的对吧第二阶段就是请求开户的第三阶段就是开户结果的一个什么
[00:57] 通知这里边你看就是1.1到1.7一个阶段2.1到2.8一个阶段然后最下边3.1到3.4一个阶段三个阶段虽然这个业务的确复杂但是呢咱化整为零各个击破大家在企业当中做开发的时候也是一样当你拿到这么复杂的一个实际图的时候也是一点一点来把它给拆分一下各个击破就可以那你看咱接下来再具体
[01:26] 实现这个开户功能的时候咱也是分成几个阶段一点一点去开发的三个阶段你看我这边的这个目录第一阶段生成开户数据第二阶段请求开户第三阶段就是什么呀开户结果通知你看然后最后进行前后端集成测试对吧所以说一点一点来就行那咱接下来先看第一阶段生成开户数据每个阶段呢我们都是在讲一讲该阶段的一个小需求然后定解口然后进行什么呀
[01:56] 功能实现整体的套路都是如此那大家下去你再参考我这个讲义的时候也心里边也得清楚整体的这个结构那咱说说第一阶段的这个需求那这个需求呢我们仍然是要看这个时序图当然这个时候呢我们就只需要看哪到哪对1.1到1.7了其他你暂时就先不用管了咱们说了吗各个击破啊那第一阶段我们说呢这是叫生成开户数据对吧
[02:26] 就相当于是为开户做的一些数据的一个准备工作那前端的发请求请求先到哪先到我们的什么样用户中心看好啊用户中心这涉及到一个微服务了那这边呢他还会再提供或者准备一些数据一会儿在编码上你会看到有什么样request number这其实叫流水号啊还有一个user number这个user number其实是专门用来跟银行的存款系统在
[02:55] 做交互做对接的时候呢用的一个用户的编号一个唯一标识这个你要跟咱们本身表里边其实咱有主见啊你看咱的consumerconsumer你看咱这里边咱这里边你像ID啊这些是不是都是主见啊对不对但是我们又加了一个user number刚才又说了它主要是用来跟谁这个打交道使用的对跟银行那边的系统打交道使用的啊
[03:24] 然后把用户中心这边主要是准备数据把相关的数据准备好之后发给谁进行加密发到存管代理服务这边进行加密你看他这边通过什么密钥对吧这个生成这个签名然后进行数据的一个什么加密当然了这个用户中心这边都需要准备哪些数据那是不是要看存管系统那边都需要啥就银行那边都需要啥这个咱是不是可以查那个银行存管系统的那个接口
[03:53] 说明文档对不对那加密完之后呢存款代理服务这边要保存一个什么呀交易记录诶注意了交易记录诶有的学生说老师咱咱现在都开始交易了吗诶这里边是这样子的我们把开户也当成是一种什么呀交易记录就是说将来我们的交易肯定有这个什么呀比如投资人要投投投资嘛这肯定是交易嘛对不对但我们把开户啊用户开户啊包括将来用户销户
[04:23] 对不对这些也都作为交易记录进行什么呀保存啊所以说呢从来代理服务证就会把这次这个开户呢就当成一次什么呀交易记录进行保存但是这时候呢状态它里边有个状态值是什么呀未同步这个状态跟哪有关呢咱前面在做整体的需求分析的时候说是不是跟这有关系对不对啊跟这有关系因为其实你第一个阶段走的时候这个开户还没成功嘛所以你这只能是先临时
[04:53] 设置成这个状态将来整个开户都没问题了我们再改成什么一同步那这边保存完之后呢就返回什么呀返回那个加密获得数据给用户中心用户中心再返回给谁呀前端来至此第一阶段我们说这个需求包括这个流程我们就给大家说明白其实第一阶段不是很复杂你只看第一阶段不是很复杂就这一块它不是很复杂所以这是需求我们给大家先明确一下
[05:26] 然后接下来咱回到讲义里边那么讲义里边提醒大家注意一点就是说呢因为咱整个开货呢涉及到将来对吧要访问银行存款系统所以他建议你查一查这个接口说明里边的个人榜卡开户因为咱开户这一块呢就用到这个接口他说让你熟悉一下啊这个接口呢他都接收哪一参数有什么返回之道呢这个呢其实我们前面说过是想让大家下去自己看一下我们这也打开吧打开就是这个啊
[05:55] 这个结果说明这个我们打开字节一起看一下在这他说就是这个个人绑卡贷户这个和接口名称哎这这个你要你要去那个银行存款系统里面查一查有这么一个接口这个接口是干嘛的呀对不对啊他的接口模式是要过什么呀过网关对不对啊是不是一部通知啊这里边是整个接口的一个说明啊然后这里边重点你要看就是你访问他的时候都需要传来的数据你看
[06:24] user number request number哎你看好了是不是跟我们刚才讲这个第一阶段需求的时候这里边的东西对应吗跟这对应吗对对应刚才呢我也给大家提过了我们说啊用户中心这边是不是要准备一堆数据准备哪些数据呢其实你要看银行这边要哪些东西他要啥我们这边就准备啥那银行那边到底要啥呢那你要去哪瞅啊
[06:47] 那就要查这个什么文档你看他这边要查User Number,Credit Number包括其他一些信息他要查你就准备啥就行只不过这里边他要的数据有些是前端直接传过来前端直接传有的是在用户中心咱们直接在这提供的这是要看情况对不对然后你再看他那边处理完之后会给我们返回什么东西对不对流水号也有User Number等等相关的一些信息这异故通知咱回头再说现在还用不着了
[07:17] 就是提醒大家一定要注意看这些东西呃这是咱第一阶段啊生成开户数据相关的需求那这个明确了之后咱接下来跟以往的套路一样先定义什么呀对接口这个定义接口你要注意可是分两个地方定义为啥两个地方你看看咱第一阶段这个业务当中涉及到几个微服啊两个吧一个用户中心一个什么呀从两代里服
[07:46] 所以说这两边啊这两个微服里边都要定义什么呀接口那咱按照他这个流程对不对我们先去用户中心把这个接口先定义一下然后再去存管代理服务这边定义接口呃那咱看看啊接口大家都比较熟悉我们的接口全部都是放在哪个工程里边的呀对API工程就这个我们找一找那个consumer用户中心他的这个接口就是这个
[08:20] 那在这呢我们是不是需要再加一个方法了对不对加什么样的方法呢咱看一下讲一把这个代码我就不再给大家敲了啊核心的代码我们给大家敲一敲你这里边就是可注意的consumer发明就开户吧啊开户然后呢你看看重点观察他的什么呀这个方法的参数和什么呀反合体就是这个范写那这两个类呢不需要大家这个去编写了我们直接提问给大家整个开户这个
[08:51] 整个开会这个功能当中有好多这样的类都需要大家写你去哪找你去哪找资料文件夹里边有一个类这里边都在这里边放着你看是不是就有这样你把相关的类考到包里边就行了那具体考到哪个包里边呢你打开这个代码你看一下这个观察不方便你看它这个package你就观察这就行了你看它是不是在consumer API工程consumer model里边对不对然后你再看这个
[09:21] gitway request他是在发你看他是在什么呀depository这个包里边对不对所以说呢那你就按照他这个要求放呗这个control c然后呢我们张到这个什么呀model里边对不对control v张过来这就有了代码一会再看啊然后刚才这个gitway这个他是不是要求你再建一个包吗depository是不是那你在这就按照要求在这在这啊
[09:53] 这一层新建一个包包呢在这deposter啊然后呢我们就把给他位request然后呢也给他粘过来伸到这对这样吧然后呢咱们接下来把这两块粘过来的这个类我们看一下先看一下consumer request呃这块大家要注意你看他在这个方法里边是不是充当什么呢呀充当参数那这里边刚才大家看这个图了
[10:30] 我们是不是前端会发请求到用户中心那你应该基本上能猜出来这个consumer request不就是封装前端发过来的那些数据对不对都有哪些数据呢我们可以看一下大家过一遍了想一下你现在自己看啊有什么用户名啊正式姓名啊什么身份证号啊银行卡号啊手机号啊等等相关的一些东西啊当然你像这些数据可能不是前端提供的而是这个请求到达我们consumer的时候咱在consumer里边再给它生成这些值
[11:01] 有些只是前端重来有些不是这是封装封装一些请求数据的或者开会的一些数据然后还有 gateway requestgaytway request其实就是最终返回的数据gaytway request你看图是封装这看好了这这个地方是不是他整个要将来要到存款代理服务这边要加密了加密完之后返回一些数据签证数据然后再给前端锁这一块的数据是封装到哪来
[11:34] 对封装到我们说的这个哪里边对就是这个gateway request就这一块具体的这些数据都是干嘛咱到时候开发了这个功能的时候你自然就明白这是那咱先来把这个接口给粘过来就行了就这一块外嘛下到下面对吧好这是接口我们定义好定义好之后咱跟以前一样顺手把扛出了里边的这个方法先来一个空实现先知道了
[12:13] 那这就要去哪个微服里边了consumer嘛对不对consumer我们找一找好consumer在这对吧consumer control他正常应该要报错了吧是不是因为我没有加接口员加了一个方法嘛对不对所以这一定会报错好咱让他来个这个什么呀我们说的空时线是不是就行了就这个对吧他应该会出现在最下面稍等跑哪去了在这这个地方
[12:55] 这然后呢咱们把相关的一些注释给他加上了好吧这注释我就不再敲了这里边就好多都是sweat的那些注释这个比较消耗时间我就在这直接粘过来了不耽误时间是这里吧呃这里边的话就是你粘过来之后你要熟悉一下这里边的一些代码啊熟悉啥呢sweat这个注释其实你看不看都可以你重点这个你得看一下
[13:29] 是不是这个访问路径将来对吧前端是不是要往这发请求数据是不是要封装到这里对吧整个第一阶段这个业务处理完之后返回的数据加密后的数据是不是封装到这里边然后发到前端了对不对这刚才需求咱们说过这是这个那么这是哪一块的接口咱要搞定了呀对于用户中心呢那咱一会儿再搞定哪边存管代理服务那边的接口

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解银行开户流程的系统架构与代码实现，重点是用户中心生成开户数据接口的定义与开发。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示开户业务流程图，包含浏览器/App、用户中心、存管代理服务、存管系统、开卡银行五个模块，以及各模块间交互的详细步骤（如1.1生成开户请求数据、1.2准备开户基础数据、2.1跳转相关开户接口等）。
画面2：PPT页面，标题为“3.3 第一阶段: 生成开户数据”，内容包括“3.3.1 需求分析”和“3.3.2 接口定义”，并指出在“wanning2p-api”工程中新增`createConsumer`方法。
画面3：文件资源管理器，显示“wanning2p > day06”目录下的文件，包括“开户业务流程图.jpg”、“系统对接规范与安全机制方案.docx”等。
画面4：PPT页面，标题为“接口参数”，展示“请求”和“返回”两个部分的参数表，包括参数名称、必填、类型、长度、参数说明等字段。
画面5：PPT页面，展示“请求”部分的参数表，包含userNo、requestNo、realName、userRole、mobile、cardNumber、callbackUrl等字段。
画面6：IDEA开发工具界面，显示“wanning2p-api”工程结构，同时弹出多个窗口，包括“wanning2p-apollo”、“adminservice”、“Apollortal”、“configservice”等。
画面7：Notepad++编辑器，显示“GatewayRequest.java”文件内容，包含`@ApiModel`注解定义的类，字段包括`serviceNames`、`platformNo`、`requestData`、`signature`、`depositoryUrl`。
画面8：IDEA开发工具界面，显示“ConsumerRequest.java”文件内容，包含`@ApiModel`注解定义的类，字段包括`id`、`username`、`fullname`、`idnumber`、`bankCode`、`cardnumber`、`mobile`、`role`、`requestNo`、`userNo`、`callbackUrl`。
画面9：IDEA开发工具界面，显示“ConsumerRequest.java”文件内容，展示`@ApiModel`注解定义的类，字段包括`id`、`username`、`fullname`、`idnumber`、`bankCode`、`cardnumber`、`mobile`、`role`、`requestNo`、`userNo`、`callbackUrl`。
画面10：IDEA开发工具界面，显示“ConsumerRequest.java”文件内容，展示`@ApiModel`注解定义的类，字段包括`id`、`username`、`fullname`、`idnumber`、`bankCode`、`cardnumber`、`mobile`、`role`、`requestNo`、`userNo`、`callbackUrl`。
画面11：IDEA开发工具界面，显示“GatewayRequest.java”文件内容，包含`@ApiModel`注解定义的类，字段包括`serviceNames`、`platformNo`、`requestData`、`signature`、`depositoryUrl`。
画面12：IDEA开发工具界面，显示“ConsumerAPI.java”文件内容，包含`RestResponse register(ConsumerRegisterDTO consumerRegisterDTO)`和`RestResponse GatewayRequest createConsumer(ConsumerRequest consumerRequest)`方法。
画面13：IDEA开发工具界面，显示“ConsumerController.java”文件内容，包含`@ApiOperation("用户注册")`和`@PostMapping(value = "/consumers")`方法。
画面14：IDEA开发工具界面，显示“ConsumerController.java”文件内容，包含`@ApiOperation("生成开户请求数据")`和`@PostMapping(value = "/my/consumers")`方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```
1. 在wanning2p-api工程中的ConsumerAPI接口中新增createConsumer方法：
    * 生成开户请求数据
    @param consumerRequest 开户信息
    @return
    RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);

2. 在wanning2p-consumer-Service工程的ConsumerController类中实现该方法：
```

画面4：
```
请求
参数名称	必填	类型	长度	参数说明
userNo	Y	S	50	平台用户编号
requestNo	Y	S	50	请求流水号
realName	N	S	50	用户真实姓名
idNumber	N	S	50	用户证件号
userRole	Y	S	50	如投资人/借款人/担保机构
mobile	N	S	50	银行预留手机号
cardNumber	N	S	50	银行卡号
callbackUrl	Y	S	256	页面回调 URL

返回
参数名称	必填	类型	长度	参数说明
```

画面7：
```
package cn.ictcast.wanning2p.sql.depository.model;

import io.Swagger.annotations.ApiModel;
import io.Swagger.annotations.ApiModelProperty;
import lombok.Data;

@ApiModel(value = "与银行存管系统对接使用的签名请求数据")
public class GatewayRequest {
    @ApiModelProperty("请求的存管接口名")
    private String serviceNames;
    @ApiModelProperty("平台编号，平台与存管系统签约时获取")
    private String platformNo;
    @ApiModelProperty("业务数据报文，json格式")
    private String requestData;
    @ApiModelProperty("对requestData参数的签名")
    private String signature;
    @ApiModelProperty("银行存管系统地址")
    private String depositoryUrl;
}
```

画面8：
```
package cn.ictcast.wanning2p.api.consumer.model;

@ApiModel(value = "ConsumerRequest", description = "平台-端用户开户信息")
public class ConsumerRequest {
    @ApiModelProperty("id")
    private Long id;
    @ApiModelProperty("用户名")
    private String username;
    @ApiModelProperty("真实姓名")
    private String fullname;
    @ApiModelProperty("身份证号")
    private String idnumber;
    @ApiModelProperty("银行编码")
    private String bankCode;
    @ApiModelProperty("银行卡号")
    private String cardnumber;
    @ApiModelProperty("手机号")
    private String mobile;
    @ApiModelProperty("角色")
    private String role;
    @ApiModelProperty("请求流水号")
    private String requestNo;
    @ApiModelProperty("用户编号")
    private String userNo;
    @ApiModelProperty("页面回调 URL")
    private String callbackUrl;
}
```

画面11：
```
package cn.ictcast.wanning2p.api.consumer.model;

@ApiModel(value = "GatewayRequest", description = "与银行存管系统对接使用的签名请求数据")
public class GatewayRequest {
    @ApiModelProperty("请求的存管接口名")
    private String serviceNames;
    @ApiModelProperty("平台编号，平台与存管系统签约时获取")
    private String platformNo;
    @ApiModelProperty("业务数据报文，json格式")
    private String requestData;
    @ApiModelProperty("对requestData参数的签名")
    private String signature;
    @ApiModelProperty("银行存管系统地址")
    private String depositoryUrl;
}
```

画面12：
```
RestResponse register(ConsumerRegisterDTO consumerRegisterDTO),
RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
```

画面13：
```
@ApiOperation("用户注册")
@ApiImplicitParam(name = "consumerRegisterDTO", value = "注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumers")
public RestResponse register(ConsumerRegisterDTO consumerRegisterDTO) {
    consumerService.register(consumerRegisterDTO);
    return RestResponse.success();
}

@Override
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    return null;
}
```

画面14：
```
@ApiOperation("用户注册")
@ApiImplicitParam(name = "consumerRegisterDTO", value = "注册信息", required = true,
        dataType = "AccountRegisterDTO", paramType = "body")
@PostMapping(value = "/consumers")
public RestResponse register(ConsumerRegisterDTO consumerRegisterDTO) {
    consumerService.register(consumerRegisterDTO);
    return RestResponse.success();
}

@Override
@ApiOperation("生成开户请求数据")
@PostMapping(value = "/my/consumers")
public RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest) {
    return null;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，包含五个模块：浏览器/App、用户中心、存管代理服务、存管系统、开卡银行。各模块间有带编号的箭头连接，表示流程顺序。
画面2：PPT标题“3.3 第一阶段: 生成开户数据”，内容包括“3.3.1 需求分析”和“3.3.2 接口定义”。
画面4：表格数据，标题“接口参数”，包含“请求”和“返回”两个部分，每个部分有“参数名称”、“必填”、“类型”、“长度”、“参数说明”等字段。
画面5：表格数据，标题“接口参数”，包含“请求”部分，字段包括“userNo”、“requestNo”

