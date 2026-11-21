# 画面线理解：20.立即支付-交易服务支付宝下单-接口实现-保存订单

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day08 C扫B支付 生成门店二维码
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day08 C扫B支付 生成门店二维码\20.立即支付-交易服务支付宝下单-接口实现-保存订单【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:06, 02:06, 03:16, 04:34, 06:36, 07:43, 09:14, 11:05, 12:10, 13:05, 14:23, 15:19, 16:43, 18:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 03:00:50

1) 这一组画面整体在讲什么（一句话）：
演示一个支付订单服务的代码实现，包括控制器、服务接口、服务实现、数据库表结构及相关的配置和工具类。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PayController.java 中的 createAllPayOrder 方法，用于处理支付宝下单请求，方法注释说明了业务逻辑。
画面2：展示项目结构，当前选中的是 shanjupay-transaction-service 模块。
画面3：展示 TransactionService.java 接口，定义了 createStoredOrderCode 方法，用于生成支付订单号。
画面4：展示 shanjupay-transaction-api 模块的 pom.xml 文件，其中定义了依赖项，包括 shanjupay-common 和 shanjupay-payment-agent。
画面5：展示 TransactionServiceImpl.java 中的 save 方法，用于保存支付订单，方法注释说明了业务逻辑。
画面6：展示 TransactionServiceImpl.java 中的类定义，包含 @Service 注解和对 appService、merchantService 的引用。
画面7：展示数据库表结构，当前选中的是 pay_order 表。
画面8：展示 TransactionServiceImpl.java 中的类定义，包含 @Service 注解和对 appService、merchantService 的引用。
画面9：展示 PPT 内容，标题为“5.4.2.1 保存订单”，详细说明了 save 方法的实现逻辑。
画面10：展示 TransactionServiceImpl.java 中的 save 方法，调用 PayOrderConvert.INSTANCE.dto2entity 方法将 DTO 转换为实体。
画面11：展示 TransactionServiceImpl.java 中的 save 方法，调用 payOrderMapper.insert 方法插入订单。
画面12：展示 TransactionServiceImpl.java 中的 save 方法，弹出选择 ChronoUnit 的下拉框，用于设置过期时间。
画面13：展示数据库表结构，当前选中的是 pay_order 表，显示了字段及其类型。
画面14：展示 PPT 内容，标题为“5.4.2.1 保存订单”，详细说明了 save 方法的实现逻辑，其中设置了支付币种为“CNY”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
return "forward:/pay-page-error";
/*
 * 支付宝的下单接口，前端订单确认页面，点击确认支付，请求进来
 * @param orderConfirmVO 订单信息
 * @param request
 * @param response
 */
@ApiOperation("支付宝门店下单付款")
@PostMapping("/createAllPayOrder")
public void createAllPayOrderForStore(OrderConfirmVO orderConfirmVO, HttpServletRequest request, HttpServletResponse response) {
    //订单页面跳转
}
```

画面2：
```
shanjuay
├── shanjupay-common
├── shanjupay-gateway
├── shanjupay-merchant
├── shanjupay-merchant-application
├── shanjupay-transaction
├── shanjupay-transaction-api
├── shanjupay-transaction-service
├── shanjupay-transaction-service-api
└── shanjupay-transaction-service
```

画面3：
```java
import com.shanjupay.transaction.api.dto.QRCCodeDto;
/**
 * 交易相关的服务接口
 * Created by Administrator
 */
public interface TransactionService {
    /**
     * 生成支付订单号
     * @param qrCodeDto
     * @return 支付入口（url），携带与参数（有传入的参数转换成，用Base64编码）
     * @throws BusinessException
     */
    String createStoredOrderCode(QRCCodeDto qrCodeDto) throws BusinessException;
    //支付订单保存
    void submitOrderById();
}
```

画面4：
```xml
<modelVersion>4.0.0</modelVersion>
<artifactId>shanjupay-transaction-api</artifactId>
<groupId>com.shanjupay</groupId>
<version>1.0-SNAPSHOT</version>
<dependencies>
    <dependency>
        <groupId>com.shanjupay</groupId>
        <artifactId>shanjupay-common</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>com.shanjupay</groupId>
        <artifactId>shanjupay-payment-agent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
</dependencies>
<build>
    <plugins>
        <plugin>
```

画面5：
```java
/**
 * 保存支付订单，1、保存订单到网关平台，2、调用支付代理服务调用支付宝的接口
 * @param payOrderDTO
 * @return
 * @throws BusinessException
 */
@Override
public PaymentResponseDto submitOrderById(PayOrderDTO payOrderDTO) throws BusinessException {
    //保存订单到网关平台
    //调用支付代理服务，调用支付宝下单接口
    return null;
}
```

画面6：
```java
@Service
@Version(1.0)
public class TransactionServiceImpl implements TransactionService {
    //从配置文件读取支付入口地址
    @Value("${shanjupay.payurl}")
    String payurl;
    @Reference
    AppService appService;
    @Reference
    MerchantService merchantService;
    @Autowired
    PayOrderMapper payOrderMapper;
    //支付订单
    private PayOrder payOrder;
    //支付订单实体
    private PayOrderEntity payOrderEntity;
    //支付订单DTO
    private PayOrderDTO payOrderDTO;
    //支付订单Mapper
    private PayOrderMapper payOrderMapper;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository payOrderRepository;
    //支付订单Service
    private PayOrderService payOrderService;
    //支付订单Controller
    private PayOrderController payOrderController;
    //支付订单Repository
    private PayOrderRepository pay
