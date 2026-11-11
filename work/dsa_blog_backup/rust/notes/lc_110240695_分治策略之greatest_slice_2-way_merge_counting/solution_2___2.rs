// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
// LeetCode 110240695. 分治策略之 greatest slice — Rust 版（方案B：增量扫描）
fn max_sub_array_ic(arr: &[i32]) -> i64 {
    // 定义函数/方法 max_sub_array_ic
    let n = arr.len(); // 把 数组.长度() 存入 元素个数
    if n == 0 {
        // 若 元素个数 等于 0
        return 0; // 返回 0
    }
    let mut gs = arr[0] as i64; // 把 数组[0] as i64; 写入 let mut gs
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        let mut s = 0i64; // 把 0i64; 写入 let mut s
        for j in i..n {
            // 逐个取出 下标 i 的元素（下标 j）
            s += arr[j] as i64; // 字符串累加 数组[下标 j] as i64
            if gs < s {
                // 若 gs 小于 字符串
                gs = s; // 把 字符串; 写入 gs
            }
        }
    }
    gs // gs
}

fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(max_sub_array_ic(&[-2, 1, -3, 4, -1, 2, 1]), 6, "ms1"); // 断言校验
    assert_eq!(max_sub_array_ic(&[-1, -2, -3]), -1, "ms2"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
