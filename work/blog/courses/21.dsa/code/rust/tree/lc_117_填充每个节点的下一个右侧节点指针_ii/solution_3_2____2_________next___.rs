// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298
// LeetCode 117. 填充每个节点的下一个右侧节点指针 II — Rust 版（方案3）
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

#[derive(Debug)]
struct NNode {
    val: i32,
    left: Option<Rc<RefCell<NNode>>>,
    right: Option<Rc<RefCell<NNode>>>,
    next: Option<Rc<RefCell<NNode>>>,
} // 定义类型
impl NNode {
    fn new(v: i32) -> Rc<RefCell<NNode>> {
        Rc::new(RefCell::new(NNode {
            val: v,
            left: None,
            right: None,
            next: None,
        }))
    }
} // 定义函数/方法 new
fn build_ntree(vals: &[i32]) -> Option<Rc<RefCell<NNode>>> {
    // 定义函数/方法 build_ntree
    if vals.is_empty() {
        return None;
    } // 若 vals 是否为空 { return None; }
    let root = NNode::new(vals[0]); // 把 NNode::new(vals[0]) 存入 根节点
    let mut q = vec![root.clone()]; // 把 vec取反 [根节点.clone()]; 写入 let mut q
    let mut i = 1; // 把 1; 写入 let mut i
    while !q.is_empty() && i < vals.len() {
        // while 取反 节点 是否为空 且 下标 i 小于 vals.长度() {
        let node = q.remove(0); // 把 节点 弹出 0) 存入 节点
        if i < vals.len() {
            let c = NNode::new(vals[i]);
            node.borrow_mut().left = Some(c.clone());
            q.push(c);
            i += 1;
        }
        if i < vals.len() {
            let c = NNode::new(vals[i]);
            node.borrow_mut().right = Some(c.clone());
            q.push(c);
            i += 1;
        }
    }
    Some(root) // Some(根节点)
}
fn connect(root: Option<Rc<RefCell<NNode>>>) -> Option<Rc<RefCell<NNode>>> {
    // 定义函数/方法 connect
    let mut cur = match root.clone() {
        Some(x) => x,
        None => return None,
    };
    loop {
        // loop {
        let dummy = NNode::new(0); // 把 NNode::new(0) 存入 哨兵节点
        let mut prev = dummy.clone(); // 把 哨兵节点.clone(); 写入 let mut prev
        let mut node = Some(cur.clone()); // 把 Some(当前值.clone()); 写入 let mut node
        let mut any = false; // 把 false; 写入 let mut any
        while let Some(n) = node {
            // 边取边处理，取空即停
            let nb = n.borrow(); // 把 元素个数.borrow() 存入 nb
            if let Some(l) = nb.left.clone() {
                // 若 let Some(左指针) 赋值为 nb.左边界.clone(
                prev.borrow_mut().next = Some(l.clone()); // 把 Some(左指针.clone()); 写入 下一个
                prev = l; // 把 左指针; 写入 前一个
                any = true; // 把 true; 写入 any
            }
            if let Some(r) = nb.right.clone() {
                // 若 let Some(右指针) 赋值为 nb.右边界.clone(
                prev.borrow_mut().next = Some(r.clone()); // 把 Some(右指针.clone()); 写入 下一个
                prev = r; // 把 右指针; 写入 前一个
                any = true; // 把 true; 写入 any
            }
            node = nb.next.clone(); // 把 nb.下一个.clone(); 写入 节点
        }
        if !any {
            break;
        } // 若 取反 any { break; }
        let nxt = dummy.borrow().next.clone(); // 把 哨兵节点.borrow().下一个.clone() 存入 nxt
        match nxt {
            // 按情况匹配处理
            Some(n) => cur = n,
            None => break,
        }
    }
    root // 根节点
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(connect(None).is_none()); // 断言校验
    let root = connect(build_ntree(&[1, 2, 3, 4, 5, 6, 7])); // 把 connect(build_ntree( 按位与 [1, 2, 3, 4, 5, 6, 7])) 存入 根节点
    let mut levels: Vec<Vec<i32>> = Vec::new(); // 把 Vec::new(); 写入 let mut levels: Vec<Vec<i32>>
    let mut cur = root.clone(); // 把 根节点.clone(); 写入 let mut cur
    while let Some(c) = cur {
        // 边取边处理，取空即停
        let mut vals = Vec::new(); // 把 Vec::new(); 写入 let mut vals
        let mut node = Some(c.clone()); // 把 Some(字符.clone()); 写入 let mut node
        while let Some(n) = node {
            // 边取边处理，取空即停
            vals.push(n.borrow().val); // 把 元素个数.borrow( 压入栈/数组尾部
            node = n.borrow().next.clone(); // 把 元素个数.borrow().下一个.clone(); 写入 节点
        }
        levels.push(vals); // 把 vals 压入栈/数组尾部
        cur = c.borrow().left.clone().or_else(|| c.borrow().right.clone());
        if levels.len() > 5 {
            break;
        } // 若 levels.长度() 超过 5 { break; }
    }
    assert_eq!(levels, vec![vec![1], vec![2, 3], vec![4, 5, 6, 7]]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
