# 13_后端通用封装-通用service-查询方法2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\13_后端通用封装-通用service-查询方法2【海量资源尽在 666java.com】.mp4
- 时长 6分54秒（音频 414s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下写啊下面你看啊今天那个超新条件拿到了然后还有呢就是你的网名也拿到了但是你进行查询的时候啊其实你还发现还少参数啊今天查询里边是不是有可能会有分页有分页吧所以说这个分页条件呢咱们也要去拿到啊在这写那分页条件该怎么拿呢首先呢咱们是有一个start是吧有一个int startstart等于谁呢
[00:29] 这三个实例啊我们在当前的DTO中啊其实有一个可以拿到一个配置配置呢其实最终你要是直接传配置的话有可能是0所以说咱们应该是有一个算法这个算法大家都知道吧比如说我们要DTO.getPage然后是减去1然后乘以谁乘以DTO中的什么getSize说错了啊.getSize好
[01:00] 这样的话其实就是他起始值是吧要从哪个开始查还要去判断一下啊如果说他为空的话呢小于负一啊在这写一下如果说你判断完之后start然后是小于负一小于负一的话呢咱们就让他等于谁呀start不等于好吧就等于0好了这样的话就算是完了啊这时候呢咱们就可以去查询了查询的话该怎么查询里边啊
[01:32] 一共有四个查询方法到底该叫哪个呢这边有两个一个是带条件的这是没条件的这两个是带条件的那你怎么查呀怎么在这需要去做一个判断判断啥呢StringUtils.isEmpty如果说这张条件的物业为空那就是没有条件然后否则呢那就是有条件呗
[02:04] 这时候就比较容易了这时候咱们就可以去查了第一个common.list这个很显然是没有条件所以说你直接传一个table name然后第二个是start第三个是前的dto中的getSize这样的话就能去查询出来一个list这个list你会发现咱们下面好像也需要是吧
[02:36] 咱们这样啊咱们可以把它给抽出来可以抽出来啊那怎么抽呢好背一下它呢是先等于一个浪可以吧然后最终呢是类似的去接收如果说它也不确定的话你可以写一个问号写一个问号也是可以的这个是查评类别这边还有一个没有条件的时候是不是还有一个打开这个DTO是不是这个也是啊是吧这是没条件的统计
[03:11] 你也应该去查出来啊所以说咱们在这啊也再去加一个啊比如说咱们叫什么int的什么total等于0吧然后这时候呢咱们就可以再去查评一个啊common.listcount然后咱们只需要去传一个table name就完成了啊最终呢咱们就可以去用前的total去接收这样就可以了啊下面呢无非呢就是要多传一些条件啊因为下面是带条件的嘛所以说是
[03:44] comment.tto.listlist for will是吧一个是什么table name第二个呢是will然后第三个呢就是咱们的start第四个是tto.getsizetto.getsize完了啊中呢他也可以用list去接收不是等于好那这样就可以了啊可以看一下当前这个listlist for will
[04:16] 一个是表明啊 二个是表现是吧第三个是起始意那起始的位置是吧然后第三个第四个呢是当前的条数啊好继续往下看下面还有一个total是吧什么呢我们点list count for year是吧一个呢就是table name然后第二个就是位置他不需要分语好吧那这样嗯错了吗
[04:49] 我看看啊他说我这错了int不行count will这一块应该他不应该返回这东西啊他不应该返回一个集合他返回谁啊他应该返回的是当前的一个int啊返回int啊好这呢是加上什么是integer啊这是DAO中写错了大家注意一下啊要是写错的话您稍微改一改这是count啊count返回的肯定是某一个数值类型的啊行那这时候啊咱们改完了改完之后啊
[05:25] 这个事就算做完了然后下面咱们要返回啊那返回的话呢咱们统一的都会返回一个卖然后卖破里边去装当前的利子和头头就可以了好吧行那咱们这啊在这写一下首先是卖破是一个死尊的然后是 object写错了啊我不这个怎么着呢这是先打一包啊好你说这是叫什么呢叫卖破等于你有一个哈西卖吧对吧可以啊
[05:58] 是map.put然后第一个呢咱们就可以把这个list装进去啊好然后是list第二个呢咱们是可以把这个total装进去啊map.put然后是total好呃当然这个就算是装完了装完之后呢咱们最终可以返回返回啊response result.ok然后是把当前的map装进去完了那这个咱们就算是做完了啊
[06:28] 做完之后这一块咱们还要再去加个东西就是我们要在这去用谁后处理的后处理的就是后处理的方法咱们在这才去拖内部那这个没有这个一会咱们会统一去处理这个到底该怎么处理其实咱们还要再去封装一个方法好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中编写并完善一个通用分页查询服务类（CommonServiceImpl）的代码，涉及参数校验、SQL拼装、分页逻辑和返回结果封装。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 2: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 3: 查看 CommonDto.java 文件，其中定义了分页查询的参数类，包含 size、page、model、tableName、where 和 sets 字段。
画面 4: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 5: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 6: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 7: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 8: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 9: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 10: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 11: 在 CommonDao.java 中，查看并编辑了 listForWhere 方法的 SQL 模板，其中包含占位符 #start 和 #size。
画面 12: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 13: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。
画面 14: 在 CommonServiceImpl.java 中，为分页查询方法添加了对页码为 0 的处理逻辑，将 start 设置为 0。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public ResponseResult list(CommonDto dto) {
    if(dto.getTableName().isList()) {
        return ResponseResult.errorResult(ApolloCodeEnum.NO_OPERATOR_AUTH);
    }
    String where = getWhere(dto);
    String tableName = dto.getTableName().name().toLowerCase();
    int start = (dto.getPage()-1)*dto.getSize();
    if(start < 0) {
        start = 0;
    }
    return null;
}
```

画面 3:
```java
package com.heima.model.admin.dtos;

