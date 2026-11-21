# 画面线理解：09.ES6新特性之map和reduce方法的使用

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\09.ES6新特性之map和reduce方法的使用【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:40, 01:03, 01:39, 02:02, 03:01, 03:29, 03:49, 05:06, 06:07, 06:25, 07:28, 09:14, 09:39, 10:06
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:02:43

1) 这一组画面整体在讲什么（一句话）：
讲解 ES6 中的数组方法 map 和 reduce 的用法与区别。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 ES6 中的 let 声明、解构赋值、箭头函数等特性。
- 代码：const person = { name: 'jack', age: 21, language: ['java', 'js', 'css'] }; function hello(person) { console.log("hello," + person.name); } const hello2 = (name) => console.log("hello," + name); hello(person); hello2(person);

画面 2:
- 展示了 let 声明的数组，并调用 console.log 输出。
- 代码：let arr = ['1','20','-5','3']; console.log(arr);

画面 3:
- 在数组上使用 map 方法，对每个元素应用 parseInt 函数。
- 代码：arr.map(s => parseInt(s));

画面 4:
- 将 map 方法的处理结果赋值给新变量 newArr，并输出。
- 代码：let newArr = arr.map(s => parseInt(s)); console.log(newArr);

画面 5:
- 代码与画面 4 相同，无新增内容。

画面 6:
- 在 map 方法中使用 function 语法，并在函数内调用 parseInt。
- 代码：let newArr2 = arr.map(function (a) { return parseInt(a); }); console.log(newArr2);

画面 7:
- 展示了 PPT 中关于 reduce 方法的说明。
- 标题：1.5.1. reduce
- 内容：reduce() 接收一个函数（必须）和一个初始值（可选），该函数接收两个参数：第一个参数是上一次 reduce 处理的结果，第二个参数是数组中要处理的下一个元素。
- 示例：const arr = [1,20,-5,3]

画面 8:
- 在 HTML 文件中使用 reduce 方法。
- 代码：const arr = [1,20,-5,3]; arr.reduce(() => { });

画面 9:
- 在 reduce 方法中定义回调函数。
- 代码：arr.reduce((a, b) => { return a + b; });

画面 10:
- 将 reduce 的处理结果赋值给 result，并输出。
- 代码：let result = arr.reduce((a, b) => { return a + b; }); console.log(result);

画面 11:
- 代码与画面 10 相同，无新增内容。

画面 12:
- 为 reduce 方法提供初始值 0。
- 代码：let result = arr.reduce((a, b) => { return a + b; }, 0); console.log(result);

画面 13:
- 展示了 PPT 中关于 map 和 reduce 方法的对比说明。
- 标题：1.5. map和reduce
- 内容：map() 接收一个函数，将原数组中的所有元素用这个函数处理后放入新数组返回。
- 示例：let arr = ['1','20','-5','3']; console.log(arr); let newArr = arr.map(s => parseInt(s)); console.log(newArr);

画面 14:
- 展示了 PPT 中关于 reduce 方法的说明。
- 标题：1.5.1. reduce
- 内容：reduce() 接收一个函数（必须）和一个初始值（可选），该函数接收两个参数：第一个参数是上一次 reduce 处理的结果，第二个参数是数组中要处理的下一个元素。
- 示例：const arr = [1,20,-5,3]
