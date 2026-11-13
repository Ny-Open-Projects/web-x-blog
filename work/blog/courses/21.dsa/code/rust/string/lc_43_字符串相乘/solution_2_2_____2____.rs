// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130701795
// LeetCode 43. 字符串相乘 — Rust 版（方案2）
fn multiply(num1: String, num2: String) -> String {
    // 定义函数/方法 multiply
    if num1 == "0" || num2 == "0" {
        return "0".to_string();
    } // 若 num1 等于 「0」 或 num2 等于 「0」 { return 「0」.to_string(); }
    let (a, b) = (num1.as_bytes(), num2.as_bytes()); // 把 (num1.as_bytes(), num2.as_bytes()); 写入 let (a, b)
    let (m, n) = (a.len(), b.len()); // 把 (数组.长度(), b.长度()); 写入 let (m, n)
    let mut result = vec![0u8; m + n]; // 把 vec取反 [0u8; 映射表 加 元素个数]; 写入 let mut result
    for i in (0..m).rev() {
        // for 下标 i in (0..映射表).rev() {
        for j in (0..n).rev() {
            // for 下标 j in (0..元素个数).rev() {
            let mul = (a[i] - b'0') * (b[j] - b'0'); // 把 (数组[下标 i] 减 b'0') 乘 (b[下标 j] 减 b'0') 存入 mul
            let (p1, p2) = (i + j, i + j + 1); // 把 (下标 i 加 下标 j, 下标 i 加 下标 j 加 1); 写入 let (p1, p2)
            let total = mul + result[p2]; // 把 mul 加 结果[p2] 存入 总和
            result[p2] = total % 10; // 把 总和 对…取模 10; 写入 result[p2]
            result[p1] += total / 10; // result[p1]累加 总和 除以 10
        }
    }
    let mut out = String::new(); // 把 String::new(); 写入 let mut out
    let mut started = false; // 把 false; 写入 let mut started
    for &d in &result {
        // for 按位与 d in 按位与 结果 {
        if d != 0 || started {
            out.push((b'0' + d) as char);
            started = true;
        }
    }
    if out.is_empty() {
        out.push('0');
    } // 若 out 是否为空 { out 追加 '0'); }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(multiply("2".into(), "3".into()), "6"); // 断言校验
    assert_eq!(multiply("123".into(), "456".into()), "56088"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
