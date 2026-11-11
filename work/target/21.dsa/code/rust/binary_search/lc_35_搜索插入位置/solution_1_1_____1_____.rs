// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
// LeetCode 35. 搜索插入位置 — Rust 版（方案1：二分查找）
fn search_insert(nums: &[i32], target: i32) -> usize {
    // 定义函数/方法 search_insert
    let (mut left, mut right) = (0usize, nums.len()); // 把 (0usize, 数组.长度()); 写入 let (mut left, mut right)
    while left < right {
        // while 左边界 小于 右边界 {
        let mid = left + (right - left) / 2; // 把 左边界 加 (右边界 减 左边界) 除以 2 存入 中点
        if nums[mid] < target {
            left = mid + 1;
        } else {
            right = mid;
        } // 若 数组[中点] 小于 目标值 { 左边界 赋值为 中点 加 1; } else { 右边界 赋值为 中点; }
    }
    left // 左边界
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let a1 = [1, 2, 3]; // 把 [1, 2, 3] 存入 a1
    let a2 = [1, 3, 5, 6]; // 把 [1, 3, 5, 6] 存入 a2
    let cases = [
        (&a1[..], 1, 0usize),
        (&a2[..], 5, 2),
        (&a2[..], 2, 1),
        (&a2[..], 7, 4),
        (&a2[..], 0, 0),
    ];
    for (nums, t, want) in cases {
        // for (数组, 另一字符串, want) in cases {
        assert_eq!(search_insert(nums, t), want); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
