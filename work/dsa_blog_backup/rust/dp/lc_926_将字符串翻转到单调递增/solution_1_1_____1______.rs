// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130659442
// LeetCode 926. 将字符串翻转到单调递增 — Rust 版（方案1）
fn min_flips_mono_incr(s: String) -> i32 {
    // 定义函数/方法 min_flips_mono_incr
    let mut ones = 0i32; // 把 0i32; 写入 let mut ones
    let mut flips = 0i32; // 把 0i32; 写入 let mut flips
    for c in s.bytes() {
        // 逐个取出 字符串 的元素（字符）
        if c == b'1' {
            ones += 1;
        }
        // 若 字符 等于 b'1' { ones 累加 1; }
        else {
            // 否则
            flips += 1; // flips累加 1
            if ones < flips {
                flips = ones;
            } // 若 ones 小于 flips { flips 赋值为 ones; }
        }
    }
    flips // flips
}
fn main() {
    assert_eq!(min_flips_mono_incr("00110".into()), 1);
    assert_eq!(min_flips_mono_incr("010110".into()), 2);
    assert_eq!(min_flips_mono_incr("00011000".into()), 2);
    println!("PASS");
} // 程序入口：跑内嵌自测用例
