# 画面线理解：day06-12-开户第一阶段-功能实现8

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-16 实现开户功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-16 实现开户功能\day06-12-开户第一阶段-功能实现8_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 02:10, 03:15, 04:39, 05:38, 06:18, 07:38, 08:09, 09:24, 11:46, 12:26, 12:43, 13:30, 14:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 06:21:20

1) 这一组画面整体在讲什么（一句话）：
演示一个P2P平台开户流程的系统架构图，并展示相关服务中实现签名、保存记录、配置读取等核心功能的Java代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示P2P平台开户流程的架构图，包含“浏览器/App”、“用户中心”、“存管代理服务”、“存管系统”、“开卡银行”五个模块，以及各模块间的数据交互步骤（如1.1生成开户请求数据、1.4通过短信生成实名及数据、2.1跳转关闭开户接口等）。
画面2：展示IDE中“DepositoryRecordServiceImpl.java”文件，其中“createConsumer”方法内有注释“//1.保存交易记录”和“//2.签名数据并返回”，代码中调用“saveDepositoryRecord”方法并执行“JSON.toJSONString”和“RSAUtil.sign”操作。
画面3：展示IDE中“RSAUtil.java”文件，其中包含生成私钥的代码“PrivateKey privateKey = keyFactory.generatePrivateKey();”和生成密钥对的静态方法“public static KeyPair genKeyPair() throws Exception { ... }”。
画面4：展示IDE中“DepositoryRecordServiceImpl.java”文件，代码中“RSAUtil.sign”方法调用时传入了“configService.getPpPrivateKey()”。
画面5：展示IDE中“ConfigService.java”文件，其中包含获取配置的三个方法：“public String getPpPublicKey()”、“public String getPpCode()”和“public String getPpPrivateKey()”，并注释说明“万信P2P系统 标识”和“万信P2P系统私钥”。
画面6：展示IDE中“DepositoryRecordServiceImpl.java”文件，代码中“RSAUtil.sign”方法调用时传入了“configService.getPpPrivateKey()”。
画面7：展示IDE中“DepositoryRecordServiceImpl.java”文件，代码中“saveDepositoryRecord”方法内设置“requestType”和“objectType”等字段。
画面8：展示IDE中“DepositoryRecordServiceImpl.java”文件，代码中“saveDepositoryRecord”方法内设置“requestNo”、“requestType”、“objectType”、“objectId”、“createDate”等字段，并注释说明“//1.银行存管代理服务保存记录、数据状态为未同步”、“//设置请求流水号”、“//设置请求类型”、“//设置关联业务实体对象”、“//设置关联业务实体标识，这个不存在”、“//设置请求时间”。
画面9：展示Apollo配置中心界面，显示“micro_service.spring-boot-http”和“micro_service.spring-eureka”两个配置项，以及多个服务的截图，如“adminService”、“configService”、“ApolloPortal”等。
画面10：展示IDE中“DepositoryRecordServiceImpl.java”文件，代码中“RSAUtil.sign”方法调用时传入了“configService.getPpPrivateKey()”。
画面11：展示IDE中“VerificationInterceptor.java”文件，其中包含“@Autowired private ConfigService configService;”和“String signature = httpRequest.getParameter(name: “signature”);”等代码。
画面12：展示IDE中“P2PRequestInterceptor.java”文件，其中包含“@Value("${depository.privateKey}") private String depositoryPrivateKey;”和“String reqData = EncryptUtil.decodeUTF8StringBase64(httpRequest.getParameter(name: “reqData”));”等代码。
画面13：展示Apollo配置中心界面，显示多个服务的截图，如“adminService”、“configService”、“ApolloPortal”等。
画面14：展示IDE中“DepositoryRecordServiceImpl.java”文件，代码中“RSAUtil.sign”方法调用时传入了“configService.getPpPrivateKey()”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面2代码：
```java
public class DepositoryRecordServiceImpl extends ServiceImpl<DepositoryRecordMapper, DepositoryRecord> implements DepositoryRecordService {
    @Override
    public GatewayRequest createConsumer(ConsumerRequest consumerRequest) {
        //1.保存交易记录
        saveDepositoryRecord(consumerRequest);
        //2.签名数据并返回
        String reqData = JSON.toJSONString(consumerRequest);
        RSAUtil.sign(reqData, configService.getPpPrivateKey(), "utf-8");
    }
}
```
画面3代码：
```java
PrivateKey privateKey = keyFactory.generatePrivateKey();
return privateKey;

//生成密钥对
public static KeyPair genKeyPair() throws Exception {
    KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
    keyGen.initialize(1024); //可以理解为，加密后的密文长度，实际还是要小些，加大加密解像
    KeyPair keyPair = keyGen.generateKeyPair();
    return keyPair;
}
```
画面4代码：
```java
String reqData = JSON.toJSONString(consumerRequest);
RSAUtil.sign(reqData, configService.getPpPrivateKey(), "utf-8");
```
画面5代码：
```java
public String getPpPublicKey() { return config.getProperty(key: "p2p.publicKey", defaultValue: null); }
public String getPpCode() { return config.getProperty(key: "p2p.code", defaultValue: null); }
public String getPpPrivateKey() { return config.getProperty(key: "p2p.privateKey", defaultValue: null); }
```
画面6代码：
```java
String reqData = JSON.toJSONString(consumerRequest);
String sign = RSAUtil.sign(reqData, configService.getPpPrivateKey(), "utf-8");
```
画面7代码：
```java
private void saveDepositoryRecord(ConsumerRequest consumerRequest) {
    DepositoryRecord depositoryRecord = new DepositoryRecord();
    depositoryRecord.setRequestNo(consumerRequest.getRequestNo());
    depositoryRecord.setRequestType(DepositoryRequestTypeCode.CONSUMER_CREATE.getCode());
    depositoryRecord.setObjectType("Consumer");
    depositoryRecord.setObjectId(consumerRequest.getObjectId());
    depositoryRecord.setCreateDate(LocalDateTime.now());
}
```
画面8代码：
```java
//1.银行存管代理服务保存记录、数据状态为未同步
DepositoryRecord depositoryRecord = new DepositoryRecord();
//设置请求流水号
depositoryRecord.setRequestNo(requestNo);
//设置请求类型
depositoryRecord.setRequestType(requestType);
//设置关联业务实体对象
depositoryRecord.setObjectType(objectType);
//设置关联业务实体标识，这个不存在
depositoryRecord.setObjectId(objectId);
//设置请求时间
depositoryRecord.setCreateDate(localDateTime);
```
画面9配置：
```yaml
micro_service.spring-boot-http
micro_service.spring-eureka
```
画面10代码：
```java
String reqData = JSON.toJSONString(consumerRequest);
String sign = RSAUtil.sign(reqData, configService.getPpPrivateKey(), "utf-8");
```
画面11代码：
```java
@Autowired
private ConfigService configService;

@Override
public boolean preHandle(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, Object handler) throws Exception {
    String serviceName = httpServletRequest.getParameter(name: "serviceName");
    String platformNo = httpServletRequest.getParameter(name: "platformNo");
    String signature = httpServletRequest.getParameter(name: "signature");
    BaseResponse baseResponse = new BaseResponse();
}
```
画面12代码：
```java
@Value("${depository.privateKey}")
private String depositoryPrivateKey;

@Autowired
private RequestDetailsService requestDetailsService;

@Override
public boolean preHandle(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, Object handler) throws Exception {
    String serviceName = httpServletRequest.getParameter(name: "serviceName");
    String platformNo = httpServletRequest.getParameter(name: "platformNo");
    String reqData = EncryptUtil.decodeUTF8StringBase64(httpServletRequest.getParameter(name: "reqData"));
}
```
画面13配置：
```yaml
adminService
configService
ApolloPortal
```
画面14代码：
```java
String reqData = JSON.toJSONString(consumerRequest);
String sign = RSAUtil.sign(reqData, configService.getPpPrivateKey(), "utf-8");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1架构图：
- 模块“浏览器/App”指向“用户中心”；
- “用户中心”指向“存管代理服务”；
- “存管代理服务”指向“存管系统”；
- “存管系统”指向“开卡银行”；
- “开卡银行”指向“存管系统”；
- “存管系统”指向“用户中心”；
- “用户中心”指向“浏览器/App”；
- “存管代理服务”指向“存管系统”；
- “存管系统”指向“开卡银行”；
- “开卡银行”指向“存管系统”；
- “存管系统”指向“用户中心”；
- “用户中心”指向“浏览器/App”；
- “存管代理服务”指向“存管系统”；
- “存管系统”指向“开卡银行”；
- “开卡银行”指向“存管系统”；
- “存管系统”指向“用户中心”；
- “用户中心”指向“浏览器/App”；
- “存管代理服务”指向“存管系统”；
- “存管系统”指向“开卡银行”；
