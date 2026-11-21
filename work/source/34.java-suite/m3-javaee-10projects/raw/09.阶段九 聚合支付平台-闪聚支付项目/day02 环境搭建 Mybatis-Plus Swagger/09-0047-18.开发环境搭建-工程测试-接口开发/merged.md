# 18.开发环境搭建-工程测试-接口开发

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\18.开发环境搭建-工程测试-接口开发【海量资源尽在 666java.com】.mp4
- 时长 14分2秒（音频 842s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们继续来进行工程测试那接下来我们就可以直接来写根据ID查询商户的接口来测试一下整个的这个调用的流程有应用层调到服务层服务层呢再连接数据库来查商户信息好那首先来我们首先写接口那这个接口要在哪里写呢因为我们有很多工程慢慢慢慢随着这个业务的开展呢你会发现这里面会建很多的工程
[00:29] 你要记着啊这个我们要写这个接口啊其实我们项目当中也有很多接口你比如像这个application对前端是不是也提供接口然后呢这个微服务像应用是不是也提供接口所以这里边你先要搞清楚我们要写什么接口你要知道我们最终的目的是不是根据ID查商户啊按照我们的开发流程我们准备先怎么弄啊是先写double服务再写
[00:58] 应用层的这个接口所以我们要写的就是这个微服务就是double服务这个工程double服务这个工程呢就是要根据ID查商户那你就在API这个工程当中我们来写接口查商户信息嘛查商户呢根据ID各位来我们写一下啊它的包然后呢在这里边呢你是不是要建一个interface呀interface
[01:27] 那你现在要根据ID查商户各位这个方法名我觉得就比较简单吧根据ID查询商户那各位是不是就是返回什么东西先不要管啊你query是吧查询商户merchant然后呢buy ID各位是不是就搞定了那这个商户的表是哪个表呢是这个表对吧你看他的ID
[01:56] 它的ID是不是一个bigint其实这个商户信息它对应的模型类你要找到因为有些类型的东西你必须得知道你看你找到商户你看你看它的ID是不是一个lang型对不对所以你在这定义接口的时候你要知道就是传进来的应该就是个lang对不对那它返回呢有人说返回那么简单吗返回你就返回它的什么
[02:25] 商户的这个模型类型就玩事了吗你看就是这个marchin是吧这里边我要说一下就是我们Service层Service层我们统一用DTO类型作为Service层的传输对象因为Service要调Mapper对吧Mapper用的是什么用的是这个模型类就是entity我们把它叫做entity而现在在Service层我们准备怎么做我们单独要定义一个DTO的
[02:55] 这么一个包里边放这些类型那有时候老师为啥呢那一会我跟你说一下啊很关键的因为各位你想呀现在呢我们要做的是Service层对吧你想呀Service层所暴露的参数所返回的对象Service给谁返对象是不是给Controller是不是给我们说的这个什么应用层Controller这块返那你返的话
[03:22] 你如果说Service也用这个entity很有可能entity的属性它不够Service要去扩制里头的属性那不行啊entity它是严格和数据库表一一对应的就是它里边的属性是和数据库表的属性一一对应所以我们Service成自己的对象我们单独来建你懂我意思吧好那现在呢我们创建一个merchant DAO
[03:49] 那么有时候老师那这个对象这个类型咋建了你会发现这里头你还是这些什么你看企业名称企业编号这些东西你注意其实我们知道这些东西你手工创建也行你说我用这个什么我在entity的基础之上去改造行不行可以但是总而言之你这个DTO和entity是不同的类型这就相当于Service和持久层是分离了
[04:19] 大家要注意这个好这些注解一会儿我会给大家单讲这就是SWAG的一些注解就是我们会讲一个接口的一个文档技术先不要管它其实这些除了这个注解你其他应该都认识这是Lombok的对吧这是它的每一个的它的属性对应商户信息但是你要记着为什么我们把DTO我们单独建了一个DTO的类型不用entity就是我刚才说的
[04:49] 你Service如果用nt的类型那里头的属性可能不够那如果你去扩那就违反了什么违反了我们说的这个模型和数据库的表字段一一对应的这么一个原则所以这里面我们单独定义一个dto好那这样的话我们就知道了在Service这儿呢它要返回这个dto这个接口我就写好了对吧这是我们的接口定义啊接口定义这一块呢我们是不是提出了一个东西叫dto的类型对不对
[05:19] 好接口弄完了之后我们接下来要做什么呀是不是就是接口实现呀接口实现要在哪写接口实现又在还是在我们double服务这个工程里边的这个什么接口实现工程当中来写啊然后这里面呢我们当中也是要建一个包叫Service对吧然后呢那你实现刚才那个接口嘛一般来说我们在接口的后边来写一个什么呀叫impl这个结尾对吧好让他去实现谁
[05:49] 但注意这里边我要说一下因为你要你这个是接口实现嘛你接口实现你要实现哪个接口你是不是先得把它给导进去对不对所以你把它导进去了之后在这儿那你就可以直接实现刚才我们导进去的这个什么接口了看见了吗
[06:14] 好现在呢我们就进到这个double服务实现类的里头开发了哎还回忆一下当初我们讲double服务架构怎么说的呀这里边我们要加什么注解呀哎这是double自己的Service注解必须有这个注解啊然后呢它才能暴露成double服务接口对吧然后呢它要调用谁呀是不是就是Mapper啊哎调用Mapper的话Mapper我们在上一步是不是已经生成了了就是这个叫marchint
[06:43] 麦普是吧所以各位这里边呢我们就直接可以引用它对吧那么我们把它引进来了之后这儿各位很简单了因为我们原来学过买Betis的嘛它不就OK了不对你看还有问题啊你没发现吗它报错了报啥错你看
[07:08] 原来Mapper返回的是Entity类型你Service用的是DAO类型就是DTO类型那你怎么弄怎么弄创建一个DTO的对象然后呢怎么弄你拷贝也就是说你设置从哪里从这个对象当中去拿东西然后设到DTO里头就这么弄然后继续你要设置谁你要设置谁
[07:41] 比如说内蒙吧你就拿内蒙有时候老师这好麻烦呀对吧这有那么多属性我需要一个一个的去设对后期我们就会讲一个工具来解决这个问题那现在呢我们只是工程简单的测试阶段先测流程看能不能跑通啊所以这个呢我们暂时先放着啊回头我们解决这个你看到这接口实现这个是不是就搞定了接口实现我写完了之后你告诉我接下来弄啥
[08:10] 是不是就是应用层了应用层又跑到哪了你要知道应用层它是要做什么事啊各位应用层做啥事啊应用层啊是给客户端报REST附接口就是我们的前端要请求应用层来查商户信息对不对而应用层呢它呢是要调用微服务就是我们的double服务来查商户信息所以我们现在的
[08:39] 战略阵地又转到了什么application这个工程了就是这个Service我已经搞定了然后呢我又要转到application那转到application的话那你要知道那其实你要暴露http rest food这个接口其实就是写一堆的Controller是不是就完事了但是你要用哪个接口要调哪个double接口那你就需要在你的依赖上你得把它依赖进去
[09:08] 对吧然后依赖进去之后在这儿你是不是就直接可以调用了那就简单了好我们来写一个control好control不好漏的是什么呀rest control对不对好没问题吧然后呢那你你要调double服务吗你是不是得reference对吧reference是不是就是我们说的要用double的这个注解我们当初讲过double的这个知识他做的事是啥事
[09:39] 是不是就是把我们的接口生成什么对代理对象然后你就可以用代理对象去进行远程调用大家理解了好那这我们就把这个什么我们把这个接口写一下吧那返回怎么呀返回怎么还叉叉叉我们先不管然后我们继续往后走反正我知道他是在这要调对不对调谁呀
[10:09] 调这个接口嘛调用double服务嘛你看他要需要一个ID那你说这里边你不得给他传一个ID吗我说对吧传一个ID传一个ID的话那你这里头这个路径呢路径那你说我要查商户吗查商户你得给我一个ID啊是吧通过这个URL路径来传ID这个当初大家学过吧Spring MVC的时候是吧那这里头其实就是啥啊
[10:39] 你把ID的这个什么变量名然后呢我是不是就拿到了lang类型给我是吧然后呢你把ID传给我各位到这儿我们是不是就拿到了这个DTO拿到DTO各位那我就直接返回不就完事了返回那是不是就是我们的这个接口就是我们定义的根据IDquery merchant这个by ID的这个方法的返回之类型也确定了这是不是就搞定对不对
[11:10] 这就是我们的应用层的开发呀就这么简单好那就做完了那现在做完了我们要接下来怎么弄啊我们是不是就可以进行测试了好那测试的话我们就需要怎么弄呀把它重启一下然后呢再把我们这个服务层一个是double服务一个是应用我们是不是都要重启一下重启一下之后呢我们就可以来测试
[11:37] 但测试的话各位你是不是这个数据库你要查询这个数据库这里头是不是还没有东西啊没错吧那没有东西的话我们先随便添一个吧叫测试商户先随便添一个保存看一下它能不能测试出来啊查询出来主要是测流程啊主要测流程好这个再起一下好那下边呢注意我们要保证整个这个都启动成功啊对启动成功了之后呢我们就要在这儿嘛
[12:10] 看他这个服务列表当中是都有的没问题的那下面我们是不是就可以来请求应用层对吧请求应用层你看他的接口是啥端口57010嘛来57010merchant然后1对不对哎报错了看见了吗这是咋回事啊嗯那其实我们就要
[12:44] 看看了那请求路径这报个404页面找不到显然应该是我们的路径请求错了路径请求错了是什么呀你看我们要怎么找呀它的主配置文件当初我们是怎么配的呀你见到Necros主配置文件在这个哪个呀application你看主配置文件你看原来它扫了一个什么对扫了一个路径在这对吧这样各位
[13:15] 是不是就拿到了这是不是就是我们整个的调用流程由application然后调用到我们的double服务double服务查询数据库给application应用返回返回一个什么json数据各位到这儿我们就完成了整个功能测试其实这个流程跟当初我们讲double服务架构的测试的时候其实流程是一样的只不过现在我们是基于什么
[13:41] 我们是基于闪居配项目的整个工程来测试这样的意义就在于我们只要把这个流程拖通了我们是不是就可以在这个各个微服务里面去填充编写我们的Service我们的control好到这儿我们完成了工程测试

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
通过一个“根据id查询商户”的案例，演示基于Spring Cloud Alibaba的微服务项目从生成代码、配置数据库、创建接口到最终在Nacos注册并测试的完整开发流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 课程大纲显示当前章节为“1.7 工程测试”，子章节“1.7.1 生成代码”。
- 画面内容为文字说明：“使用mp的自动生成工具生成entity、Mapper等文件。”
- 代码片段1：// 商户服务
  dataSourceConfig
  .setUrl("jdbc:mysql://127.0.0.1:3306/shanjupay_merchant_service?serverTimezone=Asia/Shanghai");

