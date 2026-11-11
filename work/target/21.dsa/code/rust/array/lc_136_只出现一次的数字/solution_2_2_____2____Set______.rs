// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468105
// LeetCode 136. 只出现一次的数字 — Rust 版（方案2）
fn single_number(nums: Vec<i32>) -> i32 {
    nums.iter().fold(0, |a, b| a ^ b)
} // 定义函数/方法 single_number
fn main() {
    assert_eq!(single_number(vec![2, 2, 1]), 1);
    assert_eq!(single_number(vec![4, 1, 2, 1, 2]), 4);
    assert_eq!(single_number(vec![1]), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
