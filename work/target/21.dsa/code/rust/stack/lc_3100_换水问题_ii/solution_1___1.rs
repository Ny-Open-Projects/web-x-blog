// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
// LeetCode 3100. 换水问题 II — Rust 版（方案1）
fn max_bottles_drunk(num_bottles: i32, mut num_exchange: i32) -> i32 {
    // 定义函数/方法 max_bottles_drunk
    let mut drunk = num_bottles; // 把 num_bottles; 写入 let mut drunk
    let mut empty = num_bottles; // 把 num_bottles; 写入 let mut empty
    while empty >= num_exchange {
        // 把 num_exchange { 写入 while empty >
        empty -= num_exchange; // empty累减 num_exchange
        num_exchange += 1; // num_exchange累加 1
        drunk += 1; // drunk累加 1
        empty += 1; // empty累加 1
    }
    drunk // drunk
}
fn main() {
    assert_eq!(max_bottles_drunk(10, 3), 13);
    assert_eq!(max_bottles_drunk(1, 2), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
