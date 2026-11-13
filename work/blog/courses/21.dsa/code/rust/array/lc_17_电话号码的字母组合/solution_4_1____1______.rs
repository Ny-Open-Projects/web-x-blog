// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133596542
// LeetCode 17. 电话号码的字母组合 — Rust 版（方案4）
fn letter_combinations(digits: String) -> Vec<String> {
    // 定义函数/方法 letter_combinations
    if digits.is_empty() {
        return vec![];
    } // 若 digits 是否为空 { return vec取反 []; }
    let map = [
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz",
    ]; // 把 [「」, 「」, 「」, 「」, 「」, 「」, 「」, 「」, 「」, 「」] 存入 映射表
    let ds: Vec<usize> = digits.chars().map(|c| c as usize - '0' as usize).collect();
    let mut res = vec![String::new()]; // 把 vec取反 [String::new()]; 写入 let mut res
    for d in ds {
        // 逐个取出 ds 的元素（d）
        let mut next = Vec::new(); // 把 Vec::new(); 写入 let mut next
        for prefix in &res {
            // 逐个取出 结果 的元素（prefix）
            for c in map[d].chars() {
                next.push(format!("{}{}", prefix, c));
            } // 逐个取出 映射表 的元素（字符）
        }
        res = next; // 把 下一个; 写入 结果
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = letter_combinations("23".into()); // 把 letter_combinations(「23」.into()) 存入 got
    assert_eq!(
        got,
        vec!["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    ); // 断言校验
    assert!(letter_combinations("".into()).is_empty()); // 断言校验
    assert_eq!(letter_combinations("2".into()).len(), 3); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
