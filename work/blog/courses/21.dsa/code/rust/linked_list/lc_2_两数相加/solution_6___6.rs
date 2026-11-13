// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133598918
// LeetCode 2. 两数相加 — Rust 版（方案6）
fn add_two_numbers(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 add_two_numbers
    let (mut i, mut j, mut carry) = (0usize, 0usize, 0i32); // 把 (0usize, 0usize, 0i32); 写入 let (mut i, mut j, mut carry)
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    while i < a.len() || j < b.len() || carry > 0 {
        // while 下标 i 小于 数组.长度() 或 下标 j 小于 b.长度() 或 carry 超过 0 {
        let mut total = carry; // 把 carry; 写入 let mut total
        if i < a.len() {
            total += a[i];
            i += 1;
        } // 若 下标 i 小于 数组.长度() { 总和 累加 数组[下标 i]; 下标 i 累加 1; }
        if j < b.len() {
            total += b[j];
            j += 1;
        } // 若 下标 j 小于 b.长度() { 总和 累加 b[下标 j]; 下标 j 累加 1; }
        out.push(total % 10); // 把 总和 对…取模 10 压入栈/数组尾部
        carry = total / 10; // 把 总和 除以 10; 写入 carry
    }
    if out.is_empty() {
        out.push(0);
    } // 若 out 是否为空 { out 追加 0); }
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(add_two_numbers(vec![2, 4, 3], vec![5, 6, 4]), vec![7, 0, 8]); // 断言校验
    assert_eq!(add_two_numbers(vec![0], vec![0]), vec![0]); // 断言校验
    assert_eq!(
        add_two_numbers(vec![9, 9, 9, 9, 9, 9, 9], vec![9, 9, 9, 9]),
        vec![8, 9, 9, 9, 0, 0, 0, 1]
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
