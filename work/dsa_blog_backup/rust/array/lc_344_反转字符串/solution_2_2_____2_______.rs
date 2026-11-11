// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134135902
// LeetCode 344. 反转字符串 — Rust 版（方案2）
fn reverse_string(s: &mut Vec<char>) {
    // 定义函数/方法 reverse_string
    let (mut i, mut j) = (0usize, s.len() - 1); // 把 (0usize, 字符串.长度() 减 1); 写入 let (mut i, mut j)
    while i < j {
        s.swap(i, j);
        i += 1;
        if j == 0 {
            break;
        }
        j -= 1;
    }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut v: Vec<char> = "hello".chars().collect();
    reverse_string(&mut v);
    assert_eq!(v.iter().collect::<String>(), "olleh"); // 断言校验
    let mut v2: Vec<char> = "Hannah".chars().collect();
    reverse_string(&mut v2);
    assert_eq!(v2.iter().collect::<String>(), "hannaH"); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
