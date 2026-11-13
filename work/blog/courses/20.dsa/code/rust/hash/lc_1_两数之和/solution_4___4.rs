// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
// LeetCode 1. 两数之和 — Rust 版（方案4：哈希表一次遍历）
use std::collections::HashMap; // 引入依赖
fn two_sum(nums: &[i32], target: i32) -> Vec<i32> {
    // 定义函数/方法 two_sum
    let mut seen: HashMap<i32, i32> = HashMap::new(); // 把 HashMap::new(); 写入 let mut seen: HashMap<i32, i32>
    for (i, &v) in nums.iter().enumerate() {
        // for (下标 i, 按位与 值) in 数组.iter().enumerate() {
        if let Some(&j) = seen.get(&(target - v)) {
            // 若 let Some( 按位与 下标 j) 赋值为 已见集合 查找 按位与 (目标值 减 值
            return vec![j, i as i32]; // 返回 vec取反 [下标 j, 下标 i as i32]
        }
        seen.insert(v, i as i32); // 已见集合 插入 值, 下标 i as i32);
    }
    vec![] // vec取反 []
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(two_sum(&[2, 7, 11, 15], 9), vec![0, 1]); // 断言校验
    assert_eq!(two_sum(&[3, 2, 4], 6), vec![1, 2]); // 断言校验
    assert_eq!(two_sum(&[3, 3], 6), vec![0, 1]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
