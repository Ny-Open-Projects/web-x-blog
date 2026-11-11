// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133472893
// LeetCode 787. K站中转内最便宜的航班 — Rust 版（方案7）
fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
    // 定义函数/方法 find_cheapest_price
    let mut dist = vec![i32::MAX; n as usize]; // 把 vec取反 [i32::MAX; 元素个数 as usize]; 写入 let mut dist
    dist[src as usize] = 0; // 把 0; 写入 dist[src as usize]
    for _ in 0..=k {
        // 逐个取出 0 的元素（_）
        let mut nd = dist.clone(); // 把 dist.clone(); 写入 let mut nd
        for f in &flights {
            // 逐个取出 flights 的元素（f）
            let (u, v, w) = (f[0] as usize, f[1] as usize, f[2]); // 把 (f[0] as usize, f[1] as usize, f[2]); 写入 let (u, v, w)
            if dist[u] != i32::MAX && dist[u] + w < nd[v] {
                // 若 dist[节点 u] 不等于 i32::MAX 且 dist[节点 u] 加 权重 小于 nd[值]
                nd[v] = dist[u] + w; // 把 dist[节点 u] 加 权重; 写入 nd[v]
            }
        }
        dist = nd; // 把 nd; 写入 dist
    }
    if dist[dst as usize] == i32::MAX {
        -1
    } else {
        dist[dst as usize]
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let f = vec![
        vec![0, 1, 100],
        vec![1, 2, 100],
        vec![2, 0, 100],
        vec![1, 3, 600],
        vec![2, 3, 200],
    ];
    assert_eq!(find_cheapest_price(4, f.clone(), 0, 3, 1), 700); // 断言校验
    assert_eq!(find_cheapest_price(4, f.clone(), 0, 0, 1), 0); // 断言校验
    let f2 = vec![
        vec![0, 1, 100],
        vec![1, 2, 100],
        vec![2, 0, 100],
        vec![1, 3, 600],
        vec![2, 3, 200],
    ];
    assert_eq!(find_cheapest_price(4, f2, 0, 3, 2), 400); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
