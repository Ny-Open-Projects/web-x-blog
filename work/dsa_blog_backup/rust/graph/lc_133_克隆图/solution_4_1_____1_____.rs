// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133986698
// LeetCode 133. 克隆图 — Rust 版

// 方案4（BFS，visited 以节点对象为键）
use std::cell::RefCell; // 引入依赖
use std::collections::{HashMap, VecDeque}; // 引入依赖
use std::rc::Rc; // 引入依赖

#[derive(Debug)]
struct Node {
    // 定义类型
    val: i32,
    neighbors: Vec<Rc<RefCell<Node>>>,
}

type P = Rc<RefCell<Node>>; // 定义类型

fn new_node(val: i32) -> P {
    // 定义函数/方法 new_node
    Rc::new(RefCell::new(Node {
        // Rc::new(RefCell::new(Node {
        val,
        neighbors: Vec::new(),
    })) // }))
}

fn clone_graph(node: Option<P>) -> Option<P> {
    // 定义函数/方法 clone_graph
    let node = node?; // 把 节点? 存入 节点
                      // visited 以节点对象（Rc 指针地址）为键
    let mut visited: HashMap<usize, P> = HashMap::new(); // 把 HashMap::new(); 写入 let mut visited: HashMap<usize, P>
    visited.insert(Rc::as_ptr(&node) as usize, new_node(node.borrow().val));
    let mut q: VecDeque<P> = VecDeque::new(); // 把 VecDeque::new(); 写入 let mut q: VecDeque<P>
    q.push_back(node.clone()); // 节点 追加 节点.clone());
    while let Some(n) = q.pop_front() {
        // 边取边处理，取空即停
        let nbrs = n.borrow().neighbors.clone(); // 把 元素个数.borrow().neighbors.clone() 存入 nbrs
        let nclone = visited // 把 已访问集合 存入 nclone
            .get(&(Rc::as_ptr(&n) as usize)) // 查找 按位与 (Rc::as_ptr( 按位与 元素个数) as usize))
            .cloned() // cloned()
            .expect("current node must be visited"); // expect(「current 节点 must be 已访问集合」);
        for ne in &nbrs {
            // 逐个取出 nbrs 的元素（ne）
            let key = Rc::as_ptr(ne) as usize; // 把 Rc::as_ptr(ne) as usize 存入 key
            if !visited.contains_key(&key) {
                // 若 取反 已访问集合.contains_key( 按位与 key
                q.push_back(ne.clone()); // 节点 追加 ne.clone());
                visited.insert(key, new_node(ne.borrow().val)); // 已访问集合 插入 key, new_node(ne.borrow().值));
            }
            let neclone = visited // 把 已访问集合 存入 neclone
                .get(&key) // 查找 按位与 key)
                .cloned() // cloned()
                .expect("neighbor must be visited"); // expect(「neighbor must be 已访问集合」);
            nclone.borrow_mut().neighbors.push(neclone); // 把 neclone 压入栈/数组尾部
        }
    }
    Some(
        visited // 已访问集合
            .get(&(Rc::as_ptr(&node) as usize)) // 查找 按位与 (Rc::as_ptr( 按位与 节点) as usize))
            .cloned() // cloned()
            .expect("root must be visited"),
    )
}

fn build_graph(adj: &[&[i32]]) -> P {
    // 定义函数/方法 build_graph
    let n = adj.len(); // 把 邻接表.长度() 存入 元素个数
    let mut nodes: Vec<P> = Vec::with_capacity(n + 1); // 把 Vec::with_capacity(元素个数 加 1); 写入 let mut nodes: Vec<P>
    nodes.push(new_node(0)); // 占位，下标从 1 开始
    for i in 1..=n {
        // 逐个取出 1 的元素（下标 i）
        nodes.push(new_node(i as i32)); // 把 new_node(下标 i as i32 压入栈/数组尾部
    }
    for (idx, nbrs) in adj.iter().enumerate() {
        // for (idx, nbrs) in 邻接表.iter().enumerate() {
        for &nb in nbrs.iter() {
            // for 按位与 nb in nbrs.iter() {
            let target = nodes[nb as usize].clone(); // 把 nodes[nb as usize].clone() 存入 目标值
            nodes[idx + 1].borrow_mut().neighbors.push(target); // 把 目标值 压入栈/数组尾部
        }
    }
    nodes[1].clone() // nodes[1].clone()
}

// 收集签名：每个节点的邻居值列表（排序后），按节点 val 键控
fn signature(root: &P) -> HashMap<i32, Vec<i32>> {
    // 定义函数/方法 signature
    fn dfs(n: &P, vis: &mut HashMap<i32, Vec<i32>>) {
        // 定义函数/方法 dfs
        let v = n.borrow().val; // 把 元素个数.borrow().值 存入 值
        if vis.contains_key(&v) {
            // 若 vis.contains_key( 按位与 值
            return; // return;
        }
        let mut vals: Vec<i32> = n // 把 元素个数 写入 let mut vals: Vec<i32>
            .borrow() // borrow()
            .neighbors // neighbors
            .iter() // iter()
            .map(|x| x.borrow().val) // 映射表( 按位或 x 按位或 x.borrow().值)
            .collect(); // collect();
        vals.sort_unstable(); // vals.sort_unstable();
        vis.insert(v, vals); // vis 插入 值, vals);
        let nbrs = n.borrow().neighbors.clone(); // 把 元素个数.borrow().neighbors.clone() 存入 nbrs
        for x in &nbrs {
            // 逐个取出 nbrs 的元素（x）
            dfs(x, vis); // dfs(x, vis);
        }
    }
    let mut vis = HashMap::new(); // 把 HashMap::new(); 写入 let mut vis
    dfs(root, &mut vis); // dfs(根节点, 按位与 mut vis);
    vis // vis
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let adj: [&[i32]; 4] = [&[2, 4], &[1, 3], &[2, 4], &[1, 3]];
    let root = build_graph(&adj); // 把 build_graph( 按位与 邻接表) 存入 根节点
    let cloned = clone_graph(Some(root.clone())).expect("cloneGraph returned null");
    assert!(!Rc::ptr_eq(&root, &cloned), "not a deep copy (same object)"); // 断言校验
    let sig = signature(&cloned); // 把 signature( 按位与 cloned) 存入 sig
    let expected: [(i32, Vec<i32>); 4] = [
        (1, vec![2, 4]),
        (2, vec![1, 3]),
        (3, vec![2, 4]),
        (4, vec![1, 3]),
    ];
    for (k, b) in &expected {
        // for (下标 k, b) in 按位与 expected {
        let a = sig // 把 sig 存入 数组
            .get(k) // 查找 下标 k)
            .unwrap_or_else(|| panic!("signature missing at {}", k));
        assert_eq!(a, b, "signature mismatch at {}", k); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
