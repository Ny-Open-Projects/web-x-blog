# 17_后端通用封装-通用service-删除方法

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\17_后端通用封装-通用service-删除方法【海量资源尽在 666java.com】.mp4
- 时长 3分14秒（音频 194s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那修改做完之后咱们这里边还有一个方法这个给它删了不要了这里边还有一个叫做delete找到那个删除的方法这个方法相对来说就比较简单了因为咱们该封装的都已经封装了在这咱们可以直接去写这个是通用的封装通用的什么通用的删除方法好吧在这写首先咱们还是要去拿到当前的Wire
[00:29] 然后是DTO因为他这个删除是要有条件的啊再往下啊我们可以拿到他的一个什么名称就是表名点什么set name点name应该是啊什么呢咱们把这个前的啊小写好这是table name好然后再往下呢咱们就可以去判断啊当前的表啊具不具有前的删除的功能
[01:03] dto.什么咱们可以直接去直接去getName.getName.isDelete看看它有没有删除的权限然后如果说它没有直接返回response.error还是没有权限这个大家都写的烦了是吧再写下最后一个了.noOperation Author再往下看
[01:35] 放下去判断一个现在这个vr也不能为空说你的string utils.isEmpty然后是vr它为空的话咱们也可以去返回返回你的错误然后这里边是你的参数有问题你可以提示一句话提示什么呢说删除条件不合法删除条件不合法好
[02:04] 都没事,那咱们就可以去调用TO去删除一个是tableName,第二个是无印完了,最终它会返回一个这种影响的函数还是老套路,咱们还是要去调一下他们的后处理品所以说在这,真正去影响的时候tmp大于0然后就可以去调toFiltertoFilter,一个是DTO第二个就是你的一个字幕串
[02:34] delete好吧行最终呢我们就可以去返回了这是什么response result然后是把这个temp进去
[02:48] 好了那这个呢咱们就算是绒装完了啊到目前的话呢咱们这个所有的增删改查的方法呢咱们就绒装到这啊这里边呢该写都写了这个内容比较多大家呢一定要写的时候一定要细心先把这个思路捋清捋清完之后呢你再去写可能会容易一些或者说呢你先去看一下当前老师写在哪看明白之后呢你再去写好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

