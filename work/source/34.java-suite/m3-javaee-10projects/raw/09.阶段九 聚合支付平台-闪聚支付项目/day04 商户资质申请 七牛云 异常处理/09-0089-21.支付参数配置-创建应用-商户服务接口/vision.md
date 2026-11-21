# 画面线理解：21.支付参数配置-创建应用-商户服务接口

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day04 商户资质申请 七牛云 异常处理
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day04 商户资质申请 七牛云 异常处理\21.支付参数配置-创建应用-商户服务接口【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 01:44, 03:06, 03:53, 04:57, 06:08, 06:57, 07:55, 08:50, 09:45, 10:36, 11:25, 12:42, 13:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:15:11

1) 这一组画面整体在讲什么（一句话）：
演示如何在商户平台创建应用的接口实现，包括定义数据传输对象、接口契约、数据库表结构以及核心业务逻辑的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示系统交互流程图，说明商户平台应用与商户服务之间的交互步骤，包括创建应用、保存应用信息、校验并保存商户应用信息等。
画面2：展示项目结构，重点是AppDTO类，其中定义了商户名称、商户ID、公钥、回调地址等属性。
画面3：展示接口定义，AppService接口中定义了createApp方法，用于创建应用。
画面4：展示接口实现，AppServiceImpl类实现了AppService接口，包含createApp方法的实现。
画面5：展示数据库表结构，包括APP_ID和APP_NAME字段，以及对应的索引。
画面6：展示AppCovert接口的定义，用于对象转换。
画面7：展示createApp方法的实现，包括校验商户信息、生成应用ID、保存商户应用信息等步骤。
画面8：展示商户实体类Merchant的属性，包括商户名称、地址、类型等。
画面9：展示应用ID生成的逻辑，使用UUID方式生成。
画面10：展示异常处理，包括BusinessException和各种运行时异常。
画面11：展示数据库操作，使用appMapper进行数据插入。
画面12：展示应用名称唯一性校验的SQL语句。
画面13：展示应用名称唯一性校验的Java代码。
画面14：展示保存应用信息的代码，包括设置应用ID、商户ID、转换对象、插入数据库等操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@ApiModelProperty(value = "商户名称")
private String appName;
@ApiModelProperty(value = "应用公钥（RSA1thSHA256）")
private Long merchantId;
@ApiModelProperty(value = "我收回调地址")
private String notifyUrl;
```

画面3：
```java
public interface AppService {
    /**
     * 创建应用
     * @param merchantId 商户ID
     * @param appDTO 应用信息
     * @return 创建成功的应用信息
     * @throws BusinessException
     */
    AppDTO createApp(Long merchantId, AppDTO appDTO) throws BusinessException;
}
```

画面4：
```java
import com.shanjuay.merchant.api.dto.AppDTO;
import org.apache.dubbo.config.annotation.Service;

public class AppServiceImpl implements AppService {
    /**
     * 创建应用
     * @param merchantId 商户ID
     * @param appDTO 应用信息
     * @return 创建成功的应用信息
     * @throws BusinessException
     */
    @Override
    public AppDTO createApp(Long merchantId, AppDTO appDTO) throws BusinessException {
```

画面5：
```sql
CREATE TABLE app (
    id bigint(20) NOT NULL,
    app_name varchar(50) NOT NULL,
    app_id varchar(50) NOT NULL,
    ...
);
```

画面6：
```java
@Mapper
public interface AppCovert {
    AppCovert INSTANCE = Mappers.getMapper(AppCovert.class);
    AppDTO entity2dto(App entity);
    App dto2entity(AppDTO dto);
    List<AppDTO> listentity2dto(List<App> app);
}
```

画面7：
```java
if (merchantId == null || appDTO == null) {
    throw new BusinessException(CommonErrorCode.E_30009);
}
// 1) 校验商户是否通过资质审核
if (merchant == null) {
    throw new BusinessException(CommonErrorCode.E_20002);
}
// 校验商户资质状态
merchant.
```

画面8：
```java
public class Merchant {
    private String getBusinessLicenseImg();
    private String getContactsAddress();
    private String getIdCardFroning();
    private String getIdCardRear();
    private String getMerchantAddress();
    private String getMerchantName();
    private String getMerchantWo();
    private String getMobile();
    private String getTel();
}
```

画面9：
```java
// 应用ID使用UUID方式生成
String appid = UUID.randomUUID().toString();
```

画面10：
```java
// 异常处理
throw new BusinessException(CommonErrorCode.E_30009);
```

画面11：
```java
// 保存应用信息
app.setAppId(RandomUtil.getUUID());
app.setMerchantId(merchant.getId());
App entity = AppCovert.INSTANCE.dto2entity(app);
appMapper.insert(entity);
return AppCovert.INSTANCE.entity2dto(entity);
```

画面12：
```java
// 校验应用名是否已被使用
@Param appname
public Boolean isExistAppName(String appname) {
    Integer count = appMapper.selectCount(new QueryWrapper<App>()
            .eq(App::getAppName, appname));
    return count.intValue() > 0;
}
```

画面13：
```java
// 为防止应用名重复
private Boolean isExistAppName(String appname) {
    Integer count = appMapper.selectCount(new LambdaQueryWrapper<App>().eq(App::getAppName, appname));
    return count > 0;
}
```

画面14：
```java
// 保存应用信息
app.setAppId(RandomUtil.getUUID());
app.setMerchantId(merchant.getId());
App entity = AppCovert.INSTANCE.dto2entity(app);
appMapper.insert(entity);
return AppCovert.INSTANCE.entity2dto(entity);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“4.1 需求分析”，子标题“4.1.1 系统交互流程”。架构图显示“浏览器/APP”指向“商户平台应用”，再指向“商户服务”，最后返回“创建应用成功”。
画面6：PPT标题为“4.2.1.2 接口实现”，内容为“定义AppCovert负责对象转换”。
画面14：PPT标题为“4.2.2 商户平台应用创建应用接口（接口②）”，子标题“4.2.2.1 接口定义”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
