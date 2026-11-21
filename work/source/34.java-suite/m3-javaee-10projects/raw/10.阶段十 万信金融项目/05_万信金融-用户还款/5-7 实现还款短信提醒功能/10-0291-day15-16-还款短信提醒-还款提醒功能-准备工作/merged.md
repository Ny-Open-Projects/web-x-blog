# day15-16-还款短信提醒-还款提醒功能-准备工作

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-7 实现还款短信提醒功能
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-7 实现还款短信提醒功能\day15-16-还款短信提醒-还款提醒功能-准备工作_【海量资源尽在 666java.com】.mp4
- 时长 9分27秒（音频 567s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们把还款短信提醒这个功能当中所涉及到的两个接口呢已经定义好那咱接下来就进行功能实现首先我们要实现的是这个还款提醒接口那这个接口的功能呢主要就是查询还款人的什么呀相关信息就是这个用户的信息我们主要要的就是他的什么信息啊手机号因为我要给他发那个短信吧所以我得知道他的手机号
[00:30] 所以说我们接下来呢先把这个接口给他实现了那咱接下来简单分析分析吧我们这个什么呀还款短信提醒这个功能是不是应该是在哪个微服里边啊是在repayment Service这个微服里边但是呢我现在是不是需要获取获取什么呀用户的信息是不是借款人或者还款人他都是用户嘛我要得到他的手机号是不是那这个信息在哪
[01:00] 这个信息呢大家一定要注意了这个信息呢是在之前我们说的这个什么consumer这个表里面你看这里边是不是就有手机号在哪呢在这是不是就有手机号对吧我现在就要获取这个手机号这可以怎么获取对不对这个功能咋实现呢那你说呢功能我是要放到这个什么呀repayment Service这边但是我需要的数据其实是在哪边对是在我们的consumer呢
[01:34] 是在consumer这边那我们很自然想到什么呀对我要在repayment这边通过fain发起远程请求到哪consumer让consumer这边是不是帮我们查询某个用户的手机号是不是就行了那我们的这个环卫服务往这儿发请求的时候是不是要传过去一个一个什么数据让他根据这个数据进行查询对吧我们能传给他什么数据呢咱看看
[02:03] 我们还款微服这边是不是要查询这个还这个到期的还款计划吗你有印象吗对不对我们要查这个那这里边的话你看我们都能得到用户的什么信息我们在查这个还款计划到期还款计划的时候你看这里边是不是有用户的ID是不是你看是不是哎我们在查询这个到期还款计划的时候我可以得到这个还款得到这个用户的ID那得到这个ID之后呢我就可以把这个ID干什么呀通过Fain发到什么呀发到Consumer那边
[02:34] 让他根据ID去哪个表里边查手机号对consumer这个表里边对不对就可以查到他的手机号所以这个功能咱整体是需要这么设计一下的啊那咱看看讲义吧接下来你看讲义里边说了啊我们首先要在这个consumer这边对吧接口里边是不是新增一个方法哎这个就是根据用户的ID查询这个什么呀他的手机号这个信息了对不对
[03:02] 然后呢在Controller当中就要实现这个方法大家注意这是L开头的对不对是专门供微服务访问的是吧那然后呢这边啊就是consumer这边的功能都搞定了之后呢我们就可以在还款微服务这边创建一个什么呀非印代理对不对将来呢我通过这个非印代理就可以往这干什么呀发请求从而得到借款人的信息那咱接下来呢就把这块的这个准备工作先做一做
[03:32] 咱先找到这个API工厂找到consumer的这个接口应该是consumer API是不是咱先看以前咱有没有这个现成的功能咱看看啊你看这儿这儿有个什么呀获取借款人用户信息哎我觉得这个不就是咱正好想要的这个方法吗是不是大家看一下这个参数应该是用户的ID吗是不是
[03:58] 然后呢这个查询出来的就是用户信息封装到这个包卖DQ里面这里边封装了肯定有手机号我们可以进去看看你看有手机号没有有吧这功能是不是咱以前开发过了那这个功能到底能用不能呢那咱看看它的具体实现吧它这个实现是不是应该是在consumer这个v4里边啊我们找一找找一找它的Controller吧get a bow是不是哎就是这个什么那你看这个咱能用吗
[04:31] 感觉功能上是能用的对不对你看传过来一个ID它掉药藏是不是这个方法我们就查出来这个用户的信息了但是大家注意你看这它配的这个路径是不是L开头的不是不是L开头的一般这种请求或者这个服务是给谁去用的给前端去用而我们现在这个需求是谁去用是一个微服务对吧缓缓微服务去用
[05:00] 所以说呢我们让缓缓微服务往这发起来我们觉得不合适啊就是功能是我们想要的功能但是就是这个路径啊或者请求地址他不是给谁啊给微服务去用了是给前端用那怎么办那简单呀咱们单独再定义一个接口就行了呗对不对我们再定义一个接口啊那当然这个接口呢跟咱现有的这个功能都是什么样一样的是不是我就复制粘贴一下改一改啊
[05:29] 你比如说这我加个注释是供什么呀对微服务访问的上面这个肯定是供前端嘛是不是那这个名字我们不能一样呢对不对方案名是不是我这就加个MOBILE吧虽然我们是把整个用户的信息都查出来了但是我最终想要的是他的什么呀手机号所以这个方案名呢我们跟上面呢要有所区别啊这咱先吧
[05:55] 这个接口里边的这个方法先定义出来啊咱看跟讲义是否保持一致啊没错吧对不对啊这呢我们可以再加上一个注释这是谁啊用户id吗用户标识是吧然后呢我们就可以去control这里边control了一定是报错了吗对不对那我们把这个什么样方法先给他生成出来生成出来生成出来之后呢你要注意我们说的功能都是一样的吗所以说这里边代码一模一样你直接拿过来
[06:30] 对吧然后上面这一堆基本上也是一样的但是你需要改一下那个请求路基这呢我为了区分啊这也加上供什么呀供对微服务方然后这呢我们就要给他改成什么呀你看下面是不是改成L开头了就行那我将来在这个什么呀环环微服务这边发请求是不是就往这发对吧通过飞是不是往这发请求传过来一个用户ID
[07:02] 哎他掉到右层就可以把用户的信息查出来封装到这个包包DTO里边这里边就有什么呀我们想要的手机号对让我们看讲义里边我们是否保持一致对不对你看这是不是L开头的是不是放下名对吧其他的其实跟我们现有的就是这个方法都是什么一样的哎这里边注意了这个注解可不敢少了呀来我们给他加上啊
[07:32] 其他的这些细节你反正你写的时候要注意一下啊这是大家看一下这是我们用户中心这边就是卡村吗这边我们要编写的代码是不是就搞定了对不对那接下来我们是不是就应该在repayment Service这边新建一个什么呀非应代理然后呢是不是就是往这干什么呀对发请求就行了啊那咱接下来看看讲义我们要定义一个什么样的非应代理呢看一眼啊
[08:01] 飞行代理对于大家来说应该是一点都不陌生了其实就是一个接口对不对那这里边重点呢就是这个路径你别写错了这个路径是不是应该跟这儿是要保持什么呀一致的当然前面呢你要多加一层微幅的这个什么呀基本访问路径那这块呢我就不再过多给大家编写了因为这个大家都比较熟那我们应该是要去哪
[08:26] 去对缓缓微服务这边找到argent这个包然后我们再定义一个代理它是一个接口对吧然后这里边的代码我就不再给大家编写了再次给大家强调一下就是这个路径千万别写错了啊这是非硬代理那有了这个代理之后呢大家想一下我将来是不是就可以在缓缓微服务这边通过调用这个方法是不是就往什么呀consumer这边
[09:04] 发了一个请求我把ID传过来之后这边就帮我查出来什么呀借款人的用户信息封装到这个DTO对象里边里边就包含有手机号对不对这是咱爸这个什么呀爸实现这个什么呀还款服务还款提醒功能的准备工作吧相当于是一个准备工作给搞定

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在还款服务中通过 Feign 客户端调用用户服务，获取借款人信息并发送还款提醒。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了还款服务的项目结构，包含 Controller、entity、Mapper 等包，以及多个配置类和 Mapper 文件。
画面 2: 在数据库管理工具中查看了 `p2p_borrower` 表的结构，包含字段如 FULLNAME、USER_NO、MOBILE 等。
画面 3: 在数据库管理工具中查看了 `repayment_plan` 表的结构，包含字段如 ID、PROJECT_ID、USER_NO 等。
画面 4: 在数据库管理工具中查看了 `consumer` 表的结构，包含字段如 ID、FULLNAME、USER_NO 等。
画面 5: 在 IDEA 中查看了 PPT 内容，其中包含在 ConsumerAPI 中新增方法、在 ConsumerController 中实现方法、创建 Feign 代理、在 RepaymentService 中实现 sendRepaymentNotify 方法。
画面 6: 在 IDEA 中查看了 ConsumerAPI 接口定义，包含获取当前登录用户、获取借款人用户信息、获取当前登录用户余额信息等方法。
画面 7: 在 IDEA 中查看了 ConsumerAPI 接口定义，高亮显示了获取借款人用户信息的方法。
画面 8: 在 IDEA 中查看了 ConsumerController.java 文件，其中包含获取当前登录用户、获取借款人用户信息、获取用户可用余额等方法。
画面 9: 在 IDEA 中查看了 ConsumerAPI 接口定义，高亮显示了获取借款人用户信息的方法。
画面 10: 在 IDEA 中查看了 PPT 内容，其中包含在 ConsumerAPI 中新增方法、在 ConsumerController 中实现方法、创建 Feign 代理、在 RepaymentService 中实现 sendRepaymentNotify 方法。
画面 11: 在 IDEA 中查看了 ConsumerController.java 文件，高亮显示了获取借款人用户信息的方法。
画面 12: 在 IDEA 中查看了项目结构，高亮显示了还款服务的包路径。
画面 13: 在 IDEA 中查看了 ConsumerAgent.java 文件，其中定义了 ConsumerAPI 接口。
画面 14: 在 IDEA 中查看了 PPT 内容，其中包含在 ConsumerAPI 中新增方法、在 ConsumerController 中实现方法、创建 Feign 代理、在 RepaymentService 中实现 sendRepaymentNotify 方法。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 5:
```java
/**
 * 获取借款人用户信息-供服务访问
 * @param id 用户标识
 * @return
 */
RestResponse<BorrowerDTO> getBorrowerMobile(Long id);

@Override
@ApiOperation("获取借款人用户信息-供服务访问")
@ApiImplicitParam(name = "id", value = "用户标识", required = true, dataType = "Long", paramType = "path")
@GetMapping("/l/borrowers/{id}")
public RestResponse<BorrowerDTO> getBorrower(Long id) {
    return RestResponse.success(consumerService.getBorrower(id));
}

// 在还款服务中创建Feign代理
@FeignClient(value = "consumer-Service")
public interface ConsumerApiAgent {
    @GetMapping(value = "/consumer/l/borrowers/{id}")
    RestResponse<BorrowerDTO> getBorrowerMobile(@PathVariable "id") Long id;
}
```

