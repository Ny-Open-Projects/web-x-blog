import os

base = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/go/string/lc_557_反转字符串中的单词_iii"

go557 = '''package main

import ("fmt"; "os"; "strings")

func reverseWords(s string) string {
    words := strings.Split(s, " ")
    for i, w := range words {
        words[i] = reverseString(w)
    }
    return strings.Join(words, " ")
}

func reverseString(w string) string {
    r := []rune(w)
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}

func main() {
    ok := true
    cases := []struct {
        in   string
        want string
    }{
        {"Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"},
        {"ab cd", "ba dc"},
        {"", ""},
        {"a", "a"},
    }
    for _, c := range cases {
        if got := reverseWords(c.in); got != c.want {
            ok = false
            fmt.Printf("FAIL reverseWords(%q)=%q want %q\\n", c.in, got, c.want)
        }
    }
    if !ok {
        os.Exit(1)
    }
    fmt.Println("PASS")
}
'''

for n in range(1, 17):
    fn = "solution_%d___%d.go" % (n, n)
    with open(os.path.join(base, fn), "w") as f:
        f.write(go557)
print("wrote 16 go files")
