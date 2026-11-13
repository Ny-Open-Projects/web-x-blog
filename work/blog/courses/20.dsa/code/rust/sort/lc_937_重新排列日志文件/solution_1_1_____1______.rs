// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/139965098
// LeetCode 937. 重新排列日志文件 — Rust 版（方案1）
fn reorder_log_files(logs: Vec<String>) -> Vec<String> {
    // 定义函数/方法 reorder_log_files
    let is_digit = |s: &str| !s.is_empty() && s.as_bytes()[0].is_ascii_digit();
    let mut letter: Vec<String> = Vec::new(); // 把 Vec::new(); 写入 let mut letter: Vec<String>
    let mut digit: Vec<String> = Vec::new(); // 把 Vec::new(); 写入 let mut digit: Vec<String>
    for log in logs {
        // 逐个取出 logs 的元素（log）
        let idx = log.find(' ').unwrap(); // 把 log 查找 ' ').unwrap() 存入 idx
        let content = &log[idx + 1..]; // 把 按位与 log[idx 加 1..] 存入 content
        if is_digit(content) {
            digit.push(log);
        } else {
            letter.push(log);
        }
    }
    letter.sort_by(|a, b| {
        // letter.sort_by( 按位或 数组, b 按位或 {
        let ia = a.find(' ').unwrap(); // 把 数组 查找 ' ').unwrap() 存入 ia
        let ib = b.find(' ').unwrap(); // 把 b 查找 ' ').unwrap() 存入 ib
        let ca = &a[ia + 1..]; // 把 按位与 数组[ia 加 1..] 存入 ca
        let cb = &b[ib + 1..]; // 把 按位与 b[ib 加 1..] 存入 cb
        ca.cmp(cb).then(a.cmp(b)) // ca.cmp(cb).then(数组.cmp(b))
    }); // });
    letter.extend(digit); // letter.extend(digit);
    letter // letter
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let logs = vec![
        "a1 9 2 3 1".to_string(),
        "g1 act car".to_string(),
        "zo4 4 7".to_string(),
        "ab1 off key dog".to_string(),
        "a8 act zoo".to_string(),
    ];
    let got = reorder_log_files(logs); // 把 reorder_log_files(logs) 存入 got
    assert_eq!(
        got,
        vec![
            "g1 act car",
            "a8 act zoo",
            "ab1 off key dog",
            "a1 9 2 3 1",
            "zo4 4 7"
        ]
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
