-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133596542
-- LeetCode 17. 电话号码的字母组合 — Lua 版（方案4）
local function letter_combinations(digits) -- local function letter_combinations(digits)
	if #digits == 0 then
		return {}
	end -- 若 #digits 等于 0 then return {} 终点
	local map =
		{ [2] = "abc", [3] = "def", [4] = "ghi", [5] = "jkl", [6] = "mno", [7] = "pqrs", [8] = "tuv", [9] = "wxyz" }
	local res = { "" } -- 把 {「」} 写入 local res
	for d in digits:gmatch("%d") do -- for d in digits:gmatch(「 对…取模 d」) do
		local next = {} -- 把 {} 写入 local next
		for _, prefix in ipairs(res) do -- 遍历取 prefix
			for c in map[tonumber(d)]:gmatch(".") do -- for 字符 in 映射表[tonumber(d)]:gmatch(「.」) do
				next[#next + 1] = prefix .. c -- 把 prefix .. 字符 写入 next[#next + 1]
			end -- 终点
		end -- 终点
		res = next -- 把 下一个 存入 结果
	end -- 终点
	return res -- 返回 结果
end -- 终点
local got = letter_combinations("23") -- 把 letter_combinations(「23」) 写入 local got
assert(#got == 9 and got[1] == "ad" and got[9] == "cf") -- 断言校验
assert(#letter_combinations("") == 0) -- 断言校验
assert(#letter_combinations("2") == 3) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
