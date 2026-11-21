# 画面线理解：16_后端通用封装-通用service-修改方法

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\16_后端通用封装-通用service-修改方法【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:53, 01:29, 02:32, 04:07, 04:41, 05:09, 06:05, 06:49, 07:34, 08:18, 08:51, 09:23, 09:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:09:14

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