画面2：
- 展示了IDE中“merchant-api”模块的目录结构。
- 代码片段2：// 根据ID查询商户
  public interface MerchantService {
  }

画面3：
- 展示了IDE中“merchant-Service”模块的目录结构。
- 代码片段3：// 商户实体类
  public class Merchant implements Serializable {
  private static final long serialVersionUID = 1L;
  // 主键
  @TableId(value = "ID", type = IdType.ID_WORKER)
  private Long id;
  // 商户名称
  @TableField("MERCHANT_NAME")
  private String merchantName;
  }

画面4：
- 展示了IDE中“merchant-api”模块的目录结构。
- 弹出窗口“Create New Class”，Name输入框为空，Kind选择“Class”。
- 代码片段4：// 企业编号
  @TableField("MERCHANT_NO")
  private Long merchantNo;
  // 企业地址
  @TableField("MERCHANT_ADDRESS")
  private String merchantAddress;
  // 行业类型
  @TableField("MERCHANT_TYPE")
  private String merchantType;

画面5：
- 展示了IDE中“merchant-api”模块的目录结构。
- 代码片段5：// 商户DTO
  public class MerchantDTO implements Serializable {
  @ApiModelProperty(value = "商户ID")
  private Long id;
  @ApiModelProperty(value = "企业名称")
  private String merchantName;
  @ApiModelProperty(value = "企业编号")
  private Long merchantNo;
  @ApiModelProperty(value = "企业地址")
  private String merchantAddress;
  @ApiModelProperty(value = "行业类型")
  private String merchantType;
  }

