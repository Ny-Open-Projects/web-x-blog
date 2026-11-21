# 15_后端通用封装-通用service-新增方法

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\15_后端通用封装-通用service-新增方法【海量资源尽在 666java.com】.mp4
- 时长 14分44秒（音频 885s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成当前这个update但是你要知道啊update呢update呢它其实是有两个功能是吧两个功能啊新增和修改的修改啊不是修改啊修改的什么通用封装方法这时候呢你怎么去决定怎么去判断当前到底是新增还是修改呢这时候啊这里边有一个字段两个字段还知道吧
[00:28] 当前DTO中是不是有一个叫做modulemodule你看,add是新增,get就是编辑编辑就是修改是吧所以说你在这先通过dto.getmodule然后是拿到一个module然后这时候你就可以去判断了那什么如果说add.exe当前module这时候就是新增不然就是修改那就是修改ok那这会就是
[00:57] 进增的逻辑这一块就是修改的逻辑好吧行那这时候呢咱们呢就可以去真正的去调用在调用之前呢首先呢咱们呃还是得去拿到条件啊还是getware这个咱们直接封装过拿到这个条件这是无印啊然后呢还要拿到这个表名表名怎么拿呀get name点 name点什么咱们要去转上小写是吧最终这个呢就是table name吧
[01:30] 这时候你准备好了这时候咱们还要再去多做一个判断我想问一下新灯需不需要加无约条件新灯需要吗新灯是不是不需要SprintUtilsIsNot如果说这个无约破为空那这时候咱们就直接return什么东西return一个错误就可以了好吧ResponseWithoutTheError然后这里边你就可以去设置APP这里边是参数非法就可以了好吧
[02:00] 当然你可以提示一句话说咱们的新增数据新增数据不能设置条件好吧行然后如果说没有它这个wallet的确是空的那这时候咱们就可以真正的去照用咱们的新增的逻辑再去封装一个方法这时候里边就是一个DTO第二个就是table name
[02:32] 那这个方法没有是吧没有就创建一下啊这个呢其实就是插入插入一条数据封方法这时候咱们还要看啊我想问一下现在啊你就是说你要想去插入你看这个搜索吧还是还是看这个DL打开insertinsert里边呢首先呢他是要有有一个啊table name咱们已经有了然后第二个呢就是当前的什么pyrams
[03:07] 里面有个Fuse就是字段然后第二个就是Values就是还是你的值是吧有值和对应的字段这时候你要拼接两个所以说咱们在这应该是拿到两个值哪两个值呢这时候咱们需要再去封装一个Circle我们再去写一个方法Insert Circle它这个条件就是DTO然后最终它会返回什么东西
[03:35] 返回的就是一个数组数组里边有两部分一个是fuse 一个是values就在这写啊string它这个数组sql就等于它sql两部分啊这数组里边有两部分一个是说了第一个啥第一个是fuse第二个是valuesok行那这时候咱们就可以去写一下这个方法没有是吧没有就创建出来好
[04:05] 这个方法呢就是干嘛的就是连接什么插入的字符好吧行那咱们下面就来去写首先呢嗯首先呢咱们要还是要去准备两个什么呢两个这种字符份啊buffer好吧一个呢是fieldsfields啊等于什么呢stringbuffer又一个stringbuffer错了啊又一个stringbuffer
[04:38] 还要再另外一个string buffer就等于value 4就等于什么呢又一个string buffer好吧那这个准备好了最终咱们在这再去可以去循环了那循环之前咱们还是要做一个判断那什么呢说dto.set4如果说等于那的话咱们再去做循环
[05:04] 就用完之前呢我们在这直接写dto.set4.github.forEach然后是w还是用当前的理由去写写错了啊好这时候呢就能去拿到它对应的值拿到对应的值之前呢咱们还是要再做一步判断啊说啥呢说这个啊你这个里边的值啊你不能就是这样啊打开这个表比如说它有五个字段
[05:35] 它是自断是有了但是某一个值之为空的话这时候呢咱们是不允许的某一个值为空肯定是不允许的所以说咱们在这啊去统计一下怎么统计呢咱们可以在这去加一个东西咱们先去判断吧SpringU2S.isMetal就是说哪个为空呢W.getY6就是说某一个值为空那就有问题那这样啊可以在这去加一个东西加一个AutomicInteger
[06:05] 这个呢就是一个countnew一个automic这个类是干嘛的呢这个类呢就相当于你在这定义了一个int这个increment的get呢就是相当于加加相当于加加它是一个现成安全的啊现成安全的啊你相当于在这定义一个int然后最终呢是每次都要加1有一个我要加1如果说呢咱们后期啊咱们去判断当前那个count如果说它有值
[06:37] 他有值的话说明这个Value是有空的有空的话咱们就不允许或者叫不会正常返回当前这个Circle这能听明白吧好了啊好那下面咱们就来往下写啊如果说往下走如果不会空的话咱们就真正的去迎接咱们的Circle啊现在怎么还是要老方法啊还是要passValue是第一个值呢就是getW.getFields
[07:06] 然后最终是拿到一个什么tmp还是叫tmptmp然后还有一个叫pass.getValue这个就是谁就是Value tmpv拿到之后这时候咱们就可以去拼接可以拼接咱们的src同时要拼接两个同时要拼两个一个是fuse一个是values那好
[07:35] 下面呢咱们就来真正的评计啊那这个大家没有忘记是干嘛的吧这是不是就要来去匹配或者替换当前的一些这种比如说单引号吧百分号或者说注释号吧是吧要去防止circle注入好吧行咱们继续写啊然后下面咱们再去判断一下啊说什么呢说这个什么tempf点f啊f点什么呢
[08:07] 怎么要去让他去先去匹配一下看看有没有数字是吧然后是新好但是不等于了好加一个飞然后最终呢咱们在这啊再加一个咱们之前套路是一样啊说这个temp f那也不能等于谁啊不能等于当前的value好这时候呢咱们才去真正的去拼接搜索啊行那这时候呢你可以直接去拼接vios.open
[08:37] 首先拼接的是第一个谁一个是mpof然后第二个咱们要去拼接拼接什么y64y64是第一个是open的open的啥呢open的比如说咱们要去设置引号因为每一个都要去设置引号下面加一个斜线这时候他去加一个加一个引号那open的这时就是mpov最终你要再去加一个open的什么
[09:07] 引号引号啊好反斜线就是反编译一下啊弄这样就拼接完了啊拼接完了啊那完之后呢这里边啊你看有可能的你这个这个逗号啊有可能没有加上或者说你在第一个值的时候咱们咱们不应该去加这个引号啊所以说呢怎么办呢咱们要处理一下当前这个这个逗号处理一下当前这个逗号那怎么处理呢在这啊
[09:37] 你要去加逗号用每个字段值都要去加逗号比如说你第一个是name然后第二个是password是不是name跟password中间要有一个逗号啊所以说咱们在这去加个逗号啊if fields.length大于0的时候啊咱们再加一个不加一个不加啊fields.png谁呀就是一个好吧啊这个value是一样value是png好那这样就完了啊
[10:09] 中的一个效果呢其实就是什么效果呀他说写写效果啊这效果什么平凡的效果什么呢相当于比如name然后逗号password是吧然后还有什么还有什么比如说你还有什么item是吧记住你的字段值呢值是量啊值是量值呢比如说name是张三当然加引号了啊张三然后呢这是什么密码是123
[10:41] 然后可能后边啊后边可能后边还有其他的值能看明白吧OK啊这是费用资资段然后这个呢是你的virus就是你的值那你说为什么为什么不加括号啊因为括号啊已经在DL中去加上了你看这不是一个括号吗看到了吧所以说啊在这你不用去拼接拼接括号你只要拼接当前这个值就可以好吧行那这个咱们就算了啊最终呢咱们就可以去返回了啊返回的时候这样返回啊
[11:12] 首先呢,我们在这儿去做一个判断一旦它有值,就说明这个V65有空的有空的话允许吗?
[11:19] 不允许所以说在这儿先去做个判断如果说当前那个count.getget就相当于++如果说它大于0说明有值,有空的有空的话咱们就直接return什么了不让它拼接了啊读正常范围就return那就可以了然后呢,然后咱们就可以return什么呢如果说没事啊,咱们就有一个string
[11:42] 然后呢是一个数组我里边放两个值放两个值啊一个值呢就是非优姿点出分然后第二个呢是Values点出分OK那这样就可以了好吧可以了啊然后呢咱们就再可以再回到上面的方法那到这之后呢咱们就可以在这去写了啊就说因为这个circle你已经拿到了啊拿到了然后下面呢咱们就可以再去做判断啊
[12:09] 判断啥呢现在先去判断一个dto.getName.isAdd按它是否包含了Add现在咱们是要做新增吧如果说它不包含如果它没有这个权限的话呢咱们可以直接return一个responseWithoutError说你的权限不足然后是.noOperationAltered好吧你没有权限那下面咱们继续往下看啊还是要判断一下如果说
[12:41] 当前这个circle啊,等于none这时候是不是就没有条件了可能你的value是有空的,咱们返回了一个none这时候呢,我们也可以去返回一个空比如说response,不是返回空,是返回一个错误response result好,点什么error然后呢是什么app说你的参数啊有问题啊有问题咱们可以提示一句话是啥呢说你的传入的参数不能为空
[13:19] 不能未空那说完了啊接着往下看说似乎也没问题那就那就准备那就能信中呗我们也有点影色然后第一个是一波内幕了咱们传过来了是吧第二个呢那个其实就是你的费用咱们刚才第一个啊王这个王当前的数据中第一个放上第一个放是不是费用死的所以说你可以在这搜扣零
[13:53] 0的话不就是fuse吗第二个呢是circle1就是values是吧最终它会返回一个呃叫影响的值吧咱们叫temp好吧那最终呢咱们就可以在这去不用do filter了啊首先呢咱们temp如果说它真正的去查了或者真正的去新增了我们就可以do filter把当前dto放进去然后第二个呢是add好吧是按照方法吧好
[14:23] 没事咱们最终就可以return什么呢return一个response withoutresponse withoutROP太不好做事了好吧目前的话呢这个新增的就完了一会呢咱们再去完成当前修改的这个逻辑

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 Spring Boot 项目中，如何在 CommonService 中实现通用的增删改查（CRUD）逻辑，特别是通过动态 SQL 构建和条件判断来处理不同操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 CommonDto 类的定义，包含 size、page、model、name、where、sets 等字段，用于封装通用查询参数。
画面 2: 展示 CommonServiceImpl 中的 update 方法，通过 model 字段判断是新增还是修改，并调用 getWhere 方法获取条件。
画面 3: 展示 update 方法中，如果 model 为 "add"，则调用 addData 方法；否则返回 null。
画面 4: 展示 CommonServiceImpl 中的 delete 方法，目前仅返回 null，后续将实现删除逻辑。
画面 5: 展示 CommonServiceImpl 中的 addData 方法，用于构建插入 SQL。
画面 6: 展示 addData 方法中，导入了必要的工具类如 StringUtils、StringBuilder、AtomicInteger 等。
画面 7: 展示 addData 方法中，定义了用于构建 SQL 的 StringBuffer 对象。
画面 8: 展示 addData 方法中，对 dto.getSets() 进行流式处理，遍历 sets 字段并构建 SQL。
画面 9: 展示 addData 方法中，对 sets 字段进行处理，如果字段值不为空，则构建对应的 SQL 语句。
画面 10: 展示 addData 方法中，对 sets 字段进行处理，如果字段值不为空，则构建对应的 SQL 语句。
画面 11: 展示 addData 方法中，对 sets 字段进行处理，如果字段值不为空，则构建对应的 SQL 语句。
画面 12: 展示 addData 方法中，对 sets 字段进行处理，如果字段值不为空，则构建对应的 SQL 语句。
画面 13: 展示 addData 方法中，调用 commonDao.insert(sql) 方法执行插入操作。
画面 14: 展示 update 方法中，如果 model 不是 "add"，则调用 addData 方法；否则返回 null。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.heima.model.admin.dto;
import ...
public class CommonDto {
    private Integer size;
    private Integer page;
    // 操作类型：add 新增，edit 编辑
    private String model;
    // 操作的对象
    private String tableName;
    // 重要的条件
    private List<CommonWhereDto> where;
    // 修改的字段
    private List<CommonWhereDto> sets;
}
```

画面 2:
```java
@Override
public ResponseResult update(CommonDto dto) {
    String model = dto.getModel();
    String where = getWhere(dto);
    dto.setTableName(dto.getTableName().toLowerCase());
    if("add".equals(model)) {
        return addData(dto, tableName);
    } else {
        return null;
    }
}
```

画面 3:
```java
@Override
public ResponseResult update(CommonDto dto) {
    String model = dto.getModel();
    String where = getWhere(dto);
    dto.setTableName(dto.getTableName().toLowerCase());
    if("add".equals(model)) {
        if(StringUtils.isNotBlank(where)) {
            return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "新增数据不能有where条件");
        } else {
            return addData(dto, tableName);
        }
    } else {
        return null;
    }
}
```

画面 4:
```java
@Override
public ResponseResult delete(CommonDto dto) {
    return null;
}
```

画面 5:
```java
@Override
public ResponseResult addData(CommonDto dto, String tableName) {
    String sql = "";
    if(StringUtils.isBlank(tableName)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "表名不能为空");
    }
    // 构建插入语句
    String insertSql = getInsertSql(dto, tableName);
    if(StringUtils.isBlank(insertSql)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "SQL语句不能为空");
    }
    return commonDao.insert(insertSql);
}
```

画面 6:
```java
private ResponseResult addData(CommonDto dto, String tableName) {
    String sql = "";
    if(StringUtils.isBlank(tableName)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "表名不能为空");
    }
    // 构建插入语句
    String insertSql = getInsertSql(dto, tableName);
    if(StringUtils.isBlank(insertSql)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "SQL语句不能为空");
    }
    return commonDao.insert(insertSql);
}
```

画面 7:
```java
private String getInsertSql(CommonDto dto, String tableName) {
    StringBuffer fields = new StringBuffer();
    StringBuffer values = new StringBuffer();
    AtomicInteger count = new AtomicInteger();
    if(dto.getSets() != null) {
        dto.getSets().stream().forEach(w -> {
            if(StringUtils.isNotBlank(w.getValue())) {
                count.incrementAndGet();
            }
        });
    }
    if(count.get() == 0) {
        return null;
    }
    return "INSERT INTO " + tableName + " (" + fields.toString() + ") VALUES (" + values.toString() + ")";
}
```

画面 8:
```java
private String getInsertSql(CommonDto dto, String tableName) {
    StringBuffer fields = new StringBuffer();
    StringBuffer values = new StringBuffer();
    AtomicInteger count = new AtomicInteger();
    if(dto.getSets() != null) {
        dto.getSets().stream().forEach(w -> {
            if(StringUtils.isNotBlank(w.getValue())) {
                count.incrementAndGet();
            }
        });
    }
    if(count.get() == 0) {
        return null;
    }
    return "INSERT INTO " + tableName + " (" + fields.toString() + ") VALUES (" + values.toString() + ")";
}
```

画面 9:
```java
private String getInsertSql(CommonDto dto, String tableName) {
    StringBuffer fields = new StringBuffer();
    StringBuffer values = new StringBuffer();
    AtomicInteger count = new AtomicInteger();
    if(dto.getSets() != null) {
        dto.getSets().stream().forEach(w -> {
            if(StringUtils.isNotBlank(w.getValue())) {
                count.incrementAndGet();
            }
        });
    }
    if(count.get() == 0) {
        return null;
    }
    return "INSERT INTO " + tableName + " (" + fields.toString() + ") VALUES (" + values.toString() + ")";
}
```

画面 10:
```java
private String getInsertSql(CommonDto dto, String tableName) {
    StringBuffer fields = new StringBuffer();
    StringBuffer values = new StringBuffer();
    AtomicInteger count = new AtomicInteger();
    if(dto.getSets() != null) {
        dto.getSets().stream().forEach(w -> {
            if(StringUtils.isNotBlank(w.getValue())) {
                count.incrementAndGet();
            }
        });
    }
    if(count.get() == 0) {
        return null;
    }
    return "INSERT INTO " + tableName + " (" + fields.toString() + ") VALUES (" + values.toString() + ")";
}
```

画面 11:
```java
private String getInsertSql(CommonDto dto, String tableName) {
    StringBuffer fields = new StringBuffer();
    StringBuffer values = new StringBuffer();
    AtomicInteger count = new AtomicInteger();
    if(dto.getSets() != null) {
        dto.getSets().stream().forEach(w -> {
            if(StringUtils.isNotBlank(w.getValue())) {
                count.incrementAndGet();
            }
        });
    }
    if(count.get() == 0) {
        return null;
    }
    return "INSERT INTO " + tableName + " (" + fields.toString() + ") VALUES (" + values.toString() + ")";
}
```

画面 12:
```java
private String getInsertSql(CommonDto dto, String tableName) {
    StringBuffer fields = new StringBuffer();
    StringBuffer values = new StringBuffer();
    AtomicInteger count = new AtomicInteger();
    if(dto.getSets() != null) {
        dto.getSets().stream().forEach(w -> {
            if(StringUtils.isNotBlank(w.getValue())) {
                count.incrementAndGet();
            }
        });
    }
    if(count.get() == 0) {
        return null;
    }
    return "INSERT INTO " + tableName + " (" + fields.toString() + ") VALUES (" + values.toString() + ")";
}
```

画面 13:
```java
private String getInsertSql(CommonDto dto, String tableName) {
    StringBuffer fields = new StringBuffer();
    StringBuffer values = new StringBuffer();
    AtomicInteger count = new AtomicInteger();
    if(dto.getSets() != null) {
        dto.getSets().stream().forEach(w -> {
            if(StringUtils.isNotBlank(w.getValue())) {
                count.incrementAndGet();
            }
        });
    }
    if(count.get() == 0) {
        return null;
    }
    return "INSERT INTO " + tableName + " (" + fields.toString() + ") VALUES (" + values.toString() + ")";
}
```

画面 14:
```java
@Override
public ResponseResult update(CommonDto dto) {
    String model = dto.getModel();
    String where = getWhere(dto);
    dto.setTableName(dto.getTableName().toLowerCase());
    if("add".equals(model)) {
        return addData(dto, tableName);
    } else {
        return null;
    }
}
```

4) 出现的 PPT 标题

