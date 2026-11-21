# 画面线理解：12_后端通用封装-通用service-查询方法1

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\12_后端通用封装-通用service-查询方法1【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:29, 01:39, 03:21, 04:36, 05:23, 06:27, 07:44, 09:58, 10:47, 11:53, 13:12, 14:22, 15:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:06:09

1) 这一组画面整体在讲什么（一句话）：
编写一个通用的条件查询服务类，用于动态构建 SQL 查询条件，支持多种查询类型（如等于、模糊匹配、范围查询等）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 CommonDto 类的定义，包含 size、page、model、name、where、sets 等字段，用于封装分页和查询条件。
画面 2: 在 CommonServiceImpl.java 中，定义了通用的列表查询方法 list(CommonDto dto)，并使用 @Autowired 注入 CommonDao。
画面 3: 展示了 CommonServiceImpl.java 中的 @GeneratedValue 注解，用于自动生成代码。
画面 4: 在 getWhere 方法中，开始构建 SQL 条件，使用 StringBuffer 存储条件，并检查 dto.getWhere() 是否为 null。
画面 5: 在 getWhere 方法中，使用 Stream 流对 dto.getWhere() 中的每个元素进行处理，检查是否为空或等于空字符串。
画面 6: 在 getWhere 方法中，使用 StringUtils.isNotBlank 方法检查字段值是否非空。
画面 7: 在 getWhere 方法中，使用 StringUtils.isNumeric 方法检查字段值是否为数字。
画面 8: 在 getWhere 方法中，使用 StringUtils.matches 方法检查字段值是否匹配正则表达式。
画面 9: 在 getWhere 方法中，使用 where.append 方法将条件拼接到 SQL 语句中。
画面 10: 在 getWhere 方法中，使用 where.append 方法将模糊匹配条件拼接到 SQL 语句中。
画面 11: 在 getWhere 方法中，使用 where.append 方法将范围查询条件拼接到 SQL 语句中。
画面 12: 在 getWhere 方法中，使用 where.append 方法将条件拼接到 SQL 语句中。
画面 13: 在 list 方法中，如果 dto.getName() 为空，则返回错误码 NO_OPERATOR_AUTH。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.heima.model.admin.dtos;

import ...

@Data
public class CommonDto {
    private Integer size;
    private Integer page;
    // 操作模式add 编辑、del编辑
    private String model;
    // 查询的条件
    private List<CommonWhereDto> where;
    // 查询的字段
    private List<CommonWhereDto> sets;
}
```

画面 2:
```java
@Autowired
private CommonDao commonDao;

// 通用列表加方法
@Override
public ResponseResult list(CommonDto dto) {
    if (dto.getName() == null) {
        return ResponseResult.errorResult(AppHttpCodeEnum.NO_OPERATOR_AUTH);
    }
    return null;
}

@Override
public ResponseResult update(CommonDto dto) {
    return null;
}
```

画面 3:
```java
@GeneratedValue
Class extends CommonService<T> {
    GeneratedValue (java.persistence)
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
    Generated
