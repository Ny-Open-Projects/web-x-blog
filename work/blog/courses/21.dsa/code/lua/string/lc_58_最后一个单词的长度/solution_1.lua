-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130668538
-- LeetCode 58. 最后一个单词的长度 — Lua 版（方案1）
local function length_of_last_word(s) -- local function length_of_last_word(字符串)
	local t = s:gsub("^%s+", ""):gsub("%s+$", "")
	if t == "" then
		return 0
	end -- 若 另一字符串 等于 「」 then return 0 终点
	local last = t:match("([%w]+)%s*$") -- 把 另一字符串:match(「([ 对…取模 权重] 加 ) 对…取模 字符串 乘 $」) 写入 local last
	return last and #last or 0 -- 返回 last and #last or 0
end -- 终点
assert(length_of_last_word("Hello World") == 5) -- 断言校验
assert(length_of_last_word(" ") == 0) -- 断言校验
assert(length_of_last_word("a") == 1) -- 断言校验
assert(length_of_last_word(" fly me to the moon ") == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
