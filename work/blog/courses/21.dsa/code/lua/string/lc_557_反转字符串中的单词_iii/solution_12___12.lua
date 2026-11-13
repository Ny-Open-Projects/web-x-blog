-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
-- LeetCode 557. 反转字符串中的单词III — Lua 版（方案12）
local function reverse_words(s) -- local function reverse_words(字符串)
	local out = {} -- 把 {} 写入 local out
	for w in s:gmatch("[^ ]+") do -- for 权重 in 字符串:gmatch(「[ 按位异或 ] 加 」) do
		out[#out + 1] = w:reverse() -- 把 权重:reverse() 写入 out[#out + 1]
	end -- 终点
	return table.concat(out, " ") -- 返回 table.concat(out, 「 」)
end -- 终点
assert(reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc") -- 断言校验
assert(reverse_words("God Ding") == "doG gniD") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
