// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771608
// LeetCode 674. 最长连续递增序列 — Rust 版（方案3）
fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 find_length_of_lcis
    let (mut best, mut cur) = (1, 1); // 把 (1, 1); 写入 let (mut best, mut cur)
    for i in 1..nums.len() {
        // 逐个取出 1 的元素（下标 i）
        if nums[i] > nums[i - 1] {
            cur += 1;
            if cur > best {
                best = cur;
            }
        } else {
            cur = 1;
        }
    }
    if nums.is_empty() {
        0
    } else {
        best
    } // 若 数组 是否为空 { 0 } else { 当前最优 }
}
fn main() {
    assert_eq!(find_length_of_lcis(vec![1, 3, 5, 4, 7]), 3);
    assert_eq!(find_length_of_lcis(vec![2, 2, 2, 2, 2]), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
