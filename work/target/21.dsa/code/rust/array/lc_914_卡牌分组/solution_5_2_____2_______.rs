// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134934324
// LeetCode 914. 卡牌分组 — Rust 版（方案5）
fn gcd(a: i32, b: i32) -> i32 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
} // 定义函数/方法 gcd
fn has_groups_size_x(deck: Vec<i32>) -> bool {
    // 定义函数/方法 has_groups_size_x
    use std::collections::HashMap; // 引入依赖
    let mut counts: HashMap<i32, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut counts: HashMap<i32, i32>
    for &c in &deck {
        *counts.entry(c).or_insert(0) += 1;
    } // 把 1; } 写入 for &c in &deck { *counts.entry(c).or_insert(0) +
    let mut g = 0; // 把 0; 写入 let mut g
    for v in counts.values() {
        g = gcd(g, *v);
    } // 逐个取出 counts 的元素（值）
    g >= 2 // 把 2 写入 g >
}
fn main() {
    assert!(has_groups_size_x(vec![1, 2, 3, 4, 4, 3, 2, 1]));
    assert!(!has_groups_size_x(vec![1, 1, 1, 2, 2, 2, 3, 3]));
    assert!(!has_groups_size_x(vec![1]));
    println!("PASS");
} // 程序入口：跑内嵌自测用例
