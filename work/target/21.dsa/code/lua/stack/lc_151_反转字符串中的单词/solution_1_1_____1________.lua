-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130846022
-- LeetCode 151. 反转字符串中的单词 — Lua 版（方案1）
local function reverse_words(s) -- local function reverse_words(字符串)
	local words = {} -- 把 {} 写入 local words
	for w in s:gmatch("%S+") do
		words[#words + 1] = w
	end -- 把 权重 终点 写入 for w in s:gmatch("%S+") do words[#words + 1]
	local out = {} -- 把 {} 写入 local out
	for i = #words, 1, -1 do
		out[#out + 1] = words[i]
	end -- 把 #单词列表, 1, 减 1 do out[#out 加 1] 赋值为 单词列表[下标 i] 终点 写入 for i
	return table.concat(out, " ") -- 返回 table.concat(out, 「 」)
end -- 终点
assert(reverse_words("the sky is blue") == "blue is sky the") -- 断言校验
assert(reverse_words("  hello world  ") == "world hello") -- 断言校验
assert(reverse_words("a good   example") == "example good a") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
