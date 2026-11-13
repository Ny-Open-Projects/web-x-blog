// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107849059
// Gnome Sort（侏儒排序）+ Bubble Sort（冒泡排序）+ 贪心找零 对比
fn gnome_sort(arr: &[i32]) -> Vec<i32> {
    // 定义函数/方法 gnome_sort
    let mut a = arr.to_vec(); // 把 数组.to_vec(); 写入 let mut a
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    while i < a.len() {
        // while 下标 i 小于 数组.长度() {
        if i == 0 || a[i] >= a[i - 1] {
            // 若 下标 i 等于 0 或 数组[下标 i] 不低于 数组[下标 i 减 1]
            i += 1; // 下标 i累加 1
        } else {
            // 否则
            a.swap(i - 1, i); // 数组.交换 下标 i 减 1, 下标 i);
            i -= 1; // 下标 i累减 1
        }
    }
    a // 数组
}

fn bubble_sort(arr: &[i32]) -> Vec<i32> {
    // 定义函数/方法 bubble_sort
    let mut a = arr.to_vec(); // 把 数组.to_vec(); 写入 let mut a
    let mut swapped = true; // 把 true; 写入 let mut swapped
    while swapped {
        // while swapped {
        swapped = false; // 把 false; 写入 swapped
        for i in 0..a.len().saturating_sub(1) {
            // 逐个取出 0 的元素（下标 i）
            if a[i] > a[i + 1] {
                // 若 数组[下标 i] 超过 数组[下标 i 加 1]
                a.swap(i, i + 1); // 数组.交换 下标 i, 下标 i 加 1);
                swapped = true; // 把 true; 写入 swapped
            }
        }
    }
    a // 数组
}

fn coin_change(coins: &[i32], amount: i32) -> i32 {
    // 定义函数/方法 coin_change
    let mut cs = coins.to_vec(); // 把 硬币面额.to_vec(); 写入 let mut cs
    cs.sort_by(|x, y| y.cmp(x)); // cs.sort_by( 按位或 x, y 按位或 y.cmp(x));
    let mut remaining = amount; // 把 目标金额; 写入 let mut remaining
    let mut count = 0; // 把 0; 写入 let mut count
    for coin in cs {
        // 逐个取出 cs 的元素（coin）
        while remaining >= coin {
            // 把 coin { 写入 while remaining >
            remaining -= coin; // remaining累减 coin
            count += 1; // 计数累加 1
        }
    }
    if remaining == 0 {
        count
    } else {
        -1
    } // 若 remaining 等于 0 { 计数 } else { 减 1 }
}

fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(gnome_sort(&[3, 2, 1]), vec![1, 2, 3], "g"); // 断言校验
    assert_eq!(bubble_sort(&[3, 2, 1]), vec![1, 2, 3], "b"); // 断言校验
    assert_eq!(coin_change(&[1, 5, 10, 25], 63), 6, "c"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
