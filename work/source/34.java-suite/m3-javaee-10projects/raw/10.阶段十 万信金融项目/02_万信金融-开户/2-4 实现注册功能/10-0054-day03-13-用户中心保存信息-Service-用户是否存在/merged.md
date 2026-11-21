# day03-13-用户中心保存信息-Service-用户是否存在

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day03-13-用户中心保存信息-Service-用户是否存在_【海量资源尽在 666java.com】.mp4
- 时长 14分3秒（音频 843s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 数据访问层的代码咱们编写完毕之后接下来的重点应该是在Service就是业务层对不对这层的代码一般编写的时候都会稍微多一些稍微麻烦一些业务层咱首先也是要定义一个接口对叫consumer Service咱先把接口给创建出来然后定义一些方法
[00:27] 那咱找到Service这个包啊这个包目前肯定是空的了咱进来先定义接口然后起个名字就是con sumer Service接口那在这个接口里边呢咱就要定义一些什么呀方法都定义哪些方法呢这个地方大家一定要注意了我们需要定义两个方法一个是查一查手机号是否存在一个是用户是否存在
[01:00] 然后一个就是什么呀保存信息就是注册那有的学员会说这个检测用户是不是存在这个功能貌似是不是在前面已经实现过你说的没错但是我要提醒大家注意的咱现在是不是在consumer这个wifu当中以前的这个功能是在哪实现的呀是在统一账户中心对吧就是account那边那这里边你要注意了这个用户中心跟统一账户这俩是两个独立的wifu
[01:30] 他俩有关系吗有关系但是毕竟呢是你是你我是我不是一家人所以你前面实现那些功能啊就是教研手机号教研验证本那是同一账户那边的那跟人家用户中心有啥关系所以用户中心这边呢仍然是要教研手机号还要干什么呀保存这个相关的信息所以这个你一定要注意那我们最终确定就是在这个接口里边我们一共要定义两个方法
[01:59] 一个叫checkmobile就是检测这个用户是否存在就是手机号是否存在一个就是我们说到什么呀注册另外呢提醒大家注意我们前面在学习MP的时候说过MP是不是对业务层也完成了什么呀封装对不对也进行封装所以说你在写代码的时候业务层的接口一定要继承MP的这个接口这需要大家注意的啊那相关的这块代码呢比较简单我就不再从头给大家编写了我把这一块扔过来
[02:31] 把咱们这个替换一下这个导包没导进来是吧我们人工导一下我们再导一下好了没有错了很简单check mobile就是传进来一个手机号然后最终返回一个01表示这个用户是否存在了那么register跟前面account那边是一样的就是保存用户信息的那么前端发过来的这个数据会用consumerregister.to对象进行什么封口
[03:16] 所以说这是我们设计的接口里边的两个方法那咱接下来一个一个来吧先实现这个什么呀checkmobile因为这个相来说会比较简单一些那咱是不是要接下来要干什么呀创建该接口的一个实现类了con sumer se vice然后impl好我们让他去干什么呀实现
[03:48] 我们刚才定义的接口consumer Service另外别忘了我们说了P是不是对业务层进行封装所以说我们这还要继承谁对我们的实现类也要继承MP的叫Service imprserviceimpl就是这个地方而且它是不是有两个什么
[04:24] 两个范围型呃第一个范围型是写啥呢那如果你已经忘记的话那你就可以查一查以前的什么呀代码啊第一个范围型应该是指定那个Mapper接口conconsumer mapperconso m1r m第二个范围型是用来设置那个实体类的就是conso m1r没错啊这个包我们再成功导一下吧
[05:04] 好这就可以那为什么还报错呀这报错是正常的吧因为咱刚才在接口里边是不定义了两个方法吗这两个方法你还没重写了所以他报错很正常来咱把这两个方法给他快速的生成一下OK那么目前的话咱只实现checkmobile然后再实现这个register那这个checkmobile我们刚才说它是实现什么功能的呀
[05:42] 是不是检测用户受存在说白了就是去表里边查一查这个手机号是否什么呀存在那不就是一次查询吗对不对那用MP实现这样的查询调什么方法你还有一项吗叫什么呀叫什么名get one是吧是不是get one对就是get one那我们考虑到将来这一块代码就是里边这一块代码有可能这个好多地方都要用所以说我们把这个代码准备呢单独摘出来定义一个方法
[06:16] 呃我们这样写private sale的嘛因为他即使将来有地方用也是在conceal这边用啊所以说我们这儿就定义成私有的起个方法就叫getby mobile见名之一吧是不是根据手机号做一次什么呀查询那自然他一定是怎么着啊对自然他一定有一个参数就是手机号了st 啊
[06:52] Stream Mobile那有没有返回值呢那肯定得有返回值那这个返回值的话你可以返回一个查出来的一个对象你也可以直接把结果返回它就是01那我们这就返回一个对象因为考虑到将来这个方案有可能别的地方要用所以说咱返回01不太合适01是它的功能所以我这就返回一个对象对叫Consumer DTO
[07:22] 看看有没有提供这个现成的一个类有的话我们直接拿过来我们直接拿过来用吧consumer DTO有吧control C这个DTO是粘到什么地方了你还有印象吗没有印象没有关系打开看看是不是在API工程里面对吧consumer这个包下边子包MODL好我们接下来就c然后去API工程里边有consumer对不对然后control V粘过来
[07:59] 这里边就是一个DTO对象里边封装了一些属性我这里边就可以写上返回值就是consumercon sumerdto对所以说这个方法非常简单纯粹就是给我一个手机号我做一次查询然后查出来数据就返回查不出来我返回一个null对不对这都是可以或者说我可以抛一个什么一场这都是可以都是可以
[08:33] 那咱接下来怎么实现这个查询呢还有印象吗那肯定要用MP了咱刚才提到用哪个方法是叫get1对不对get什么呀对get1是这个get1吧对不对大家看一下这个get1是不是有两个方法咱一般就用上面这个就行下面这个是用来决定这个如果没有查出来数据要不要po异常呃想想啊这个地方的话
[09:02] 其实你怎么写都行你将来查不到数据你跑一场也可以或者说呢你查不到数据将来也可以返回一个什么呀那都可以那咱就用第一个方法了第一个方法他要的是不是那个呃叫条件构造器对吧Warp啊Warp那我们直接就直接在这儿Nio了啊因为这个东西大家都比较熟了Query Q U E R YQuery Warp直接Nio出来Nio出来之后呢这里边大家注意这里边是不是要设置一个饭行就是我们说的Consumer
[09:33] C-O-N-S-U-M-E-R对不对C-O-N-S-U-M-E-R好 随后然后这个对象有了之后呢当时在Count里边我们讲过是不是两种写法第一种就是咱普通的一种写法第二种呢是不是用Lambda表示我们当时也提过Lambda表示的好处是不是那个字段名不容易写错对不对咱这次仍然用Lambda表示第二Lambda然后呢再第二什么呀我们现在是不是
[10:06] 拿着手机号做相等判断对不对做相等判断的话我们应该调一个方法叫什么呀对EQ对哪个字段进行判断呢那就是consumer里边的什么呀对consumer里边的手机号就应该这么写然后呢跟谁进行判判断呀跟谁进行对比呀那是不是就是传过来的这个什么呀手机号对不对那就是MO就是这个参数了吗莫非就是这么写
[10:42] 这就是我们的get one方法那他返回的是不是一个对象吧consumer对象对吧那咱接下来用consumer来接受一下接受一下对那无非良人结果如果查出来他就不给空如果查出来如果查不出来他就是一个什么呀空的那咱接下来就可以直接进行什么呀返回吗直接可以进行返回不行啊不行一定要注意你看他这返回的是consumer咱这要的是什么呀
[11:14] 对consumer DTO啊所以说你这还是需要进行什么呀进行一个转换把这个consumer转换成consumer什么呀DTO啊我们还是单独写一个方法这个咱也不用大家从头自己写了我们粘过来一个得了从这啊这个地方我们把它粘过来分两批粘吧粘到下边啊这种操作在咱们P2P当中很常见好我们把它都粘过来
[12:07] 好大概就这个样子吧具体的你下去自己粘过来之后呢可以自己改一下啊我大概就整成这个样子呃这里边代码呢其实大家都见过啊前面都见过也比较简单那就是传过来一个实体类对象对吧然后我自己在拧一个DTO对象通过这个工具类进行属性值的一个复制就完事那我在这是不是就可以直接返回哎这个方法的这个返回值就行return谁啊
[12:38] convert consumer对吧entity to DTO然后把它传过去就行这里边你要注意你看它这里边是这样如果安抬腿为空就是我们查反那个队伍围空它直接就反而空了对不对我逻辑是没问题的这个发能写完了写完之后是不是需要在这进行什么是要在这进行调用这个调用就简单了直接就是get mobileget by mobile
[13:08] 把这个手机号呢给他传过去然后呢我们这边就我来个什么呀来个比较风骚的一种写法三点运算符吧好吧不等于闹的话然后呢问号一冒号什么零哎看这个你能看懂吗能看懂吗这是不是咱要查询的手机号吗手机号是不是扔给这个方法这个方法查完之后是不是又调上这个方法转成DTO对象反正我不管怎么着反正你这个反应值要么是闹要么不是闹
[13:40] 那如果不是闹我就表示它存在就妨碍几啊一如果是闹就妨碍什么呀零没问题吧那目前呢咱就把呃业务层当中的第一块代码给写完就检查这个手机号或者用户设备存在这个代码的写号那一会呢咱就编写这个什么代码对注册就是保存这个用户信息这个代码

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过 MyBatis-Plus 和 Lambda 表达式实现消费者服务的手机号校验与用户注册功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示项目结构，聚焦于 `ConsumerMapper.xml` 文件，其内容为 MyBatis Mapper 配置，namespace 指向 `cn.itcast.wanxing2p.consumer.Mapper.ConsumerMapper`。
画面 2: 展示 `ConsumerService.java` 接口，定义了 `checkMobile` 和 `register` 方法。
画面 3: 展示右键 `ConsumerService.java` 选择“Generate”生成实现类，提示将生成 `ConsumerServiceImpl`。
画面 4: 展示生成的 `ConsumerServiceImpl.java` 文件，其继承自 `ServiceImpl<ConsumerMapper, Consumer>` 并实现 `ConsumerService` 接口。
画面 5: 在 `ConsumerServiceImpl.java` 中，展示 `checkMobile` 方法的实现，当前返回 `null`。
画面 6: 在 `ConsumerServiceImpl.java` 中，将 `checkMobile` 方法改为私有方法，并添加了 `private` 修饰符。
画面 7: 展示 `ConsumerRegisterDTO` 类，其包含 `id`、`username`、`fullname`、`idNumber` 等字段，并使用 `@ApiModel` 和 `@ApiModelProperty` 注解。
画面 8: 在 `ConsumerServiceImpl.java` 中，展示 `getByMobile` 方法的 Lambda 表达式实现，使用 `QueryWrapper` 和 `lambda` 方法。
画面 9: 在 `ConsumerServiceImpl.java` 中，展示 `getByMobile` 方法的完整实现，使用 `QueryWrapper` 和 `lambda` 方法。
画面 10: 在 `ConsumerServiceImpl.java` 中，展示 `getByMobile` 方法的 Lambda 表达式实现，使用 `QueryWrapper` 和 `lambda` 方法。
画面 11: 展示一个 Word 文档，内容为“万方数据-消费者注册流程”，其中包含“检查手机号是否已注册”、“创建 Consumer 实体”、“保存 Consumer”等步骤。
画面 12: 屏幕空白，无内容。
画面 13: 展示 `ConsumerServiceImpl.java` 中 `convertConsumerEntityToDTO` 方法的实现，用于将实体转换为 DTO。
画面 14: 展示 `ConsumerServiceImpl.java` 中 `checkMobile` 方法的实现，当前返回 `null`，并展示 `getByMobile` 方法的 Lambda 表达式实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0.0/EN" "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.itcast.wanxing2p.consumer.Mapper.ConsumerMapper">
</Mapper>
```

画面 2:
```java
package cn.itcast.wanxing2p.consumer.Service;

