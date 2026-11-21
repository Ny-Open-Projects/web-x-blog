# 03.对接SaaS-代码实现-为门店设置管理员

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day06 SaaS对接 OAuth2.0 前后端集成测试
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day06 SaaS对接 OAuth2.0 前后端集成测试\03.对接SaaS-代码实现-为门店设置管理员【海量资源尽在 666java.com】.mp4
- 时长 3分37秒（音频 217s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那下面呢我们就给这个门店呢设置员工的作为他的管理员那么最终的记录呢会插到我们这个stores staff这个关系表中大家看到这张表呢也是比较简单的有一个门店的ID和一个什么员工的ID好那来我们呢说干就干啊接下来我们来把这个接口写一下这个接口呢叫为门店设置管理员那简单理解呢其实就可以说给这个门店呢哎把这个员工呢他们之间关系呢给他绑起来
[00:29] 那其实各位我说到这呢我要强调一下在我们员工表其实有一个字段呢就是门店的ID的就是员工所属门店他俩的关系其实在这都已经有了而这个关系表注意而这个叫Store Staff这个关系表呢里边存在的记录呢就表示这个门店呢他的管理员是谁好那我们就准备在我们的Service接口中啊还把刚才的这个在这接着写啊
[00:56] 就是将员工和门店进行绑定是吧那这时候绑定呢其实各位目的主要是啥设置管理员对不对将员工设置为门店的管理员好那么设置为门店的管理员的话这里边你肯定要给我一个什么这个门店的ID还有一个啥这个叫员工的ID对吧好那么
[01:26] 如果你绑定成功那这个方法就执行正常执行完成就可以了但如果说你这个设置失败那我们就让它抛之一长所以这里边呢我们就不要它的这个返回值了就是外的好那接下来我们继续来做那么就该写接口实现了吧好那来看一下把它报出来那这个时候呢因为你要做这个门店和
[01:56] 员工的关系表嘛所以这里面呢还需要导入一个Mapper好那么这个呢就是叫做什么呀对叫做Store Staff Mapper好那么接下来这里边那怎么做呀那肯定是直接Insert就行吧但是Insert的话这里边你看我是需要创建一个Entity的吧Store Staff然后呢你看它呢是不是需要去
[02:30] set一个是谁就是员工的ID吧就是这个管理员的ID是吧员工ID好那还有啥这个错了你看它报错了然后还有一个是storestore呢其实应该也是了数据库里面它保存的是数字类型啊这是门店ID这样的话我们把它放进去各位这个过程就OK了吧
[03:01] 好那我们需要去把刚才这个接口呢把这个类型改一下好这个接口呢就做完了好了以上呢我们就完成了什么就是新增门店啊然后呢新增员工然后呢给这个门店设置管理员这个过程是不是就做完了
[03:25] 最后一步我们是要在商户注册的时候我们来调这些接口顺便还要调一个非常重要的就是SaaS的接口来完成整个商户注册的流程好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲：在商户服务中实现“绑定门店与员工”的功能，包括数据库表结构查看、接口定义与代码实现。

2) 按时间顺序列出每张画面的要点：
画面1：查看数据库表 store_staff 的结构，包含字段 ID、STORE_ID、STAFF_ID，以及主键索引 PRIMARY KEY。
画面2：在数据库导航树中选中 store_staff 表，准备查看其结构。
画面3：在 MerchantService 接口中定义 createStaff 方法，用于新增员工，参数为 StaffDTO，返回 StaffDTO，抛出 BusinessException。
画面4：在 MerchantService 接口中定义 bindStaffToStore 方法，用于绑定员工与门店，参数为 storeId 和 staffId，抛出 BusinessException。
画面5：在 MerchantService 接口中定义 bindStaffToStore 方法，参数为 storeId 和 staffId，抛出 BusinessException。
画面6：在 MerchantService 接口中定义 bindStaffToStore 方法，参数为 storeId 和 staffId，抛出 BusinessException。
画面7：在 MerchantServiceImpl 中实现 createStore 方法，用于创建门店，参数为 StoreDTO，返回 Store，抛出 BusinessException。
画面8：在 MerchantServiceImpl 中定义自动注入的 storeMapper 和 staffMapper。
画面9：在 MerchantServiceImpl 中查看自动注入的 storeMapper 和 staffMapper。
画面10：在 MerchantServiceImpl 中实现 bindStaffToStore 方法，参数为 storeId 和 staffId，抛出 BusinessException。
画面11：在 MerchantServiceImpl 中实现 bindStaffToStore 方法，调用 storeStaffMapper.insert()。
画面12：在 MerchantServiceImpl 中实现 bindStaffToStore 方法，创建 StoreStaff 对象并设置属性。
画面13：在 MerchantServiceImpl 中实现 bindStaffToStore 方法，设置 StoreStaff 的 staffId 和 storeId。
画面14：查看 PPT 中的接口定义，接口方法为 void bindStaffToStore(long storeId, long staffId) throws BusinessException。

3) 画面中出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
表: store_staff
Columns (3)
Field Type Comment
ID bigint(20) NOT NULL
STORE_ID bigint(20) NULL 门店标识
STAFF_ID bigint(20) NULL 员工标识
Indexes (1)
Index Name Column Index Type
PRIMARY ID Unique

画面3：
Boolean isExistStaffByMobile = isExistStaffByMobile(staffDTO.getMobile(), staffDTO.getMerchantId());
if (isExistStaffByMobile) {
    throw new BusinessException(CommonErrorCode.E_10013);
}
Staff staff = staffMapper.insert(staffDTO);
return StaffConvert.INSTANCE.entity2dto(staff);

画面4：
StaffDTO createStaff(StaffDTO staffDTO) throws BusinessException.
//将员工设置为门店的管理员
bindStaffToStore(String storeId, String staffId)

画面5：
void bindStaffToStore(String storeId, String staffId) throws BusinessException.

画面7：
@Override
public StoreDTO createStore(StoreDTO storeDTO) throws BusinessException {
    Store entity = StoreConvert.INSTANCE.dto2entity(storeDTO);
    log.info("新增门店：{}", JSON.toJSONString(entity));
    storeMapper.insert(entity);
    return StoreConvert.INSTANCE.entity2dto(entity);
}

画面8：
@Autowired
StoreMapper storeMapper;
@Autowired
StaffMapper staffMapper;

画面10：
public void bindStaffToStore(String storeId, String staffId) throws BusinessException {

画面11：
storeStaffMapper.insert();

画面12：
StoreStaff storeStaff = new StoreStaff();
storeStaff.setStaffId(staffId); //员工id
storeStaff.setStoreId(storeId); //门店id

画面14：
void bindStaffToStore(long storeId, long staffId) throws BusinessException;

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14：
标题：1.4.3 商户服务门店设置管理员接口
子标题：1.4.3.1 接口定义
内容：在MerchantService接口类中定义接口：
/** 为门店设置管理员
@param storeId
@param staffId
@throws BusinessException
*/
void bindStaffToStore(long storeId, long staffId) throws BusinessException;

子标题：1.4.3.2 接口实现
内容：在MerchantServiceImpl实现bindStaffToStore。
@Override
public void bindStaffToStore(long storeId, long staffId) {

5) 不要评价画面美观，不要输出与课程无关的内容。

