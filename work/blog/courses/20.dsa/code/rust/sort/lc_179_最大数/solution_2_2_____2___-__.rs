// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134577890
// LeetCode 179. 最大数 — Rust 版（方案2）
fn largest_number(nums: Vec<i32>) -> String {
    // 定义函数/方法 largest_number
    let mut strs: Vec<String> = nums.iter().map(|x| x.to_string()).collect();
    strs.sort_by(|a, b| {
        // strs.sort_by( 按位或 数组, b 按位或 {
        let ab = format!("{}{}", a, b); // 把 format取反 (「{}{}」, 数组, b) 存入 ab
        let ba = format!("{}{}", b, a); // 把 format取反 (「{}{}」, b, 数组) 存入 ba
        ba.cmp(&ab) // ba.cmp( 按位与 ab)
    }); // });
    if strs[0] == "0" {
        return "0".to_string();
    } // 若 strs[0] 等于 「0」 { return 「0」.to_string(); }
    strs.concat() // 打印输出
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(largest_number(vec![10, 2]), "210"); // 断言校验
    assert_eq!(largest_number(vec![3, 30, 34, 5, 9]), "9534330"); // 断言校验
    assert_eq!(largest_number(vec![0, 0]), "0"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
