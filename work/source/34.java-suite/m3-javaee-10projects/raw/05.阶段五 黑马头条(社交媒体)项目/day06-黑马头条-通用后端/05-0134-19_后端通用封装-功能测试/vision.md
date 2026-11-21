# 画面线理解：19_后端通用封装-功能测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\19_后端通用封装-功能测试【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:13, 02:02, 02:50, 03:21, 03:55, 04:21, 04:41, 05:32, 06:04, 06:35, 07:03, 07:30, 07:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:11:54

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
