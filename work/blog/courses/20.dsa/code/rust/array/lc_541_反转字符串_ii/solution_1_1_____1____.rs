// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134588341
// LeetCode 541. 反转字符串II — Rust 版（方案1）
fn reverse_str(s: String, k: i32) -> String {
    // 定义函数/方法 reverse_str
    let chars: Vec<char> = s.chars().collect(); // 把 字符串.chars().collect(); 写入 let chars: Vec<char>
    let mut out = chars.clone(); // 把 chars.clone(); 写入 let mut out
    let n = chars.len(); // 把 chars.长度() 存入 元素个数
    let k = k as usize; // 把 下标 k as usize 存入 下标 k
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    while i < n {
        // while 下标 i 小于 元素个数 {
        let end = (i + k).min(n); // 把 (下标 i 加 下标 k).取较小值 元素个数) 存入 终点
        let mut l = i; // 把 下标 i; 写入 let mut l
        let mut r = end - 1; // 把 终点 减 1; 写入 let mut r
        while l < r {
            out.swap(l, r);
            l += 1;
            if r == 0 {
                break;
            }
            r -= 1;
        }
        i += 2 * k; // 下标 i累加 2 乘 下标 k
    }
    out.into_iter().collect() // out.into_iter().collect()
}
fn main() {
    assert_eq!(reverse_str("abcdefg".into(), 2), "bacdfeg");
    assert_eq!(reverse_str("abcd".into(), 2), "bacd");
    assert_eq!(reverse_str("abc".into(), 1), "abc");
    println!("PASS");
} // 程序入口：跑内嵌自测用例
