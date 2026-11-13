// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135167108
// LeetCode 128. 最长连续序列 — Rust 版（方案1）
use std::collections::HashSet; // 引入依赖
fn longest_consecutive(nums: &[i32]) -> i32 {
    // 定义函数/方法 longest_consecutive
    let set: HashSet<i32> = nums.iter().cloned().collect(); // 把 数组.iter().cloned().collect(); 写入 let set: HashSet<i32>
    let mut best = 0; // 把 0; 写入 let mut best
    for &num in &set {
        // for 按位与 num in 按位与 set {
        if !set.contains(&(num - 1)) {
            // 若 取反 set 是否包含 按位与 (num 减 1
            let mut cur = num; // 把 num; 写入 let mut cur
            let mut streak = 1; // 把 1; 写入 let mut streak
            while set.contains(&(cur + 1)) {
                cur += 1;
                streak += 1;
            }
            if streak > best {
                best = streak;
            } // 若 streak 超过 当前最优 { 当前最优 赋值为 streak; }
        }
    }
    best // 当前最优
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(longest_consecutive(&[100, 4, 200, 1, 3, 2]), 4); // 断言校验
    assert_eq!(longest_consecutive(&[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9); // 断言校验
    assert_eq!(longest_consecutive(&[]), 0); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
