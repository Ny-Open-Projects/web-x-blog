-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134135902
-- LeetCode 344. 反转字符串 — Lua 版（方案2）
local function reverse_string(s)
	return s:reverse()
end -- local function reverse_string(字符串) return 字符串:reverse() 终点
assert(reverse_string("hello") == "olleh") -- 断言校验
assert(reverse_string("Hannah") == "hannaH") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
