// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135038527
// LeetCode 217. 存在重复元素 — Rust 版（方案1）
use std::collections::HashSet; // 引入依赖
fn contains_duplicate(nums: &[i32]) -> bool {
    // 定义函数/方法 contains_duplicate
    let set: HashSet<i32> = nums.iter().cloned().collect(); // 把 数组.iter().cloned().collect(); 写入 let set: HashSet<i32>
    set.len() != nums.len() // 把 数组.长度() 写入 set.len() !
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert!(contains_duplicate(&[1, 2, 3, 1])); // 断言校验
    assert!(!contains_duplicate(&[1, 2, 3, 4])); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