画面 6:
```java
RestResponse<ConsumerDTO> getCurUser(String mobile);
// 获取当前登录用户
@return
RestResponse<ConsumerDTO> getCurUser();

// 获取借款人用户信息
@Param id
@return
RestResponse<BorrowerDTO> getBorrower(Long id);

// 获取当前登录用户余额信息
@Param userNo 用户编码
@return
RestResponse<BalanceDetailsDTO> getBalance(String userNo);
```

画面 8:
```java
public RestResponse<ConsumerDTO> getMyUser() {
    ConsumerDTO consumerDTO = consumerService.getBorrower(SecurityUtil.getUser());
    return RestResponse.success(consumerDTO);
}

@Override
@ApiOperation("获取借款人用户信息-供服务访问")
@ApiImplicitParam(name = "id", value = "用户标识", required = true, dataType = "Long", paramType = "path")
@GetMapping("/my/borrowers/{id}")
public RestResponse<BorrowerDTO> getBorrower(@PathVariable Long id) {
    return RestResponse.success(consumerService.getBorrower(id));
}

@Override
@ApiOperation("获取用户可用余额")
@ApiImplicitParam(name = "userNo", value = "用户编码", required = true, dataType = "String")
@GetMapping("/l/balances/{userNo}")
public RestResponse<BalanceDetailsDTO> getBalance(@PathVariable String userNo) {
    return RestResponse.success(consumerService.getBalance(userNo));
}
```

