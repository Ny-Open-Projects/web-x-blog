// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133531071
// LeetCode 169. 多数元素 — Rust 版（方案1）
use std::collections::HashMap; // 引入依赖
fn majority_element(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 majority_element
    let mut counts: HashMap<i32, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut counts: HashMap<i32, i32>
    let mut best = (nums[0], 0); // 把 (数组[0], 0); 写入 let mut best
    for &v in &nums {
        let c = counts.entry(v).or_insert(0);
        *c += 1;
        if *c > best.1 {
            best = (v, *c);
        }
    }
    best.0 // 当前最优.0
}
fn main() {
    assert_eq!(majority_element(vec![3, 2, 3]), 3);
    assert_eq!(majority_element(vec![2, 2, 1, 1, 1, 2, 2]), 2);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
