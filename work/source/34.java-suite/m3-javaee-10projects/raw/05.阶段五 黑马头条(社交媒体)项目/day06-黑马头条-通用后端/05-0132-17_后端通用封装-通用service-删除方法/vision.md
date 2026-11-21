# 画面线理解：17_后端通用封装-通用service-删除方法

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\17_后端通用封装-通用service-删除方法【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:28, 00:38, 00:57, 01:16, 01:30, 01:41, 01:50, 02:06, 02:19, 02:30, 02:52, 03:00, 03:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:10:11

1) 这一组画面整体在讲什么（一句话）：
演示在 IntelliJ IDEA 中为 CommonService 的 delete 方法添加参数校验和 SQL 语句生成逻辑，涉及使用 StringUtils、ApptHttpCodeEnum 和 CommonDao。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 CommonServiceImpl.java 中 updateData 方法，其中包含对 dto.sets 的校验和调用 commonDao.update。
画面 2: 在 updateData 方法中，光标位于 return null; 行，弹出的代码补全建议显示了 CommonServiceImpl 类的成员方法。
画面 3: 光标移动到 delete 方法的开头，弹出的代码补全建议显示了 CommonServiceImpl 类的成员方法。
画面 4: 光标位于 delete 方法的 if (count.get() > 0) { return null; } 语句块中，弹出的代码补全建议显示了 CommonServiceImpl 类的成员方法。
画面 5: 展示 delete 方法的开头部分，光标位于 if (dto.getIsList()) { return null; } 语句块中。
画面 6: 光标位于 delete 方法的 if (dto.getIsList()) { return null; } 语句块中，弹出的代码补全建议显示了 ApptHttpCodeEnum 的常量。
画面 7: 光标位于 delete 方法的 if (StringUtils.isEmpty(where)) { return ResponseResult.errorResult(...); } 语句块中。
画面 8: 光标位于 delete 方法的 if (StringUtils.isEmpty(where)) { return ResponseResult.errorResult(...); } 语句块中，弹出的代码补全建议显示了 ResponseResult 类的静态方法。
画面 9: 光标位于 delete 方法的 if (StringUtils.isEmpty(where)) { return ResponseResult.errorResult(...); } 语句块中，弹出的代码补全建议显示了 CommonDao 类的成员方法。
画面 10: 光标位于 delete 方法的 if (StringUtils.isEmpty(where)) { return ResponseResult.errorResult(...); } 语句块中，弹出的代码补全建议显示了 CommonDao 类的成员方法。
画面 11: 光标位于 delete 方法的 if (StringUtils.isEmpty(where)) { return ResponseResult.errorResult(...); } 语句块中，弹出的代码补全建议显示了 CommonDao 类的成员方法。
画面 12: 光标位于 delete 方法的 if (StringUtils.isEmpty(where)) { return ResponseResult.errorResult(...); } 语句块中，弹出的代码补全建议显示了 CommonDao 类的成员方法。
画面 13: 展示 CommonServiceImpl.java 中的 private String parseValue(String filed) 方法，用于处理 SQL 中的特殊字符。
画面 14: 展示 CommonServiceImpl.java 中的 public ResponseResult list(CommonDto dto) 方法，用于分页查询数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
private ResponseResult updateData(CommonDto dto, String tableName, String where) {
    String sets = getSets(dto);
    if (dto.getIsUpdate()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(sets)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "修改的参数值不能为空");
    }
    int temp = commonDao.update(tableName, where, sets);
    return null;
}
```

画面 2:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 3:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 4:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 5:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 6:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 7:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 8:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 9:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 10:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 11:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 12:
```java
public ResponseResult delete(CommonDto dto) {
    String where = getWhere(dto);
    String tableName = dto.getTableName().toLowerCase();
    if (dto.getIsList()) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    if (StringUtils.isEmpty(where)) {
        return ResponseResult.errorResult(AppHttpCodeEnum.PARAM_INVALID, errorMessage: "删除条件不能为空");
    }
    int temp = commonDao.delete(tableName, where);
    return null;
}
```

画面 13:
```java
private String parseValue(String filed) {
    if (StringUtils.isNotBlank(filed)) {
        return filed.replaceAll("regex: \"(\\d{1,2})\\.(\\d{1,2})\"", "");
    }
    return filed;
}
```

画面 14:
```java
public ResponseResult list(CommonDto dto) {
    if (dto.getIsList()) {
