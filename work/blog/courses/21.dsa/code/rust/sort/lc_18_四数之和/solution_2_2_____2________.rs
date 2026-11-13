// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133894317
// LeetCode 18. 四数之和 — Rust 版（方案2）
fn four_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
    // 定义函数/方法 four_sum
    let mut arr = nums; // 把 数组; 写入 let mut arr
    arr.sort(); // 排序
    let mut res: Vec<Vec<i32>> = Vec::new(); // 把 Vec::new(); 写入 let mut res: Vec<Vec<i32>>
    let n = arr.len() as i64; // 把 数组.长度() as i64 存入 元素个数
    let t = target as i64; // 把 目标值 as i64 存入 另一字符串
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        if i > 0 && arr[i as usize] == arr[(i - 1) as usize] {
            continue;
        }
        for j in i + 1..n {
            // 逐个取出 下标 i 的元素（下标 j）
            if j > i + 1 && arr[j as usize] == arr[(j - 1) as usize] {
                continue;
            }
            let (mut left, mut right) = (j + 1, n - 1); // 把 (下标 j 加 1, 元素个数 减 1); 写入 let (mut left, mut right)
            while left < right {
                // while 左边界 小于 右边界 {
                let s = arr[i as usize] as i64
                    + arr[j as usize] as i64
                    + arr[left as usize] as i64
                    + arr[right as usize] as i64;
                if s == t {
                    // 若 字符串 等于 另一字符串
                    res.push(vec![
                        arr[i as usize],
                        arr[j as usize],
                        arr[left as usize],
                        arr[right as usize],
                    ]);
                    left += 1; // 左边界累加 1
                    right -= 1; // 右边界累减 1
                    while left < right && arr[left as usize] == arr[(left - 1) as usize] {
                        left += 1;
                    }
                    while left < right && arr[right as usize] == arr[(right + 1) as usize] {
                        right -= 1;
                    }
                } else if s < t {
                    left += 1;
                } else {
                    right -= 1;
                } // 否则，若 字符串 小于 另一字符串 { 左边界 累加 1; } else { 右边界 累减 1; }
            }
        }
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = four_sum(vec![1, 0, -1, 0, -2, 2], 0); // 把 four_sum(vec取反 [1, 0, 减 1, 0, 减 2, 2], 0) 存入 got
    assert_eq!(got.len(), 3); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
