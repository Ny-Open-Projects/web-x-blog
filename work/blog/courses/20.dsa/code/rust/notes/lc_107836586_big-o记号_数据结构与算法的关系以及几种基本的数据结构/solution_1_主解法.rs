// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107836586
// LeetCode 107836586. Big-O 记号 — Rust 版（Big-O 记号：按最高次非零系数给出多项式复杂度分类）

// coeffs[i] 为 n^i 的系数，返回最高次非零项对应的复杂度记号
fn classify(coeffs: &[i64]) -> String {
    // 定义函数/方法 classify
    for deg in (0..coeffs.len()).rev() {
        // for deg in (0..coeffs.长度()).rev() {
        if coeffs[deg] != 0 {
            // 若 coeffs[deg] 不等于 0
            if deg > 1 {
                // 若 deg 超过 1
                return format!("O(n^{})", deg); // 返回 format取反 (「O(元素个数 按位异或 {})」, deg)
            } else if deg == 1 {
                // 否则，若 deg 等于 1
                return "O(n)".to_string(); // 返回 「O(元素个数)」.to_string()
            } else {
                // 否则
                return "O(1)".to_string(); // 返回 「O(1)」.to_string()
            }
        }
    }
    "O(1)".to_string() // 「O(1)」.to_string()
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(Vec<i64>, &str)> = vec![
        (vec![1, 0, 0, 0], "O(1)"),
        (vec![0, 0, 0, 35], "O(n^3)"),
        (vec![0, 0, 1, 0], "O(n^2)"),
        (vec![0, 1, 0, 0], "O(n)"),
    ];
    for (idx, (c, want)) in cases.iter().enumerate() {
        // for (idx, (字符, want)) in cases.iter().enumerate() {
        let got = classify(c); // 把 classify(字符) 存入 got
        assert_eq!(got, *want, "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