public interface ConsumerService {
}
```

画面 4:
```java
package cn.itcast.wanxing2p.consumer.Service;

import cn.itcast.wanxing2p.api.consumer.model.ConsumerRegisterDTO;
import cn.itcast.wanxing2p.consumer.entity.Consumer;
import cn.itcast.wanxing2p.consumer.Mapper.ConsumerMapper;
import com.baomidou.mybatisplus.extension.Service.impl.ServiceImpl;

public class ConsumerServiceImpl extends ServiceImpl<ConsumerMapper, Consumer> implements ConsumerService {
}
```

画面 5:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}
```

画面 6:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}

private getMobile(String mobile) {
}
```

画面 7:
```java
import ...

@Data
@ApiModel(value = "ConsumerDTO", description = "平台-端用户信息")
public class ConsumerDTO {

    @ApiModelProperty("用户id")
    private Long id;

    @ApiModelProperty("用户名")
    private String username;

    @ApiModelProperty("真实姓名")
    private String fullname;

    @ApiModelProperty("身份证号")
    private String idNumber;
}
```

画面 8:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}

private ConsumerDTO getMobile(String mobile) {
    return getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
}
```

画面 9:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}

private ConsumerDTO getMobile(String mobile) {
    return getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
}
```

画面 10:
```java
@Override
public Integer checkMobile(String mobile) {
    return null;
}

