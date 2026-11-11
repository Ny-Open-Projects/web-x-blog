// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/113764246
// 图搜索之DFS详解 — Rust 版（方案2）
fn dfs_order(graph: &[Vec<i32>], start: usize) -> Vec<i32> {
    // 定义函数/方法 dfs_order
    let mut visited = vec![false; graph.len()]; // 把 vec取反 [false; graph.长度()]; 写入 let mut visited
    let mut order = Vec::new(); // 把 Vec::new(); 写入 let mut order
    fn go(c: usize, graph: &[Vec<i32>], visited: &mut Vec<bool>, order: &mut Vec<i32>) {
        // 定义函数/方法 go
        visited[c] = true; // 把 true; 写入 visited[c]
        order.push(c as i32); // 把 字符 as i32 压入栈/数组尾部
        for &nx in &graph[c] {
            // for 按位与 nx in 按位与 graph[字符] {
            if !visited[nx as usize] {
                go(nx as usize, graph, visited, order);
            }
        }
    }
    go(start, graph, &mut visited, &mut order); // go(起点, graph, 按位与 mut 已访问集合, 按位与 mut order);
    order // order
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let g = vec![vec![1, 2], vec![3, 4], vec![5], vec![], vec![], vec![]];
    assert_eq!(dfs_order(&g, 0), vec![0, 1, 3, 4, 2, 5]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
