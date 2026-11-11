// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Rust 版（方案3：KMP，next 表失配大步跳跃）
fn build_next(p: &[u8]) -> Vec<i64> {
    // 定义函数/方法 build_next
    let m = p.len(); // 把 节点.长度() 存入 映射表
    let mut n = vec![-1i64; m]; // 把 vec取反 [ 减 1i64; 映射表]; 写入 let mut n
    let mut j: i64 = 0; // 把 0; 写入 let mut j: i64
    let mut t: i64 = -1; // 把 减 1; 写入 let mut t: i64
    while (j as usize) < m.saturating_sub(1) {
        // 循环，直到不满足「下标 j as usize) 小于 映射表.saturating_sub(1」
        if t < 0 || p[j as usize] == p[t as usize] {
            // 若 另一字符串 小于 0 或 节点[下标 j as usize] 等于 节点[另一字符串 as usize]
            j += 1; // 下标 j累加 1
            t += 1; // 另一字符串累加 1
            n[j as usize] = t; // 把 另一字符串; 写入 n[j as usize]
        } else {
            // 否则
            t = n[t as usize]; // 把 元素个数[另一字符串 as usize]; 写入 另一字符串
        }
    }
    n // 元素个数
}

fn kmp_match(p: &[u8], t: &[u8]) -> i64 {
    // 定义函数/方法 kmp_match
    let next = build_next(p); // 把 build_next(节点) 存入 下一个
    let n = t.len(); // 把 另一字符串.长度() 存入 元素个数
    let m = p.len(); // 把 节点.长度() 存入 映射表
    let mut i: i64 = 0; // 把 0; 写入 let mut i: i64
    let mut j: i64 = 0; // 把 0; 写入 let mut j: i64
    while j < m as i64 && i < n as i64 {
        // while 下标 j 小于 映射表 as i64 且 下标 i 小于 元素个数 as i64 {
        if j < 0 || t[i as usize] == p[j as usize] {
            // 若 下标 j 小于 0 或 另一字符串[下标 i as usize] 等于 节点[下标 j as usize]
            i += 1; // 下标 i累加 1
            j += 1; // 下标 j累加 1
        } else {
            // 否则
            j = next[j as usize]; // 把 下一个[下标 j as usize]; 写入 下标 j
        }
    }
    if j as usize == m {
        // 若 下标 j as usize 等于 映射表
        i - j // 下标 i 减 下标 j
    } else {
        // 否则
        -1 // 减 1
    }
}

fn eq_arr(a: &[i64], b: &[i64]) -> bool {
    // 定义函数/方法 eq_arr
    a == b // 把 赋值为 b 写入 数组
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let t = b"now is the time for all good people to come"; // 把 b「now is the time for all good people to come」 存入 另一字符串
    let normal: Vec<(&str, i64)> = vec![
        ("people", 29),
        ("all", 20),
        ("no", 0),
        ("xyz", -1),
        ("a", -1),
    ];
    for (idx, (p, want)) in normal.iter().enumerate() {
        // for (idx, (节点, want)) in normal.iter().enumerate() {
        let text: &[u8] = if *p == "a" && *want == -1 { b"" } else { t };
        let got = kmp_match(p.as_bytes(), text); // 把 kmp_match(节点.as_bytes(), text) 存入 got
        assert_eq!(got, *want, "case {} failed: kmp_match({})", idx, p); // 断言校验
    }
    // 重叠前缀：'aaaa' in 'aaaaa' -> 0
    assert_eq!(kmp_match(b"aaaa", b"aaaaa"), 0, "overlap case failed"); // 断言校验
                                                                        // 回退复用：'aaab' in 'aaabaaa' -> 0
    assert_eq!(kmp_match(b"aaab", b"aaabaaa"), 0, "reuse case failed"); // 断言校验
                                                                        // next 表
    assert!(
        eq_arr(&build_next(b"ababaca"), &[-1, 0, 0, 1, 2, 3, 0]),
        "next ababaca failed"
    ); // 断言校验
    assert!(
        eq_arr(&build_next(b"aaaa"), &[-1, 0, 1, 2]),
        "next aaaa failed"
    ); // 断言校验
    assert!(
        eq_arr(&build_next(b"abcd"), &[-1, 0, 0, 0]),
        "next abcd failed"
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
