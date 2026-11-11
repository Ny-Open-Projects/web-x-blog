// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135003383
// LeetCode 164. 最大间距 — Rust 版（方案7）
fn maximum_gap(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 maximum_gap
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    if n < 2 {
        return 0;
    } // 若 元素个数 小于 2 { return 0; }
    let min_val = *nums.iter().min().unwrap(); // 把 乘 数组.iter().取较小值 ).unwrap() 存入 min_val
    let max_val = *nums.iter().max().unwrap(); // 把 乘 数组.iter().取较大值 ).unwrap() 存入 max_val
    if min_val == max_val {
        return 0;
    } // 若 min_val 等于 max_val { return 0; }
    let d = std::cmp::max(1, (max_val - min_val) / (n as i32 - 1));
    let bucket_size = ((max_val - min_val) / d) as usize + 1; // 把 ((max_val 减 min_val) 除以 d) as usize 加 1 存入 bucket_size
    let mut buckets: Vec<(i32, i32)> = vec![(-1, -1); bucket_size];
    for &x in &nums {
        // for 按位与 x in 按位与 数组 {
        let idx = ((x - min_val) / d) as usize; // 把 ((x 减 min_val) 除以 d) as usize 存入 idx
        if buckets[idx].0 == -1 {
            buckets[idx] = (x, x);
        }
        // 若 buckets[idx].0 等于 减 1 { buckets[idx] 赋值为 (x, x); }
        else {
            // 否则
            buckets[idx].0 = buckets[idx].0.min(x); // 把 buckets[idx].0.取较小值 x); 写入 buckets[idx].0
            buckets[idx].1 = buckets[idx].1.max(x); // 把 buckets[idx].1.取较大值 x); 写入 buckets[idx].1
        }
    }
    let mut ans = 0; // 把 0; 写入 let mut ans
    let mut prev_max = -1i32; // 把 减 1i32; 写入 let mut prev_max
    for b in buckets {
        // 逐个取出 buckets 的元素（b）
        if b.0 == -1 {
            continue;
        } // 若 b.0 等于 减 1 { continue; }
        if prev_max != -1 {
            ans = ans.max(b.0 - prev_max);
        } // 若 prev_max 不等于 减 1 { 答案 赋值为 答案.取较大值 b.0 减 prev_max); }
        prev_max = b.1; // 把 b.1; 写入 prev_max
    }
    ans // 答案
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(maximum_gap(vec![1, 2, 3]), 1); // 断言校验
    assert_eq!(maximum_gap(vec![3, 6, 9, 1]), 3); // 断言校验
    assert_eq!(maximum_gap(vec![10]), 0); // 断言校验
    assert_eq!(maximum_gap(vec![]), 0); // 断言校验
    assert_eq!(maximum_gap(vec![1, 10000000]), 9999999); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