画面6：
- 展示了IDE中“merchant-api”模块的目录结构。
- 代码片段6：// 根据ID查询商户
  public interface MerchantService {
  // 根据ID查询商户
  public MerchantDTO queryMerchantById(Long id);
  }

画面7：
- 展示了IDE中“merchant-Service”模块的目录结构。
- 代码片段7：// 服务层接口
  @Service
  @ApiService
  public interface MerchantService {
  // 根据ID查询商户
  public MerchantDTO queryMerchantById(Long id);
  }

画面8：
- 展示了IDE中“merchant-Service”模块的目录结构。
- 代码片段8：// 服务层实现
  @Autowired
  MerchantMapper merchantMapper;
  @Override
  public MerchantDTO queryMerchantById(Long id) {
  Merchant merchant = merchantMapper.selectById(id);
  MerchantDTO merchantDTO = new MerchantDTO();
  merchantDTO.setId(merchant.getId());
  merchantDTO.setMerchantName(merchant.getMerchantName());
  merchantDTO.setMerchantNo(merchant.getMerchantNo());
  merchantDTO.setMerchantAddress(merchant.getMerchantAddress());
  merchantDTO.setMerchantType(merchant.getMerchantType());
  return merchantDTO;
  }

画面9：
- 展示了IDE中“merchant-Service”模块的目录结构。
- 代码片段9：// 服务层实现
  @Autowired
  MerchantMapper merchantMapper;
  @Override
  public MerchantDTO queryMerchantById(Long id) {
  Merchant merchant = merchantMapper.selectById(id);
  MerchantDTO merchantDTO = new MerchantDTO();
  merchantDTO.setId(merchant.getId());
  merchantDTO.setMerchantName(merchant.getMerchantName());
  merchantDTO.setMerchantNo(merchant.getMerchantNo());
  merchantDTO.setMerchantAddress(merchant.getMerchantAddress());
  merchantDTO.setMerchantType(merchant.getMerchantType());
  return merchantDTO;
  }

