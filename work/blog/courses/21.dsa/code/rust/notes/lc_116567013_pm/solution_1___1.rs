// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Rust 版（方案1：Brute-Force 主串指针回退）
fn match_v1(p: &[u8], t: &[u8]) -> i64 {
    // 定义函数/方法 match_v1
    let n = t.len(); // 把 另一字符串.长度() 存入 元素个数
    let m = p.len(); // 把 节点.长度() 存入 映射表
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    let mut j = 0usize; // 把 0usize; 写入 let mut j
    while j < m && i < n {
        // while 下标 j 小于 映射表 且 下标 i 小于 元素个数 {
        if t[i] == p[j] {
            // 若 另一字符串[下标 i] 等于 节点[下标 j]
            i += 1; // 下标 i累加 1
            j += 1; // 下标 j累加 1
        } else {
            // 否则
            i -= j - 1; // 主串回退到本次对齐的下一位置
            j = 0; // 把 0; 写入 下标 j
        }
    }
    if j == m {
        // 若 下标 j 等于 映射表
        (i - j) as i64 // (下标 i 减 下标 j) as i64
    } else {
        // 否则
        -1 // 减 1
    }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let t = b"now is the time for all good people to come"; // 把 b「now is the time for all good people to come」 存入 另一字符串
    let cases: Vec<(&str, i64)> = vec![
        ("people", 29),
        ("good", 24),
        ("xyz", -1),
        ("a", -1), // 边界：空文本
        ("is", 4),
    ];
    for (idx, (p, want)) in cases.iter().enumerate() {
        // for (idx, (节点, want)) in cases.iter().enumerate() {
        let text: &[u8] = if *want == -1 && *p == "a" { b"" } else { t };
        let got = match_v1(p.as_bytes(), text); // 把 match_v1(节点.as_bytes(), text) 存入 got
        assert_eq!(got, *want, "case {} failed: match_v1({})", idx, p); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
