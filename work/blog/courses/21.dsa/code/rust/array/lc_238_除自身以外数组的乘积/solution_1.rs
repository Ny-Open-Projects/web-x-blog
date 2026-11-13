// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133907522
// LeetCode 238. 除自身以外数组的乘积 — Rust 版（方案1）
fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 product_except_self
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let mut out = vec![1i64; n]; // 把 vec取反 [1i64; 元素个数]; 写入 let mut out
    let mut left = 1i64; // 把 1i64; 写入 let mut left
    for i in 0..n {
        out[i] = left;
        left *= nums[i] as i64;
    } // 逐个取出 0 的元素（下标 i）
    let mut right = 1i64; // 把 1i64; 写入 let mut right
    for i in (0..n).rev() {
        out[i] *= right;
        right *= nums[i] as i64;
    }
    out.into_iter().map(|x| x as i32).collect() // out.into_iter().映射表( 按位或 x 按位或 x as i32).collect()
}
fn main() {
    assert_eq!(product_except_self(vec![1, 2, 3, 4]), vec![24, 12, 8, 6]);
    assert_eq!(
        product_except_self(vec![-1, 1, 0, -3, 3]),
        vec![0, 0, 9, 0, 0]
    );
    println!("PASS");
} // 程序入口：跑内嵌自测用例
