# 画面线理解：05.ES6新特性之解构表达式

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\05.ES6新特性之解构表达式【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:52, 01:09, 01:22, 02:11, 02:20, 02:52, 03:07, 03:37, 04:30, 04:37, 04:56, 05:57, 06:31, 06:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:00:07

1) 这一组画面整体在讲 ES6 新特性中的解构赋值（Destructuring）语法，包括数组解构和对象解构。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 代码内容：在 HTML 文件中，使用 JavaScript 的字符串方法，如 includes、startsWith、endsWith。
- 代码片段：
  ```javascript
  let str = "hello heima";
  console.log(str, "中是否包含了 heima", str.includes("heima"));
  console.log(str, "中是否包含 baima", str.includes("baima"));
  console.log(str, "中是否以 hello 开头", str.startsWith("hello"));
  console.log(str, "中是否以 heima 开头", str.startsWith("heima"));
  console.log(str, "中是否以 hello 结束", str.endsWith("hello"));
  console.log(str, "中是否以 heima 结束", str.endsWith("heima"));
  let str2 = "abc 123";
  ```

画面 2:
- 代码内容：在 HTML 文件中，定义一个数组并使用 console.log 输出。
- 代码片段：
  ```javascript
  let arr = [1,2,3];
  console.log(arr[1]);
  ```

画面 3:
- 代码内容：在 HTML 文件中，定义一个数组并使用 console.log 输出。
- 代码片段：
  ```javascript
  let arr = [1,2,3];
  let [x, y, z] = arr;
  console.log(x, y, z);
  ```

画面 4:
- 代码内容：在 HTML 文件中，定义一个数组并使用 console.log 输出。
- 代码片段：
  ```javascript
  let arr = [1,2,3];
  let [x, y, z] = arr;
  console.log(x);
  ```

画面 5:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 6:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 7:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 8:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 9:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 10:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 11:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 12:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 13:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

画面 14:
- 代码内容：在 HTML 文件中，定义一个对象并使用 console.log 输出。
- 代码片段：
  ```javascript
  const person = {
    name: "jack",
    age: 21,
    language: ["java", "js", "css"]
  };
  let [name, age, language] = person;
  console.log(name, age, language);
  ```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1:
```javascript
let str = "hello heima";
console.log(str, "中是否包含了 heima", str.includes("heima"));
console.log(str, "中是否包含 baima", str.includes("baima"));
console.log(str, "中是否以 hello 开头", str.startsWith("hello"));
console.log(str, "中是否以 heima 开头", str.startsWith("heima"));
console.log(str, "中是否以 hello 结束", str.endsWith("hello"));
console.log(str, "中是否以 heima 结束", str.endsWith("heima"));
let str2 = "abc 123";
```

画面 2:
```javascript
let arr = [1,2,3];
console.log(arr[1]);
```

画面 3:
```javascript
let arr = [1,2,3];
let [x, y, z] = arr;
console.log(x, y, z);
```

画面 4:
```javascript
let arr = [1,2,3];
let [x, y, z] = arr;
console.log(x);
```

画面 5:
```javascript
const person = {
  name: "jack",
  age: 21,
  language: ["java", "js", "css"]
};
let [name, age, language] = person;
console.log(name, age, language);
```

画面 6:
```javascript
const person = {
  name: "jack",
  age: 21,
  language: ["java", "js", "css"]
};
let [name, age, language] = person;
console.log(name, age, language);
```

画面 7:
```javascript
const person = {
  name: "jack",
  age: 21,
  language: ["java", "js", "css"]
};
let [name, age, language] = person;
console.log(name, age, language);
```

画面 8:
```javascript
const person = {
  name: "jack",
  age: 21,
  language: ["java", "js", "css"]
};
let [name, age, language] = person;
console.log(name, age, language);
```

画面 9:
```javascript
const person = {
  name: "jack",
  age: 21,
  language: ["java", "js", "css"]
};
let [name, age, language] = person;
console.log(name, age, language);
```

画面 10:
```javascript
const person = {
  name: "jack",
  age: 21,
  language: ["java", "js", "css"]
};
let [name, age, language] = person;
console.log(name, age, language);
```

画面 11:
```javascript
const person = {
  name: "jack",
  age: 21,
  language: ["java", "js", "css"]
};
let [name, age, language] = person;
console.log(name, age, language);
```

画面 12:
```javascript
const person = {
  name: "jack",
  age: 21,
  language: ["java", "js", "css"]
};
let [name, age, language] = person;
console.log(name, age, language);
```

画面 13:
```javascript
const person = {
