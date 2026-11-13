// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134866839
// LeetCode 89. 格雷编码 — Rust 版（方案2）
fn gray_code(n: i32) -> Vec<i32> {
    // 定义函数/方法 gray_code
    let m = 1i32 << n; // 把 1i32 小于 小于 元素个数 存入 映射表
    let mut out = Vec::with_capacity(m as usize); // 把 Vec::with_capacity(映射表 as usize); 写入 let mut out
    for i in 0..m {
        out.push(i ^ (i >> 1));
    } // 逐个取出 0 的元素（下标 i）
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let g2 = gray_code(2); // 把 gray_code(2) 存入 g2
    assert_eq!(g2, vec![0, 1, 3, 2]); // 断言校验
    let g1 = gray_code(1); // 把 gray_code(1) 存入 g1
    assert_eq!(g1, vec![0, 1]); // 断言校验
                                // 校验性质：相邻两项恰好一位不同
    let g3 = gray_code(3); // 把 gray_code(3) 存入 g3
    for i in 0..g3.len() {
        // 逐个取出 0 的元素（下标 i）
        let x = (g3[i] ^ g3[(i + 1) % g3.len()]).count_ones();
        assert_eq!(x, 1); // 断言校验
    }
    println!("PASS");
} // 全部用例通过，输出 PASS
