# 18.商户注册-MapStruct对象转换-MapStruct测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day03 商户注册 短信验证接口
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day03 商户注册 短信验证接口\18.商户注册-MapStruct对象转换-MapStruct测试【海量资源尽在 666java.com】.mp4
- 时长 14分9秒（音频 850s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来学习一下map struct刚才我们理解了数据传输对象那么map struct和数据传输对象有什么关系呢来我们来看在代码当中啊我们发现有很多这样的代码当初我们在写double服务的接口的时候我们知道它要调用entity也就是我们说的持久层方法它要把什么这个DTO转换成entity对吧你看这里边
[00:28] 是一个转换的过程这个我们在进行数据传输对象的时候我们是不是简单说过每一层都要使用自己的对象由于持久层要用entity而右层用的是DTO所以在Service这里边它会把DTO转换成entity但同样在Controller当中它也会进行转化它会把VO转成什么转成DTO但是在转换的过程中你会发现这个代码是比较反说的
[00:55] 也就是我们把VO转换成DTO我们是不是需要把VO里面的属性都set到DTO里面假如说VO里面有10个属性这里面你是不是要set很多次你看见吗这个是不是就比较繁琐所以这里面我们给大家推荐一个工具就可以来解决对象转换之间的繁琐这个就是MapStructMapStruct它是一个代码的生成器
[01:22] 就是你会发现啊我们在进行代码转换的时候呀你会发现一个特点就是说你看这个VO里边的这个属性的名称诶正好是和DTO里边的属性的名称是一样的你发现了吗对不对对那我们就在想基于这样的特点我们是不是可以很方便的来用一些工具来帮助我们
[01:50] 批量的来进行转换就不用这样一行一行的set去写了所以这就是MapStruct它的一个实现的方法它可以轻而易举的就将加码对象之间按照我刚才说的那种规律进行映射转换好那我们来看一下官方网站大家私下可以点开看一下我这里面就不打开了我们来学习一下怎么样来用MapStruct首先你需要加入它的依赖
[02:17] 那么在哪里加入呢就是你哪个工程用Mapstruct你就在哪加入我们发现在这个double服务里边它需要进行把DTO转换成entity那么这儿你需要那你就加那么你会发现在这个application应用工程当中你需要把VO转换成DTO你也要加对吧也就是你用的地方都可以加好那现在我们来看那具体怎么用呢如果我们现在要进行
[02:46] 这个对象的转换我们要告诉你的代码要将什么对象转换成什么所以这里面我们要写一个叫转换类这个转换类呢就是要定义转换的规则好那现在呢我们来看我们在Service这个工程当中我们准备定一个转换类让entity和do之间来回转换所以来看啊我定一个包叫converter然后在这个里边呢我定一个转换类这个类呢其实是一个接口看好
[03:16] 然后在这个里边注意首先你要加什么注解然后你这里边注意这个注解你看它是MapStrength的注解Mapper这个Mapper就表示什么对映射的意思什么映射就是对象属性的映射然后呢首先我们来看将来我们要用这个转换类那么你需要去实例一个对象对不对所以这里边呢我们要定义它的一个实例
[03:45] 定义它的一个实例的话这里边你要注意看讲义那它其实要用到什么就是Mappers也就是MappersDrag给我们提供的一个什么一个get的方法就可以得到一个基于这个转换类型它所构造的一个什么一个实例注意看那么也就是Mapp然后get然后呢你把它放进去对这就是创建了一个什么创建一个
[04:20] 转换实力转换类实力那么你拿了这个实力对象呢就可以来用了你比如说一会如果我要进行测试的话那么我告诉你其实你就可以怎么做呀你就可以在这儿看好很简单你就这就算得到一个实力了懂吧这就是得到一个实力好那现在呢我们说拿到实力之后我们要进行转换了你要指定这个转换的规则了你这个类
[04:47] 它的目的就是要定义什么DTO和entity它们之间的一个什么转换规则对不对那好那这里边呢我们首先那么我们需要把DTO转换成entity也需要把entity转换成DTO对不对那你说这规则咋定义呢我们先说一个一个的吧我们把DTO转换成entity那你说假如说我写一个方法
[05:21] 我叫一个叫entity2把DTO转换成entity应该是DTO在头也就是DTO2 entity这就是我的方法名行不行那你说如果你写一个方法要将DTO转换成entity通常你是不是要把DTO给传进来大家理解吗然后呢你传回去的输出的应该是谁是不是就是entity有同学不太理解
[05:50] 就是这个方法虽然现在你只定义了一个接口但是我告诉你你现在如何要定义一个方法要实现把DTO转换成entity那么你是不是入餐就是DTO输出的返回值就是entity大家理解吧你把谁转换成什么那这个DTO就是入餐entity就是输出那好那如果我要把entity转换成DTO呢
[06:21] 那这个就简单了嘛这个entity转成DTO我可以定义一个方法啊比如叫DTO然后呢它的入餐就变成谁了就变成什么entity类型了这个不就是我们说entity类型就是和数据库对应的那个什么那个类型吧它的属性是不是和数据库字段一一对应好它的输出的返回值类型是不是就是DTO了大家理解吗对好
[06:53] 那我问你个问题有人说老师这个方法名这个入餐返回值我知道方法名呢我叫abc行不行可以没问题方法名不重要但是重要的是入餐和输出也就是说mapstruck的呢它会根据你的什么输入参数类型它来决定是将谁来转换成什么输入参数就是转换对象的原对象返回值类型
[07:23] 对转换对象的目标对象类型大家理解吗好现在我们把这个写好了之后我给大家测试一下大家就完全明白了看好首先我们定义一个闷方法我们来测假如说现在我准备把DTO转换成entity你看我是不是就可以调用这个方法你将DTO转成entity我问你你是不是需要定义一个DTO的对象没错吧
[07:51] 对吧你定一个GTO对象你是不是要把这个对象转换成GTO类型啊好你注意看我随便往里边写点东西啊你注意这叫测试行不行我再写一个属性因为为啥你写属性因为我写属性的目的就是一会我让你看看它这个对象转换成另外一个对象类型它这个数据还在看好我把它放进去注意现在你哎这事写错了吧对不对你现在要你看
[08:21] 你定义的是entity你是不是应该入餐是entity所以这里边入餐是entity也就是谁啊也就是这里入餐是entity返回值是不是就是DTO是不是就把entity转成DTO所以看好返回值就是DTO大家看懂了好那有时候老师他怎么个效果呀看好我在这打断点我运行让你看一下啊原来我们是手动去定义对象然后呢set set set
[08:49] 是不是往里边写但是现在呢你会发现看好首先你刚才定义的merchant是不是一个是不是一个entityentity的数据是不是还在但是经过你调用这么一个entity to DTO的这么一个方法他这儿是不是就自动把这个DTO对象给创建起来了并且数据也自动set成功看懂了吗所以你看到这儿你就应该知道如果没有这一行代码你会怎么做你肯定会这么做
[09:19] 你遛一个DTO对不对然后又开始了set然后呢从entity里边拿大家懂吧所以这个是不是比较繁琐那现在你有了这个代码那你说是不是就把刚才那个繁琐的对象之间转换给替代了对这就是我们说的把entity转成DTO对不对那有时候老师那你倒过来转能不能转呢
[09:48] 当然可以啊现在我们就可以把什么将entity转成dtu那entity转成dtu这不就是有一个现成的entity吗看好我里边再写一个东西我再转我写完了之后你就知道看好哎这是商户名称看好告诉我现在这个dtu里边是不是有数据现在我准备转了啊看好转哎那你就是谁啊dtu转entity那你就把dtu放进去
[10:23] 好这个时候我们是不是又得到了一个什么一个对象这个对象你再打断点来跟着我看好走你这时候就发现它就可以转换成功你看这个这是不是这个最后的一个对象里面是不是就有商户名称这是不是把DTO转成了entity类型大家看懂了吗这就是我们说的对象之间转换MapsDrag的非常强大它不光可以单个对象之间转换我告诉你
[10:54] list之间也可以转换啥意思你比如说我给你举个例子我现在准备让你将什么呀将这个merchant entity list转成dto list很有意思很好玩将entity list然后呢转成dto list有时候老师这是啥意思呀dto list看好
[11:28] 很有意思我准备如果说各位我现在定义一个list而这个list你注意看这个list就是我的entity list就是我查询数据库完了之后我是不是可能就得到一个entity list我告诉你这个场景很多的然后这里边呢我就往里边放数据了看好啊我放啥呀我放一个entity我问你现在这个list里边是不是有一个entity对我现在让你将这个
[11:59] list注意看啊转成转成什么转成包含dto的list现在这个list上面这个list是不是有entity但是现在我让一个转成包含dto list咋弄很好用mapstack的也可以来转方法跟这个一样嘛你就定一个叫entity listtodto list有时候老师这方法的名字需要注意吗我跟你说
[12:29] 这个方法的名字随便定义但是你定义完了之后你得看懂啥意思你现在要做的是不是就是要将这个什么list里边有这个dto的来转一下对吧你转完了之后你是不是转成list里边有谁是不是有dt将list里边有entity的转成list里边有dto的对不对是吧跟绕口令一样是吧好现在你来看看好点
[12:58] 然后我是不是就可以把它填进去你看好它是不是转成一个list然后你打印看好你就看一下这个效果你就知道了非常神奇注意看那我一运行这个代码你会发现这里边这个entity里头你告诉我是不是填的是entity就是list里边填的entity而下面这个list被转换成了这个list里边
[13:29] 填的是不是就是DTO对不对这是不是就转换层了看到了吗看见了也就是将上面这个包含Entity的List转换成包含DTO的List如果我们有了这么一个工具各位我们之前写的这些代码就是set set set对象之间转换的这些代码我觉得就可以非常方便的来实现了对不对好以上就是我们用
[14:01] MapStruct来解决对象之间转换的这个繁琐这个MapStruct的这个测试入门我们就讲完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