private ConsumerDTO getMobile(String mobile) {
    return getOne(new QueryWrapper<Consumer>().lambda().eq(Consumer::getMobile, mobile));
}
```

画面 13:
```java
private ConsumerDTO convertConsumerEntityToDTO(Consumer entity) {
    if (entity == null) {
        return null;
    }
    ConsumerDTO dto = new ConsumerDTO();
    BeanUtils.copyProperties(entity, dto);
    return dto;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 11:
标题：“万方数据-消费者注册流程”
内容：
- 4.5.1 检查手机号是否已注册
- 4.5.2 生成用户信息
- 4.5.3 保存用户信息
- 4.5.4 返回结果
- 4.5.5 保存用户信息
- 4.5.6 保存用户信息
- 4.5.7 保存用户信息
- 4.5.8 保存用户信息
- 4.5.9 保存用户信息
- 4.5.10 保存用户信息
- 4.5.11 保存用户信息
- 4.5.12 保存用户信息
- 4.5.13 保存用户信息
- 4.5.14 保存用户信息
- 4.5.15 保存用户信息
- 4.5.16 保存用户信息
- 4.5.17 保存用户信息
- 4.5.18 保存用户信息
- 4.5.19 保存用户信息
- 4.5.20 保存用户信息
- 4.5.21 保存用户信息
- 4.5.22 保存用户信息
- 4.5.23 保存用户信息
- 4.5.24 保存用户信息
- 4.5.25 保存用户信息
- 4.5.26 保存用户信息
- 4.5.27 保存用户信息
- 4.5.28 保存用户信息
- 4.5.29 保存用户信息
- 4.5.30 保存用户信息
- 4.5.31 保存用户信息
- 4.5.32 保存用户信息
- 4.5.33 保存用户信息
- 4.5.34 保存用户信息
- 4.5.35 保存用户信息
- 4.5.36 保存用户信息
- 4.5.37 保存用户信息
- 4.5.38 保存用户信息
- 4.5.39 保存用户信息
- 4.5.40 保存用户信息
- 4.5.41 保存用户信息
- 4.5.42 保存用户信息
- 4.5.43 保存用户信息
- 4.5.44 保存用户信息
- 4.5.45 保存用户信息
- 4.5.46 保存用户信息
- 4.5.47 保存用户信息
- 4.5.48 保存用户信息
- 4.5.49 保存用户信息
- 4.5.50 保存用户信息
- 4.5.51 保存用户信息
- 4.5.52 保存用户信息
- 4.5.53 保存用户信息
- 4.5.54 保存用户信息
- 4.5.55 保存用户信息
- 4.5.56 保存用户信息
- 4.5.57 保存用户信息
- 4.5.58 保存用户信息
- 4.5.59 保存用户信息
- 4.5.60 保存用户信息
- 4.5.61 保存用户信息
- 4.5.62 保存用户信息
- 4.5.63 保存用户信息
- 4.5.64 保存用户信息

