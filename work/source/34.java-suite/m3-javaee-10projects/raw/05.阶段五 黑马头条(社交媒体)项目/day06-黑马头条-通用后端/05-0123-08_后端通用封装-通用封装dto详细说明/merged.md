# 08_后端通用封装-通用封装dto详细说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\08_后端通用封装-通用封装dto详细说明【海量资源尽在 666java.com】.mp4
- 时长 6分47秒（音频 407s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来针对于这些类啊这些类呢咱们再再去简单说一说啊一个一个的去过看看里边到底有什么东西好吧首先呢咱们要过上面这三个这三个啊下面这些类呢咱们是一会去写啊上面这三个已经定义完了咱们简单再去理解一下好吧首先呢咱们打开当前的这种model啊这个model里边啊model里边呢是有一个包这个包是叫admin找到admin啊admin里边有个dtos
[00:29] 这里边有首先呢咱们要看第一个啊嗯先看这个吧先看下面的enumerance啊先先看enumerance里边有一个comment table enumerance那这个呢其实刚才说了这个类主要干嘛的呢这个类呢就可以定义到底是哪个表需要进行增长改查哪个表你看啊目前的话呢目前一些内容比如说adadsistive是吧什么adarticle还有什么那就是ap啊
[00:59] AEP article config还有什么AEP user这些像这些呢都是一些表都在这已经定义好的表那我对这些表要干嘛呢对这些表啊你看这里边是第一个呢是叫field是所有的字段是吧然后是干嘛呢true true true这什么意思你看这啊事实上呢是否列表是否开启列表开启列表的话就是是否查询那是否需要去新增是否需要修改
[01:28] 和是否需要删除那目前你看目前的话这个频道的频道是需要去增加改查都可以当前这个敏感词呢也是增加改查都可以但是当前这个文章的话我只让你干嘛呢只让你查询当前这个文章的配置也是只让查询用户是啥呢你看用户不一样啊用户是我让你查我还可以干嘛呢我还可以让你改但是你不能新增和不能删除能看明白吧
[01:58] 但你说我想再加OK那你可以在这再加去加就可以了是这个对应关系大家一定要知道当前这个ADChannel可不是随便写的当前那个AD什么CST也不是随便写的这个应该或应当对应上你自己的表这个表呢其实就是你对应的表名称比如说叫ADChannel你看我这是不是AD-下滑线Channel啊
[02:25] 比如说你要再去设置一个什么ADManual那你必须的是叫当前的根据表明是一致才行能听明白吧好了啊行那这个呢咱们刚才就说了一下啊这个类或者当前这个美举类就是来干这个事的好这是来主要是定义表和它的一些权限好还有一个类啊咱们看当前这个类叫CommonWearDTO
[02:50] 那这个类呢就是有三个字段啊这三个字段也很好理解啊第一个呢是比如说啊你看VM就是条件那这个field呢就是字段名称字段名称然后这个value呢就是字段的值比如说你要去查询一个查询一个用户的按照名称去查询并且是等于那这时候呢咱们就可以说当前的name这个field就是name啊然后呢等于就是EQ等于就是EQ
[03:19] 只是啥呢?
[03:20] 只是小明OK那这个Value就是小明好吧但是这个Type的话就是它的一个查询的方式或者叫设置的方式但这个Type的咱们后期会封装的时候呢会设置三个当然你也可以增加这三个是哪三个呢?
[03:35] 默认它是等于咱们也可以设置比如说Like咱们可以模糊还有Between咱们可以按照范围查询咱们都可以去设置比如说你再有需求我按照大于啊小于啊不等于啊
[03:48] 咱们都可以进行查询都可以进行低于当下的type去设置值好吧默认值是EQEQ就是等于好吧那行那这个咱们就说完了说完之后下面是有一个commonDTO那这个DTO我来看一下前面有几个属性第一个是size配置这个都知道这就是分页插均的条件对吧那下面还有个modulemodule是啥意思呢
[04:18] 刚才说了啊因为咱们呢在去封装Service的时候common Service就是通用到Service的时候呢咱们新增和修改啊是一个是一个方法这时候呢咱们要通过model通过model来区分到底是新增还是修改通过model啊这时候你要去多传一个值也就是说啊你新增和修改的时候你要往从前在往后传传的时候要传一个model过来来区分到底是新增还是修改好吧然后下面呢还有一个值就是说你
[04:48] 最终要去操作哪个表啊哪个表是不是comment table里边comment table英文里边是不是有啊OK啊那这个呢就是你要去对应上你当前的名称才行比如说我传一个AD channel过来那我就知道你要操作的是当前的频道表好吧你要传一个它那就那我就设置谁啊那就设置对当前的敏感词的一些增长改差
[05:13] 好再往下看你生产改查的时候可能会在一些条件比如插群有一个无约条件这个条件通通都封装到当前的这个里边并且是一个粒子集合因为有可能是有多个条件common-will-tto大家要再回顾一下里边就三个值一个是field一个是type还有个value好当然这里边还有修改字段修改字段的话因为它这个修改字段是这样有可能是有多个是吧咱们也可以通过当前这种方式
[05:42] 去设置set值它还是当前的这种方式啊field type和value当然这个是where这个是set大家一定要区分当然这个只有在修改的时候才会用得着咱们大部分都应该是用的是where好吧行那这个呢就是一个common DTOOK那这三个类啊大家呢在科下的时候啊应该要重点去看一下这三个类并且知道它们的关系
[06:10] 这关系的话是这样啊这个是封装表是吧并且是操作一些表的权限这个呢是针对于某些字段它进行怎么查询应该这样说啊这里边封装了字段和值然后字段和值的关系因为它到底是like还是等于还是说不等于还是说什么范围是吧最终这个common DTO呢是封装了它两个
[06:34] 并且呢咱们要去在里边去引用当前这个表还有你的一些条件值当然他还有自己的一些条件好吧行那这个啊这几个类啊大家重点去看一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解后台管理系统中通用的 CRUD 操作相关类的定义与实现，包括枚举、DTO、DAO 等核心组件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程文档中关于 CommonTableEnum、CommonWhereDto、CommonDao 等类的说明，重点介绍 CommonTableEnum 的作用和定义。
画面 2: 展示了项目结构，当前选中的是 heima-leadnews-model 模块。
画面 3: 展示了 CommonTableEnum.java 文件内容，其中定义了 AD_CHANNEL、AD_SENSITIVE、AP_ARTICLE 等枚举常量及其布尔值。
画面 4: 展示了 MySQL 数据库中 ad_sensitive 表的 DDL 创建语句。
画面 5: 展示了 CommonTableEnum.java 文件内容，其中定义了 AP_ARTICLE_CONFIG、AP_USER 等枚举常量及其布尔值。
画面 6: 展示了 CommonWhereDto.java 文件内容，其中定义了 filed、type、value 三个私有属性。
画面 7: 展示了 CommonDto.java 文件内容，其中定义了 size、page、model、name、where、sets 等私有属性。
画面 8: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 9: 展示了 CommonWhereDto.java 文件内容，其中高亮显示了 filed、type、value 三个属性。
画面 10: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 11: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 12: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 13: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 14: 展示了 CommonDto.java 文件内容，其中高亮显示了 model 属性。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
• CommonTableEnum: 适用于定义哪些数据表可支持通用操作，及其开发的 CRUD 功能
• CommonWhereDto: 用于接收前端传入的将字段名或者查询条件参数
• CommonDto: 用于接收前端传入的接口参数（包括 CRUD 的接口参数）
• CommonServiceImp: 实现通用端口的控制定义
• BaseCommonFilter: 定义后台处理的接口方法（后置增加的BeanName定义为CommonTableEnum名称即可）
```
画面 3:
```
@Getter
public enum CommonTableEnum {
    AD_CHANNEL("**",true,true,true,true),
    AD_SENSITIVE("**",true,true,true,true),
    AP_ARTICLE("**",true,false,false,false),
    AP_ARTICLE_CONFIG("**",true,false,true,false),
    AP_USER("**",true,false,true,false),
}
```
画面 4:
```
CREATE TABLE `ad_sensitive` (
  `id` int(11) NOT NULL COMMENT '主键',
  `sensitivities` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '敏感词',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `idx_sensitivities` (`sensitivities`),
  KEY `idx_created_time` (`created_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='敏感词信息表';
```
画面 6:
```
package com.heima.model.admin.dtos;
import lombok.Data;
public class CommonWhereDto {
    private String filed;
    private String type="eq";
    private String value;
}
```
画面 7:
```
package com.heima.model.admin.dtos;
import lombok.Data;
public class CommonDto {
    private Integer size
    private Integer page
    private String model,
    // 操作的对象
    private CommonTableEnum name
    // 实际的条件
    private List<CommonWhereDto> where,
    // 修改的字段
    private List<CommonWhereDto> sets;
}
```
画面 14:
```
private String model
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

