// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
// LeetCode 108673483. 减治策略 — Rust 版（方案3：Boyer-Moore 摩尔投票求多数元素）
fn majority_element(arr: &[i32]) -> i32 {
    // 定义函数/方法 majority_element
    let mut candidate: Option<i32> = None; // 把 None; 写入 let mut candidate: Option<i32>
    let mut count = 0; // 把 0; 写入 let mut count
    for &num in arr {
        // for 按位与 num in 数组 {
        if count == 0 {
            // 若 计数 等于 0
            candidate = Some(num); // 把 Some(num); 写入 candidate
        }
        if Some(num) == candidate {
            // 若 Some(num) 等于 candidate
            count += 1; // 计数累加 1
        } else {
            // 否则
            count -= 1; // 计数累减 1
        }
    }
    let cand = candidate.unwrap(); // 把 candidate.unwrap() 存入 cand
    let mut cnt = 0; // 把 0; 写入 let mut cnt
    for &num in arr {
        // for 按位与 num in 数组 {
        if num == cand {
            // 若 num 等于 cand
            cnt += 1; // 计数累加 1
        }
    }
    if cnt > arr.len() as i32 / 2 {
        // 若 计数 超过 数组.长度() as i32 除以 2
        return cand; // 返回 cand
    }
    -1 // 减 1
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(Vec<i32>, i32)> = vec![
        (vec![2, 2, 1, 1, 1, 1, 1], 1),
        (vec![1, 2, 3], -1),
        (vec![3, 3, 4], 3),
    ];
    for (idx, (a, want)) in cases.iter().enumerate() {
        // for (idx, (数组, want)) in cases.iter().enumerate() {
        let got = majority_element(a); // 把 majority_element(数组) 存入 got
        assert_eq!(got, *want, "case {} failed", idx); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}
