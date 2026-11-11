// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130663853
// LeetCode 1. 两数之和 — Rust 版（方案1：暴力双循环）
fn two_sum(nums: &[i32], target: i32) -> Vec<i32> {
    // 定义函数/方法 two_sum
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        for j in i + 1..n {
            // 逐个取出 下标 i 的元素（下标 j）
            if nums[i] + nums[j] == target {
                // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值
                return vec![i as i32, j as i32]; // 返回 vec取反 [下标 i as i32, 下标 j as i32]
            }
        }
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
