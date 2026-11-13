// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// LeetCode 215. 数组中的第K个最大元素 — Rust 版（方案8）
fn quickselect(a: &mut [i32], l: usize, r: usize, k: usize) -> i32 {
    // 定义函数/方法 quickselect
    if l >= r {
        return a[l];
    } // 若 左指针 不低于 右指针 { return 数组[左指针]; }
    let (mut i, mut j) = (l, r); // 把 (左指针, 右指针); 写入 let (mut i, mut j)
    let pivot = a[(l + r) / 2]; // 把 数组[(左指针 加 右指针) 除以 2] 存入 pivot
    while i <= j {
        // 把 下标 j { 写入 while i <
        while a[i] > pivot {
            i += 1;
        } // 把 1; } 写入 while a[i] > pivot { i +
        while a[j] < pivot {
            if j == 0 {
                break;
            }
            j -= 1;
        } // 把 赋值为 0 { break; } 下标 j 累减 1; } 写入 while a[j] < pivot { if j
        if i <= j {
            a.swap(i, j);
            if i < usize::MAX {
                i += 1;
            }
            if j > 0 {
                j -= 1;
            } else {
                break;
            }
        }
    }
    // 分区：[l..j] >= pivot >= [i..r]（降序）
    if k <= j + 1 && j + 1 > l {
        if k - 1 <= j {
            return quickselect(a, l, j, k);
        }
    }
    if k - 1 >= i {
        return quickselect(a, i, r, k);
    }
    a[k - 1] // 数组[下标 k 减 1]
}
fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
    // 定义函数/方法 find_kth_largest
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    quickselect(&mut nums, 0, n - 1, k as usize) // quickselect( 按位与 mut 数组, 0, 元素个数 减 1, 下标 k as usize)
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5); // 断言校验
    assert_eq!(find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4); // 断言校验
    assert_eq!(find_kth_largest(vec![1], 1), 1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}
