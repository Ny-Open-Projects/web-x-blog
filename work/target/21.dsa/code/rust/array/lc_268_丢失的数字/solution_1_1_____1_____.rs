// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133968437
// LeetCode 268. 丢失的数字 — Rust 版（方案1）
fn missing_number(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 missing_number
    let n = nums.len() as i64; // 把 数组.长度() as i64 存入 元素个数
    let sum: i64 = nums.iter().map(|&x| x as i64).sum();
    (n * (n + 1) / 2 - sum) as i32 // (元素个数 乘 (元素个数 加 1) 除以 2 减 累计和) as i32
}
fn main() {
    assert_eq!(missing_number(vec![3, 0, 1]), 2);
    assert_eq!(missing_number(vec![0, 1]), 2);
    assert_eq!(missing_number(vec![9, 6, 4, 2, 3, 5, 7, 0, 1]), 8);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
