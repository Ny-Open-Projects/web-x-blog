// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134707891
// LeetCode 66. 加一 — Rust 版（方案1）
fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 plus_one
    for i in (0..digits.len()).rev() {
        // for 下标 i in (0..digits.长度()).rev() {
        if digits[i] < 9 {
            digits[i] += 1;
            return digits;
        } // 若 digits[下标 i] 小于 9 { digits[下标 i] 累加 1; return digits; }
        digits[i] = 0; // 把 0; 写入 digits[i]
    }
    let mut out = vec![1]; // 把 vec取反 [1]; 写入 let mut out
    out.extend(digits); // out.extend(digits);
    out // out
}
fn main() {
    assert_eq!(plus_one(vec![1, 2, 3]), vec![1, 2, 4]);
    assert_eq!(plus_one(vec![4, 3, 2, 1]), vec![4, 3, 2, 2]);
    assert_eq!(plus_one(vec![9]), vec![1, 0]);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
