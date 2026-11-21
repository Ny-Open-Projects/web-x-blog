# 16_后端通用封装-通用service-修改方法

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\16_后端通用封装-通用service-修改方法【海量资源尽在 666java.com】.mp4
- 时长 10分0秒（音频 600s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来完成当前这个修改啊刚才咱们已经把这个新增给完成了啊那修改的逻辑呢它也是跟这个新增是差不多啊要应该这样说吧应该是比新增要还要简单一些啊好那咱们在这一块还要再再判断一下那这个判断啥呢这还是判断当前这个vr那你说修改的时候那你说vr到底是还是没有呢这样说是吧如果说它为空的话啊如果说它为空的话应该是
[00:28] 这个修改的话肯定得有条件对吧比如说咱们在这直接按入到为空直接response without然后点 ever就说是说一个错误还是当前这个错误但是你可以提示一句话提示的是说那就是修改条件不能为空好吧然后咱们就可以真正的去修改了
[01:00] 好在这呢咱们可以再去封装一个方法方法呢是叫什么update好吧这里边参数呢就是以前的dto还有一个呢是以前的table好这里边还有一个啊咱们还要再去设置一个就是以前的Vue因为它多了一个Vue的条件是吧加上之后啊咱们在这就可以去创建当前这个方法好这个呢就是来去运接咱们的修改
[01:32] 这是更新啊更新更新一条数据好下面呢咱们就可以真正的去做修改了啊做修改之前呢首先呢你还得去拿到它的这种拼接的思考刚才呢咱们在做新增的时候啊在做新增的时候这个里边这里边啊它是不是要去返回一个同时咱是不是要拼接当前的新增的思考那时候它返回的是两个因为它需要返回它的字段
[02:02] 给打开啊返回他的字段啊字段和他的值是吧所以说这是个数组那这时候咱们再去封装的时候那这块内容呢就是只需要返回一个就可以返回一个比如说咱们可以拿到什么呢赛特斯赛特斯根据当前的DTO反回的是谁啊返回的是一个反回的是一个死镇的叫什么赛特斯它是一个不是一个数组
[02:37] 那咱们这个你可以把它给念出来这个就是去干嘛呢要去进修改语句update语句吧update语句好吧其实这里边也不是说拼接语句咱们要去拼接的是这些条件看前的DTO流转你看修改打开的修改修改的里边你看
[03:05] 首先这一块是有一个v是吧然后是有一个set其实你看看这个速度预计就可以了set火辈你说那你说咱们该怎么写是不是这么这么写法内幕啥啥啥是吧值然后奏号然后再有你的再有你的字段等于你的值最后是有个v的条件对吧那这v咱们已经有了那这时候咱们只需要去拿当前的这段就可以了
[03:31] 好吧行那这个思路有了啊那之后呢咱们在这就可以去写咱们的或者拼接咱们的这种嗯条件的参数啊这个拼接呢其实跟刚才是跟刚才那个新增的是类似啊只说类似好那这时候咱们去拼接写一下啊咱们在这啊再去放进一个死正八分怎么办啊怎么叫赛特斯仿余什么呢你有一个死正
[03:56] 然后下面咱们再去创建一个这种统计的一个类叫automicdto msinteger然后它们叫count等于new一个什么automicinteger是吧行拿到之后咱们就可以拼条件了拼条件之前咱们还是要做一个判断比如说dto它呢-set4等于
[04:33] 等于那的时候呢咱们就可以往下去做了比如说dto.getset4然后呢是.stream可以循环嘛.forEach然后是w咱们就这么写啊好拿到之后呢这时候呢咱们还是要去做一个平转啊如果说刚才这个值啊为空的话那这时候咱们还要去看了一下啊统计一下stream.utostarisempted然后呢就是w.get
[05:02] 如果说一旦有一个为空的话咱们就直接去放它一下点increment按那什么好就相当于加加啊好如果说这时候啊这时候咱们如果他没有的话咱们就可以干嘛呢一二SE是吧我可以去运接我们的参数了啊那还是老套路啊首先呢我们还是要pass然后是w.get field这个呢就是谁啊这就是当前的一个字段是吧
[05:32] string time.f然后下面还有一个是吧回一下啊get value这是value啊这是ray好吧下面咱们就可以真正的去拼接了啊然后还要再去判断真的话就是等于啊time.f它呢match咱们先去判断一下当前的这个有没有数字是吧然后呢还有一个是当前的
[06:04] temp.f你不能等于谁不能等于这个值防止screw下面咱们就拼接拼接的方式就比较简单了set.opendopend什么首先第一个就是当前的值f是吧然后是点下面点什么opend然后这个段下面是不是等于所以说咱们在这去拼接一个
[06:35] 挡鱼的时候咱们在这还要再去后边再去加个引号是吧所以说咱们在这直接就写个斜线这时候就反应了然后是下面是open的然后去加它的值然后最后你再把引号把它引上就可以了然后是引号前面加一个斜线好吧这时候说完之后这个是不是要有多次段的话不再循环吗
[07:06] 要有多个字段的话咱们是不是要与逗号隔开还是以前的那种思路如果说当前setSlith大于0的时候我们再去加一个什么setSlpend然后是加一个号第一个不加往后都要去加好吧这个咱们就拼完了拼完之后咱们在这还要再去判断一下if如果countLget有值的话对0
[07:39] 那咱们就直接return一个,那就可以了好吧如果没事,没事的话咱们就直接return一个什么东西return,直接return当前set 4.2 string就可以了好吧这个啊这个我们这个serve就算是连接完了啊好那咱们就往上走啊好那这个呢咱们条件已经拿到了拿到之后呢咱们下面呢就可以去发请求了啊发请求呢咱们还是要去做一些判断啊首先呢你要判断一下当前
[08:09] dto.getlimb然后点什么update看他有没有update的权利是非啊如果他没有的话怎么办呢没有就return 什么呢还是response然后还是说你的权限不足点no operation author然后再往下再去判断一个如果说当前的stu2
[08:41] 意思是谁未空呢set 4未空如果set 4未空的话条件就不够呗是吧所以说咱们在这直接去returnreturn response result error还是error啊然后你说你的参数有问题啊好咱们在这去继续一句话说修改的参数修改的参数值不能未空好吧继续啊
[09:11] 然后到这的话咱们就可以真正的去发请求了comment do.2然后是update第一个是table name第二个呢是咱们的weir三个呢是咱们的set4用它为返回来一个temp吧那是影响的条数啊那这时候呢咱们还要干嘛呢还要再去判断一下是吧如果说真正的去temp真有值的话就说明他真的去发送了请求
[09:40] 这时候咱们可以去测一下然后呢这个还是dq然后第二个呢这个值你可以随便改啊比如叫update哇然后呢下面就是return什么response result.o我把当前这个time放进去完事了哇行那目前这个修改啊咱们就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在 IntelliJ IDEA 中，开发人员正在为一个通用的更新数据方法（updateData）编写和调试 Java 代码，重点是处理参数校验、构建 SQL 更新语句并调用数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 CommonServiceImpl.java 文件中 update 方法的开头部分，其中包含对 dto 的字段校验和表名处理。光标位于方法体末尾的 return null; 语句。
画面 2: 光标移动到 update 方法内部，显示了对 where 条件的校验逻辑，如果 where 为空则返回错误信息“修改条件不能为空”。
画面 3: 光标跳转到 update 方法内部的 else 分支，显示了调用 updateData 方法的语句。
画面 4: 光标位于 updateData 方法的参数声明处，显示了方法签名和注释。
画面 5: 光标位于 updateData 方法内部，显示了调用 getSets 方法获取 SQL 设置语句的代码。
画面 6: 光标位于 getSets 方法内部，显示了初始化 StringBuffer 和 AtomicInteger 的代码。
画面 7: 光标位于 getSets 方法内部，显示了对 dto.getSets() 的 stream 进行遍历，统计非空字段数量。
画面 8: 光标位于 getSets 方法内部，显示了对非空字段值进行处理，使用正则表达式匹配并拼接 SQL 字符串。
画面 9: 光标位于 getSets 方法内部，显示了将拼接好的 SQL 字符串追加到 StringBuffer 中。
画面 10: 光标位于 getSets 方法内部，显示了调用 commonDao.update 方法的语句，但提示缺少导入。
画面 11: 光标位于 updateData 方法内部，显示了调用 commonDao.update 方法的语句，但提示缺少导入。
画面 12: 光标位于 updateData 方法内部，显示了调用 commonDao.update 方法的语句，但提示缺少导入。
画面 13: 光标位于 updateData 方法内部，显示了调用 commonDao.update 方法的语句，但提示缺少导入。
画面 14: 光标位于 updateData 方法内部，显示了调用 commonDao.update 方法的语句，但提示缺少导入。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public ResponseResult update(CommonDto dto) {
    String model = dto.getModel();
    String tableName = dto.getTableName().toLowerCase();
    String where = dto.getWhere();
    if (StringUtils.isEmpty(model)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "新增数据不能设置空");
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "修改条件不能为空");
    }
    return updateData(dto, tableName, where);
}
```

画面 2:
```java
if (StringUtils.isEmpty(where)) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "修改条件不能为空");
}
```

画面 3:
```java
else {
    return updateData(dto, tableName, where);
}
return null;
```

画面 4:
```java
private ResponseResult updateData(CommonDto dto, String tableName, String where) {
```

画面 5:
```java
String sets = getSets(dto);
```

画面 6:
```java
private String getSets(CommonDto dto) {
    StringBuffer sets = new StringBuffer();
    AtomicInteger count = new AtomicInteger();
    if (dto.getSets() != null) {
        dto.getSets().stream().forEach(w -> {
            if (StringUtils.isEmpty(w.getValue())) {
                count.incrementAndGet();
            }
        });
    }
```

画面 7:
```java
if (dto.getSets() != null) {
    dto.getSets().stream().forEach(w -> {
        if (StringUtils.isEmpty(w.getValue())) {
            count.incrementAndGet();
        }
    });
}
```

画面 8:
```java
else {
    String temp = parseValue(w);
    String temp1 = parseValue(w);
    if (temp1.matches("^(\\d+)$")) {
        sets.append(temp).append(" ").append(" ");
    }
}
```

画面 9:
```java
sets.append(temp).append(" ").append(" ");
```

画面 10:
```java
commonDao.update(tableName, where, sets);
```

画面 11:
```java
commonDao.update(tableName, where, sets);
```

画面 12:
```java
commonDao.update(tableName, where, sets);
```

画面 13:
```java
commonDao.update(tableName, where, sets);
```

画面 14:
```java
int temp = commonDao.update(tableName, where, sets);
if (temp > 0) {
    doFilter(dto, name: "update");
}
return ResponseResult.success();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

