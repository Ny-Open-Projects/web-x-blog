// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130724108
// LeetCode 67. 二进制求和 — Rust 版（方案1）
fn add_binary(a: String, b: String) -> String {
    // 定义函数/方法 add_binary
    let (a, b) = (a.as_bytes(), b.as_bytes()); // 把 (数组.as_bytes(), b.as_bytes()); 写入 let (a, b)
    let (mut i, mut j) = (a.len() as i32 - 1, b.len() as i32 - 1);
    let mut carry = 0u8; // 把 0u8; 写入 let mut carry
    let mut out: Vec<u8> = Vec::new(); // 把 Vec::new(); 写入 let mut out: Vec<u8>
    while i >= 0 || j >= 0 || carry > 0 {
        // 把 0 或 下标 j 不低于 0 或 carry 超过 0 { 写入 while i >
        let mut total = carry; // 把 carry; 写入 let mut total
        if i >= 0 {
            total += a[i as usize] - b'0';
            i -= 1;
        } // 若 下标 i 不低于 0 { 总和 累加 数组[下标 i as usize] 减 b'0'; 下标 i 累减 1; }
        if j >= 0 {
            total += b[j as usize] - b'0';
            j -= 1;
        } // 若 下标 j 不低于 0 { 总和 累加 b[下标 j as usize] 减 b'0'; 下标 j 累减 1; }
        out.push(b'0' + total % 2); // 把 b'0' 加 总和 对…取模 2 压入栈/数组尾部
        carry = total / 2; // 把 总和 除以 2; 写入 carry
    }
    out.reverse(); // 反转
    String::from_utf8(out).unwrap() // String::from_utf8(out).unwrap()
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(add_binary("11".to_string(), "1".to_string()), "100"); // 断言校验
    assert_eq!(add_binary("1010".to_string(), "1011".to_string()), "10101"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
