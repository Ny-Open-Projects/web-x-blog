# 画面线理解：18.商户注册-MapStruct对象转换-MapStruct测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\18.商户注册-MapStruct对象转换-MapStruct测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:12, 02:12, 02:48, 03:21, 05:24, 07:29, 08:25, 09:18, 10:26, 11:36, 12:54, 13:35, 14:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 02:00:00

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 MapStruct 框架在商户注册业务中实现 DTO 与 Entity 之间的对象转换，并展示其在服务层的使用和测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了商户注册业务中数据传输对象（DTO）与实体（Entity）转换的必要性，代码示例展示了在服务层将 DTO 转换为 Entity 并保存。
画面 2: 展示了商户注册控制器中的代码，使用 @ApiOperation 注解定义接口，并调用服务层的 createMerchant 方法。
画面 3: 介绍了 MapStruct 的概念和优势，说明其通过代码生成简化 Java Bean 对象之间的映射转换，并提供了官方地址。
画面 4: 展示了在 Maven 项目中添加 MapStruct 依赖的配置，包括 mapstruct-jdk8 和 mapstruct-processor。
画面 5: 展示了在商户服务工程中定义转换类的目录结构，位于 convert 包下。
画面 6: 展示了 MerchantConvert 接口的初始代码，准备添加 @Mapper 注解。
画面 7: 展示了在 MerchantConvert 接口中添加 @Mapper 注解，并定义了转换方法。
画面 8: 展示了在 MerchantConvert 接口中定义了两个转换方法：entity2dto 和 dto2entity。
画面 9: 展示了在 main 方法中测试 entity2dto 转换，代码中设置了商户信息并调用转换方法。
画面 10: 展示了在 main 方法中测试 dto2entity 转换，代码中设置了 DTO 信息并调用转换方法。
画面 11: 展示了在 main 方法中测试转换结果，代码中打印了转换后的 DTO 对象。
画面 12: 展示了在 main 方法中测试 List 转换，代码中定义了 List 并调用转换方法。
画面 13: 展示了在 main 方法中测试 List 转换的结果，代码中打印了转换后的 List。
画面 14: 展示了商户资质申请业务流程图，包括商户填写资质信息、上传证件信息、提交资质信息等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public MerchantDTO createMerchant(MerchantDTO merchantDTO) {
    Merchant entity = new Merchant();
    entity.setAuditStatus("0");
    entity.setUserName(merchantDTO.getUsername());
    entity.setMobile(merchantDTO.getMobile());
    //...
    merchantMapper.insert(entity);
    merchantDTO.setId(entity.getId());
    return merchantDTO;
}
```

画面 2:
```java
@ApiOperation(value = "商户注册信息", name = "merchantRegisterVO", required = true, dataType = "MerchantRegisterVO")
@PostMapping("/merchants/register")
public MerchantRegisterVO registerMerchant(@RequestBody MerchantRegisterVO merchantRegisterVO) {
    //...
    merchantDTO.setMobile(merchantRegisterVO.getMobile());
    merchantDTO.setUserName(merchantRegisterVO.getUserName());
    merchantService.createMerchant(merchantDTO);
    return merchantRegisterVO;
}
```

画面 3:
```xml
<!-- MapStruct依赖 -->
<dependency>
    <groupId>org.mapstruct</groupId>
    <artifactId>mapstruct-jdk8</artifactId>
</dependency>
<dependency>
    <groupId>org.mapstruct</groupId>
    <artifactId>mapstruct-processor</artifactId>
    <version>${org.mapstruct.version}</version>
</dependency>
```

画面 4:
```java
package com.shanju.pay.merchant.convert;
```

画面 5:
```java
package com.shanju.pay.merchant.convert;
```

画面 6:
```java
public interface MerchantConvert {

}
```

画面 7:
```java
public interface MerchantConvert {

    //转换实例
    MerchantConvert INSTANCE = Mappers.getMapper(MerchantConvert.class);

    //把dto转换成entity
    Merchant dto2entity(MerchantDTO merchantDTO);

    //把entity转换成dto
    MerchantDTO entity2dto(Merchant merchant);

}
```

画面 8:
```java
public interface MerchantConvert {

    //转换实例
    MerchantConvert INSTANCE = Mappers.getMapper(MerchantConvert.class);

    //把dto转换成entity
    Merchant dto2entity(MerchantDTO merchantDTO);

    //把entity转换成dto
    MerchantDTO entity2dto(Merchant merchant);

}
```

画面 9:
```java
public static void main(String[] args) {
    Merchant merchant = new Merchant();
    merchant.setUserName("测试");
    merchant.setMobile("123456");
    MerchantDTO merchantDTO = MerchantConvert.INSTANCE.entity2dto(merchant);
    System.out.println(merchantDTO);
}
```

画面 10:
```java
public static void main(String[] args) {
    Merchant merchant = new Merchant();
    merchant.setUserName("测试");
    merchant.setMobile("123456");
    MerchantDTO merchantDTO = MerchantConvert.INSTANCE.entity2dto(merchant);
    System.out.println(merchantDTO);
    //把entity转换dto
    merchantDTO.setMerchantName("商户名称");
    Merchant merchant1 = MerchantConvert.INSTANCE.dto2entity(merchantDTO);
    System.out.println();
}
```

画面 11:
```java
public static void main(String[] args) {
    Merchant merchant = new Merchant();
    merchant.setUserName("测试");
    merchant.setMobile("123456");
    MerchantDTO merchantDTO = MerchantConvert.INSTANCE.entity2dto(merchant);
    System.out.println(merchantDTO);
    //把entity转换dto
    merchantDTO.setMerchantName("商户名称");
    Merchant merchant1 = MerchantConvert.INSTANCE.dto2entity(merchantDTO);
    System.out.println();
}
```

画面 12:
```java
public static void main(String[] args) {
    Merchant merchant = new Merchant();
    merchant.setUserName("测试");
    merchant.setMobile("123456");
    MerchantDTO merchantDTO = MerchantConvert.INSTANCE.entity2dto(merchant);
    System.out.println(merchantDTO);
    //把entity转换dto
    merchantDTO.setMerchantName("商户名称");
    Merchant merchant1 = MerchantConvert.INSTANCE.dto2entity(merchantDTO);
    System.out.println();
    //list之间也可以转换，entityList转成MerchantDTO List
    List<MerchantDTO> entityList = new ArrayList<>();
    entityList.add(merchantDTO);
    List<Merchant> list = MerchantConvert.INSTANCE.entityList2dtoList(entityList);
    System.out.println(list);
}
```

画面 13:
```java
public static void main(String[] args) {
    Merchant merchant = new Merchant();
    merchant.setUserName("测试");
    merchant.setMobile("123456");
    MerchantDTO merchantDTO = MerchantConvert.INSTANCE.entity2dto(merchant);
    System.out.println(merchantDTO);
    //把entity转换dto
    merchantDTO.setMerchantName("商户名称");
    Merchant merchant1 = MerchantConvert.INSTANCE.dto2entity(merchantDTO);
    System.out.println();
    //list之间也可以转换，entityList转成MerchantDTO List
    List<MerchantDTO> entityList = new ArrayList<>();
    entityList.add(merchantDTO);
    List<Merchant> list = MerchantConvert.INSTANCE.entityList2dtoList(entityList);
    System.out.println(list);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14:
流程图结构：
- 开始 → 商户填写资质信息
- 商户填写资质信息 → 上传证件信息
- 上传证件信息 → 提交资质信息
- 提交资质信息 → 未通过（循环回到商户填写资质信息）
- 提交资质信息 → 通过（结束）
