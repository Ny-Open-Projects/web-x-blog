// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Rust 版（方案3）
fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
    // 定义函数/方法 find_kth_largest
    let mut a = nums; // 把 数组; 写入 let mut a
    let n = a.len(); // 把 数组.长度() 存入 元素个数
    let length = n - 1; // 把 元素个数 减 1 存入 长度
    let mut i = length; // 把 长度; 写入 let mut i
    while i > length - (k as usize) && i > 0 {
        // while 下标 i 超过 长度 减 (下标 k as usize) 且 下标 i 超过 0 {
        for j in 0..i {
            // 逐个取出 0 的元素（下标 j）
            if a[j] > a[j + 1] {
                a.swap(j, j + 1);
            } // 若 数组[下标 j] 超过 数组[下标 j 加 1] { 数组.交换 下标 j, 下标 j 加 1); }
        }
        i -= 1; // 下标 i累减 1
    }
    a[length - (k as usize) + 1] // 数组[长度 减 (下标 k as usize) 加 1]
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5); // 断言校验
    assert_eq!(find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4); // 断言校验
    assert_eq!(find_kth_largest(vec![1], 1), 1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
