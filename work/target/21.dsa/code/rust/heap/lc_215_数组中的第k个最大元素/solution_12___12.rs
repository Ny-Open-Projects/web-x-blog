// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Rust 版（方案12）
fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
    // 定义函数/方法 find_kth_largest
    let mut a = nums; // 把 数组; 写入 let mut a
    a.sort_unstable_by(|x, y| y.cmp(x)); // 数组.sort_unstable_by( 按位或 x, y 按位或 y.cmp(x));
    a[(k - 1) as usize] // 数组[(下标 k 减 1) as usize]
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5); // 断言校验
    assert_eq!(find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4); // 断言校验
    assert_eq!(find_kth_largest(vec![1], 1), 1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