画面 13:
```java
package cn.itcast.wanxingzp.repayment.agent;

import cn.itcast.wanxingzp.repayment.api.ConsumerAPI;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@FeignClient(value = "consumer-Service")
public interface ConsumerApiAgent {
    @GetMapping(value = "/consumer/l/borrowers/{id}")
    RestResponse<BorrowerDTO> getBorrowerMobile(@PathVariable Long id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构、表格数据：
画面 5:
标题：8.3.1 还款服务还款提醒接口
内容：
1. 在 ConsumerAPI 中新增一个方法，用来根据用户 id 获取用户信息
2. 在 ConsumerController 类中实现该方法
3. 在还款服务中创建 Feign 代理
4. 在 RepaymentService 中实现 sendRepaymentNotify 方法

画面 10:
标题：8.3.1 还款服务还款提醒接口
内容：
1. 在 ConsumerAPI 中新增一个方法，用来根据用户 id 获取用户信息
2. 在 ConsumerController 类中实现该方法
3. 在还款服务中创建 Feign 代理
4. 在 RepaymentService 中实现 sendRepaymentNotify 方法

画面 14:
标题：8.3.1 还款服务还款提醒接口
内容：
1. 在 ConsumerAPI 中新增一个方法，用来根据用户 id 获取用户信息
2. 在 ConsumerController 类中实现该方法
3. 在还款服务中创建 Feign 代理
4. 在 RepaymentService 中实现 sendRepaymentNotify 方法

