// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135756434
// LeetCode 696. 计数二进制子串 — Rust 版（方案5）
fn count_binary_substrings(s: String) -> i32 {
    // 定义函数/方法 count_binary_substrings
    let b = s.as_bytes(); // 把 字符串.as_bytes() 存入 b
    let n = b.len(); // 把 b.长度() 存入 元素个数
    let mut groups: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut groups: Vec<i32>
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    while i < n {
        // while 下标 i 小于 元素个数 {
        let ch = b[i]; // 把 b[下标 i] 存入 字符
        let mut cnt = 0; // 把 0; 写入 let mut cnt
        while i < n && b[i] == ch {
            // 把 赋值为 字符 { 写入 while i < n && b[i]
            cnt += 1; // 计数累加 1
            i += 1; // 下标 i累加 1
        }
        groups.push(cnt); // 把 计数 压入栈/数组尾部
    }
    let mut ans = 0; // 把 0; 写入 let mut ans
    for k in 1..groups.len() {
        // 逐个取出 1 的元素（下标 k）
        ans += groups[k - 1].min(groups[k]); // 答案累加 groups[下标 k 减 1].取较小值 groups[下标 k])
    }
    ans // 答案
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(count_binary_substrings("00110011".into()), 6); // 断言校验
    assert_eq!(count_binary_substrings("10101".into()), 4); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
