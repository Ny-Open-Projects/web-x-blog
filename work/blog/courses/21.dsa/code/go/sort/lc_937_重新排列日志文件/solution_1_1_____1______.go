// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374559
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
	"strings" // 「strings」
)

func reorderLogFiles(logs []string) []string { // 定义函数/方法 reorderLogFiles
	type letterLog struct { // 定义类型
		id      string // id string
		content string // content string
	}
	var letters []letterLog    // var letters []letterLog
	var digits []string        // var digits []string
	for _, log := range logs { // 同时取 _ 与 log 遍历
		sp := strings.Index(log, " ")                                   // 把 strings.Index(log, 「 」) 写入 sp :
		id := log[:sp]                                                  // 把 log[:sp] 写入 id :
		content := log[sp+1:]                                           // 把 log[sp 加 1:] 写入 content :
		if len(content) > 0 && content[0] >= '0' && content[0] <= '9' { // 若 长度(content) 超过 0 且 content[0] 不低于 '0' 且 content[0] 不超过 '9'
			digits = append(digits, log) // 把 append(digits, log) 写入 digits
		} else { // 否则
			letters = append(letters, letterLog{id, content}) // 把 append(letters, letterLog{id, content}) 写入 letters
		}
	}
	sort.Slice(letters, func(i, j int) bool { // sort.Slice(letters, func(下标 i, 下标 j int) bool {
		if letters[i].content != letters[j].content { // 若 letters[下标 i].content 不等于 letters[下标 j].content
			return letters[i].content < letters[j].content // 返回 letters[下标 i].content 小于 letters[下标 j].content
		}
		return letters[i].id < letters[j].id // 返回 letters[下标 i].id 小于 letters[下标 j].id
	}) // })
	res := make([]string, 0, len(logs)) // 把 make([]string, 0, 长度(logs)) 写入 res :
	for _, l := range letters {         // 同时取 _ 与 左指针 遍历
		res = append(res, l.id+" "+l.content) // 把 append(结果, 左指针.id 加 「 」 加 左指针.content) 写入 结果
	}
	res = append(res, digits...) // 把 append(结果, digits...) 写入 结果
	return res                   // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	logs := []string{"dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"}
	want := []string{"let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"}
	ok := true // 把 true 写入 ok :
	if got := reorderLogFiles(logs); !reflect.DeepEqual(got, want) {
		ok = false                                                 // 把 false 写入 ok
		fmt.Printf("FAIL reorderLogFiles=%v want %v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
