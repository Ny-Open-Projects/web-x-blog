// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135064368
// LeetCode 349. 两个数组的交集 — Rust 版（方案13）
use std::collections::HashSet; // 引入依赖
fn intersection(nums1: &[i32], nums2: &[i32]) -> Vec<i32> {
    // 定义函数/方法 intersection
    let s1: HashSet<i32> = nums1.iter().cloned().collect(); // 把 数组1.iter().cloned().collect(); 写入 let s1: HashSet<i32>
    let mut seen: HashSet<i32> = HashSet::new(); // 把 HashSet::new(); 写入 let mut seen: HashSet<i32>
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    for &v in nums2 {
        // for 按位与 值 in 数组2 {
        if s1.contains(&v) && !seen.contains(&v) {
            // 若 s1 是否包含 按位与 值) 且 取反 已见集合 是否包含 按位与 值
            res.push(v); // 把 值 压入栈/数组尾部
            seen.insert(v); // 已见集合 插入 值);
        }
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(intersection(&[1, 2, 2, 1], &[2, 2]), vec![2]); // 断言校验
    assert_eq!(intersection(&[4, 9, 5], &[9, 4, 9, 8, 4]), vec![9, 4]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