画面10：
- 展示了IDE中“merchant-application”模块的目录结构。
- 代码片段10：// 控制器
  @RestController
  public class MerchantController {
  @Autowired
  MerchantService merchantService;
  @GetMapping("/merchants/{id}")
  public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
  MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
  return merchantDTO;
  }

画面11：
- 展示了IDE中“merchant-application”模块的目录结构。
- 代码片段11：// 控制器
  @RestController
  public class MerchantController {
  @Autowired
  MerchantService merchantService;
  @GetMapping("/merchants/{id}")
  public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
  MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
  return merchantDTO;
  }

画面12：
- 展示了Nacos服务管理页面，服务列表中显示“merchant-Service”和“merchant-application”两个服务。
- 服务分组均为“DEFAULT_GROUP”，实例数均为1。

画面13：
- 展示了Nacos配置管理页面，配置列表中显示多个配置文件，包括“spring-boot.yml”、“merchant-application.yml”等。
- 配置文件所属Group为“COMMON_GROUP”或“SHANJUPAY_GROUP”。

画面14：
- 课程大纲显示当前章节为“1.7 工程测试”，子章节“1.7.1 生成代码”。
- 画面内容为文字说明：“使用mp的自动生成工具生成entity、Mapper等文件。”
- 代码片段1：// 商户服务
  dataSourceConfig
  .setUrl("jdbc:mysql://127.0.0.1:3306/shanjupay_merchant_service?serverTimezone=Asia/Shanghai");

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
// 商户服务
dataSourceConfig
.setUrl("jdbc:mysql://127.0.0.1:3306/shanjupay_merchant_service?serverTimezone=Asia/Shanghai");

