# 画面线理解：18.开发环境搭建-工程测试-接口开发

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day02 环境搭建 Mybatis-Plus Swagger
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\18.开发环境搭建-工程测试-接口开发【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:40, 02:50, 03:49, 04:29, 05:29, 06:23, 07:38, 08:46, 09:42, 11:19, 12:10, 12:59, 13:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 01:46:20

1) 这一组画面整体在讲什么（一句话）：
通过一个“根据id查询商户”的案例，演示基于Spring Cloud Alibaba的微服务项目从生成代码、配置数据库、创建接口到最终在Nacos注册并测试的完整开发流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 课程大纲显示当前章节为“1.7 工程测试”，子章节“1.7.1 生成代码”。
- 画面内容为文字说明：“使用mp的自动生成工具生成entity、mapper等文件。”
- 代码片段1：// 商户服务
  dataSourceConfig
  .setUrl("jdbc:mysql://127.0.0.1:3306/shanjupay_merchant_service?serverTimezone=Asia/Shanghai");

画面2：
- 展示了IDE中“merchant-api”模块的目录结构。
- 代码片段2：// 根据ID查询商户
  public interface MerchantService {
  }

画面3：
- 展示了IDE中“merchant-service”模块的目录结构。
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
- 展示了IDE中“merchant-service”模块的目录结构。
- 代码片段7：// 服务层接口
  @Service
  @ApiService
  public interface MerchantService {
  // 根据ID查询商户
  public MerchantDTO queryMerchantById(Long id);
  }

画面8：
- 展示了IDE中“merchant-service”模块的目录结构。
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
- 展示了IDE中“merchant-service”模块的目录结构。
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
- 展示了Nacos服务管理页面，服务列表中显示“merchant-service”和“merchant-application”两个服务。
- 服务分组均为“DEFAULT_GROUP”，实例数均为1。

画面13：
- 展示了Nacos配置管理页面，配置列表中显示多个配置文件，包括“spring-boot.yml”、“merchant-application.yml”等。
- 配置文件所属Group为“COMMON_GROUP”或“SHANJUPAY_GROUP”。

画面14：
- 课程大纲显示当前章节为“1.7 工程测试”，子章节“1.7.1 生成代码”。
- 画面内容为文字说明：“使用mp的自动生成工具生成entity、mapper等文件。”
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
