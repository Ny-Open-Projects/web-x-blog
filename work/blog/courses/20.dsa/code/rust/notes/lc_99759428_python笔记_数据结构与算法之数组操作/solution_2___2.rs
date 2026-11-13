// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428
// 数据结构与算法之数组操作 — Rust 版（方案2）
fn two_sum(nums: &[i32], target: i32) -> Vec<i32> {
    // 定义函数/方法 two_sum
    for i in 0..nums.len() {
        // 逐个取出 0 的元素（下标 i）
        for j in i + 1..nums.len() {
            // 逐个取出 下标 i 的元素（下标 j）
            if nums[i] + nums[j] == target {
                return vec![i as i32, j as i32];
            }
        }
    }
    vec![] // vec取反 []
}
fn max_sub_array(nums: &[i32]) -> i32 {
    // 定义函数/方法 max_sub_array
    let (mut best, mut cur) = (nums[0], nums[0]); // 把 (数组[0], 数组[0]); 写入 let (mut best, mut cur)
    for &v in nums.iter().skip(1) {
        // for 按位与 值 in 数组.iter().skip(1) {
        cur = if cur > 0 { cur + v } else { v }; // 把 if 当前值 超过 0 { 当前值 加 值 } else { 值 }; 写入 当前值
        best = best.max(cur); // 把 当前最优.取较大值 当前值); 写入 当前最优
    }
    best // 当前最优
}
fn rotate_array(nums: &[i32], k: i32) -> Vec<i32> {
    // 定义函数/方法 rotate_array
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let k = (k as usize) % n; // 把 (下标 k as usize) 对…取模 元素个数 存入 下标 k
    let mut v = nums.to_vec(); // 把 数组.to_vec(); 写入 let mut v
    v.rotate_right(k); // 值.rotate_right(下标 k);
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(two_sum(&[2, 7, 11, 15], 9), vec![0, 1]); // 断言校验
    assert_eq!(max_sub_array(&[-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6); // 断言校验
    assert_eq!(
        rotate_array(&[1, 2, 3, 4, 5, 6, 7], 3),
        vec![5, 6, 7, 1, 2, 3, 4]
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
