# 画面线理解：20-Hive的基本操作-内置函数

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\20-Hive的基本操作-内置函数【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:16, 01:57, 02:08, 02:52, 03:26, 04:13, 05:07, 05:54, 06:17, 06:52, 07:42, 08:32, 08:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 06:50:52

1) 这一组画面整体在讲什么（一句话）：
演示Hive内置函数的查看、描述和实际调用方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Hive内置函数章节的PPT内容，列出查看系统函数、显示函数用法、详细描述函数和调用函数四个步骤，并给出对应命令示例。
画面2：与画面1内容相同，为同一PPT页面的重复展示。
画面3：在SecureCRT终端中执行`hive desc function upper;`命令，输出函数说明，随后执行`hive desc function extended upper;`命令，输出更详细的函数信息。
画面4：在SecureCRT终端中执行`SELECT upper('Facebook') FROM src LIMIT 1;`查询语句，输出结果为'FACEBOOK'，并显示函数类和类型信息。
画面5：展示PPT页面，重点在“4. 常用内置函数”部分，列出concat、concat_ws、cast等函数的示例代码。
画面6：在SecureCRT终端中执行`select upper('hello');`、`select abs(-5);`和`select concat('hello','world','hive');`命令，分别输出结果“HELLO”、“5”和“helloworldhive”。
画面7：在SecureCRT终端中执行`select concat_ws(',', 'hello', 'world', 'hive');`命令，输出结果“hello,world,hive”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
https://cwiki.apache.org/confluence/display/Hive/LanguageManualUDF
1. 查看系统自带的函数
hive show functions;
2. 显示自带的函数的用法
hive desc function upper;
3. 详细显示自带的函数的用法
hive desc function extended upper;
4. 常用内置函数
#字符串连接函数： concat
select concat('abc','def','gh');
#字符串拼接函数： concat_ws
select concat_ws(',', 'abc', 'def', 'gh');
#类型转换函数： cast
select cast(1.5 as int);

画面3：
xpath
xpath_boolean
xpath_double
xpath_float
xpath_int
xpath_long
xpath_number
xpath_short
xpath_string
year
Time taken: 0.028 seconds, Fetched: 289 row(s)
hive> desc function upper;
OK
upper(str) - Returns str with all characters changed to uppercase
Time taken: 0.055 seconds, Fetched: 1 row(s)
hive>

画面4：
upper(str) - Returns str with all characters changed to uppercase
Synonyms: ucase
Example:
> SELECT upper('Facebook') FROM src LIMIT 1;
'FACEBOOK'
Function class:org.apache.hadoop.hive.q1.udf.generic.GenericUDFUpper
Function type:BUILTIN
Time taken: 0.024 seconds, Fetched: 7 row(s)
hive>

画面6：
hive> select upper('hello');
HELLO
Time taken: 0.158 seconds, Fetched: 1 row(s)
hive> select abs(-5);
5
Time taken: 0.157 seconds, Fetched: 1 row(s)
hive> select concat('hello','world','hive');
helloworldhive
Time taken: 0.153 seconds, Fetched: 1 row(s)

画面7：
hive> select concat_ws(',', 'hello', 'world', 'hive');
hello,world,hive
Time taken: 0.153 seconds, Fetched: 1 row(s)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1和画面5：PPT标题为“3.1. 内置函数”，子标题“内容较多，见《Hive官方文档》”，并列出四个步骤：
1. 查看系统自带的函数
2. 显示自带的函数的用法
3. 详细显示自带的函数的用法
4. 常用内置函数
画面5中在“4. 常用内置函数”部分下方有“email”字样，但无明确结构指向。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
