# 14.商户注册-商户平台应用注册商户接口-接口定义

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\14.商户注册-商户平台应用注册商户接口-接口定义【海量资源尽在 666java.com】.mp4
- 时长 8分29秒（音频 510s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们开始进行商户平台应用注册商户的接口刚才我们进行的是商户服务的注册商户接口就是对外暴露double服务的这个接口它呢是给商户平台应用去调用的所以这里边我们要写的是对外暴露http接口的商户平台应用然后呢它最终会调用刚才我们写的这个double服务的接口好那现在呢我们的这个工作的
[00:29] 地方应该转到我们的商户平台应用了这个呢大家可能刚开始去写这种微服务架构的代码了可能不太熟悉啊感觉一会切到这个工程一会切到那个工程乱乱的但是呢我还是说的你不要离开这个交互流程图刚才我们做的事是不是就是在这接口二部分写完了那你要完成整个注册的话接口三他要做的事是不是就开始去最终调用接口二啊所以你现在要写接口三
[00:59] 对吧好那接口三它要做的事是啥呢是不是第一它要校验手机验证网向验证网服务发送请求校验第二要调用三户平台服务要保存三户的信息对吧好那现在我们来先定义接口三户平台应用三户平台应用注册三户的接口定义刚才我们说了嘛一个是校验手机号手机的验证码是吧一个是
[01:28] 请求商户服务进行商户注册好了那现在呢我们来定义吧这是我们商户注册的一个标单这里边是不是有四项数据啊最终这四项数据是不是会提交到哪里啊Controller当中也就是在Controller当中我们会定义一个什么啊哎叫商户注册好这就叫商户注册对吧哎那么这时候我们要接收
[01:58] 数据我们用什么类型的数来接收呢试考一下当初我们在Service当中我们是定义了DTO那现在呢你现在要转到应用的这个工程就是对外暴露HTTP给前端的这个接口你要怎么来接收这个数据注意要给前端来提供接口我们是前后端分离开发你要注意你的参数是什么
[02:31] 你要定义什么样的类型来接受你最好不要比这个什么请求的数据还多也就是说现在你要接受这个数据的话我们就可以定义一个VO的一个对象类型这个VO呢顾名思义就是给四图层所用到的一个什么类型你也知道注册的时候是不是要提交手机号账号密码还有验证码以及验证码的key对吧因为你要校验验证码是不是这两个都少不了啊
[03:00] 所以前端会请求这五项数据所以我们要在我们的商户平台应用的这个工程中再建一个包叫VO然后在这个里头我们就定义我们的VU定义VO它是根据我们的需求来定义的前端提交什么数据你就定义什么数据来接收大家理解吧这个过程我就不再去一个一个的敲了
[03:29] 就复制讲义到这课下呢你拿到我的代码呢你也可以从我给你发的讲义当中去复制你也可以直接从我给你发的原代码当中去把这个类考到你那好那这个VO大家知道吧它是干嘛呀对用于接收前端提交的数据所以各位有人说老师我能不能这个application在我用DTO来接受那我就不建议了
[04:00] 因为这个DTO你也看到它的字段好多对吧而这个接口呢只是针对前端的这个表单提要所以我们就建议你单独定义一个view好那现在呢我们就可以来写我们的这个接口了那这个是三户平台应用它提供的一个三户注册的接口所以这里边呢我们就可以来写一下啊先写个方法最终它响应回去的还是你注册成功的这个数据
[04:29] 对吧那么你可以把它请求的这个数据呢再给它返回去然后呢现在呢我们要让它请求的数据用VO来接收大家看懂了吗好这就是这个接口的方法当然作为http写的接口你肯定要指定http是get还是post包括它的URL所以这就是它的URL以及post这么一个定义对吧
[04:58] 好另外还有作为Swagger接口呢我们需要定义这个参数的说明是吧那这个Swagger接口我们怎么定义啊有一个叫APIImplicit Param是不是这个然后里边的定义比如这个叫什么商户注册的信息前边呢我会带着大家手动来敲这些注解的内容后边我可能就复制了所以你刚开始啊你必须要知道它是啥意思啊
[05:27] 这个内幕呢表示参数的名称我们把这个参数的形态名称放进去就行好然后呢这个是否必填呀当然是啊所以就是true然后呢它的数据类型呢数据类型的话其实就是这个对象的类型名好然后还有就是它param time就是这个参数将来怎么传呢那这个是post的提交通常我们就是通过body也就是通过json数据来传对吧
[05:57] 如果通过监测数据传到华字里边呢那你是不是就可以是写成啥呀request body对吧这是不是我们之前学习过这个spring mvc啊我们这个应该就比较熟悉了对吧好这个呢我们就写好了这个接口的什么定义好那这样我先返回一个空啊好那现在呢我们看好啊我们把它给重启一下啊有时候老是重启干嘛又不能运行是不是
[06:25] 重启的目的呢我是运行起来这个什么SWIG让你看看你看报错了看到吗那报啥错呀说这个注解不存在你看看在这报了这个错然后呢我们再来再来运行一下有时候它这个IDL呢加载数据呢可能没有加载上去啊好那运行起来之后呢我们现在是不是就要打开它的SWIG了对吧
[07:08] 这就是三户平台应用的接口来看一下吧现在我刚才写的是不是就是这个三户注册呀你看这个接口是post的对不对然后呢请求的数据是不是他当然你看我刚才是不是就是这个接口的名字是他呀然后呢你看这个model这个接口的参数里边是不是就写的很清楚呀手机号呀你前段要给我传这些东西好那你说老师我想测试一下咋测虽然我们代码没有写其实你也可以
[07:38] 跑一下嘛你看这就是请求的数据对不对你比如说这个手机号随便写对吧密码123行不行随随便写点啊然后呢看好我打一段点好然后呢现在呢我们就可以怎么弄啊点击执行然后现在看数据是不是就进来了进来之后你先看它数据能不能提交进来啊OK吧看数据是不是就提交进来了对好这就是我们的三户平台应用
[08:10] 给前端提供的一个三户注册的http接口将来在这个里面各位需要调用谁是不是调用double服务的接口了对不对好这就是三户平台应用注册三户的接口定义就写完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现商户平台应用注册商户接口的开发，包括接口定义、参数校验、服务层实现及前端调用测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档目录，当前定位在“2.4.2 商户服务注册商户(接口②)”章节，说明将实现商户注册接口。
画面2：IDE中展示项目结构，鼠标选中“MerchantController”类，准备编写控制器代码。
画面3：IDE中展示项目结构，鼠标选中“MerchantController”类，准备编写控制器代码。
画面4：展示课程文档目录，当前定位在“2.4.3.1 接口定义”章节，下方显示商户注册VO类的代码片段。
画面5：IDE中展示“MerchantController”类代码，包含获取手机验证码和测试接口。
画面6：展示“MerchantRegisterVO”类的代码，定义了商户注册所需字段。
画面7：IDE中展示“MerchantController”类代码，鼠标光标在“@PostMapping”注解上。
画面8：IDE中展示“MerchantController”类代码，鼠标光标在“@PostMapping”注解上。
画面9：IDE中展示“MerchantController”类代码，鼠标光标在“@PostMapping”注解上。
画面10：IDE中展示“MerchantController”类代码，鼠标光标在“@PostMapping”注解上。
画面11：IDE中展示“StoreDTO”类代码，出现编译错误，提示“@Data”注解与“@ApiModel”注解冲突。
画面12：IDE中展示“MerchantApplicationBootstrap”类代码，配置RestTemplate并设置字符编码。
画面13：展示Swagger UI界面，显示POST请求“/merchants/register”的参数定义。
画面14：展示课程文档目录，当前定位在“1.1 商户注册”章节，介绍商户注册的业务需求。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
2.4.3 商户平台应用注册商户(接口③)
商户平台应用调用用户服务提供的商户注册接口即可完成商户注册业务，本书实现商户平台应用注册商户接口的开发。
2.4.3.1 接口定义
1、接口描述如下：
1) 接收商户填写的注册数据
2) 商户平台校验于机器验证码
3) 请求商户服务进行注册
4) 返回注册结果给前端

画面2：
//Return 近用到的商户信息
@Override
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    Merchant merchant = new Merchant();
    merchant.setMobile(merchantDTO.getMobile());
    //写入其它属性
    //审核从默认为0进行后续申请
    merchant.setAuditStatus("0");
    //调用app用户数据表写入记录
    merchantMapper.insert(merchant);
    merchantDTO.setId(merchant.getId());
    return merchantDTO;
}

画面4：
package com.shanju.pay.merchant.vo;
import io.Swagger.annotations.ApiModelProperty;
import io.Swagger.annotations.ApiModelProperty;
import lombok.Data;
import java.io.Serializable;

@ApiModel(value = "MerchantRegisterVO", description = "商户注册信息")
@Data
public class MerchantRegisterVO implements Serializable{

    @ApiModelProperty("商户手机号")
    private String mobile;
    @ApiModelProperty("商户用户名")
    private String username;
    @ApiModelProperty("商户密码")
    private String password;
    @ApiModelProperty("验证码的key")
    private String verifyKey;
    @ApiModelProperty("验证码")
    private String verifyCode;

}

画面5：
@GetMapping("/sms")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机验证码")
@ApiOperation("获取手机

