# day02-9-获取短信验证码-接口定义

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-9-获取短信验证码-接口定义_【海量资源尽在 666java.com】.mp4
- 时长 12分50秒（音频 771s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好截止到目前的话我们已经把统一账户这个微服还有短信验证码这个服务全部都已经搭建好也部署好那现在呢等于说是万事俱备只剩敲台码是不是那咱们接下来就要动手开始编码实现注册功能那么这个注册功能呢我们准备把它拆分成三块然后各个击破拆分成哪三块呢第一块呢就是
[00:32] 发送并获取短信验证码这是第一个啊来我们标一个序号第二个就是对教验了啊教验手机号和短信验证码这是第二步第三步呢就是保存账户信息这三步呢完整的组成了哪个业务呢对注册
[01:06] 所以说呢我们是按照这个时序图把它给拆分成了几部分三部分我们结合这个图再给大家强调一下大家注意看一下第一部分就是从一到几到六看好了一到六用户呢先输入手机号然后这边呢就发请求到统一账户统一账户呢在远程请求验证码服务就让他发送验证码我们这边呢要获取一些证验标识包括用户的手机上会得到这个什么呀验证码一到六这是
[01:36] 第一步就是发送并获取短信研究码然后第二步呢就是从7到哪到10或者到11都行这呢其实就是校验什么呀你这个手机号是不是已经注册过了以及校验你这个短信研究码是正确的还是错误的然后反而结果给签字那如果我们发现你的手机号没有注册过就是你是新用户对吧短信研究码呢也这样通过了那接下来就是最后一步就是第三步了然后发起注册请求到用户中心
[02:07] 用中心呢再到统计账户这边就要进行什么呀对账号信息的一些保存然后把这个结果返回以前段这是第几步啊第三步啊这三步加起来就是一个什么功能啊注册功能那咱接下来先实现第一步第一步呢我们说的就是发送并获取短信验证码咱开始动动小手先实现这功能啊咱一步一步来各个击破吧
[02:36] 那具体该编写代码的时候咱从哪开始呢他他什么步骤呢对不对哎这个我们就要给大家强调强调之前咱说过的啊说过的什么呀看这儿看这儿啊呃咱们前面提到过咱们P2P项目是不是前后端分离架构是不是在这种架构下我们给大家强调了开发步骤那咱接下来是不是开始动手开发相当于咱们P2P项目的第一个这个功能了是不是
[03:07] 那我们再给大家强调一下这个开发步骤首先是搞需求分析需求分析呢我们刚才基本上给大家讲过了基本上就是看这个图就是看图说话分析分析这里边都涉及到哪些对微服务对吧这个步骤和流程是啥发了几次请求返回来什么东西等等等等主要就是这个图非常非常重要需求分析搞定之后呢咱具体编码的时候呢就是从哪开始定义接口我们要把这个
[03:34] 接口定义好然后呢就是前端搞前端的后端搞什么后端的并行开发最后呢我们再进行什么对测试这个步骤我们要给大家强调一下所以接下来的话我们就应该先定义注册当中第一步就是发送并获取短信银行码这个功能的什么呀接口先定义这个接口那接口定义到什么地方咱刚开始实现的话我们要反复的给大家强调一下我们整个P2P项目所有的接口
[04:06] 全部是定义在万信p2p-api这个工程当中咱当时介绍这个微服技术工程的时候给大家提过对不对全是在这里面那我们接下来准备新建一个名字叫alkacountapi的这个接口然后在这里边呢定义一个什么呀对发送并获取短信验证码的这个方法那咱接下来找到这个谁呀api这个工程然后呢你在这要建一个包
[04:39] 子包叫阿克康的为啥叫阿克康的呢你看这还是看这个图你看我们在实现这个功能的时候是不是他发请求是到哪同一账户嘛对不对所以说呢统一账户相关的这个所有的接口呢我们单独定义一个包放到这个阿康的这个包里边就行那你比如说将来用户中心这个服务里边的接口我们就单独建一个包叫什么consumer放到这个包里边就行便于管理那我们在这个子包下边呢新建一个什么呀接口
[05:10] 接口的名字呢我们要跟讲义保持一致就叫什么呀对account API就行我们首先是要定义接口这是接口就定义好定义好之后呢我们紧接着是不是要在这里边定义一个什么呀方法我们说了我们首先第一步是要干什么呀发送并获取短信验证码好我们看一下讲义在这个接口里边我们定义一个方法方案的名字叫get sms code界名之一是不是就得到什么呀
[05:43] 对短信验证码大家看一下我们重点要观察接口里边的什么呀我们要重点观察接口里边方法的什么呀一个是参数一个是对返回值一定要注意参数不用说了就是什么呀手机号因为你要获取短信验证码那我这个验证码我得知道是发给谁啊发给哪个手机嘛所以我得知道他的这个什么呀手机号其实说白了就是这个手机号就是你在这填的这个什么呀手机号我们需要知道
[06:13] 所以说他这需要传过来一个什么呀手机号然后呢返回值是什么呀rest response哎这个返回值的这个类rest response对于他来说非常非常重要呃咱们前面是不是提过这个编码规范是不是是不是让大家看这个文档了对不对咱这个文档里边其实给大家强调了一个事什么事大家一定要注意听啊就是我们整个p2p项目后端啊就是微服务端凡是
[06:43] 要往前端进行响应的话这个所有的数据所有内容全部封装成rest response这是整体统一的一个一个安排啊只要是后端给前端进行响应的所有的数据所有内容全部封装成rest response那他的你可以这个这个类你可以了解一下可以看看他里边都有什么东西然后你看一下rest response我们是放到哪来呀放到Coreman对吧Coreman这个工程里边啊你可以下去自己找一下
[07:15] 那这个类呢我们整体需要大家过一遍了啊你看这里边有几个属性三个属性分别是一个一个状态码对不对比方0是正常1就表示失败了一个就是提示信息比如说这个什么呀注册成功注册失败登录成功登录失败然后呢这呢就是具体的这个返回的一些数据啊一些数据我们是要放到这个入资奥特里面你看这是用范形吗这更灵活吗你反而自不算这就是自不算你反而一个对象这就是一个什么呀一个一个一个什么对象对不对
[07:43] 然后这里边呢还提供了一些更好用的一些什么呀静态方法可以快速的对这三个属性进行什么复制啊或者一些什么呀封装的啊等等等等这些代码你下去可以自己看包括getseller方法tools用方法等等等等那么最最重要的是大家要知道我们微服务这边往前端响应的时候呢一般就是封装三块内容就这三块啊封装成rest什么呀response前端呢会从这里边取这些数据他要查他自己取
[08:13] 咱不用管所以这个类大家需要了解一下了解完之后呢咱接下来呢就把这个接口呢快速的编写一下这个方法名呢我们啥的都要跟这个讲义保持一致这块呢比较简单我就沾过了这是我们定义了一个接口然后呢接口当中的这个方法我们也定义好定义好之后呢我们接下来一般习惯于做这样一件事前面咱跟大家强调过咱这个接口是哪一层的接口
[08:45] 是表现层还是要层还是数据房层咱这个接口是哪一层的接口这个地方大家一定要注意咱们整个P2P项目当中开发的时候我们说的首先我们要定义接口对吧这个接口是表现层的接口VR是表现层的接口我们前面其实也提过因为我们是前无端分离前端发请求大家想前端发请求都是到达什么层都是到达表现层是不是所以我们定义的这个接口都是表现层的接口
[09:15] 所以这个别人层的这个接口我们定义好之后我们顺手把control也给它实现了就control这个类我们给它实现了你可以来个空实现都是可以那这个实现类我们应该放到那那可不是在API这个工程当中应该去哪应该去对可看看这个Service里面来新建一个什么呀control的类然后实现这个方法可以来个空实现先放到那我们展开这些包找到
[09:47] 一个子包叫Controller那一看名字我们就知道这里边是不是要放这个Controller类的那我们在这呢就干什么呀新建一个名字叫accont然后呢后边的名字就是controllercontroller什么呀然后呢这个类写好之后呢我们首先一定要记住要让它实现这个谁呀对刚才我们定义的这个account API这个接口对就是这个接口
[10:21] 另外别忘了在这个上面是要加一些什么呀注解对吧首先我们想要注解就是rest什么呀rest control这个大家都很熟了那这为什么报错呀这报错不就是因为我们刚才在这个接口里边定义了方法这还没实现吗对不对我们让他把这个方法给他生成一下那这里边你可以来个空实现一下扔到这就行了将来我们等着要层包括其他代码群想完之后我们再
[10:51] 完善这个代码这是我们后边编码基本上都是这么一个套路另外这里边我们也希望大家注意大家看一下这个讲义就是说这里边你看Controller这一块我们是不是要加一些什么东西这都是什么东西这都是啥东西咱前面讲过了这都是什么东西对这是swag的注解这东西干嘛用的有了这些注解swag是不是帮我们生成那个什么文档对不对说非常重要刚开始的话我建议大家
[11:19] 你要自己手敲一下我这就不手敲但是我建议大家手敲一下啊你慢慢练的熟了之后以后你可以从我这里边去粘过来上这个注解是那个那个日志的那个注解是要放机我们把这些注解给他给补充完善一下然后呢你看这个类啊这不是这个类这个方案上面是不是也有一些这个sweat的这个注解啊包括这个谁啊这个反而路径的一个配置我们都不能把它给忘掉然后我们大概这个回顾一下吧
[11:51] 这一块这个adap是用来描述整个这个类它是干嘛的是不是然后呢这一块注解是用来描述这个方法是干嘛比如这个方式或许手机验证码的然后参数对吧表什么意思什么类型等等而这个注解大家应该比较熟是属于死产mvc的是不是配置它的一个访问路径了这个手机号是不是通过这传过来了对吧相当于这是什么呀通过路径这是我们把这个相关的一些注解给它补充完善一下
[12:21] 另外这个地方千万不要忘这个很容易忘的啊这个注解很容易忘从我们以后的这个基本的步骤都是这样需求分析搞定完之后就是先定义接口接口定义完之后呢我们在这呢顺手把这个control了先来个控制线先放到上这是咱们把什么呀对注册功能当中的第一步啊就是发送并获取短线验证码这个接口给他定义好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解P2P平台开户功能的前后端开发流程，包括需求分析、接口定义、代码实现（如AccountAPI接口、RestResponse工具类、AccountController控制器）以及集成测试工具（Swagger/Postman）的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示开户业务流程图，包含“测试端/App”、“用户中心/自助”、“开户API服务”三个模块，流程包括用户输入手机号、获取验证码、注册请求、用户登录、资金查询等步骤。
画面2：展示PPT内容，标题为“2 前后端开发步骤与编码规范”，内容包括需求分析、接口定义、服务端和前端依据接口并行开发。
画面3：IDEA中显示项目结构，当前选中“wanningzp-account-Service”模块下的“account”包。
画面4：在IDEA中弹出“Create New Class”对话框，选择“Class”类型。
画面5：在IDEA中编辑“AccountAPI.java”文件，内容为一个空的接口定义，注释说明开户功能需要开通两个账户，区分注册、登录、开户三块。
画面6：展示PPT内容，标题为“3 需求概述”，子标题“3.1 什么是开户”，内容说明服务端开发人员需通过Swagger或Postman进行功能测试。
画面7：在IDEA中编辑“RestResponse.java”文件，定义一个泛型响应类，包含code、msg、result三个字段，并提供success和fail静态方法。
画面8：在IDEA中继续编辑“RestResponse.java”，展示success方法的实现。
画面9：在IDEA中继续编辑“RestResponse.java”，展示toString方法的实现。
画面10：在IDEA中编辑“AccountAPI.java”文件，内容为空接口定义。
画面11：在IDEA中编辑“AccountController.java”文件，显示类继承自“AccountAPI”，并导入相关包。
画面12：在IDEA中编辑“AccountController.java”，定义一个getSMSCode方法，返回null。
画面13：展示PPT内容，标题为“4.6.2 用户中心-开户”，内容说明在wanningzp-account-Service工程中新建SmsService类，调用短信服务发送验证码。
画面14：在IDEA中编辑“AccountController.java”，为getSMSCode方法添加注解，包括@ApiOperation、@ApiImplicitParam、@RequestMapping等，用于定义接口文档。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5：
```java
package cn.ictast.wanningzp.api.account;

public interface AccountAPI {
    // 开户：开通账户(借款人和投资人)
    // 1. 我们需要开通两个账户
    // 2. 开户和注册的不同
    // 注册：只保存了用户的基本信息（例如：手机号），此时可以登录，可以浏览信息，但是不能交易
    // 要想交易，必须进行开户(提供身份证、银行卡等)
    // 分成三块：注册、登录、开户
    // 时序图
    // 用户模型：姓名、性别、手机号...
    // 账号信息：账号和密码...权限...
    // 注册：1.发送并获取短信验证码 2.校验手机号和短信验证码 3.保存账户信息
}
```

画面7：
```java
import org.springframework.web.bind.annotation.*;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonRawValue;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml.jackson.annotation.JsonClassDescription;
import com.fasterxml

