# 画面线理解：13_后端通用封装-通用service-查询方法2

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\13_后端通用封装-通用service-查询方法2【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:09, 00:50, 01:32, 01:55, 02:13, 02:51, 03:23, 03:47, 04:03, 04:36, 05:13, 05:40, 06:07, 06:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:06:51

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
