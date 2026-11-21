# 画面线理解：12.ES6新特性之Set和Map

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\12.ES6新特性之Set和Map【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:56, 01:09, 01:54, 03:33, 04:29, 05:34, 06:02, 06:31, 07:15, 07:28, 08:16, 09:03, 09:44, 10:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:05:30

1) 这一组画面整体在讲什么（一句话）：
演示并讲解 ES6 中 Set 和 Map 数据结构的创建、操作方法及在浏览器控制台中的实际效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 IntelliJ IDEA 中打开 index.html 文件，展示一个包含 Set 数据结构示例的 JavaScript 代码，其中定义了一个 Set 并添加了元素 1、2、5、9。
画面2：在代码中光标位于 set.add(1); 后，IDE 提供了自动补全建议，显示了 add 方法的参数类型和功能说明。
画面3：在代码中光标位于 set.forEach(value => { 后，IDE 提供了 forEach 方法的参数类型和功能说明。
画面4：切换到 Typora 编辑器，显示了课程 PPT 的第 1.8 节“set和map”，其中解释了 Set 和 Map 的数据结构特性，并列出了 Set 的构造函数和方法。
画面5：在 IntelliJ IDEA 中，开始编写 Map 数据结构的代码，光标位于 let map = { 后。
画面6：在 IntelliJ IDEA 中，光标位于 let map = { 后，IDE 提供了自动补全建议，显示了 Map 构造函数的参数类型和功能说明。
画面7：在 IntelliJ IDEA 中，光标位于 const map = new Map([ 后，IDE 提供了自动补全建议，显示了 Map 构造函数的参数类型和功能说明。
画面8：在 IntelliJ IDEA 中，光标位于 const map = new Map([ 后，IDE 提供了自动补全建议，显示了 Map 构造函数的参数类型和功能说明。
画面9：在 IntelliJ IDEA 中，编写了 Map 的 set 和 get 方法，并调用 map.forEach() 方法。
画面10：在 IntelliJ IDEA 中，光标位于 console.log(map.get('key1')); 后，IDE 提供了自动补全建议，显示了 console.log 方法的参数类型和功能说明。
画面11：切换到浏览器开发者工具的 Console 面板，显示了 Map 数据结构中 key 和 value 的输出结果。
画面12：在 IntelliJ IDEA 中，光标位于 map.forEach(value, key => { 后，IDE 提供了自动补全建议，显示了 forEach 方法的参数类型和功能说明。
画面13：切换到浏览器开发者工具的 Console 面板，显示了 Map 数据结构中 key 的输出结果。
画面14：切换到 Typora 编辑器，显示了课程 PPT 的第 1.8 节“set和map”，其中解释了 Set 和 Map 的数据结构特性，并列出了 Set 的构造函数和方法。

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
let set = new Set();
set.add(1);
set.add(2);
set.add(5);
set.add(9);
set.forEach(value => {
console.log(value);
});
</script>
</body>
</html>
```

画面4：
```javascript
// Set构造函数可以接收一个数组或迭代器
let set = new Set();
set.add(1); // 添加元素
// 改变数据
let set2 = new Set([2,3,4,5,5]); // 得到[2,3,4,5]
```

画面9：
```javascript
const map = new Map([
['key1', 'value1'],
['key2', 'value2'],
]);
map.set('key3', 'value3');
console.log(map.get('key1'));
map.forEach((value, key) => {
console.log(key, value);
});
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
标题：1.8. set和map
内容：
- Set 本质与数组类似，不同在于 Set 中只存储不同元素，如果元素相同会被忽略，和 java 中的 Set 非常相似。
- 构造函数：
  ```javascript
  // Set构造函数可以接收一个数组或迭代器
  let set = new Set();
  set.add(1); // 添加元素
  // 改变数据
  let set2 = new Set([2,3,4,5,5]); // 得到[2,3,4,5]
  ```
- 方法：
  ```javascript
  set.add(1); // 添加元素
  set.clear(); // 清除
  set.delete(2); // 删除指定元素
  set.has(2); // 判断是否存在
  set.forEach(function() {}); // 遍历元素
  set.size; // 元素个数，属性，不是方法。
  ```

画面14：
标题：1.8. set和map
内容：
- Set 本质与数组类似，不同在于 Set 中只存储不同元素，如果元素相同会被忽略，和 java 中的 Set 非常相似。
- 构造函数：
  ```javascript
  // Set构造函数可以接收一个数组或迭代器
  let set = new Set();
  set.add(1); // 添加元素
  // 改变数据
  let set2 = new Set([2,3,4,5,5]); // 得到[2,3,4,5]
  ```
- 方法：
  ```javascript
  set.add(1); // 添加元素
  set.clear(); // 清除
  set.delete(2); // 删除指定元素
  set.has(2); // 判断是否存在
  set.forEach(function() {}); // 遍历元素
  set.size; // 元素个数，属性，不是方法。
  ```

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
