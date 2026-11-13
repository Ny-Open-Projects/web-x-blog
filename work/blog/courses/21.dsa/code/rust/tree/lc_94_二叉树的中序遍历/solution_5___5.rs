// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134915904
// LeetCode 94. 二叉树的中序遍历 — Rust 版（方案5）
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

fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    // 定义函数/方法 inorder_traversal
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    fn dfs(n: Option<&Rc<RefCell<TreeNode>>>, res: &mut Vec<i32>) {
        // 定义函数/方法 dfs
        let node = match n {
            Some(x) => x,
            None => return,
        };
        let nb = node.borrow(); // 把 节点.borrow() 存入 nb
        dfs(nb.left.as_ref(), res); // dfs(nb.左边界.as_ref(), 结果);
        res.push(nb.val); // 把 nb.值 压入栈/数组尾部
        dfs(nb.right.as_ref(), res); // dfs(nb.右边界.as_ref(), 结果);
    }
    dfs(root.as_ref(), &mut res); // dfs(根节点.as_ref(), 按位与 mut 结果);
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(inorder_traversal(None), Vec::<i32>::new()); // 断言校验
    assert_eq!(
        inorder_traversal(build_tree(&[Some(1), None, Some(2), None, Some(3)])),
        vec![1, 2, 3]
    ); // 断言校验
    assert_eq!(
        inorder_traversal(build_tree(&[Some(1), Some(2), Some(3)])),
        vec![2, 1, 3]
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