import ...

@Data
public class CommonDto {
    private Integer size;
    private Integer page;
    // 模式式add 新增，编辑
    private String model;
    // 表名的设置
    private CommonTableName name;
    // 查询的条件
    private List<CommonWhereDto> where;
    // 修改的字段
    private List<CommonSetDto> sets;
}
```

画面 5:
```java
public ResponseResult list(CommonDto dto) {
    if(dto.getTableName().isList()) {
        return ResponseResult.errorResult(ApolloCodeEnum.NO_OPERATOR_AUTH);
    }
    String where = getWhere(dto);
    String tableName = dto.getTableName().name().toLowerCase();
    int start = (dto.getPage()-1)*dto.getSize();
    if(start < 0) {
        start = 0;
    }
    commonDao.list(tableName, start, dto.getSize());
    return null;
}
```

画面 6:
```java
public ResponseResult list(CommonDto dto) {
    if(dto.getTableName().isList()) {
        return ResponseResult.errorResult(ApolloCodeEnum.NO_OPERATOR_AUTH);
    }
    String where = getWhere(dto);
    String tableName = dto.getTableName().name().toLowerCase();
    int start = (dto.getPage()-1)*dto.getSize();
    if(start < 0) {
        start = 0;
    }
    List<Map<String, Object>> list = null;
    if(StringUtil.isEmpty(where)) {
        list = commonDao.list(tableName, start, dto.getSize());
    } else {
        list = commonDao.listForWhere(tableName, where, start, dto.getSize());
    }
    return null;
}
```

画面 8:
```java
public ResponseResult list(CommonDto dto) {
    if(dto.getTableName().isList()) {
        return ResponseResult.errorResult(ApolloCodeEnum.NO_OPERATOR_AUTH);
    }
    String where = getWhere(dto);
    String tableName = dto.getTableName().name().toLowerCase();
    int start = (dto.getPage()-1)*dto.getSize();
    if(start < 0) {
        start = 0;
    }
    List<?> list = null;
    int total = 0;
    if(StringUtil.isEmpty(where)) {
        list = commonDao.list(tableName, start, dto.getSize());
        total = commonDao.listCount(tableName);
    } else {
        list = commonDao.listForWhere(tableName, where, start, dto.getSize());
        total = commonDao.listCountForWhere(tableName, where);
    }
    return null;
}
```

画面 11:
```java
Select * from ${tableName} where 1=1 ${where} limit #{start}, #{size}
```

画面 14:
```java
Map<String, Object> map = new HashMap<>();
map.put("list", list);
map.put("total", total);
return ResponseResult.okResult(map);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

