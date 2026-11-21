# 5-7-小花絮：使用 Prettier 自动格式化代码

上节课介绍了 ESLint 的一系列配置，这节课来一个小加餐，介绍代码格式化工具 Prettier。这是一个近两年非常火的项目，很多之前上过课的同学也经常问起这个工具。看单词就很明白：Pretty 是漂亮，Prettier 的功能不言而喻，就是把代码变得更好看。那它和 ESLint 有什么区别呢？

先看 ESLint。Lint 在计算机里的意思，是标记或检查源代码中不符合规范或者可疑的代码片段，关键在于"检查"。它能检查出两类错误。第一类可以称为代码质量问题：比如 `var a = 1` 会提示 unexpected var, use let or const instead，格式本身没问题，但这么写未来可能造成 bug 或运行问题。第二类是代码风格问题：加不加分号、用双引号还是单引号、一行最多多少字符。这类问题没那么重要：代码质量出问题代表程序可能潜在 bug，风格问题充其量只是看着不爽，两者的严重级别不一样。

于是 Prettier 出现了。它自称是 opinionated code formatter，一个"有主见"的代码格式化工具。它认为格式肯定重要，但格式问题太麻烦，所以由它来帮你定好：不需要再思考单引号还是双引号这些乱七八糟的问题，都交给它处理。最后的结果可能不是让你完全满意，但绝对不会丑。况且它还留了一部分配置项，可以通过 .prettierrc 文件修改，不过它的理念是 few options，不给你太多选项，我帮你弄满意就行。

简单了解一下使用方式。和 ESLint 一样，它首先提供一个 CLI 命令行工具，用 `npm install --save-dev --save-exact prettier` 安装，我这里已经装好了。先把 main.ts 的代码格式故意弄乱，然后执行 `npx prettier --write` 加上文件名（输入文件夹名称也可以），回车后显示耗时 212ms，刚才很乱的代码就变得井井有条了。

除了手动执行命令，显然还需要像 ESLint 一样在编辑器里快速操作。安装对应的 Prettier 插件（5.8.0 版本）之后就可以快捷操作了。按 Shift Command P，输入 Format Document，就能完成格式化；它也支持快捷键 Shift Option F。按下后会弹出菜单让我们选择，因为这个快捷键绑定了两个选项：一个是 VS Code 默认的格式化，另一个是 Prettier 格式化，选第一个 Prettier Code Formatter 就完成了操作。

刚才的选择其实等于在 settings.json 的编辑器配置里，把 editor.defaultFormatter 设置成了 esbenp.prettier-vscode，之后所有格式化都由 Prettier 完成。文档里有更详细的解释：如果想所有文件都用 Prettier 格式化，可以把配置整段复制过来；只想对某些特定文件格式化，就修改配置数组里的项。它还支持保存后直接格式化，把文档里的 format on save 配置拷贝过去就能生效，这里就不多展开了。

到这里可以给两个工具定位了：Prettier 接管了代码风格问题，ESLint 负责代码质量问题，两者配合可以完全解决这两类问题。但实际使用时配置有些小麻烦：Prettier 和 ESLint 一起使用会有冲突，因为 Prettier 自己有一套玩法，而 ESLint 也有代码格式的检查。官方文档里有一个 Integration with Linters 模块，解决办法是用 eslint-plugin-prettier，分两步走。

第一步，禁用所有和 Prettier 冲突的 ESLint 规则：既然要让 Prettier 帮你格式化代码，格式这块 ESLint 就别管了，听 Prettier 的。第二步，把 Prettier 的规则导入 ESLint 中。为什么要这么做？因为希望 ESLint 成为所有错误的统一来源：格式错误也通过 ESLint 显示，这样在编辑器和命令行中就能看到所有错误；编辑器里有实时显示，写错立刻标红；同时用 ESLint fix 的时候，这些格式问题也能一并修复。这就是这个插件的工作原理。

在 Vue 代码中使用 Prettier 和 ESLint，官方还推出了一个特殊的插件 eslint-plugin-prettier-vue。因为 Vue 文件不是普通的 JS 文件，而是多种文件的混合体，需要一些特殊配置，这里就不演示整个过程了。我会创建一个分支专门添加 Prettier 配置，想用的同学切换到对应分支安装即可。

这节课讲了格式化代码的利器 Prettier，对比了它和 ESLint 的区别，讲了安装和简单使用。最重要的是理解工具的定位：自动把代码格式改得更漂亮，同时可以和 ESLint 配合使用。谢谢大家。
