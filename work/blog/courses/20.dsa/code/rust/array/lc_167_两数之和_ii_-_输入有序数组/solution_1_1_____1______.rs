// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133524779
// LeetCode 167. 两数之和II — Rust 版（方案1）
fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    // 定义函数/方法 two_sum
    let (mut l, mut r) = (0usize, numbers.len() - 1); // 把 (0usize, numbers.长度() 减 1); 写入 let (mut l, mut r)
    while l < r {
        // while 左指针 小于 右指针 {
        let s = numbers[l] + numbers[r]; // 把 numbers[左指针] 加 numbers[右指针] 存入 字符串
        if s == target {
            return vec![l as i32 + 1, r as i32 + 1];
        }
        if s < target {
            l += 1;
        } else {
            r -= 1;
        } // 若 字符串 小于 目标值 { 左指针 累加 1; } else { 右指针 累减 1; }
    }
    vec![] // vec取反 []
}
fn main() {
    assert_eq!(two_sum(vec![2, 7, 11, 15], 9), vec![1, 2]);
    assert_eq!(two_sum(vec![2, 3, 4], 6), vec![1, 3]);
    assert_eq!(two_sum(vec![-1, 0], -1), vec![1, 2]);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
