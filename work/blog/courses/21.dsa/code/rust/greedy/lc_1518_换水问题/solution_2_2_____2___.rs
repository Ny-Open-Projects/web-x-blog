// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
// LeetCode 1518. 换水问题 — Rust 版（方案2）
fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
    // 定义函数/方法 num_water_bottles
    let mut ans = num_bottles; // 把 num_bottles; 写入 let mut ans
    let mut empty = num_bottles; // 把 num_bottles; 写入 let mut empty
    while empty >= num_exchange {
        // 把 num_exchange { 写入 while empty >
        let new_b = empty / num_exchange; // 把 empty 除以 num_exchange 存入 new_b
        ans += new_b; // 答案累加 new_b
        empty = new_b + empty % num_exchange; // 把 new_b 加 empty 对…取模 num_exchange; 写入 empty
    }
    ans // 答案
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(num_water_bottles(9, 3), 13); // 断言校验
    assert_eq!(num_water_bottles(15, 4), 19); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
