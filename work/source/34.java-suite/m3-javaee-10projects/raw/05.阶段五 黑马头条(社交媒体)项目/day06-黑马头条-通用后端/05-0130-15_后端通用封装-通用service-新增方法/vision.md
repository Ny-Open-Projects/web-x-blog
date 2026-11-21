# 画面线理解：15_后端通用封装-通用service-新增方法

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\15_后端通用封装-通用service-新增方法【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:20, 02:10, 03:28, 04:51, 05:48, 06:53, 08:22, 09:03, 11:14, 11:57, 12:51, 13:39, 14:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:08:36

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
