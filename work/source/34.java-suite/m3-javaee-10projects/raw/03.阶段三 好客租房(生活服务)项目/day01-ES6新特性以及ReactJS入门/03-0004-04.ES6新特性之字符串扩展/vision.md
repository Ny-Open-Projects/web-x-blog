# 画面线理解：04.ES6新特性之字符串扩展

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\04.ES6新特性之字符串扩展【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:19, 01:02, 01:16, 01:36, 01:57, 03:09, 03:37, 03:59, 04:18, 04:46, 04:55, 06:03, 07:14, 07:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 19:59:08

1) 这一组画面整体在讲什么（一句话）：
讲解 ES6 中字符串扩展的 API，包括 includes、startsWith、endsWith 方法，并演示模板字符串的用法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 ES6 字符串扩展的介绍，列出 includes、startsWith、endsWith 方法，并给出实验代码示例。
画面 2: 在 HTML 文件中，定义了一个字符串变量 str 并输出。
画面 3: 在代码中，将变量 str 的值修改为 "hello heima"。
画面 4: 在代码中，调用 str.includes("heima") 方法并输出结果。
画面 5: 在浏览器控制台中，显示了语法错误：Assignment to constant variable。
画面 6: 在浏览器控制台中，显示了字符串包含检查的结果。
画面 7: 在代码中，调用 str.startsWith("hello") 方法并输出结果。
画面 8: 在代码中，调用 str.endsWith("hello") 方法并输出结果。
画面 9: 在代码中，调用 str.endsWith("heima") 方法并输出结果。
画面 10: 在代码中，定义了一个新的字符串变量 str2。
画面 11: 在代码中，将变量 str2 的值修改为 "abc" + "123"。
画面 12: 在浏览器控制台中，显示了语法错误：Identifier 'str' has already been declared。
画面 13: 展示了 ES6 模板字符串的用法，并给出示例代码。
画面 14: 展示了模板字符串的输出结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
console.log("a", "a");
```
```javascript
// Uncaught TypeError: Assignment to constant variable.
at [code].html:11
```
```javascript
// 实验一下：
<script>
let str = "hello heima";
console.log(str, "中是否包含了 heima", str.includes("heima"));
console.log(str, "中是否包含了 baima", str.includes("baima"));
console.log(str, "中是否以 hello 开头", str.startsWith("hello"));
console.log(str, "中是否以 heima 开头", str.startsWith("heima"));
console.log(str, "中是否以 hello 结束", str.endsWith("hello"));
console.log(str, "中是否以 heima 结束", str.endsWith("heima"));
</script>
```
画面 2:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ES6新特性的学习</title>
</head>
<body>
<script>
const str = "abc";
console.log(str);
</script>
</body>
</html>
```
画面 3:
```javascript
let str = "hello heima";
```
画面 4:
```javascript
let str = "hello heima";
console.log(str, "中是否包含了 heima", str.includes("heima"));
```
画面 6:
```javascript
hello heima 中是否包含了 heima true
hello heima 中是否包含了 baima false
hello heima 中是否以 hello 开头 true
hello heima 中是否以 heima 开头 false
hello heima 中是否以 hello 结束 false
hello heima 中是否以 heima 结束 true
```
画面 7:
```javascript
let str = "hello heima";
console.log(str, "中是否包含了 heima", str.includes("heima"));
console.log(str, "中是否包含了 baima", str.includes("baima"));
console.log(str, "中是否以 hello 开头", str.startsWith("hello"));
console.log(str, "中是否以 heima 开头", str.startsWith("heima"));
console.log(str, "中是否以 hello 结束", str.endsWith("hello"));
console.log(str, "中是否以 heima 结束", str.endsWith("heima"));
```
画面 10:
```javascript
let str2 = "abc" + "123";
```
画面 13:
```javascript
// 半符模板
ES6中提供了 作为字符串模板标记，我们可以这么玩：
<script>
let str = `
hello
itheima
str
`;
console.log(str);
</script>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.3、字符串扩展”，并列出 includes、startsWith、endsWith 方法。
画面 13: PPT 标题为“半符模板”，并给出模板字符串的示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
