// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130644389
// LeetCode 198. 打家劫舍 — Rust 版（方案2）
fn rob(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 rob
    let (mut a, mut b) = (0, 0); // 把 (0, 0); 写入 let (mut a, mut b)
    for v in nums {
        let t = (b).max(a + v);
        a = b;
        b = t;
    } // 逐个取出 数组 的元素（值）
    b
}
fn main() {
    assert_eq!(rob(vec![1, 2, 3, 1]), 4);
    assert_eq!(rob(vec![2, 7, 9, 3, 1]), 12);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
