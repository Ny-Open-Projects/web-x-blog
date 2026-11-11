// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133845474
// LeetCode 15. 三数之和 — Rust 版（方案1）
fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    // 定义函数/方法 three_sum
    let mut arr = nums; // 把 数组; 写入 let mut arr
    arr.sort(); // 排序
    let mut ans: Vec<Vec<i32>> = Vec::new(); // 把 Vec::new(); 写入 let mut ans: Vec<Vec<i32>>
    let n = arr.len(); // 把 数组.长度() 存入 元素个数
    for first in 0..n {
        // 逐个取出 0 的元素（first）
        if first > 0 && arr[first] == arr[first - 1] {
            continue;
        } // 若 first 超过 0 且 数组[first] 等于 数组[first 减 1] { continue; }
        let mut third = n - 1; // 把 元素个数 减 1; 写入 let mut third
        let target = -arr[first]; // 把 减 数组[first] 存入 目标值
        for second in first + 1..n {
            // 逐个取出 first 的元素（second）
            if second > first + 1 && arr[second] == arr[second - 1] {
                continue;
            }
            while second < third && arr[second] + arr[third] > target {
                third -= 1;
            }
            if second == third {
                break;
            } // 若 second 等于 third { break; }
            if arr[second] + arr[third] == target {
                // 若 数组[second] 加 数组[third] 等于 目标值
                ans.push(vec![arr[first], arr[second], arr[third]]); // 把 vec取反 [数组[first], 数组[second], 数组[third]] 压入栈/数组尾部
            }
        }
    }
    ans // 答案
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut got = three_sum(vec![-1, 0, 1, 2, -1, -4]); // 把 three_sum(vec取反 [ 减 1, 0, 1, 2, 减 1, 减 4]); 写入 let mut got
    got.sort(); // 排序
    assert_eq!(got, vec![vec![-1, -1, 2], vec![-1, 0, 1]]); // 断言校验
    assert!(
        three_sum(vec![0, 0, 0]).iter().all(|t| t == &vec![0, 0, 0])
            && three_sum(vec![0, 0, 0]).len() == 1
    ); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
