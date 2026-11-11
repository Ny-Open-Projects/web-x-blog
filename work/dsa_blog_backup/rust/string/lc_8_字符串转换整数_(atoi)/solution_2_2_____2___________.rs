// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135129920
// LeetCode 8. 字符串转换整数 (atoi) — Rust 版（方案2）
fn my_atoi(s: String) -> i32 {
    // 定义函数/方法 my_atoi
    let b = s.as_bytes(); // 把 字符串.as_bytes() 存入 b
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    let n = b.len(); // 把 b.长度() 存入 元素个数
    while i < n && (b[i] == b' ') {
        i += 1;
    } // 把 赋值为 b' ') { 下标 i 累加 1; } 写入 while i < n && (b[i]
    let mut sign = 1i64; // 把 1i64; 写入 let mut sign
    if i < n && (b[i] == b'+' || b[i] == b'-') {
        // 若 下标 i 小于 元素个数 且 (b[下标 i] 等于 b' 加 ' 或 b[下标 i] 等于 b' 减 '
        if b[i] == b'-' {
            sign = -1;
        } // 若 b[下标 i] 等于 b' 减 ' { sign 赋值为 减 1; }
        i += 1; // 下标 i累加 1
    }
    let mut ans: i64 = 0; // 把 0; 写入 let mut ans: i64
    while i < n && b[i].is_ascii_digit() {
        // while 下标 i 小于 元素个数 且 b[下标 i].is_ascii_digit() {
        ans = ans * 10 + (b[i] - b'0') as i64; // 把 答案 乘 10 加 (b[下标 i] 减 b'0') as i64; 写入 答案
        if ans > i32::MAX as i64 + 1 {
            ans = i32::MAX as i64 + 1;
        } // 若 答案 超过 i32::MAX as i64 加 1 { 答案 赋值为 i32::MAX as i64 加 1; }
        i += 1; // 下标 i累加 1
    }
    ans *= sign; // 把 sign; 写入 ans *
    if ans > i32::MAX as i64 {
        return i32::MAX;
    } // 若 答案 超过 i32::MAX as i64 { return i32::MAX; }
    if ans < i32::MIN as i64 {
        return i32::MIN;
    } // 若 答案 小于 i32::MIN as i64 { return i32::MIN; }
    ans as i32 // 答案 as i32
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(my_atoi("42".to_string()), 42); // 断言校验
    assert_eq!(my_atoi(" -42".to_string()), -42); // 断言校验
    assert_eq!(my_atoi("4193 with words".to_string()), 4193); // 断言校验
    assert_eq!(my_atoi("-91283472332".to_string()), -2147483648); // 断言校验
    assert_eq!(my_atoi("words and 987".to_string()), 0); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
