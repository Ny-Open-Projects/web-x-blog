// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 104. 二叉树的最大深度 — Rust 版
use std::cell::RefCell;
use std::rc::Rc; // 引入依赖 // 引入依赖

#[derive(Debug)]
struct TreeNode {
    // 定义类型
    val: i32,
    left: Option<Rc<RefCell<TreeNode>>>,
    right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    // 实现块
    fn new(val: i32) -> Rc<RefCell<TreeNode>> {
        // 定义函数/方法 new
        Rc::new(RefCell::new(TreeNode {
            val,
            left: None,
            right: None,
        })) // Rc::new(RefCell::new(TreeNode { 值, 左边界: None, 右边界: None }))
    }
}

// 层序数组构建二叉树，null 用 None 表示
fn build_tree(vals: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
    // 定义函数/方法 build_tree
    if vals.is_empty() || vals[0].is_none() {
        // 若 vals 是否为空 或 vals[0].is_none(
        return None; // 返回 None
    }
    let root = TreeNode::new(vals[0].unwrap()); // 把 TreeNode::new(vals[0].unwrap()) 存入 根节点
    let mut queue: Vec<Rc<RefCell<TreeNode>>> = vec![root.clone()];
    let mut i = 1; // 把 1; 写入 let mut i
    while !queue.is_empty() && i < vals.len() {
        // while 取反 队列 是否为空 且 下标 i 小于 vals.长度() {
        let node = queue.remove(0); // 把 队列 弹出 0) 存入 节点
        if i < vals.len() {
            // 若 下标 i 小于 vals.长度(
            if let Some(v) = vals[i] {
                // 若 let Some(值) 赋值为 vals[下标 i]
                let child = TreeNode::new(v); // 把 TreeNode::new(值) 存入 子节点
                node.borrow_mut().left = Some(child.clone()); // 把 Some(子节点.clone()); 写入 左边界
                queue.push(child); // 把 子节点 压入栈/数组尾部
            }
            i += 1; // 下标 i累加 1
        }
        if i < vals.len() {
            // 若 下标 i 小于 vals.长度(
            if let Some(v) = vals[i] {
                // 若 let Some(值) 赋值为 vals[下标 i]
                let child = TreeNode::new(v); // 把 TreeNode::new(值) 存入 子节点
                node.borrow_mut().right = Some(child.clone()); // 把 Some(子节点.clone()); 写入 右边界
                queue.push(child); // 把 子节点 压入栈/数组尾部
            }
            i += 1; // 下标 i累加 1
        }
    }
    Some(root) // Some(根节点)
}

// 主解法：DFS，叶子节点时刷新最大深度（与 blog 方案1一致）
fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    // 定义函数/方法 max_depth
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, l: i32, dep: &mut i32) {
        // 定义函数/方法 dfs
        if let Some(node) = n {
            // 若 let Some(节点) 赋值为 元素个数
            let node = node.borrow(); // 把 节点.borrow() 存入 节点
            if node.left.is_none() && node.right.is_none() {
                // 若 节点.左边界.is_none() 且 节点.右边界.is_none(
                *dep = (*dep).max(l);
            }
            dfs(node.left.as_ref(), l + 1, dep); // dfs(节点.左边界.as_ref(), 左指针 加 1, dep);
            dfs(node.right.as_ref(), l + 1, dep); // dfs(节点.右边界.as_ref(), 左指针 加 1, dep);
        }
    }
    let mut dep = 0; // 把 0; 写入 let mut dep
    dfs(root.as_ref(), 1, &mut dep); // dfs(根节点.as_ref(), 1, 按位与 mut dep);
    dep // dep
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let tests: Vec<(Vec<Option<i32>>, i32)> = vec![
        (vec![], 0),
        (vec![Some(1)], 1),
        (
            vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)],
            3,
        ),
        (vec![Some(1), None, Some(2), None, Some(3)], 3),
    ];
    for (idx, (vals, want)) in tests.iter().enumerate() {
        // for (idx, (vals, want)) in tests.iter().enumerate() {
        let got = max_depth(build_tree(vals)); // 把 max_depth(build_tree(vals)) 存入 got
        assert_eq!(got, *want, "case {} failed: got {} want {}", idx, got, want);
        // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
