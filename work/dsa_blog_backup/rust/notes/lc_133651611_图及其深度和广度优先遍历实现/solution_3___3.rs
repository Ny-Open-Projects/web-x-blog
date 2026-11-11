// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
// LeetCode 133651611. 图及其深度和广度优先遍历实现 — Rust 版（方案3）
use std::collections::{HashMap, HashSet}; // 引入依赖

#[derive(Default)]
struct Graph {
    // 定义类型
    adj: HashMap<i32, Vec<i32>>,
}

impl Graph {
    // 实现块
    fn add_edge(&mut self, from: i32, to: i32) {
        // 定义函数/方法 add_edge
        self.adj.entry(from).or_default().push(to); // 把 to 压入栈/数组尾部
        self.adj.entry(to).or_default().push(from); // 把 from 压入栈/数组尾部
    }

    fn dfs(&self, start: i32) -> Vec<i32> {
        // 定义函数/方法 dfs
        let mut visited: HashSet<i32> = HashSet::new(); // 把 HashSet::new(); 写入 let mut visited: HashSet<i32>
        let mut result: Vec<i32> = vec![]; // 把 vec取反 []; 写入 let mut result: Vec<i32>
        self.dfs_helper(start, &mut visited, &mut result); // self.dfs_helper(起点, 按位与 mut 已访问集合, 按位与 mut 结果);
        result // 结果
    }

    fn dfs_helper(&self, node: i32, visited: &mut HashSet<i32>, result: &mut Vec<i32>) {
        // 定义函数/方法 dfs_helper
        if visited.contains(&node) {
            // 若 已访问集合 是否包含 按位与 节点
            return; // return;
        }
        visited.insert(node); // 已访问集合 插入 节点);
        result.push(node); // 把 节点 压入栈/数组尾部
        if let Some(neighbors) = self.adj.get(&node) {
            // 若 let Some(neighbors) 赋值为 self.邻接表 查找 按位与 节点
            for &neighbor in neighbors {
                // for 按位与 neighbor in neighbors {
                self.dfs_helper(neighbor, visited, result); // self.dfs_helper(neighbor, 已访问集合, 结果);
            }
        }
    }

    fn bfs(&self, start: i32) -> Vec<i32> {
        // 定义函数/方法 bfs
        let mut visited: HashSet<i32> = HashSet::new(); // 把 HashSet::new(); 写入 let mut visited: HashSet<i32>
        let mut result: Vec<i32> = vec![]; // 把 vec取反 []; 写入 let mut result: Vec<i32>
        let mut queue: std::collections::VecDeque<i32> = std::collections::VecDeque::new();
        queue.push_back(start); // 队列 追加 起点);
        visited.insert(start); // 已访问集合 插入 起点);

        while let Some(node) = queue.pop_front() {
            // 边取边处理，取空即停
            result.push(node); // 把 节点 压入栈/数组尾部
            if let Some(neighbors) = self.adj.get(&node) {
                // 若 let Some(neighbors) 赋值为 self.邻接表 查找 按位与 节点
                for &neighbor in neighbors {
                    // for 按位与 neighbor in neighbors {
                    if !visited.contains(&neighbor) {
                        // 若 取反 已访问集合 是否包含 按位与 neighbor
                        visited.insert(neighbor); // 已访问集合 插入 neighbor);
                        queue.push_back(neighbor); // 队列 追加 neighbor);
                    }
                }
            }
        }
        result // 结果
    }
}

fn eq(a: &[i32], b: &[i32]) -> bool {
    // 定义函数/方法 eq
    a == b // 把 赋值为 b 写入 数组
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // case 1: 方形图 0-1-3-2-0
    let mut g1 = Graph::default(); // 把 Graph::default(); 写入 let mut g1
    g1.add_edge(0, 1); // g1.add_edge(0, 1);
    g1.add_edge(0, 2); // g1.add_edge(0, 2);
    g1.add_edge(1, 3); // g1.add_edge(1, 3);
    g1.add_edge(2, 3); // g1.add_edge(2, 3);
    assert!(eq(&g1.dfs(0), &[0, 1, 3, 2]), "case1 dfs(0)"); // 断言校验
    assert!(eq(&g1.bfs(0), &[0, 1, 2, 3]), "case1 bfs(0)"); // 断言校验

    // case 2: 从另一节点出发
    assert!(eq(&g1.dfs(2), &[2, 0, 1, 3]), "case2 dfs(2)"); // 断言校验
    assert!(eq(&g1.bfs(2), &[2, 0, 3, 1]), "case2 bfs(2)"); // 断言校验

    println!("PASS"); // 全部用例通过，输出 PASS
}
