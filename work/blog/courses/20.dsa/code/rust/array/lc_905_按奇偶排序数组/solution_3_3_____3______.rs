// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134893847
// LeetCode 905. 按奇偶排序数组 — Rust 版（方案3）
fn sort_array_by_parity(mut nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 sort_array_by_parity
    let mut pos = 0usize; // 把 0usize; 写入 let mut pos
    for i in 0..nums.len() {
        // 逐个取出 0 的元素（下标 i）
        if nums[i] % 2 == 0 {
            nums.swap(pos, i);
            pos += 1;
        } // 若 数组[下标 i] 对…取模 2 等于 0 { 数组.交换 pos, 下标 i); pos 累加 1; }
    }
    nums // 数组
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = sort_array_by_parity(vec![3, 1, 2, 4]); // 把 sort_array_by_parity(vec取反 [3,1,2,4]) 存入 got
    assert_eq!(got.len(), 4); // 断言校验
    assert!(got[0] % 2 == 0 && got[1] % 2 == 0); // 断言校验
    assert!(got[2] % 2 != 0 && got[3] % 2 != 0); // 断言校验
    let got2 = sort_array_by_parity(vec![1, 2, 3]); // 把 sort_array_by_parity(vec取反 [1,2,3]) 存入 got2
    assert_eq!(got2[1], 1); // 断言校验
    assert_eq!(got2[0], 2); // 断言校验
    assert_eq!(got2[2], 3); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
