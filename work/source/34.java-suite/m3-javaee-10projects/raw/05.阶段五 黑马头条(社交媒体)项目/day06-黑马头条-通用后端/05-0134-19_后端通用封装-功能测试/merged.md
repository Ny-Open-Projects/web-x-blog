# 19_后端通用封装-功能测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\19_后端通用封装-功能测试【海量资源尽在 666java.com】.mp4
- 时长 8分1秒（音频 482s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲刚才咱们是把后台都已经封装完了那封装完之后下面咱们就用前台启动一下启动完之后咱们可以来先测试一下首先你需要把前台项目给启动了启动完之后你看我后台也启动了两个都启动启动完之后我可以在这去登录咱们的账号是啥悟空是吧密码是123123好点登录
[00:28] 弄完之后呢咱们可以看一下比如说我点用户管理那这个模块我肯定在后台没有开发咱们只开发了什么是开发了当前的一个通用的模块通用的后端是吧好点先看好用不好用啊点数据是不是出来了是吧没问题啊然后再往下看啊看看其他的模块有没有有行不行呢比如说咱们要去看当前的频道哎这个数据是不是也有了是吧
[00:56] 你要相信你自己的眼睛啊这个的确是就是从后台查出来的一会咱们再去调试好吧再去走一遍啊比如说咱们再去看一个敏感词好吧敏感词你看这个是不是也查出来了是吧比如说我想去新增一个啊我想新增一个吧比如说新增一个什么测试好吧测试啊测试好点确定测试是不是上来了我删除了我删除能不能用
[01:26] 删除是不是也好事OK你看我现在目前测的都测完了比如说我想去编辑一下那编辑不就是修改吗加个1呗加个3个1好确定你看是不是修改了比如我再修过来我再改过来好点确定没问题OK这个的确是没有问题你可以检查一下我的代码我代码的确就这么点东西没有太多东西这时候咱们可以去来打断点看看他到底走没走这好吧
[01:57] 咱们可以去随便点哪个都行点频道看是不是到这了是吧没问题比如说我把它放行了放行在这咱们再去点一下谁再点一下敏感词它是不是也到这了是吧它两个肯定走的是同一个Controller的确是同一个Controller但是呢它的参数是不太一样的
[02:23] 那这时候咱们下面就可以去往后去提报一下顺便去回顾一下咱们封装的一个过程好吧比如说咱们先去看当前的这种查询是吧目前的话很明显是一个无条件的查询无条件的列表查询好你可以往下走点进去在这打断点然后让它过来好过来了然后你就看一下当前TTO
[02:49] DTO中的他应该是过传过来的一个表的名称这个表就叫ADCISTIVE是吧当前的敏感词好往下走走他有有查询功能吗咱们这个是有查询功能的对吧好往下然后看他有条件吗这个5月应该是空的5月是没有条件的因为他们现在是没有条件啊好他这时候呢就去把当前的表给拿到了OK这个表名就叫他
[03:15] 然后再往下呢再往下的话就是一些分页的条件设置了啊咱们从零开始是吧然后再往下这是total是吧然后呢再往下看看这个是微空吧微空呢肯定是走这个呀是吧不微空的话有条件才会走下面的呀是吧然后往下走走看这个list就可以了因为他把这个table传进去了然后把这个start零传过去了size默认是10也传过去了所以说这个list就有值了看到了吗list目前只有一条
[03:45] 只有一条有三条有三条有三条有但是目前的话其实应该就是一条他会把这一条数据存到当前一个MAP中看到了吧那是行那咱们下面再往下看这里边应该是一个1应该是1看到了吧最终他就会干嘛呢就会去装到MAP然后最终的是掉了当前的MAP就把这个MAP封装到了当前的Redisbounce的中
[04:13] 这时候咱们前台就能去拿到数据了没有我再走一遍这有可能没反应过来它可能超时了有可能点一下我把这两个都放行都放行了放行好你看这时候数据是不是拿到了没问题这时候咱们再去做一个新增新增的话你看还是在当前的Controller中去打的点这个
[04:43] 很显然他走的是update但是update里边那怎么去判断到底是新增还是修改呀这个DTO中是不是有一个叫什么model啊这个model是不是就能去决定到底是新增还是修改好吧好那咱们来试一下啊比如说我去新增一条测试还是要测试吧我手里啊叫黑马吧好吧黑马头条好点确定好来了你可以看一下DTO啊DTO里边你看
[05:16] 当前modal是不是add是吧没问题那Ware里边咱们有一个值就是id有id然后还有啥还有就是当前的你看当前的这个就是黑马头条看到了吗还有什么还有credit time咱们都已经拿到了好吧现在这时候咱们就可以往下去走了好往下走这吧然后往下走这时候拿到modal是add
[05:47] 拿到位置条件咱们没有条件因为现在是新增新增物业应该是没有条件的然后tab就是当前的他是吧cst就是当前的敏感词然后再往下看因为他这个他这个是一个新增所以说他肯定会走到这好往下走然后他这个位置会空吗肯定是为空的他就会走到这走这之后你可以再往下看好点到这往下走拿到搜扣
[06:16] 我先拿到搜索搜索里边其实没有东西只有一个黑马头条然后是还有一个当前的时间是吧当你当年的时间然后你再往下走再往下走这时候他就会真正的去调用搜索了当然了最终咱们就会去往里边去插入一条数据好这个就结束了好吧行这个数据咱们就算是拿到了咱们好像是没看着是吧没看着就刷信息好
[06:46] 我断点太多了我放行然后点敏感词你看这时候黑马头条是不是就在这啊没问题啊那这个咱们再去测另外一个再测一个再测一个这种测删除吧好吧点一下删除好点断点没打是吧先打断点啊打断点然后点删除确定确定完之后呢你可以往下看啊让我往下看然后这时候DTO里边呢它就是能够
[07:18] 直到我是要去删除了因为这个我本来调用的是删除这个表明他也传过来了你可以看一下这个表明就是他是吧条件的话就是当前的IDID的话值他应该拿到的好吧行然后再往下走拿到virvir的话肯定就是一个ID等于2101然后再往下走走这个没事然后最终会去删除删除完之后咱们就会去叫了一个后制的处理兵是吧最终返回就可以了
[07:48] 行那这个呢其实咱们就测完了咱们顺便呢也把这个接口又算是重新回顾了一遍好吧行那咱们一会儿啊咱们再去分析前端前端它到底是怎么传参数的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在“黑马头条”后台管理系统中，如何通过前端界面操作敏感词管理，并在后端 Java 代码中实现敏感词的增删查改功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 WebStorm 中浏览项目结构，当前选中 `src/main/java/com/heima/admin/components` 目录。
画面2：在浏览器中打开敏感词管理页面，弹出“新增-敏感词”对话框，输入“敏感词”后点击“确定”。
画面3：在浏览器中显示敏感词管理页面，列表为空，显示“共1条”。
画面4：在 IntelliJ IDEA 中调试 `CommonServiceImpl.java`，查看 `list` 方法中 `dto` 对象的属性，其中 `model` 为 "collecting_data"。
画面5：在 IntelliJ IDEA 中调试 `CommonServiceImpl.java`，查看 `list` 方法中 `dto` 对象的属性，其中 `model` 为 "ad_sensitive"。
画面6：在 IntelliJ IDEA 中调试 `CommonServiceImpl.java`，查看 `list` 方法中 `dto` 对象的属性，其中 `model` 为 "ad_sensitive"，`where` 为 "id=1"。
画面7：在浏览器中显示敏感词管理页面，列表为空，显示“共1条”。
画面8：在 IntelliJ IDEA 中查看 `CommonController.java`，显示 `list`、`update`、`delete` 方法的代码。
画面9：在 IntelliJ IDEA 中调试 `CommonController.java`，查看 `delete` 方法中 `dto` 对象的属性，其中 `type` 为 "eq"，`value` 为 "1"。
画面10：在 IntelliJ IDEA 中调试 `CommonServiceImpl.java`，查看 `update` 方法中 `dto` 对象的属性，其中 `model` 为 "add"，`where` 为 "id=1"。
画面11：在 IntelliJ IDEA 中调试 `CommonServiceImpl.java`，查看 `update` 方法中 `dto` 对象的属性，其中 `model` 为 "add"，`where` 为 "id=1"。
画面12：在浏览器中显示敏感词管理页面，弹出“提示”对话框，询问“确定要删除吗？”，并显示“2019-09-27 15:34:23”。
画面13：在 IntelliJ IDEA 中查看 `CommonController.java`，显示 `delete` 方法的代码。
画面14：在 IntelliJ IDEA 中调试 `CommonServiceImpl.java`，查看 `delete` 方法中 `dto` 对象的属性，其中 `model` 为 "ad_sensitive"，`where` 为 "id=1"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```java
@Override
public ResponseResult list(CommonDto dto) {
    if(dto.getPageSize() <= 0) {
        return ResponseResult.errorResult();
    }
    String where = getWhere(dto);
    String tableName = dto.getTableName();
    int start = (dto.getPage() - 1) * dto.getPageSize();
    if(start < 0) {
        start = 0;
    }
    List<String> list = null;
    int total = 0;
    if(StringUtils.isEmpty(where)) {
        list = commonDao.list(tableName, start, dto.getPageSize());
        total = commonDao.listCount(tableName);
    } else {
        list = commonDao.listForWhere(tableName, where, start, dto.getPageSize());
        total = commonDao.listCountForWhere(tableName, where);
    }
    Map<String, Object> map = new HashMap<>();
```

