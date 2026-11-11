-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135756434
-- LeetCode 696. 计数二进制子串 — Lua 版（方案3）
local function count_binary_substrings(s) -- local function count_binary_substrings(字符串)
	local groups = {} -- 把 {} 写入 local groups
	local i, n = 1, #s -- 把 1, #字符串 写入 local i, n
	while i <= n do -- 把 元素个数 do 写入 while i <
		local ch = s:sub(i, i) -- 把 字符串:sub(下标 i, 下标 i) 写入 local ch
		local cnt = 0 -- 把 0 写入 local cnt
		while i <= n and s:sub(i, i) == ch do -- 把 元素个数 and 字符串:sub(下标 i, 下标 i) 等于 字符 do 写入 while i <
			cnt = cnt + 1 -- 把 计数 加 1 存入 计数
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
		groups[#groups + 1] = cnt -- 把 计数 写入 groups[#groups + 1]
	end -- 终点
	local ans = 0 -- 把 0 写入 local ans
	for k = 2, #groups do -- 把 2, #groups do 写入 for k
		ans = ans + math.min(groups[k - 1], groups[k]) -- 把 答案 加 math.取较小值 groups[下标 k 减 1], groups[下标 k]) 存入 答案
	end -- 终点
	return ans -- 返回 答案
end -- 终点
assert(count_binary_substrings("00110011") == 6) -- 断言校验
assert(count_binary_substrings("10101") == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
