// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108717090
// 减治策略之详解Dijkstra算法 — Rust 版（方案1）
fn dijkstra_shortest(graph: &[Vec<(usize, i32)>], start: usize) -> Vec<i32> {
    // 定义函数/方法 dijkstra_shortest
    let n = graph.len(); // 把 graph.长度() 存入 元素个数
    let mut dist = vec![i32::MAX; n]; // 把 vec取反 [i32::MAX; 元素个数]; 写入 let mut dist
    dist[start] = 0; // 把 0; 写入 dist[start]
    let mut visited = vec![false; n]; // 把 vec取反 [false; 元素个数]; 写入 let mut visited
    loop {
        // loop {
        let mut u = usize::MAX; // 把 usize::MAX; 写入 let mut u
        for i in 0..n {
            // 逐个取出 0 的元素（下标 i）
            if !visited[i] && (u == usize::MAX || dist[i] < dist[u]) {
                u = i;
            }
        }
        if u == usize::MAX || dist[u] == i32::MAX {
            break;
        } // 若 节点 u 等于 usize::MAX 或 dist[节点 u] 等于 i32::MAX { break; }
        visited[u] = true; // 把 true; 写入 visited[u]
        for &(v, w) in &graph[u] {
            // for 按位与 (值, 权重) in 按位与 graph[节点 u] {
            if dist[u] + w < dist[v] {
                dist[v] = dist[u] + w;
            }
        }
    }
    dist // dist
}
fn main() {
    // 程序入口：跑内嵌自测用例
    // 5节点: 0->1(10), 0->2(3), 1->2(1), 2->1(4), 1->3(2), 2->3(8), 3->4(7)
    let g = vec![
        vec![(1, 10), (2, 3)],
        vec![(2, 1), (3, 2)],
        vec![(1, 4), (3, 8)],
        vec![(4, 7)],
        vec![],
    ];
    let d = dijkstra_shortest(&g, 0); // 把 dijkstra_shortest( 按位与 g, 0) 存入 d
    assert_eq!(d[0], 0); // 断言校验
    assert_eq!(d[1], 7); // 0->2->1 = 3+4
    assert_eq!(d[2], 3); // 断言校验
    assert_eq!(d[3], 9); // 0->2->1->3 = 3+4+2
    assert_eq!(d[4], 16); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
