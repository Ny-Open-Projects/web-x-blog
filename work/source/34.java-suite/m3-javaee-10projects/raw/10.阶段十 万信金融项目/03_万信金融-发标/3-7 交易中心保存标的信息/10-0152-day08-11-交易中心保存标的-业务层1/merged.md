# day08-11-交易中心保存标的-业务层1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-7 交易中心保存标的信息
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-7 交易中心保存标的信息\day08-11-交易中心保存标的-业务层1_【海量资源尽在 666java.com】.mp4
- 时长 12分36秒（音频 756s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好我们把数据防护层的代码编写完之后呢接下来该哪一层了对接下来该右层了而且根据咱之前的经验右层的代码往往会比较多比较复杂一些那咱右层呢也是一个接口一个实现类是吧那咱接来先快速的把这个接口定义出来Service 包新建一个接口接口呢我们跟讲义保持一致这样过来这个接口比较简单啊这个代码我就不再重新敲了就是发标啊
[00:38] 给大家大家看一下这不是那个dto对象吗啊我们在这个方案里边进来实现功能的时候就保存他里边的信息最终呢我们还把这个dto也返回了啊因为我们还要在其他地方要用一下这是接口吧我们快速定义了一下接口定义完之后呢咱们顺手就把实现类啊也给他定义出来定义一个实现类名字呢我们也跟讲义保持一致project Service impr
[01:09] 那么这个实验类呢大家要注意啊我们首先是要加一些必要的注解啊这个不再说了另外呢呃由于我们是在用mybattic plus在进行资产概察所以说呢我们业务层的实验类要继承mp的一个什么样类同时实现我们刚才定义的结构这个大家都比较熟悉了稍等调整一下格式啊这个导包呢我们再导一下浪爆客的啊别导错了啊那这为啥报错呀
[01:57] 这包错很正常我们刚才接口里边定义一个方法还没有重写我们生成一下这是来了一个空时线是不是那咱们接下来是不是该动手来编写Credits Project这个方案里边代码当然我们最终的目标是要保存什么对标底信息就是这里边传过来的一些信息那无非就是增删改良当中的一个增就是一个保存这个代码按说应该挺简单的是吧但是你看讲义看讲义你就觉得它不简单
[02:28] 代码多吗非常非常多那只是一个保存功能为什么代码这么多呢哎这里边呢我们要提现给大家说一说一个原因啊第一个原因就是大家看这个类project的这个类啊这个类呢你一定要注意这个类呢其实就是对应啊我们哪个表呢对应我们这个project这个表它的一个实体类啊跟这儿是对应的就是我们的标的信息表这个类呢也是我们直接提问给大家
[02:58] 这里边你看各个属性跟哪个字段对应对吧这个类跟什么呀哪个表对应吗是不是你看这里边全部都有该有的都已经有呃原因第一个呢就是这个属性比较多啊我们保存吧基本上要给每个属性都要复制第二个呢就是这些属性里边有些值呢你还得从别的地方获取你比如说这个这里你看我们在保存标底信息的时候呢就要保存发标人的用户的一些标识
[03:32] 一些编码这些信息从哪来这些我告诉你他这个在这个地方他可是没有的在地球对象里面是没有那这些信息呢我们必须从什么地方从考虑往那边查一下查出来我们获取到然后在这用第三个就是我们发标的时候呢还要做一些业务处理一些业务判断说综合下来吧这个整个保存这个代码就比较复杂那咱就需要一点一点去写了
[04:02] 咱首先要做一些准备工作做一些准备工作哪些准备工作呢刚才大家看到了我们在保存这个标底信息的时候里边是不是涉及到我们需要获取什么发标人的一些信息比如说用户标识就这个ID比如说这个username等等等等而且我们刚才说了这些信息是不是在用户中心那边那我们就需要通过FIN远程访问consumer那边来得到这些信息这就是一个准备工作我们需要做一下
[04:34] 那具体怎么做呢我们就需要去consumer那边先把这个功能给实现consumer那边我们要实现什么功能我们要获取当前登录用户当前登录用户不就是这个发表人吗那肯定是谁登录这个就是谁谁就是发表人嘛对不对所以我们要实现的功能就是如何获取到当前登录用户得到这个用户呢那这些信息你想得到那就是很轻松的事那么怎么得到当前登录用户呢
[05:08] 那我们先定义一个方法这个要实现这个功能那我们还是跟之前一样啊需要去API当中找到接口定义一个方法再说这是我们以前consumer的这个API对不对这里原先有注册有开户那我们这需要新增一个方法什么方法呢就是获取当前登录用户的方法就这获取当前登录用户啊来我们加一个注释这就是获取获得
[05:47] 当前登录什么呀用户不需要参数为啥不需要参数咱一会实现功能的时候你就知道这个代码其实咱以前写过啊那反正这肯定就是consumer detail啊这里边就是封装好的当前登录用户的一些什么呀信息对呃这是我们在扛consumer API当中定义了一个接口定义完接口之后我们自然就要顺手在Controller当中去实现这个方法实现这个功能也这已经报错了
[06:23] 咱们接下来把这个方法呢给它实现一下先生成一下get convert consumer就是获取当前登录用户那具体怎么获取当前登录用户啊这个代码咱以前写过啊大家看一下讲义应该有印象啊看这行那了有印象吗securityutil.getuser这个其实就得到当前登录用户因为这个呢涉及到这个咱们之前讲过的注册登录时候那个那个什么技术
[06:59] 对strong security还有os2咱之前在一个地方应该是已经用过这个代码就咱封装好了一个工具类这个工具类就可以从另一排里是不是获取到当前登录用户就调这个方法会有当然登录用户得到登录用户之后它里边存的有手机号我们拿了手机号之后我们调右层右层调到第O层就可以根据手机号查到这个什么用户的一些信息了所以这个代码实行起来是非常简单
[07:35] 咱们站过来看一下这个security youtube这个类你还有印象吗咱进去看一下你看它里边封装好的一个静态方案给的user这边不知道大家有没有印象这个其实就是从请求里边取那个令牌的这就是做类型转换的返回了一个什么一个封装当前登录用户信息的一个login user这样一个对象这咱之前说过那大家看一下我们这是得到当前登录用户
[08:11] 然后得到他的什么手机号得到手机号之后对得到手机号之后我们就可以根据手机号是不是获取当前登录用户的一些信息了所以我们需要在右层是定义一个get bymobile这样一个方法这个方法咱以前是不是写过没有我们查一查写过没有get bymobile没有吗checkmobile是吧没有的话我们就需要把这个方法也定义一下叫get bymobile是不是传进来一个手机号就完事了然后返回来是一个consumer DTO
[08:44] 这个比较简单consumerconsumerdto这是反应值然后发明就叫什么getbymobile然后有一个参数就是mobile那么这个方法我们加一个注释吧这个方式干嘛了对就是通过手机号获取当前用户的什么
[09:21] 信息那这是右层的介绍右层介绍定义好之后呢咱就需要去实现类里边出实现类里边有没有这个方法之前我们得找一找叫什么名啊叫咱以前其实写过这个方法只不过当时呢是作为私有方法存在然后去用的那这简单了这改成public对吧上面加上这么一个注解这对以前的代码也没啥影响
[09:50] 也能满足我们当前的需求是不是咱以前其实已经写过这个方法给他办目标啊就扔进来一个手机号这个代码大家看起来应该很熟悉吧这不是那个全年购道器吗这呢是不是导到一个consumer对象然后再转化成DTO返回吗呃那这儿呢我们也不会报错了对不对那大家看一下这是我们把consumer那一块就用户中心那一块代码全部搞定了啊大家注意看一下我们是这样的我们在这个consumer这边加了一个方法就这么一个方法
[10:23] 就获取当前登录用户信息的我们获取呢有一个工具类就得到了根据手机号呢我们访问药厂就查出来一个DTO对象然后把这个DTO对象作为访问值返回了那么提醒大家注意这里边有个细节由于呢这个获取当前登录用户呢基本上都是让别的微服务去访问那根据咱以前的这个编码规定我们这种服务啊它的访问路径应该是什么开头的对L开头这个大家不知道还有没有印象
[10:51] 那用户中心这边功能实现完之后呢我们回到讲义里边我们的这个交易中心这边是不是需要创建一个什么非硬代理然后去访问咱刚才consumer那边的那个那个control是不是所以我们接下来需要在交易中心这边呢需要定义一个非硬代理那就需要去拿对transication这边在argent这个包里边我们需要新建一个接口
[11:20] 名字呢跟讲义保持一致吧叫consumer API urgent对吧然后呢我们就需要加一些注解就OK了这代码咱以前经常写啊就不再过多说了好大家看一下吧我们首先要加一个fineclient这个注解用来设置什么呀我们将来是要往这个微服务发请求的然后下边呢我们订阅了一个方法这个方法包括上面这个请求路径是不是其实直接就是跟这儿是保持什么呀可以保持一致的
[11:59] 比如说呢我们将来交易中心啊要通过这个非信代理往这儿对不对发请求发请求干嘛给发请求不就到这儿了吗到这之后就是获取当前登录用户的这个相关的信息就是得到这个DTO对象得到DTO对象之后呢将来我在这儿来保存这个标底的时候这个标底里边的这些值我们就有哪些值就我们刚才一开始提到的这个呃用户的
[12:26] 发表员的用户标识包括这个UterNumber等等这些值就有说这是我们做的一个什么准备工作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在交易系统中创建项目服务接口、实现类，并关联用户中心的消费者注册功能，涉及 MyBatis 映射文件、Service 层接口与实现、实体类及 Controller 层的 API 接口定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了在 MyBatis 的 Mapper 文件中定义了 ProjectMapper.xml 的结构。
- 代码内容：
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
  <Mapper namespace="cn.itcast.wanxingzp.transaction.Mapper.ProjectMapper">
  </Mapper>
  ```

画面 2：
- 展示了在 Service 包中新建的 ProjectService 接口，定义了 createProject 方法。
- 代码内容：
  ```java
  /**
   * 交易中心Service接口
   */
  public interface ProjectService {
      /**
       * 创建标的
       * @param project
       * @return ProjectDTO
       */
      ProjectDTO createProject(ProjectDTO project);
  }
  ```

画面 3：
- 展示了在 IDEA 中打开的 ProjectServiceImpl.java 文件，准备编写实现类。
- 项目结构显示了 Service 包下的 ProjectService 接口和 ProjectServiceImpl 类。

画面 4：
- 展示了在 ProjectDTO 类中设置用户 ID、生成项目编号、设置状态等业务逻辑。
- 代码内容：
  ```java
  projectDTO.setUserId(consumer.getResultSet().getUserId());
  projectDTO.setProjectNo(CodeUtil.getNo(CodePrefixCode.CODE_PROJECT_PREFIX));
  projectDTO.setProjectStatus(ProjectCode.COLLECTING.getCode());
  projectDTO.setStatus(StatusCode.STATUS_OUT.getCode());
  projectDTO.setCreateDate(LocalDateTime.now());
  projectDTO.setRepaymentWay(RepaymentWay.FIXED_REPAYMENT.getCode());
  ```

画面 5：
- 展示了 Project 实体类中定义了 ID、CONSUMER_ID、USER_NO、PROJECT_NO 等字段。
- 代码内容：
  ```java
  @TableId("ID")
  private Long id;
  @TableField("CONSUMER_ID")
  private Long consumerId;
  @TableField("USER_NO")
  private String userNo;
  @TableField("PROJECT_NO")
  private String projectNo;
  ```

画面 6：
- 展示了 Project 实体类中定义了 USER_NO 字段的注解和类型。

画面 7：
- 展示了 ConsumerAPI 接口，定义了注册和创建消费者的方法。
- 代码内容：
  ```java
  public interface ConsumerAPI {
      /**
       * 用户注册，操作用户信息
       * @param consumerRegisterDTO
       * @return
       */
      RestResponse register(ConsumerRegisterDTO consumerRegisterDTO);
      /**
       * 生成开户请求数据
       * @param consumerRequest 开户信息
       * @return
       */
      RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
  }
  ```

画面 8：
- 展示了 ConsumerController 类，定义了 hello 和 hi 两个测试接口。
- 代码内容：
  ```java
  @RestController("用户服务的Controller", tags = "Consumer", description = "用户服务API")
  public class ConsumerController implements ConsumerAPI {
      @Autowired
      private ConsumerService consumerService;
      @ApiOperation("测试Hello")
      @RequestMapping(path = "/hello")
      public String hello() { return "hello"; }
      @ApiOperation("测试Hi")
      @ApiImplicitParam(name = "name", value = "姓名", required = true, dataType = "String")
      public String hi(String name) { return "hi,"+name; }
  }
  ```

画面 9：
- 展示了 SecurityUtil 类，用于获取当前登录用户。
- 代码内容：
  ```java
  public static LoginUser getUser() {
      ServletRequestAttributes servletRequestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
      if (servletRequestAttributes != null) {
          HttpServletRequest request = servletRequestAttributes.getRequest();
          Object jwt = request.getAttribute("jsonToken");
          if (jwt instanceof LoginUser) {
              return (LoginUser) jwt;
          }
      }
      return new LoginUser();
  }
  ```

画面 10：
- 展示了 ConsumerService 类中定义了 register 和 createConsumer 方法。
- 代码内容：
  ```java
  void register(ConsumerRegisterDTO consumerRegisterDTO);
  RestResponse<GatewayRequest> createConsumer(ConsumerRequest consumerRequest);
  ```

画面 11：
- 展示了 ConsumerController 类中定义了获取当前消费者信息的接口。
- 代码内容：
  ```java
  @ApiOperation("获取登录用户信息")
  @RequestMapping("/currConsumer")
  public RestResponse<ConsumerDTO> getCurrConsumer() {
      ConsumerDTO consumerDTO = consumerService.getCurrConsumer(SecurityUtil.getUser().getMobile());
      return RestResponse.success(consumerDTO);
  }
  ```

画面 12：
- 展示了 ConsumerController 类中定义了测试接口。
- 代码内容：
  ```java
  @ApiOperation("过网关保护资源，进行认证测试")
  @ApiImplicitParams({
      @ApiImplicitParam(name = "jsonToken", value = "访问令牌", required = true, dataType = "String")
  })
  @RequestMapping(value = "/m/consumers/test")
  public RestResponse<String> testResources(String jsonToken) {
  }
  ```

画面 13：
- 展示了 ConsumerApiAgent 类，用于代理 ConsumerController 的接口。
- 代码内容：
  ```java
  @ApiOperation("生成开户请求数据")
  @PostMapping("/consumers")
  public RestResponse<GatewayRequest> createConsumer(@RequestBody ConsumerRequest consumerRequest) {
      return consumerService.createConsumer(consumerRequest);
  }
  ```

画面 14：
- 展示了 Project 实体类中定义了 USER_NO 字段的注解和类型。

