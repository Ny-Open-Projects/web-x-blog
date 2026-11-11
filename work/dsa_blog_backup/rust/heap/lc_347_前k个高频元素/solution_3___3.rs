// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
// LeetCode 347. 前K个高频元素 — Rust 版（方案3）
use std::collections::HashMap; // 引入依赖
fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    // 定义函数/方法 top_k_frequent
    let mut counts: HashMap<i32, i64> = HashMap::new(); // 把 HashMap::new(); 写入 let mut counts: HashMap<i32, i64>
    for &v in &nums {
        *counts.entry(v).or_insert(0) += 1;
    } // 把 1; } 写入 for &v in &nums { *counts.entry(v).or_insert(0) +
    let mut items: Vec<(i32, i64)> = counts.into_iter().collect();
    items.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
    items.into_iter().take(k as usize).map(|(v, _)| v).collect()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = top_k_frequent(vec![1, 1, 1, 2, 2, 3], 2); // 把 top_k_frequent(vec取反 [1, 1, 1, 2, 2, 3], 2) 存入 got
    let mut g = got.clone(); // 把 got.clone(); 写入 let mut g
    g.sort(); // 排序
    assert_eq!(g, vec![1, 2]); // 断言校验
    assert_eq!(top_k_frequent(vec![1], 1), vec![1]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
