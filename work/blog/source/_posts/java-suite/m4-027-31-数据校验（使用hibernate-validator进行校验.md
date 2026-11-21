---
title: "基础数据服务收尾：校验全链路验证与其余功能代码导入"
date: 2026-11-18
categories: [Java后端进阶全套, M4 六大进阶项目, 品达物流TMS]
tags: [Java, 项目实战, 物流TMS]
---

# 基础数据服务收尾：校验全链路验证与其余功能代码导入

第二章只剩最后两步。上一节已经给 GoodsTypeDto 加好校验注解、在 Controller 上开了 @Validated，这节先在 Swagger UI 里把校验链路实测一遍——合法数据放行入库、非法数据直接拦截；然后导入资料提供的其余功能代码，pd-base 基础数据服务到此收尾，后面哪个微服务要用基础数据，直接 Feign 调用即可。

## 先给结论

- 添加货物类型接口的最终形态是 `saveGoodsType(@Validated @RequestBody GoodsTypeDto dto)`：@Validated 负责开启参数校验；@RequestBody 与校验无关，它规定前端必须以 JSON 形式提交（Content-Type: application/json），后端解析后封装成 DTO——本节顺手补上，与讲义对齐。
- status 字段的校验组合是 @NotNull + @Max(1) + @Min(0)，取值只允许 0 或 1；name 加了非空校验；字段同时配 @ApiModelProperty 做描述，Swagger 文档同步受益。
- 合法数据（名称 4C、status=1）提交后正常返回并入库；非法数据（去掉 name、status 改成 3）返回 400 Bad Request，响应里带出非空、超上限两类校验提示。
- 校验生效的硬证据在数据库：非法请求前 pd_goods_type 共 35 条，请求之后仍是 35 条——校验失败根本没走到业务层，脏数据没有落库。
- 其余功能代码不再重复开发：资料提供两类文件，MyBatis 映射 XML（按 agency、transportline、truck、user 分包）和 Java 分层代码（controller、entity、mapper、service），整包拷进 pd-base 覆盖同名位置即可。
- 映射 XML 基本是空壳：常规增删改查 SQL 由 MyBatis-Plus 提供，文件只按规范占位，有特殊 SQL 需求再手写；导入完成后 Rebuild 模块，第二章基础数据微服务开发结束。

## 接口形态：@Validated 与 @RequestBody 各管一件事

进入测试前先把接口签名补齐。Controller 里的添加方法长这样：

```java
/**
 * 添加货物类型
 * @param dto 货物类型信息
 */
@PostMapping("")
@ApiOperation(value = "添加货物类型")
public GoodsTypeDto saveGoodsType(@Validated @RequestBody GoodsTypeDto dto) {
    ...
}
```

两个注解分工明确。@Validated 是本节主角，它开启方法参数的校验；@RequestBody 只负责数据传输形式——前端传过来的应该是 JSON，通过它解析之后再封装成 DTO 对象。之前工程里少了这个注解，与讲义不一致，补上之后 Swagger UI 里提交的请求体就从零散参数变成了 JSON 格式，请求头也能看到 application/json。

DTO 侧的校验注解上一节已经就位，以 status 为例：

```java
@ApiModelProperty("状态：禁用 0；正常 1")
@NotNull
@Max(value = 1)
@Min(value = 0)
private Integer status;
```

@NotNull 保证不为空，@Max(1) 和 @Min(0) 把取值锁死在 0 和 1 之间，正好对应"禁用/正常"两种状态；name 字段加了非空校验。也就是说，这几个字段只要有一个不合法，请求就进不了业务逻辑。

## Swagger UI 实测：一正一反两笔请求

服务启动后用 Swagger UI 测 POST /base/goodsType，Parameter content type 选 application/json，一正一反各来一笔：

| 场景 | 请求体 | 结果 |
| --- | --- | --- |
| 合法数据 | defaultVolume、defaultWeight 随意，name=4C，remark 随意，status=1，id 不传 | 正常返回，数据库新增一条 |
| 非法数据 | 去掉 name，status 改成 3 | 400 Bad Request，数据库不变 |

先测合法的。提交后请求正常返回，切到 Navicat 刷新 pd_goods_type 表，4C 这条记录已经写进去了——这是没有校验问题时本来就该有的表现：数据合法，一切照旧。

再测非法的：把 name 从请求体里删掉，再把 status 改成 3，直接 Execute。返回的是 400 Bad Request，响应内容里能看到对应的校验信息——一个是 name 不能为空，一个是 status 超过了上限。回到数据库刷新，表里还是 35 条。对比请求前后的记录数就能确认：这条请求被校验拦在了业务层之外，没有产生任何写入。

到这里校验链路就闭环了：注解定义在 DTO 属性上、开关在 Controller 参数上、失败发生在参数绑定阶段、结果体现在 400 响应和不变的记录数上。前面所有接口只测过合法数据的窟窿，这一节补上了。

## 其余功能代码导入：两类文件、一次覆盖

货物类型只是一张表，基础数据服务实际涉及十几张表（网点、运力、车辆、用户等相关基础数据），技术上都是纯增删改查，没有新东西，课程不再逐个重复开发，直接导入资料里提供的代码。资料位置是「基础数据服务(pd-base)代码导入」，里面分两类内容：

| 资料 | 内容 | 落位 |
| --- | --- | --- |
| mapper 映射文件 | 按 agency、transportline、truck、user 分包的 XML | pd-base 的 resources/mapper 下 |
| Java 代码 | controller、entity、mapper、service 四层 | com.ithema.pinda 包下覆盖 |

先拷映射文件：把 mapper 目录整体复制，粘贴到 pd-base 的 mapper 目录下。这些 XML 打开看基本都是空的，以 PdCourierScopeMapper.xml 为例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.ithema.pinda.mapper.user.PdCourierScopeMapper">

</mapper>
```

空壳的原因是当前用的 MyBatis-Plus：常规增删改查的 SQL 框架已经提供，只需要按规范把映射文件提供出来；后面有特殊需求（比如复杂查询）时，再在对应文件里定义自己的 SQL。

再拷 Java 代码。Controller 分包很细、数量多；Service 是接口加实现，同样按包划分；Mapper 就是 DAO 接口；Entity 是实体——十几张表每张对应一个实体类，Mapper 与之基本一一对应。整体复制包结构，注意层级别放错：要贴到 pinda 这一层目录下，直接覆盖（Override）粘贴。覆盖完成后，Controller、Entity、Mapper、Service 下面的内容就全了，对 pd-base 模块执行一次 Rebuild，保证编译通过。

到这里 pd-base 基础数据服务全部完成，第二章到此结束。后续哪个微服务需要基础数据，直接通过 Feign 调用它即可。

## 小结

本篇两件事。其一，把上一节加好的 hibernate-validator 校验做了一次全链路实测：@Validated 开关、DTO 注解、Swagger UI 提交、400 拦截、数据库记录数对比，一正一反两笔请求把校验效果钉死——非法数据进不了业务层。其二，基础数据服务其余功能代码以整包导入的方式收尾：映射 XML 空壳占位、Java 四层覆盖粘贴、Rebuild 编译，pd-base 完成，等待 Feign 调用。纯 CRUD 的模块不值得重复手写，把校验这种横切能力做扎实，才是这一章真正的收获。
