# 画面线理解：06.ES6新特性之函数优化-参数默认值

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\06.ES6新特性之函数优化-参数默认值【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:30, 00:34, 00:44, 00:49, 00:58, 01:17, 01:31, 01:50, 01:59, 02:06, 02:15, 02:22, 03:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:00:37

1) 这一组画面整体在讲什么（一句话）：
演示并讲解 JavaScript ES6 中的函数参数默认值和箭头函数特性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个包含 ES6 解构赋值和 console.log 的 HTML 页面代码，用于演示 ES6 新特性。
画面2：在代码中删除了之前的解构赋值代码，准备演示函数。
画面3：在 script 标签内添加了一个名为 add 的函数，用于演示函数参数默认值。
画面4：在 add 函数内部添加了 console.log() 语句，用于调试。
画面5：切换到 PPT 页面，标题为“1.4. 函数优化”，内容包括“1.4.1. 函数参数默认值”和“1.4.2. 箭头函数”。
画面6：在代码编辑器中弹出一个浏览器窗口，显示了“ES6新特性学习 - Google Chrome”的多窗口预览。
画面7：在代码编辑器中，光标位于 add 函数内部，准备添加条件判断语句。
画面8：在浏览器中打开页面，显示了“ES6新特性学习”的标题和多个窗口预览。
画面9：在代码编辑器中，添加了 if(!b) { b = 1; } 语句，用于处理参数默认值。
画面10：在代码编辑器中，将 if(!b) { b = 1; } 语句中的 b = 1; 改为 b = 1; 以确保语句正确。
画面11：在代码编辑器中，弹出一个浏览器窗口，显示了“ES6新特性学习 - Google Chrome”的多窗口预览。
画面12：在代码编辑器中，将 add 函数的返回语句改为 return a + b; 以确保函数正常工作。
画面13：在浏览器的 Console 面板中，显示了“Default views”和“index.html”的信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ES6新特性的学习</title>
</head>
<body>
<script>
const person = {
name: 'jack',
age: 21,
language: ['java', 'js', 'css']
};
let [name, age, language] = person;
console.log(name, age, language);

let {name:n, age:a, language:l} = person;
console.log(n, a, l);
</script>
</body>
</html>
```

画面3：
```javascript
function add(a, b) {
return a + b;
}
```

画面4：
```javascript
function add(a, b) {
return a + b;
}
console.log();
```

画面5：
```javascript
// 参数默认值
function add(a, b) {
b = b || 1;
return a + b;
}
// 每一个参数
console.log(add(10));
```

画面9：
```javascript
function add(a, b) {
if(!b) {
b = 1;
}
return a + b;
}
```

画面10：
```javascript
function add(a, b) {
if(!b) {
b = 1;
}
return a + b;
}
```

画面12：
```javascript
function add(a, b) {
return a + b;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：
标题：1.4. 函数优化
子标题：1.4.1. 函数参数默认值
内容：
在ES6中，对函数的参数做了优化，使得我们在操作函数时更加的便捷。
在ES6以前，我们无法给一个函数参数设置默认值，只能采用类似写法：
```javascript
function add(a, b) {
b = b || 1;
return a + b;
}
```
现在可以这么写：
```javascript
function add(a, b = 1) {
return a + b;
}
```
子标题：1.4.2. 箭头函数
内容：
ES6中定义函数的写与方式：

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
