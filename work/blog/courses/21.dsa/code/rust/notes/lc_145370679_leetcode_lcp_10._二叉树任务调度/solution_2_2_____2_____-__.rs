// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — Rust 版（方案2：深度优先-优化）

struct TreeNode {
    // 二叉树节点：val 为自身执行时间（f64 承载均摊的 0.5）
    val: f64,
    left: Option<Box<TreeNode>>,
    right: Option<Box<TreeNode>>,
}

struct ArenaNode {
    // 建树中转用的 arena 节点（下标引用，规避 Box 的所有权问题）
    val: f64,
    left: Option<usize>,
    right: Option<usize>,
}

// 层序数组建树，None 表示空节点；先用 arena 组装，再转成 Box 链式树
fn build_tree(vals: &[Option<f64>]) -> Option<Box<TreeNode>> {
    if vals.is_empty() {
        return None;
    }
    let mut arena: Vec<ArenaNode> = Vec::new();
    arena.push(ArenaNode {
        val: vals[0].unwrap(),
        left: None,
        right: None,
    }); // 根节点
    let mut queue: std::collections::VecDeque<usize> = std::collections::VecDeque::new();
    queue.push_back(0); // 队列里只放非空节点的下标
    let mut i = 1; // 下一个待处理的数组位置
    while i < vals.len() {
        let p = match queue.pop_front() {
            // 出队一个父节点
            Some(p) => p,
            None => break,
        };
        if let Some(v) = vals[i] {
            // 左孩子
            let k = arena.len();
            arena.push(ArenaNode {
                val: v,
                left: None,
                right: None,
            });
            arena[p].left = Some(k);
            queue.push_back(k);
        }
        i += 1;
        if i < vals.len() {
            if let Some(v) = vals[i] {
                // 右孩子
                let k = arena.len();
                arena.push(ArenaNode {
                    val: v,
                    left: None,
                    right: None,
                });
                arena[p].right = Some(k);
                queue.push_back(k);
            }
            i += 1;
        }
    }
    // 递归把 arena 下标树转成 Box 链式树
    fn link(arena: &[ArenaNode], idx: Option<usize>) -> Option<Box<TreeNode>> {
        let i = idx?;
        let n = &arena[i];
        Some(Box::new(TreeNode {
            val: n.val,
            left: link(arena, n.left),
            right: link(arena, n.right),
        }))
    }
    link(&arena, Some(0))
}

// dfs 返回 (子树总耗时, 子树最小完成时间 max_exec)
fn dfs(root: Option<&TreeNode>) -> (f64, f64) {
    let node = match root {
        Some(n) => n,
        None => return (0.0, 0.0), // 空子树
    };
    let (left_sum, left_exec) = dfs(node.left.as_deref()); // 左子树的总耗时与最小完成时间
    let (right_sum, right_exec) = dfs(node.right.as_deref()); // 右子树的总耗时与最小完成时间
                                                              // 当前任务自身必须独占串行跑完；孩子任务两条机器可穿插：
                                                              // 下界取「较慢的一侧」与「两侧工作量均分到两台机器」的较大者
    let parallel = (left_sum + right_sum) / 2.0; // 两台机器均摊左右子树总工作量（浮点）
    let max_exec = node.val + f64::max(f64::max(left_exec, right_exec), parallel);
    (left_sum + right_sum + node.val, max_exec)
}

// 答案 = 整棵树的最小完成时间
fn minimal_execution_time(root: Option<&TreeNode>) -> f64 {
    dfs(root).1
}

fn main() {
    // 程序入口：跑内嵌自测用例（三个官方用例）
    let cases: Vec<(Vec<Option<f64>>, f64)> = vec![
        (vec![Some(47.0), Some(74.0), Some(31.0)], 121.0),
        (
            vec![
                Some(15.0),
                Some(21.0),
                None,
                Some(24.0),
                None,
                Some(27.0),
                Some(26.0),
            ],
            87.0,
        ),
        (
            vec![
                Some(1.0),
                Some(3.0),
                Some(2.0),
                None,
                None,
                Some(4.0),
                Some(4.0),
            ],
            7.5,
        ),
    ];
    let mut fail = false;
    for (vals, want) in cases {
        let tree = build_tree(&vals);
        let got = minimal_execution_time(tree.as_deref());
        if (got - want).abs() >= 1e-6 {
            // 浮点比较用 1e-6 容差
            println!("FAIL got {} want {}", got, want); // 失败打印 FAIL
            fail = true;
        }
    }
    if fail {
        std::process::exit(1); // 非零退出
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
