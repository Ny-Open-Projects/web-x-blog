// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Rust 版（方案11）
use std::collections::BinaryHeap; // 引入依赖
fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
    // 定义函数/方法 find_kth_largest
    let mut heap: BinaryHeap<i32> = BinaryHeap::new(); // 把 BinaryHeap::new(); 写入 let mut heap: BinaryHeap<i32>
    for v in nums {
        heap.push(v);
    } // 逐个取出 数组 的元素（值）
    for _ in 0..k - 1 {
        heap.pop();
    } // 逐个取出 0 的元素（_）
    heap.peek().copied().unwrap_or(-1) // 堆.peek().copied().unwrap_or( 减 1)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5); // 断言校验
    assert_eq!(find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4); // 断言校验
    assert_eq!(find_kth_largest(vec![1], 1), 1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
