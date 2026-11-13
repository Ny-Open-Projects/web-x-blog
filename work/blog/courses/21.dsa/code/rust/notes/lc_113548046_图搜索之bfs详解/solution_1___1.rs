// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113548046
// 图搜索之BFS详解 — Rust 版（方案1）
fn bfs_order(graph: &[Vec<i32>], start: usize) -> Vec<i32> {
    // 定义函数/方法 bfs_order
    let n = graph.len(); // 把 graph.长度() 存入 元素个数
    let mut visited = vec![false; n]; // 把 vec取反 [false; 元素个数]; 写入 let mut visited
    let mut order = Vec::new(); // 把 Vec::new(); 写入 let mut order
    let mut queue = std::collections::VecDeque::new(); // 把 std::collections::VecDeque::new(); 写入 let mut queue
    visited[start] = true; // 把 true; 写入 visited[start]
    queue.push_back(start); // 队列 追加 起点);
    while let Some(c) = queue.pop_front() {
        // 边取边处理，取空即停
        order.push(c as i32); // 把 字符 as i32 压入栈/数组尾部
        for &nx in &graph[c] {
            // for 按位与 nx in 按位与 graph[字符] {
            if !visited[nx as usize] {
                // 若 取反 已访问集合[nx as usize]
                visited[nx as usize] = true; // 把 true; 写入 visited[nx as usize]
                queue.push_back(nx as usize); // 队列 追加 nx as usize);
            }
        }
    }
    order // order
}
fn main() {
    // 程序入口：跑内嵌自测用例
    // 6节点图: 0-1,0-2,1-3,1-4,2-5
    let g = vec![vec![1, 2], vec![3, 4], vec![5], vec![], vec![], vec![]];
    assert_eq!(bfs_order(&g, 0), vec![0, 1, 2, 3, 4, 5]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
