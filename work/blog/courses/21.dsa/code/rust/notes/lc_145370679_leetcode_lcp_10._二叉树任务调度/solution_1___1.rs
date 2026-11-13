// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370679
// LeetCode LCP 10. 二叉树任务调度 — Rust 版（方案1：深度优先-贪心）

struct TreeNode {
    // 二叉树节点：val 为自身执行时间（f64 承载并行节省的 0.5）
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

// dfs 返回 (子树总耗时, 两台机器并行可节省的耗时)
fn dfs(root: Option<&TreeNode>) -> (f64, f64) {
    let node = match root {
        Some(n) => n,
        None => return (0.0, 0.0), // 空子树：总耗时 0，节省 0
    };
    let (a, b) = dfs(node.left.as_deref()); // a: 左子树总耗时, b: 左子树已节省
    let (c, d) = dfs(node.right.as_deref()); // c: 右子树总耗时, d: 右子树已节省
    let saved = if (c - 2.0 * d <= a && a <= c) || (a - 2.0 * b <= c && c <= a) {
        // 一侧的串行下界落在另一侧的耗时区间内：两台机器互相填空，左右几乎完全并行
        (a + c) / 2.0 // 浮点除法：总和为奇数时会出现 0.5
    } else if a - 2.0 * b > c {
        // 左子树串行段太长：右子树整体塞进左边空闲的那台机器
        b + c
    } else {
        // 右子树占主导：左子树整体塞进右边空闲的那台机器
        a + d
    };
    (a + c + node.val, saved) // 加上当前节点自身的执行时间
}

// 答案 = 子树总和 - 并行节省
fn minimal_execution_time(root: Option<&TreeNode>) -> f64 {
    let (total, saved) = dfs(root);
    total - saved
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
