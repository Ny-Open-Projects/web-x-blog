// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138671078
// LeetCode 1356. 根据数字二进制下1的数目排序 — Rust 版（方案1）
fn count_bits(mut n: i32) -> i32 {
    // 定义函数/方法 count_bits
    let mut c = 0; // 把 0; 写入 let mut c
    while n > 0 {
        c += n & 1;
        n >>= 1;
    } // 把 元素个数 按位与 1; 元素个数 超过 不低于 1; } 写入 while n > 0 { c +
    c // 字符
}
fn sort_by_bits(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 sort_by_bits
    let mut arr = nums; // 把 数组; 写入 let mut arr
    arr.sort_by(|&a, &b| {
        // 数组.sort_by( 按位或 按位与 数组, 按位与 b 按位或 {
        let (ba, bb) = (count_bits(a), count_bits(b)); // 把 (count_bits(数组), count_bits(b)); 写入 let (ba, bb)
        ba.cmp(&bb).then(a.cmp(&b)) // ba.cmp( 按位与 bb).then(数组.cmp( 按位与 b))
    }); // });
    arr // 数组
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(
        sort_by_bits(vec![0, 1, 2, 3, 4, 5, 6, 7, 8]),
        vec![0, 1, 2, 4, 8, 3, 5, 6, 7]
    ); // 断言校验
    assert_eq!(
        sort_by_bits(vec![1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]),
        vec![1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
