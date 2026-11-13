# 新语言代码生成规范（rust/lua/c/cpp/r/zig/dart）

## 总原则
1. **每个文件自包含**：类型定义（TreeNode/ListNode 等）、build 辅助函数、解法函数、main 测试全在一个文件
2. **内嵌测试用例**：与现有 Go/TS 文件中的用例保持一致（LeetCode 官方示例），全部通过后打印 `PASS`（大写，最后一行）
3. **来源注释**：文件头部保留 `// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/<id>`（各语言注释语法）
4. **算法逻辑忠于原解法**：从 TS 参考文件提取逻辑（TS 是事实源），函数名保持 camelCase/snake_case 按语言惯例
5. **null 表示**：层序数组建树时空节点用各语言惯用方式（Option/None、nil、"null"、nullopt、NA、-1 哨兵、null）

## 目录结构
`dsa/{lang}/{topic}/{problem_dir}/solution_{N}_{desc}.{ext}`
- 与 ts/go/java 完全同构，文件名去扩展名一致
- 扩展名：`.rs .lua .c .cpp .R .zig .dart`

## 运行命令（验证）
- rust: `rustc -O file.rs -o bin && ./bin`
- lua: `lua file.lua`
- c: `clang -O2 file.c -o bin && ./bin`
- cpp: `clang++ -std=c++17 -O2 file.cpp -o bin && ./bin`
- r: `Rscript file.R`
- zig: `~/langs/zig/zig run file.zig`
- dart: `~/langs/dart-sdk/bin/dart run file.dart`
- 批量: `_tools/verify_new.sh <lang> [topic]`

## 语言要点
- **rust**: `Option<Rc<RefCell<TreeNode>>>` 树节点；嵌套 fn 递归；assert_eq! + println!("PASS")
- **lua**: metatable 模拟类；closure 递归（local function）；"null" 字符串占位；assert + print("PASS")
- **c**: malloc/free 手动内存；INT_MIN 哨兵表示 null；队列用数组；free_tree 释放；printf("PASS\n")
- **cpp**: std::optional<int> 层序数组；std::queue；assert + std::cout << "PASS"
- **r**: ⚠️ **树/链表/图节点必须用 environment 引用语义**（`new.env(parent=emptyenv())`，list 是值语义改副本！）；⚠️ **动态键列表必须预分配** `vector("list", n)`（`list()[[key]]` 读缺失下标直接报错）；`<<-` 闭包赋值；stopifnot + cat("PASS\n")；NA 表示 null；Rscript 路径 ~/langs/R.framework/Versions/4.3-x86_64/Resources/Rscript
- **zig**: ?*TreeNode 可空指针；ArenaAllocator；-1 哨兵；std.debug.print("PASS\n")；⚠️ Zig 0.14.1 的 `@memset` 对二维 bool 数组需元素类型 `@memset(&arr, [1]bool{false} ** N)`；嵌套 fn 参数名不得遮蔽外层变量名
- **dart**: TreeNode? 可空；null 直接用；throw StateError 失败；print('PASS')

## 试点参考模板
`dsa/{各新语言}/tree/lc_104_二叉树的最大深度/solution_1___1.{ext}` — 全部已验证 PASS

## 生成流程（每题）
1. 读 `dsa/ts/{topic}/{problem}/` 下所有 solution_*.ts（事实源）与对应 `_meta` blog 引用
2. 每个解法生成 7 个新语言文件
3. 用 `_tools/verify_new.sh <lang> {topic}` 或单文件命令验证
4. FAIL 的修复直至 PASS；无法修复的记录到报告
