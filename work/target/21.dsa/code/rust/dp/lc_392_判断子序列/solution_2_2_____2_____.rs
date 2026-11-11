// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753613
// LeetCode 392. 判断子序列 — Rust 版（方案2）
fn is_subsequence(s: String, t: String) -> bool {
    // 定义判定函数 is_subsequence
    let (sb, tb) = (s.as_bytes(), t.as_bytes()); // 把 (字符串.as_bytes(), 另一字符串.as_bytes()); 写入 let (sb, tb)
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    for &c in tb {
        // for 按位与 字符 in tb {
        if i < sb.len() && sb[i] == c {
            i += 1;
        } // 若 下标 i 小于 sb.长度() 且 sb[下标 i] 等于 字符 { 下标 i 累加 1; }
    }
    i == sb.len() // 把 赋值为 sb.长度() 写入 下标 i
}
fn main() {
    assert!(is_subsequence("abc".into(), "ahbgdc".into()));
    assert!(!is_subsequence("axc".into(), "ahbgdc".into()));
    println!("PASS");
} // 程序入口：跑内嵌自测用例