画面3：
// 商户实体类
public class Merchant implements Serializable {
private static final long serialVersionUID = 1L;
// 主键
@TableId(value = "ID", type = IdType.ID_WORKER)
private Long id;
// 商户名称
@TableField("MERCHANT_NAME")
private String merchantName;
}

画面4：
// 企业编号
@TableField("MERCHANT_NO")
private Long merchantNo;
// 企业地址
@TableField("MERCHANT_ADDRESS")
private String merchantAddress;
// 行业类型
@TableField("MERCHANT_TYPE")
private String merchantType;

画面5：
// 商户DTO
public class MerchantDTO implements Serializable {
@ApiModelProperty(value = "商户ID")
private Long id;
@ApiModelProperty(value = "企业名称")
private String merchantName;
@ApiModelProperty(value = "企业编号")
private Long merchantNo;
@ApiModelProperty(value = "企业地址")
private String merchantAddress;
@ApiModelProperty(value = "行业类型")
private String merchantType;
}

画面6：
// 根据ID查询商户
public interface MerchantService {
// 根据ID查询商户
public MerchantDTO queryMerchantById(Long id);
}

画面7：
// 服务层接口
@Service
@ApiService
public interface MerchantService {
// 根据ID查询商户
public MerchantDTO queryMerchantById(Long id);
}

画面8：
// 服务层实现
@Autowired
MerchantMapper merchantMapper;
@Override
public MerchantDTO queryMerchantById(Long id) {
Merchant merchant = merchantMapper.selectById(id);
MerchantDTO merchantDTO = new MerchantDTO();
merchantDTO.setId(merchant.getId());
merchantDTO.setMerchantName(merchant.getMerchantName());
merchantDTO.setMerchantNo(merchant.getMerchantNo());
merchantDTO.setMerchantAddress(merchant.getMerchantAddress());
merchantDTO.setMerchantType(merchant.getMerchantType());
return merchantDTO;
}

画面9：
// 服务层实现
@Autowired
MerchantMapper merchantMapper;
@Override
public MerchantDTO queryMerchantById(Long id) {
Merchant merchant = merchantMapper.selectById(id);
MerchantDTO merchantDTO = new MerchantDTO();
merchantDTO.setId(merchant.getId());
merchantDTO.setMerchantName(merchant.getMerchantName());
merchantDTO.setMerchantNo(merchant.getMerchantNo());
merchantDTO.setMerchantAddress(merchant.getMerchantAddress());
merchantDTO.setMerchantType(merchant.getMerchantType());
return merchantDTO;
}

画面10：
// 控制器
@RestController
public class MerchantController {
@Autowired
MerchantService merchantService;
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
return merchantDTO;
}

画面11：
// 控制器
@RestController
public class MerchantController {
@Autowired
MerchantService merchantService;
@GetMapping("/merchants/{id}")
public MerchantDTO queryMerchantById(@PathVariable("id") Long id) {
MerchantDTO merchantDTO = merchantService.queryMerchantById(id);
return merchantDTO;
}

画面

