# 画面线理解：08_后端通用封装-通用封装dto详细说明

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day06-黑马头条-通用后端
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day06-黑马头条-通用后端\08_后端通用封装-通用封装dto详细说明【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:19, 00:49, 02:18, 02:38, 03:59, 04:57, 05:22, 05:31, 05:41, 05:50, 05:57, 06:39, 06:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 14:02:22

1) 这一组画面整体在讲什么（一句话）：
讲解后台管理系统中通用的 CRUD 操作相关类的定义与实现，包括枚举、DTO、DAO 等核心组件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程文档中关于 CommonTableEnum、CommonWhereDto、CommonDao 等类的说明，重点介绍 CommonTableEnum 的作用和定义。
画面 2: 展示了项目结构，当前选中的是 heima-leadnews-model 模块。
画面 3: 展示了 CommonTableEnum.java 文件内容，其中定义了 AD_CHANNEL、AD_SENSITIVE、AP_ARTICLE 等枚举常量及其布尔值。
画面 4: 展示了 MySQL 数据库中 ad_sensitive 表的 DDL 创建语句。
画面 5: 展示了 CommonTableEnum.java 文件内容，其中定义了 AP_ARTICLE_CONFIG、AP_USER 等枚举常量及其布尔值。
画面 6: 展示了 CommonWhereDto.java 文件内容，其中定义了 filed、type、value 三个私有属性。
画面 7: 展示了 CommonDto.java 文件内容，其中定义了 size、page、model、name、where、sets 等私有属性。
画面 8: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 9: 展示了 CommonWhereDto.java 文件内容，其中高亮显示了 filed、type、value 三个属性。
画面 10: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 11: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 12: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 13: 展示了 CommonDto.java 文件内容，其中高亮显示了 where 属性。
画面 14: 展示了 CommonDto.java 文件内容，其中高亮显示了 model 属性。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
• CommonTableEnum: 适用于定义哪些数据表可支持通用操作，及其开发的 CRUD 功能
• CommonWhereDto: 用于接收前端传入的将字段名或者查询条件参数
• CommonDto: 用于接收前端传入的接口参数（包括 CRUD 的接口参数）
• CommonServiceImp: 实现通用端口的控制定义
• BaseCommonFilter: 定义后台处理的接口方法（后置增加的BeanName定义为CommonTableEnum名称即可）
```
画面 3:
```
@Getter
public enum CommonTableEnum {
    AD_CHANNEL("**",true,true,true,true),
    AD_SENSITIVE("**",true,true,true,true),
    AP_ARTICLE("**",true,false,false,false),
    AP_ARTICLE_CONFIG("**",true,false,true,false),
    AP_USER("**",true,false,true,false),
}
```
画面 4:
```
CREATE TABLE `ad_sensitive` (
  `id` int(11) NOT NULL COMMENT '主键',
  `sensitivities` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '敏感词',
  `created_time` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `idx_sensitivities` (`sensitivities`),
  KEY `idx_created_time` (`created_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='敏感词信息表';
```
画面 6:
```
package com.heima.model.admin.dtos;
import lombok.Data;
public class CommonWhereDto {
    private String filed;
    private String type="eq";
    private String value;
}
```
画面 7:
```
package com.heima.model.admin.dtos;
import lombok.Data;
public class CommonDto {
    private Integer size
    private Integer page
    private String model,
    // 操作的对象
    private CommonTableEnum name
    // 实际的条件
    private List<CommonWhereDto> where,
    // 修改的字段
    private List<CommonWhereDto> sets;
}
```
画面 14:
```
private String model
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