画面5：
```java
int start = (dto.getPage() - 1) * dto.getPageSize();
if(start < 0) {
    start = 0;
}
List<String> list = null;
int total = 0;
if(StringUtils.isEmpty(where)) {
    list = commonDao.list(tableName, start, dto.getPageSize());
    total = commonDao.listCount(tableName);
} else {
    list = commonDao.listForWhere(tableName, where, start, dto.getPageSize());
    total = commonDao.listCountForWhere(tableName, where);
}
Map<String, Object> map = new HashMap<>();
```

画面6：
```java
Map<String, Object> map = new HashMap<>();
```

画面8：
```java
public ResponseResult list(RequestBody CommonDto dto) {
    return commonService.list(dto);
}

@PostMapping("/update")
public ResponseResult update(@RequestBody CommonDto dto) {
    return commonService.update(dto);
}

@PostMapping("/delete")
public ResponseResult delete(@RequestBody CommonDto dto) {
    return commonService.delete(dto);
}
```

画面9：
```java
dto = (CommonDto) toString();
size = 2
page = "add"
model = "ad_sensitive"
name = "collecting_data"
set = CollectingData
```

画面10：
```java
@Override
public ResponseResult update(CommonDto dto) {
    String model = dto.getModel();
    String where = getWhere(dto);
    String tableName = dto.getTableName();
    if("add".equals(model)) {
        if(StringUtils.isEmpty(where)) {
            return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "新增数据不能设置条件");
        } else {
            return addData(dto, tableName);
        }
    } else if(StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "传入的参数值不能为空");
    }
```

画面11：
```java
return ResponseResult.errorResult(AppHttpCodeEnum.NOL_OPERATOR_AUTH);
if(sql == null) {
    return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, "传入的参数值不能为空");
}
int temp = commonDao.insert(tableName, sql[0], sql[1]);
if(temp > 0) {
    doFilter(dto, name);
    dto = CommonDto;
}
return ResponseResult.okResult(temp);
```

画面13：
```java
@PostMapping("/delete")
public ResponseResult delete(@RequestBody CommonDto dto) {
    return commonService.delete(dto);
}
```

画面14：
```java
StringBuffer values = new StringBuffer();
AtomicInteger count = new AtomicInteger();
if(dto.getBeta() != null) {
    dto.getSets().stream().forEach(w -> {
        if(StringUtils.isEmpty(w.getValue())) {
            count.incrementAndGet();
        } else {
            String tempF = parseValue(w.getFiled());
            String tempV = parseValue(w.getValue());
            if(tempF.matches("^\\d+$") && tempF.equals(tempV)) {
                fields.append(",");
                values.append(",");
            }
        }
    });
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

