// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
// LeetCode 104. 二叉树的最大深度 — Rust 版（方案3：分治递归（紧凑版，附层序/相同树/中序辅助函数））
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

// 辅助：层序遍历按层分组
fn level_list(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
    // 定义函数/方法 level_list
    let mut res: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut res: Vec<Vec<i32>>
    let mut level: Vec<Rc<RefCell<TreeNode>>> = root.into_iter().collect();
    while !level.is_empty() {
        // while 取反 level 是否为空 {
        let mut vals = vec![]; // 把 vec取反 []; 写入 let mut vals
        let mut nxt = vec![]; // 把 vec取反 []; 写入 let mut nxt
        for node in &level {
            // 逐个取出 level 的元素（节点）
            let b = node.borrow(); // 把 节点.borrow() 存入 b
            vals.push(b.val); // 把 b.值 压入栈/数组尾部
            if let Some(l) = b.left.clone() {
                nxt.push(l);
            } // 若 let Some(左指针) 赋值为 b.左边界.clone() { nxt 追加 左指针); }
            if let Some(r) = b.right.clone() {
                nxt.push(r);
            } // 若 let Some(右指针) 赋值为 b.右边界.clone() { nxt 追加 右指针); }
        }
        res.push(vals); // 把 vals 压入栈/数组尾部
        level = nxt; // 把 nxt; 写入 level
    }
    res // 结果
}

// 辅助：判断两棵树是否相同
fn same_tree(a: Option<Rc<RefCell<TreeNode>>>, b: Option<Rc<RefCell<TreeNode>>>) -> bool {
    // 定义函数/方法 same_tree
    match (a, b) {
        // 按情况匹配处理
        (None, None) => true,
        (Some(x), Some(y)) => {
            let (xv, yv) = (x.borrow().val, y.borrow().val); // 把 (x.borrow().值, y.borrow().值); 写入 let (xv, yv)
            if xv != yv {
                return false;
            } // 若 xv 不等于 yv { return false; }
            let (xl, xr) = (x.borrow().left.clone(), x.borrow().right.clone());
            let (yl, yr) = (y.borrow().left.clone(), y.borrow().right.clone());
            same_tree(xl, yl) && same_tree(xr, yr) // same_tree(xl, yl) 且 same_tree(xr, yr)
        }
        _ => false,
    }
}

// 辅助：中序遍历
fn inorder_t(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    // 定义函数/方法 inorder_t
    fn go(n: Option<&Rc<RefCell<TreeNode>>>, out: &mut Vec<i32>) {
        // 定义函数/方法 go
        if let Some(x) = n {
            // 若 let Some(x) 赋值为 元素个数
            let b = x.borrow(); // 把 x.borrow() 存入 b
            go(b.left.as_ref(), out); // go(b.左边界.as_ref(), out);
            out.push(b.val); // 把 b.值 压入栈/数组尾部
            go(b.right.as_ref(), out); // go(b.右边界.as_ref(), out);
        }
    }
    let mut out = vec![]; // 把 vec取反 []; 写入 let mut out
    go(root.as_ref(), &mut out); // go(根节点.as_ref(), 按位与 mut out);
    out // out
}

// 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    // 定义函数/方法 max_depth
    match root {
        // 按情况匹配处理
        None => 0,
        Some(node) => {
            let b = node.borrow(); // 把 节点.borrow() 存入 b
            let l = max_depth(b.left.clone()); // 把 max_depth(b.左边界.clone()) 存入 左指针
            let r = max_depth(b.right.clone()); // 把 max_depth(b.右边界.clone()) 存入 右指针
            1 + if l > r { l } else { r } // 1 加 if 左指针 超过 右指针 { 左指针 } else { 右指针 }
        }
    }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let tests: Vec<(Vec<Option<i32>>, i32)> = vec![
        (
            vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)],
            3,
        ),
        (
            vec![
                Some(1),
                Some(2),
                Some(3),
                Some(4),
                Some(5),
                None,
                None,
                None,
                Some(6),
            ],
            4,
        ),
        (vec![], 0),
    ];
    for (idx, (vals, want)) in tests.iter().enumerate() {
        // for (idx, (vals, want)) in tests.iter().enumerate() {
        let got = max_depth(build_tree(vals)); // 把 max_depth(build_tree(vals)) 存入 got
        assert_eq!(got, *want, "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
