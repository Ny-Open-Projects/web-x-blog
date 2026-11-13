// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134055742
// LeetCode 283. 移动零 — Rust 版（方案1）
fn move_zeroes(nums: &mut Vec<i32>) {
    // 定义函数/方法 move_zeroes
    let mut pos = 0usize; // 把 0usize; 写入 let mut pos
    for i in 0..nums.len() {
        // 逐个取出 0 的元素（下标 i）
        if nums[i] != 0 {
            nums.swap(pos, i);
            pos += 1;
        } // 若 数组[下标 i] 不等于 0 { 数组.交换 pos, 下标 i); pos 累加 1; }
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut v = vec![0, 1, 0, 3, 12];
    move_zeroes(&mut v);
    assert_eq!(v, vec![1, 3, 12, 0, 0]); // 断言校验
    let mut v2 = vec![0];
    move_zeroes(&mut v2);
    assert_eq!(v2, vec![0]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
