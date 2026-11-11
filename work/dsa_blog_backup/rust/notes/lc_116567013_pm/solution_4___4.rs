// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/116567013
// LeetCode 116567013. PM — Rust 版（方案4：buildNext 单测）
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

fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        build_next(b"ababaca"),
        vec![-1, 0, 0, 1, 2, 3, 0],
        "ababaca"
    ); // 断言校验
    assert_eq!(build_next(b"aaaa"), vec![-1, 0, 1, 2], "aaaa"); // 断言校验
    assert_eq!(build_next(b"abcabc"), vec![-1, 0, 0, 0, 1, 2], "abcabc"); // 断言校验
    assert_eq!(build_next(b"abcd"), vec![-1, 0, 0, 0], "abcd"); // 断言校验
    assert_eq!(build_next(b"a"), vec![-1], "a"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
