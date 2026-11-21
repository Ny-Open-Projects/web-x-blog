# day08-15-交易中心保存标的先决条件

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-15-交易中心保存标的先决条件_【海量资源尽在 666java.com】.mp4
- 时长 11分21秒（音频 681s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好前面呢我们把发标业务当中的1.1到1.3这一块代码呢全部编写完毕了那接下来呢咱还不能着急着测试因为这里边呢还有一个细节问题需要解决而且呢这个问题呢是跟前端有关的我们需要配合前端的代码配合前端的业务去编写一块代码是啥问题呢咱看一下
[00:29] 就是说呢你现在能登录啊用户能登录但不代表你一定能发标说这个借钱啊不是说你想借就能借我们发标呢它是有一些先决条件我们要做一些什么呀判断啊看你能不能干什么呀发标你能不能借钱我们都需要做哪些判断呢大家看一下两个判断大家看这儿啊他说用户登录成功之后可以直接进行发标但是根据业务需求只有在什么呀
[00:59] 以开户的情况下才可以发表哎这个业务咱是之前开发过的咱是不是讲的注册登录开户对不对那讲了登录之后其实用户就能登录登完之后呢你这个前端里边好多功能他都能点包括这个谁啊发表但这个时候有可能他还没有进行什么呀开户啊也就是说他还没有绑定什么呀洋卡呀还没有登记身份证号啊等等相关的一些信息那你说他在没有开户的情况下
[01:29] 他发标有意义吗有意义吗你不开户不登记你的身份证银行卡信息我让你发标了别人给你投标了钱打到什么地方我都不知道你的银行卡是什么对不对这钱给谁是不是所以说没有开户不允许进行什么呀发标这是一个先决条件如果发现你没有开户你就去发标他会判断前端会判断
[01:57] 会给你跳转到什么呀开户界面哎你先开户然后你就可以进行发表这是第一个先进条件第二个先进条件就是这个借款的金额不能超标哪个借款金额咱看这儿啊这儿看这儿这儿呢其实是一个文本框这儿是一个文本框就是你可以自己填写一个数字就是你想借的这个金额但是这个金额你不能随便填我我借个一千万是不是那那那肯定不行这儿呢我们得
[02:27] 有一个限制也就是说呢每个用户他都有自己的一个可带的一个什么样额度来看这儿吧然后我们还需要判断用户申请的这个什么借款金额是否超标如果超标就不允许发标那这个什么叫超标什么叫不超标呢其实每个用户啊每个用户都有自己的一个什么样可带额度大家应该好多人都熟悉吸引卡了熟悉吸引卡
[02:58] 甚至在座各位应该有的人都办过信用卡每个人的信用卡你那个那个额度一样吗不一样吧是不是每个人都有一个这个额度那我问你你偷吃信用卡的时候刷卡的时候能超过这个额度吗一般是不允许的是不是不允许那我们这也是一样的你每个用户啊我们都会给你指定一个可带的额度比如说五万块钱比如说五万块钱那你将来借钱的时候你就不允许超过什么呀对不允许超过五万就这个意思
[03:29] 那我要判断你要是输入一个6万那我就不允许你进行什么呀发标了所以说呢呃用户登录成功之后要想发标我们还得做两个判断啊再次给大家强调一下一个就是判断他有没有开户一个就是判断他的这个借款的金额有没有什么呀超标就是超过他本身的这个可待额度那这些判断呢其实都是前端帮我们搞定了就是前端代码已经搞定过了这个代码都写好但是呢
[03:57] 肯定是需要我们后端做配合怎么配合呢大家注意了啊他有没有开户他有没有开户包括他这个什么可待额都是多少这个是需要我们后端进行查询的查询完之后返回给谁啊前端前端呢拿到这些信息之后就可以做一些处理那现在呢我们怎么知道他有没有开户怎么知道他的可待额都是多少很简单查一下当前登录用户的相关信息就OK啊
[04:27] 然后呢具体来说就是这个表大家看好了就是大家很熟悉的consumer这个表就这个表咱以前都用过了注册登录都用过了consumer这个表里边呢你看好了啊这儿有一个字段咱以前介绍过叫is bound cut这个值这个值其实就是01了比如说0就表示没开户没绑定银行卡1就表示已开户已经绑定过银行卡还有一个字段叫这个字段就它下面这个这个
[04:57] 这个字段它的值就表示当前这个用户的最大的这个什么呀对可以贷款的一个额度所以说我们后端要做的事很简单就是查一下当前登录用户的这个什么信息就行重点就是这两个字段的信息很简单前端的就会往这发请求来获取这个信息你看咱的表数据咱表里边你看目前这个谁呀你看这个ease bond card你看有的是零有的是一是一的表是开过货
[05:29] 是零的就表示能登录啊但是你还没有开户然后这个字段咱目前都是空的嘛就可待而度咱一会自己设置一下就行所以咱接下来要做的事就是干什么呀对我们呃后端很简单啊就是在control了里边就是用户中心这边啊增加一个方法来实现对当前登录用户信息的一个什么呀查询就行很简单翻个个前端前端怎么用他那个代码写好咱不用管
[05:58] 那咱就需要找到这个consumer这一块的接口API吧是不是consumerconsumer API在这里边的话我们需要增加一个方法增加什么方法呢就是获取当前登录用户有的学生说老师这不是有了吗咱刚才这个在实现保存这个标底信息的时候是不是刚刚用过这个方法但是这个方法咱暂时用不了为啥用不了呢来我给大家说一说
[06:31] 功能倒是咱要的功能但是呢你打开control的啊咱看不就是他吗是不是大家看一下我们刚才在实现这个方法的时候说的是L打头L打头证明这个方法是给什么呀后端其他微服使用的不是给谁使用的呀不是给前端使用的我们现在这个功能就获取登录用户的信息是谁去调用要获取这个信息是前端所以功能是我们想要的功能但是呢
[07:02] 我们用不了啊我们单独需要再定义一个方法就OK了让我们跟讲义保持一致吧单独写一个啊功能的确是一样好大家看一下我们仍然也是获取当前登录用户的什么呀相关对信息的一模一样然后发展名换一换啊叫get my什么呀consumer反正指啥的都一样将来查出来的用户信息就封装到consumer.co里了
[07:39] 这是接口里边加了一个放加完之后呢咱就去扛出来里边他应该会报错了吧然后咱把这个方案生成一下里边代码呢很简单给大家想一下是不是谁发标我就要获取谁的信息那谁发标这个发标人不就是当前登录用户吗是不是怎么获取当年登录用户你还有印象吗这个咱刚才刚写过这个代码是不是通过咱封装好的一个工具类对吧security youtube他有个方案叫get user
[08:12] 他就能帮我们获取到当前登录用户然后获取到当前登录用户之后呢我们是根据他的手机号做了一次什么呀查询这个是不是他刚才也刚写过给他目标是不是就调药草做一次查询然后就得到考试吗地球这个对象里边就存有这一堆数据这一堆数据当然就包含我们想用的这个一字班卡的呀包括这个什么呀可带小度说这个代码是非常简单我就不再挨个给他敲了
[08:44] 我刚写过这类似的这种代码好大家看一下就是一个简单的查询嘛我们先得到当前动用户然后就得到他的手机号然后呢调要从根据手机号做一次查询就查到该用户所有的信息了然后就返回给谁啊这是我们后端要要配合前端写的一块代码那这个功能实现完之后呢最后呢我们要注意啊再次给大家强调一下当你的这个代码写完之后前端啊前端那个发标页面那会自动往这发请求这个事你都不用管
[09:22] 刚才说了前段代码他写好他会自动往这发请发请之后是拿到这里边的信息拿这个信息之后他会判断里边什么东西对就这两个资格然后判断他们的值然后做一些业务处理咱就不用管另外这里边就是给大家强调一下这个可待额度我们刚才说了每个人的可待额度是不一样有的人可能是5000有的人1万有的人3万有的人5万对吧都不一样这个其实是跟借款人自身的综合情况比如说你的信用记录
[09:53] 你的月收入对吧你的工作姓氏等等包括你的年龄都是有关系那么这个熬度的这个值到底是怎么产生的它是由P2P平台根据你借款人的资深综合情况来进行评估的这个不是说你想借多少就能借多少这是真实的一个业务我们给大家说一说那咱们这儿呢暂时做了一个讲话处理因为咱这儿还没有没有讲到那个那个分控风险控制那一块其实这个呢是可以在风险控制那一块由P2P平台
[10:23] 评估完之后给你设置一个值啊我们这呢暂时咱自己怎么办呢你直接啊去表里边你找到你看你要用哪个用户对不对找到这个用户直接在这啊自己给一个值就行了比如我这就给了一个多少3万对不对啊就可以我们自己给一个值先拿着用一下就行啊所以这是这个细节吗给大家说一下另外这个值不能低于2000啊啊低于2000我们觉得你就
[10:54] 借这么点钱你就找亲戚朋友一件完事了你用不着去我们这个什么呀屁股屁股心态不用费这个劲这是吧我们针对这个哪一块对就是1.1到1.3这个其实就是保存标的信息针对这个业务我们做了一些完善就是补充了一个发表业务的一个什么先决条件的一个判断这一块我们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解发标业务的先决条件，包括在ConsumerAPI和ConsumerController中实现获取当前登录用户的方法，并展示相关数据库表结构和数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档“3.2.3 发标业务的先决条件”，说明在ConsumerAPI中新增获取当前登录用户的方法，代码为：RestResponse<ConsumerDTO> getMyConsumer();。
画面2：展示数据库表“consumer”的字段结构，包括ID、USERNAME、PASSWORD、MOBILE、USER_TYPE、AUTH_LIST、IS_BIND_CARD、HOME_ADDRESS、STATUS、REQUEST_ID等字段。
画面3：在画面2基础上，鼠标悬停在“IS_BIND_CARD”字段上，显示其注释“是否绑定卡片”。
画面4：展示数据库表“consumer”的数据记录，包含用户名、手机号、用户类型、授权列表等信息。
画面5：在IDE中展示ConsumerAPI.java文件，代码为：RestResponse register(ConsumerRegisteredDTO consumerRegisterDTO); 和 RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);。
画面6：在IDE中展示ConsumerAPI.java文件，代码为：RestResponse<ConsumerDTO> getCurConsumer();。
画面7：在IDE中展示ConsumerController.java文件，代码为：@ApiOperation("获取登录用户信息") @GetMapping("/1/curConsumer") public RestResponse<ConsumerDTO> getCurConsumer() { ConsumerDTO consumerDTO = consumerService.getByMobile(SecurityUtil.getter().getMobile()); return RestResponse.success(consumerDTO); }。
画面8：在IDE中展示ConsumerController.java文件，代码为：RestResponse<ConsumerDTO> getCurConsumer();。
画面9：在IDE中展示ConsumerController.java文件，代码为：@ApiOperation("对网关保护资源，进行认证拦截测试") @ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String") @GetMapping(value = "/a/consumers/test") public RestResponse<String> testResources(String jsonToken) { return RestResponse.success(EncryptUtil.decodeUTFSStringBase64(jsonToken)); }。
画面10：展示数据库表“consumer”的字段结构，包括ID、USERNAME、PASSWORD、MOBILE、USER_TYPE、AUTH_LIST、IS_BIND_CARD、HOME_ADDRESS、STATUS、REQUEST_ID等字段。
画面11：在IDE中展示ConsumerController.java文件，代码为：@Override @ApiOperation("获取登录用户信息") @GetMapping("/1/curConsumer") public RestResponse<ConsumerDTO> getCurConsumer() { ConsumerDTO consumerDTO = consumerService.getByMobile(SecurityUtil.getter().getMobile()); return RestResponse.success(consumerDTO); }。
画面12：展示文档“3.2.3 发标业务的先决条件”，说明consumerDTO中的loanAmount属性表示可贷额度，isBindCard表示是否开户，前端发标页面会自动访问该方法，获得这些数据后会自动进行业务处理。
画面13：展示数据库表“consumer”的数据记录，包含用户名、手机号、用户类型、授权列表等信息。
画面14：展示文档“3.2.3 发标业务的先决条件”，说明在ConsumerAPI中新增获取当前登录用户的方法，代码为：RestResponse<ConsumerDTO> getMyConsumer();。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
// 获取当前登录用户
@return
RestResponse<ConsumerDTO> getMyConsumer();
```
画面5：
```java
RestResponse register(ConsumerRegisteredDTO consumerRegisterDTO);
RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
```
画面6：
```java
RestResponse<ConsumerDTO> getCurConsumer();
```
画面7：
```java
@ApiOperation("获取登录用户信息")
@GetMapping("/1/curConsumer")
public RestResponse<ConsumerDTO> getCurConsumer() {
    ConsumerDTO consumerDTO = consumerService.getByMobile(SecurityUtil.getter().getMobile());
    return RestResponse.success(consumerDTO);
}
```
画面9：
```java
@ApiOperation("对网关保护资源，进行认证拦截测试")
@ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String")
@GetMapping(value = "/a/consumers/test")
public RestResponse<String> testResources(String jsonToken) {
    return RestResponse.success(EncryptUtil.decodeUTFSStringBase64(jsonToken));
}
```
画面11：
```java
@Override
@ApiOperation("获取登录用户信息")
@GetMapping("/1/curConsumer")
public RestResponse<ConsumerDTO> getCurConsumer() {
    ConsumerDTO consumerDTO = consumerService.getByMobile(SecurityUtil.getter().getMobile());
    return RestResponse.success(consumerDTO);
}
```
画面12：
```java
consumerDTO中的loanAmount属性表示可贷额度，isBindCard表示是否开户，前端发标页面会自动访问该方法，获得这些数据后会自动进行业务处理。
```
画面14：
```java
// 获取当前登录用户
@return
RestResponse<ConsumerDTO> getMyConsumer();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、12、14：PPT标题为“3.2.3 发标业务的先决条件”，内容包括在ConsumerAPI中新增获取当前登录用户的方法和在ConsumerController中实现该方法。
画面7、11：在IDE中展示ConsumerController.java文件，代码为：@ApiOperation("获取登录用户信息") @GetMapping("/1/curConsumer") public RestResponse<ConsumerDTO> getCurConsumer() { ConsumerDTO consumerDTO = consumerService.getByMobile(SecurityUtil.getter().getMobile()); return RestResponse.success(consumerDTO); }。
画面9：在IDE中展示ConsumerController.java文件，代码为：@ApiOperation("对网关保护资源，进行认证拦截测试") @ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String") @GetMapping(value = "/a/consumers/test") public RestResponse<String> testResources(String jsonToken) { return RestResponse.success(EncryptUtil.decodeUTFSStringBase64(jsonToken)); }。
画面2、3、10：展示数据库表“consumer”的字段结构，包括ID、USERNAME、PASSWORD、MOBILE、USER_TYPE、AUTH_LIST、IS_BIND_CARD、HOME_ADDRESS、STATUS、REQUEST_ID等字段。
画面4、13：展示数据库表“consumer”的数据记录，包含用户名、手机号、用户类型、授权列表等信息。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

