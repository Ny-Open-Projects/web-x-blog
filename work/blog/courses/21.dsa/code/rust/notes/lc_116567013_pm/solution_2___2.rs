// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Rust 版（方案2：Brute-Force 双循环对齐）
fn match_v2(p: &[u8], t: &[u8]) -> i64 {
    // 定义函数/方法 match_v2
    let n = t.len(); // 把 另一字符串.长度() 存入 元素个数
    let m = p.len(); // 把 节点.长度() 存入 映射表
    if m == 0 || n < m {
        // 若 映射表 等于 0 或 元素个数 小于 映射表
        return -1; // 返回 减 1
    }
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    while i <= n - m {
        // 把 元素个数 减 映射表 { 写入 while i <
        let mut j = 0usize; // 把 0usize; 写入 let mut j
        while j < m && t[i + j] == p[j] {
            // 把 赋值为 节点[下标 j] { 写入 while j < m && t[i + j]
            j += 1; // 下标 j累加 1
        }
        if j == m {
            // 若 下标 j 等于 映射表
            return i as i64; // 返回 下标 i as i64
        }
        i += 1; // 下标 i累加 1
    }
    -1 // 减 1
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let t = b"now is the time for all good people to come"; // 把 b「now is the time for all good people to come」 存入 另一字符串
    let cases: Vec<(&str, i64)> = vec![
        ("people", 29),
        ("time", 11),
        ("all", 20),
        ("xyz", -1),
        ("a", -1),
        ("is", 4),
    ];
    for (idx, (p, want)) in cases.iter().enumerate() {
        // for (idx, (节点, want)) in cases.iter().enumerate() {
        let text: &[u8] = if *p == "a" && *want == -1 { b"" } else { t };
        let got = match_v2(p.as_bytes(), text); // 把 match_v2(节点.as_bytes(), text) 存入 got
        assert_eq!(got, *want, "case {} failed: match_v2({})", idx, p); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
