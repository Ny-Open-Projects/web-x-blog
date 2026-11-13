// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133547933
// LeetCode 313. 超级丑数 — Rust 版（方案4）
fn nth_super_ugly_number(n: usize, primes: &[i64]) -> i64 {
    // 定义函数/方法 nth_super_ugly_number
    let mut ugly = vec![1i64; n]; // 把 vec取反 [1i64; 元素个数]; 写入 let mut ugly
    let mut idx = vec![0usize; primes.len()]; // 把 vec取反 [0usize; primes.长度()]; 写入 let mut idx
    let mut val: Vec<i64> = primes.to_vec(); // 把 primes.to_vec(); 写入 let mut val: Vec<i64>
    for i in 1..n {
        // 逐个取出 1 的元素（下标 i）
        let mut next = i64::MAX; // 把 i64::MAX; 写入 let mut next
        for k in 0..primes.len() {
            if val[k] < next {
                next = val[k];
            }
        } // 逐个取出 0 的元素（下标 k）
        ugly[i] = next; // 把 下一个; 写入 ugly[i]
        for k in 0..primes.len() {
            // 逐个取出 0 的元素（下标 k）
            if val[k] == next {
                // 若 值[下标 k] 等于 下一个
                idx[k] += 1; // idx[k]累加 1
                val[k] = ugly[idx[k]] * primes[k]; // 把 ugly[idx[下标 k]] 乘 primes[下标 k]; 写入 val[k]
            }
        }
    }
    ugly[n - 1] // ugly[元素个数 减 1]
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(nth_super_ugly_number(12, &[2, 7, 13, 19]), 32); // 断言校验
    assert_eq!(nth_super_ugly_number(1, &[2, 7, 13, 19]), 1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
