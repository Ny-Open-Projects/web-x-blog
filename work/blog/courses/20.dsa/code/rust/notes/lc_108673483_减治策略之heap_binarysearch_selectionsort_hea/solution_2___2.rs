// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — Rust 版（方案2：快速选择求第 k 小）
fn select(a: &mut Vec<i32>, lo: usize, hi: usize, k: usize) -> i32 {
    // 定义函数/方法 select
    if lo == hi {
        // 若 左边界 等于 右边界
        return a[lo]; // 返回 数组[左边界]
    }
    let pivot = a[hi]; // 把 数组[右边界] 存入 pivot
    let mut i = lo; // 把 左边界; 写入 let mut i
    for j in lo..hi {
        // 逐个取出 左边界 的元素（下标 j）
        if a[j] <= pivot {
            // 若 数组[下标 j] 不超过 pivot
            a.swap(i, j); // 数组.交换 下标 i, 下标 j);
            i += 1; // 下标 i累加 1
        }
    }
    a.swap(i, hi); // 数组.交换 下标 i, 右边界);
    if i == k {
        // 若 下标 i 等于 下标 k
        a[i] // 数组[下标 i]
    } else if i > k {
        // 否则，若 下标 i 超过 下标 k
        select(a, lo, i - 1, k) // select(数组, 左边界, 下标 i 减 1, 下标 k)
    } else {
        // 否则
        select(a, i + 1, hi, k) // select(数组, 下标 i 加 1, 右边界, 下标 k)
    }
}

fn quick_select(arr: &[i32], k: usize) -> i32 {
    // 定义函数/方法 quick_select
    let mut a = arr.to_vec(); // 把 数组.to_vec(); 写入 let mut a
    let n = a.len(); // 把 数组.长度() 存入 元素个数
    select(&mut a, 0, n - 1, k) // select( 按位与 mut 数组, 0, 元素个数 减 1, 下标 k)
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let base = vec![3, 1, 4, 1, 5, 9, 2, 6]; // 把 vec取反 [3, 1, 4, 1, 5, 9, 2, 6] 存入 base
    let cases: Vec<(usize, i32)> = vec![(2, 2), (3, 3), (0, 1), (7, 9)];
    for (idx, (k, want)) in cases.iter().enumerate() {
        // for (idx, (下标 k, want)) in cases.iter().enumerate() {
        let got = quick_select(&base, *k); // 把 quick_select( 按位与 base, 乘 下标 k) 存入 got
        assert_eq!(got, *want, "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
