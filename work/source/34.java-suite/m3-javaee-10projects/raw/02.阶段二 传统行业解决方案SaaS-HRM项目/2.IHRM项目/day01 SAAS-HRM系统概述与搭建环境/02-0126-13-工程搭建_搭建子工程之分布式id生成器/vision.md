# 画面线理解：13-工程搭建：搭建子工程之分布式id生成器

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\13-工程搭建：搭建子工程之分布式id生成器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:23, 00:30, 01:11, 01:39, 02:08, 02:32, 04:03, 06:13, 06:31, 08:40, 08:55, 09:00, 09:03, 09:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:56:32

1) 这一组画面整体在讲微服务架构中主键ID生成方案的对比与实现，重点讲解了雪花算法（Snowflake）的代码逻辑。

2) 按时间顺序列出每张画面的要点：
画面1：展示Windows开始菜单，鼠标悬停在“Visual Studio Code”图标上，右侧PPT内容为“41bit-时间戳”、“12bit-序列号”、“10bit-工作机器id”及其对应的二进制位示意图。
画面2：空白画布，准备绘制内容。
画面3：画布上绘制了第一个椭圆，标注为“a的user表”。
画面4：画布上绘制了第二个椭圆，标注为“b的user表”。
画面5：从“a的user表”和“b的user表”分别引出连线，指向一个中间椭圆，中间椭圆内有虚线框和文字“1”。
画面6：中间椭圆内文字更新为“合并的user表”。
画面7：右侧文本框中列出四种主键ID生成方案：“方案一：数据库自增”、“方案二：uuid”、“方案三：借助全局redis”、“方案四：雪花算法”。
画面8：画面内容与画面7相同，无变化。
画面9：画布上展示多个窗口缩略图，包括“SaaS HRM-第1章.pdf”、“PowerDesigner - ICOM...”、“01.png”、“02.png”等，用于说明项目结构。
画面10：IntelliJ IDEA中打开项目“ihrm_parent”，展示“Result.java”文件内容，包含Result类的构造方法和静态方法。
画面11：IntelliJ IDEA中选中“Result.java”文件。
画面12：IntelliJ IDEA中切换到“IdWorker.java”文件，展示雪花算法核心代码，包括变量声明和构造函数。
画面13：IntelliJ IDEA中展示“IdWorker.java”文件中“tilNextMillis”和“timeGen”方法的实现。
画面14：IntelliJ IDEA中“IdWorker.java”文件内容与画面13相同，底部任务栏显示“01.png”、“02.png”等图片缩略图。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面10：
```java
public class Result {
    private boolean success;//是否成功
    private Integer code;//返回码
    private String message;//返回信息
    private Object data;//返回数据

    public Result(ResultCode code) {
        this.success = code.success;
        this.code = code.code;
        this.message = code.message;
    }

    public Result(ResultCode code,Object data) {
        this.success = code.success;
        this.code = code.code;
        this.message = code.message;
        this.data = data;
    }

    public Result(Integer code,String message,boolean success) {
        this.code = code;
        this.message = message;
        this.success = success;
    }

    public static Result SUCCESS() {
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面12：
```java
package com.ihrm.common.utils;

import java.util.concurrent.atomic.AtomicLong;

/**
 * 雪花算法生成器，作为分布式系统中的唯一ID生成器
 * 1. 时间戳41位
 * 2. 机器ID 10位
 * 3. 序列号 12位
 * 4. 工作机器ID 10位
 * 5. 数据中心ID 5位
 * 6. 序列号 12位
 * 7. 机器ID 10位
 * 8. 数据中心ID 5位
 * 9. 序列号 12位
 * 10. 机器ID 10位
 * 11. 数据中心ID 5位
 * 12. 序列号 12位
 * 13. 机器ID 10位
 * 14. 数据中心ID 5位
 * 15. 序列号 12位
 * 16. 机器ID 10位
 * 17. 数据中心ID 5位
 * 18. 序列号 12位
 * 19. 机器ID 10位
 * 20. 数据中心ID 5位
 * 21. 序列号 12位
 * 22. 机器ID 10位
 * 23. 数据中心ID 5位
 * 24. 序列号 12位
 * 25. 机器ID 10位
 * 26. 数据中心ID 5位
 * 27. 序列号 12位
 * 28. 机器ID 10位
 * 29. 数据中心ID 5位
 * 30. 序列号 12位
 * 31. 机器ID 10位
 * 32. 数据中心ID 5位
 * 33. 序列号 12位
 * 34. 机器ID 10位
 * 35. 数据中心ID 5位
 * 36. 序列号 12位
 * 37. 机器ID 10位
 * 38. 数据中心ID 5位
 * 39. 序列号 12位
 * 40. 机器ID 10位
 * 41. 数据中心ID 5位
 * 42. 序列号 12位
 * 43. 机器ID 10位
 * 44. 数据中心ID 5位
 * 45. 序列号 12位
 * 46. 机器ID 10位
 * 47. 数据中心ID 5位
 * 48. 序列号 12位
 * 49. 机器ID 10位
 * 50. 数据中心ID 5位
 * 51. 序列号 12位
 * 52. 机器ID 10位
 * 53. 数据中心ID 5位
 * 54. 序列号 12位
 * 55. 机器ID 10位
 * 56. 数据中心ID 5位
 * 57. 序列号 12位
 * 58. 机器ID 10位
 * 59. 数据中心ID 5位
 * 60. 序列号 12位
 * 61. 机器ID 10位
 * 62. 数据中心ID 5位
 * 63. 序列号 12位
 * 64. 机器ID 10位
 * 65. 数据中心ID 5位
 * 66. 序列号 12位
 * 67. 机器ID 10位
 * 68. 数据中心ID 5位
 * 69. 序列号 12位
 * 70. 机器ID 10位
 * 71. 数据中心ID 5位
 * 72. 序列号 12位
 * 73. 机器ID 10位
 * 74. 数据中心ID 5位
 * 75. 序列号 12位
 * 76. 机器ID 10位
 * 77. 数据中心ID 5位
 * 78. 序列号 12位
 * 79. 机器ID 10位
 * 80. 数据中心ID 5位
 * 81. 序列号 12位
 * 82. 机器ID 10位
 * 83. 数据中心ID 5位
 * 84. 序列号 12位
 * 85. 机器ID 10位
 * 86. 数据中心ID 5位
 * 87. 序列号 12位
 * 88. 机器ID 10位
 * 89. 数据中心ID 5位
 * 90. 序列号 12位
 * 91. 机器ID 10位
 * 92. 数据中心ID 5位
 * 93. 序列号 12位
 * 94. 机器ID 10位
 * 95. 数据中心ID 5位
 * 96. 序列号 12位
 * 97. 机器ID 10位
 * 98. 数据中心ID 5位
 * 99. 序列号 12位
 * 100. 机器ID 10位
 * 101. 数据中心ID 5位
 * 102. 序列号
