# 画面线理解：19.日志规范之阿里巴巴开发手册中的其它规范讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\19.日志规范之阿里巴巴开发手册中的其它规范讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:16, 02:48, 04:00, 05:46, 06:04, 07:07, 07:17, 07:57, 08:41, 10:36, 11:58, 12:01, 12:26, 12:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:13:35

1) 这一组画面整体在讲什么（一句话）：
讲解阿里巴巴Java开发手册中关于日志规范的强制性要求，包括日志框架使用、文件命名、输出级别控制、避免重复打印、异常信息记录等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示日志规范第1条，强制使用SLF4J日志框架，提供代码示例：import org.slf4j.Logger; import org.slf4j.LoggerFactory; private static final Logger logger = LoggerFactory.getLogger(Abc.class);
画面2：展示日志规范第2条，强制日志文件保留至少15天。
画面3：展示日志规范第3条，强制扩展日志命名方式：appName_logType_logName.log，推荐分类如stats/desc/monitor/visit等。
画面4：展示日志规范第4条，强制对trace/debug/info级别日志输出必须使用条件输出或占位符方式，并给出条件判断和占位符两种写法的示例。
画面5：展示日志规范第5条，强制避免重复打印日志，需在log4j.xml中设置additivity=false。
画面6：展示日志规范第6条，强制异常信息应包含现场信息和异常堆栈信息，通过关键字throws向上抛出。
画面7：展示日志规范第7条，推荐谨慎记录日志，生产环境禁止输出debug日志，可选择性输出info日志。
画面8：展示日志规范第8条，参考建议使用warn级别记录用户输入参数错误，避免用户投诉，注意error级别只记录系统逻辑出错等重要错误。
画面9：画面内容与画面8相同，为重复展示。
画面10：画面内容与画面8相同，为重复展示。
画面11：画面内容与画面8相同，为重复展示。
画面12：画面内容与画面4相同，为重复展示。
画面13：画面内容与画面4相同，为重复展示。
画面14：画面内容与画面1相同，为重复展示。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
private static final Logger logger = LoggerFactory.getLogger(Abc.class);

画面3：
appName_logType_logName.log。logType:日志类型，推荐分类有
stats/desc/monitor/visit等；logName:日志描述。这种命名的好处：通过文件名就可知道日志文件属于什么应用，什么类型，什么目的，也有利于归类查找。

画面4：
说明：logger.debug("Processing trade with id: " + id + " and symbol: " + symbol);
如果日志级别是 warn, 上述日志不会打印，但是会执行字符串拼接操作，如果 symbol 是对象，会执行 toString()方法，浪费了系统资源，执行了上述操作，最终日志却没有打印。
正例：（条件）
if (logger.isDebugEnabled()) {
logger.debug("Processing trade with id: " + id + " and symbol: " + symbol);
}
正例：（占位符）
logger.debug("Processing trade with id: {} and symbol: {}", id, symbol);

画面5：
正例：<logger name="com.taobao.dubbo.config" additivity="false">

画面6：
正例：logger.error(各类型参数或者对象 toString + "_" + e.getMessage(), e);

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
