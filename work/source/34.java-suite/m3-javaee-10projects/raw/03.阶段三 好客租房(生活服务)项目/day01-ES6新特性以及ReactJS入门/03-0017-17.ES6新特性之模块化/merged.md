# 17.ES6新特性之模块化

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\17.ES6新特性之模块化【海量资源尽在 ubkz.com】.mp4
- 时长 4分3秒（音频 243s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下模块化啊那么什么是模块化呢我们来看一下那么模块化呢其实就是把代码呢做一个拆分然后呢方便我们对这个代码的做一个重复的一个利用这个呢其实有点类似于我们Java中的这个导包我们是不是可以把一个类啊把这一个类是吧
[00:21] 打在一个包里面然后要应用它的时候把这个包再导入进来导入到我们的工程里面就可以去使用了这样的话我们是不是这个代码就可以达到一个重复利用的这样的一个效果但是在JS中它并没有包的这个概念而是用模块化来做一个实现那么在JS中的模块主要是有两个命令
[00:47] 或者两个关键字来完成一个是要export导出一个是要import导入这两个来完成那么导export就是规定这个模块的一个对外的一个接口导出那么import就是导入好那么下面我们分别来看一下这个export和import这两个的一个用法那么你比如说我们现在写个代码那么在哪写呢我们在这个地方来写
[01:15] 在这个位置我们创建一个js文件比如说叫util那么在这个util中我们去写一个类写一个类类的名字就叫util然后我们在这个util中写一个方法写一个方法写一个静态方法static那么什么方法比如说像什么方法如果我们用箭头函数来做怎么做上等于
[01:43] 那么参数是不是有两个单数a和b然后我们返回什么是不是就return然后我们直接就return直接写它return什么a加b好那么你可以看到是不是我们在util中写了一个类然后我们写了一个sum这个方法然后返回a加b在下面我们可以通过一个命令叫什么port
[02:11] 去导出什么呢导出这个类default导出util把它导出出去那么导出之后我们来看一下怎么去使用它比如说我们需要在 index.js中去使用它怎么去用呢咱们把这个内容就删掉了怎么去用它通过一个命令叫input叫util然后from谁from用单引号然后
[02:38] 点斜杠下面的Util好你可以不用写这个js如果你不写这个.js的话那么他就会默认加一个.js然后我们就可以去使用它了怎么样去使用我们在这个位置直接来console点log打印点什么的sum比如说10加一个5那么我们来看一下它能不能够正常执行刷新来看一下效果
[03:09] 刷新可以看到是不是正常执行了那么这个就是它的模块化我们是不是将一个util这个是不是做成一个独立的一个模块那么想要使用我们这个util的话那么是不是就可以在我们需要的位置来一个import去导入把它导入进来就可以了那么我们这个再加一个封号做一个结束这个结束你不加也可以习惯上我们还是给大家要加一下
[03:36] 好这样的话我们就完成了一个模块的一个导出和模块化的一个导入是不是非常相像我们Java中的这个类啊哎OK啊非常相像啊哎这个呢就是我们所讲的这个模块化啊那么在我们后续的开发的过程中尤其是我们在使用这个reactgest的时候呢会大量的使用这个模块化啊这个大家一定要掌握啊好那么关于这个模块化呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

