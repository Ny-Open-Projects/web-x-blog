// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397820
// LeetCode 556. 下一个更大元素 III — Rust 版（方案2）
fn next_greater_element(n: i32) -> i32 {
    // 定义函数/方法 next_greater_element
    let mut d: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut d: Vec<i32>
    let mut x = n; // 把 元素个数; 写入 let mut x
    while x > 0 {
        d.push(x % 10);
        x /= 10;
    } // 把 x 对…取模 10 压入栈/数组尾部
    d.reverse(); // 反转
    let m = d.len(); // 把 d.长度() 存入 映射表
    let mut i = m as i32 - 2; // 把 映射表 as i32 减 2; 写入 let mut i
    while i >= 0 && d[i as usize] >= d[i as usize + 1] {
        i -= 1;
    }
    if i < 0 {
        return -1;
    } // 若 下标 i 小于 0 { return 减 1; }
    let mut j = m as i32 - 1; // 把 映射表 as i32 减 1; 写入 let mut j
    while d[j as usize] <= d[i as usize] {
        j -= 1;
    } // 把 d[下标 i as usize] { 下标 j 累减 1; } 写入 while d[j as usize] <
    d.swap(i as usize, j as usize); // d.交换 下标 i as usize, 下标 j as usize);
    d[(i + 1) as usize..].reverse(); // 反转
    let mut res: i64 = 0; // 把 0; 写入 let mut res: i64
    for &v in &d {
        res = res * 10 + v as i64;
    } // 把 结果 乘 10 加 值 as i64; } 写入 for &v in &d { res
    if res > i32::MAX as i64 {
        -1
    } else {
        res as i32
    } // 若 结果 超过 i32::MAX as i64 { 减 1 } else { 结果 as i32 }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(next_greater_element(12), 21); // 断言校验
    assert_eq!(next_greater_element(21), -1); // 断言校验
    assert_eq!(next_greater_element(1), -1); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS
