# 画面线理解：17.ES6新特性之模块化

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\17.ES6新特性之模块化【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:10, 01:20, 01:49, 01:57, 02:15, 02:21, 02:28, 02:56, 03:07, 03:17, 03:23, 03:45, 03:49, 03:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:09:06

1) 这一组画面整体在讲什么（一句话）：
演示如何在 TypeScript 项目中定义和使用模块（export 和 import），并通过代码示例讲解模块化概念。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- IDE 中打开 `index.js` 文件，展示一个模拟 JavaScript 中的类 `User`，包含构造函数和 `T(target)` 方法。
- 代码内容：
  ```javascript
  // 通过Q符号进行引用该方法，类似java中的注解
  class User {
    constructor(name, age = 20) {
      this.name = name;
      this.age = age;
    }
  }

  function T(target) { //定义一个普通的方法
    console.log(target); //target对象为修饰的目标对象，这里是User对象
    target.country = "中国"; //为User类添加一个静态属性country
  }

  console.log(User.country); //打印country属性值
  ```

画面 2:
- IDE 中，`Util.js` 文件被选中，弹出“New Javascript File”对话框，准备新建文件。

画面 3:
- IDE 中打开 `Util.js` 文件，代码中定义了一个静态方法 `sum`，并显示了 TypeScript 类型提示（如 `ReadableStream`、`RegExp` 等）。

画面 4:
- IDE 中 `Util.js` 文件，代码中 `sum` 方法的实现部分被选中，显示了 `return a + b` 的实现。

画面 5:
- IDE 中 `Util.js` 文件，代码中添加了 `export default Util;`，并显示了类型提示（如 `User(name, age = 20)`、`Uint8Array` 等）。

画面 6:
- IDE 中 `Util.js` 文件，代码中 `export default Util;` 被选中，显示了类型提示（如 `User(name, age = 20)`、`Uint8Array` 等）。

画面 7:
- IDE 中，`index.js` 文件被选中，准备进行编辑。

画面 8:
- IDE 中 `index.js` 文件，代码中 `import Util from './Util'` 被选中，显示了类型提示（如 `console`、`confirm`、`Comment` 等）。

画面 9:
- 浏览器中打开 `http://localhost:8000/`，显示了 `Util.js` 文件的内容，包含 `User` 类的定义和 `T` 方法的实现。

画面 10:
- IDE 中 `Util.js` 文件，代码中 `export default Util;` 被选中。

画面 11:
- IDE 中 `Util.js` 文件，代码中 `export default Util;` 被选中。

画面 12:
- Typora 中打开 `day01-ReactJS入门.md` 文件，显示了“1.1.3. 模块化”章节，其中包含 `export` 和 `import` 的定义。

画面 13:
- Typora 中 `day01-ReactJS入门.md` 文件，显示了“1.1.3. 模块化”章节，其中包含 `export` 和 `import` 的定义。

画面 14:
- Typora 中 `day01-ReactJS入门.md` 文件，显示了“1.1.3. 模块化”章节，其中包含 `export` 和 `import` 的定义，以及 `import Util from './Util'` 的示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1:
```javascript
// 通过Q符号进行引用该方法，类似java中的注解
class User {
  constructor(name, age = 20) {
    this.name = name;
    this.age = age;
  }
}

function T(target) { //定义一个普通的方法
  console.log(target); //target对象为修饰的目标对象，这里是User对象
  target.country = "中国"; //为User类添加一个静态属性country
}

console.log(User.country); //打印country属性值
```

画面 3:
```typescript
class Util {
  static sum = (a, b) => {
    return a + b;
  }
}
```

画面 5:
```typescript
class Util {
  static sum = (a, b) => {
    return a + b;
  }
}

export default Util;
```

画面 8:
```javascript
import Util from './Util'
```

画面 12:
```javascript
class Util {
  static sum = (a, b) => a + b;
}

// 导出类
export default Util;
```

画面 14:
```javascript
// 导入模块
import Util from './Util'

// 使用模块中的方法
console.log(Util.sum(1, 2));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 12、13、14:
- PPT 标题：`1.1.3. 模块化`
- 子标题：`1.1.3.1 什么是模块化`
  - 内容：模块化就是把代码进行拆分，方便重复利用，类似java中的包，要使用一个包，必须先导入。
  - 模块功能主要由两个命令构成：`export` 和 `import`。
    - `export` 命令用于规定模块的对外接口。
    - `import` 命令用于导入其他模块提供的功能。
- 子标题：`1.1.3.2. export`
  - 内容：比如我定义一个文件 `Util.js`，里面有一个 `Util` 类：
    ```javascript
    class Util {
      static sum = (a, b) => a + b;
    }

    // 导出类
    export default Util;
    ```
- 子标题：`1.1.3.3. import`
  - 内容：使用 `export` 命令定义了模块的对外接口以后，其他 `.js` 文件可以通过 `import` 命令加载这个模块。
  - 示例：
    ```javascript
    // 导入模块
    import Util from './Util'

    // 使用模块中的方法
    console.log(Util.sum(1, 2));
    ```

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
