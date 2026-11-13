// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130753362
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
type TreeNode struct {
	val         int
	left, right *TreeNode
} // 定义类型
func buildTree(vals []interface{}) *TreeNode { // 定义函数/方法 buildTree
	if len(vals) == 0 {
		return nil
	} // 若 长度(vals) 等于 0 { return nil }
	root := &TreeNode{val: toInt(vals[0])} // 把 按位与 TreeNode{值: toInt(vals[0])} 写入 root :
	q := []*TreeNode{root}                 // 把 [] 乘 TreeNode{根节点} 写入 q :
	i := 1                                 // 把 1 写入 i :
	for i < len(vals) {                    // for 下标 i 小于 长度(vals) {
		node := q[0]
		q = q[1:] // 把 节点[0]; 节点 赋值为 节点[1:] 写入 node :
		if i < len(vals) && vals[i] != nil {
			node.left = &TreeNode{val: toInt(vals[i])}
			q = append(q, node.left)
		}
		i++ // 下标 i 加一
		if i < len(vals) && vals[i] != nil {
			node.right = &TreeNode{val: toInt(vals[i])}
			q = append(q, node.right)
		}
		i++ // 下标 i 加一
	}
	return root // 返回 根节点
}
func toInt(v interface{}) int { return v.(int) } // 定义函数/方法 toInt
func postorderTraversal(root *TreeNode) []int { // 定义函数/方法 postorderTraversal
	res := []int{}                     // 把 []int{} 写入 res :
	stack := []*TreeNode{}             // 把 [] 乘 TreeNode{} 写入 stack :
	var prev *TreeNode                 // var 前一个 乘 TreeNode
	cur := root                        // 把 根节点 写入 cur :
	for cur != nil || len(stack) > 0 { // 把 nil 或 长度(栈) 超过 0 { 写入 for cur !
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.left
		} // 把 nil { 栈 赋值为 append(栈, 当前值); 当前值 赋值为 当前值.左边界 } 写入 for cur !
		cur = stack[len(stack)-1]                  // 把 栈[长度(栈) 减 1] 写入 当前值
		if cur.right == nil || cur.right == prev { // 若 当前值.右边界 等于 nil 或 当前值.右边界 等于 前一个
			res = append(res, cur.val)   // 把 append(结果, 当前值.值) 写入 结果
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			prev = cur                   // 把 当前值 写入 前一个
			cur = nil                    // 把 nil 写入 当前值
		} else { // 否则
			cur = cur.right // 把 当前值.右边界 写入 当前值
		}
	}
	return res // 返回 结果
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		vals []interface{}
		want []int
	}{ // 把 []struct{ vals []interface{}; want []int }{ 写入 cases :
		{[]interface{}{1, nil, 2, nil, 3}, []int{3, 2, 1}},
		{[]interface{}{1, 2, 3}, []int{2, 3, 1}},
		{[]interface{}{}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := postorderTraversal(buildTree(c.vals)) // 把 postorderTraversal(buildTree(字符.vals)) 写入 got :
		if !reflect.DeepEqual(got, c.want) {         // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false
			fmt.Printf("FAIL vals=%v got %v want %v\n", c.vals, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
