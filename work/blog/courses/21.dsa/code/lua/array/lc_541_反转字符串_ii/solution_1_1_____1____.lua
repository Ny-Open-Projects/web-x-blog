-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134588341
-- LeetCode 541. 反转字符串II — Lua 版（方案1）
local function reverse_str(s, k) -- local function reverse_str(字符串, 下标 k)
	local out = {} -- 把 {} 写入 local out
	local n = #s -- 把 #字符串 写入 local n
	local i = 1 -- 把 1 写入 local i
	while i <= n do -- 把 元素个数 do 写入 while i <
		local e = math.min(i + k - 1, n) -- 把 math.取较小值 下标 i 加 下标 k 减 1, 元素个数) 写入 local e
		local seg = s:sub(i, e):reverse() -- 把 字符串:sub(下标 i, e):reverse() 写入 local seg
		out[#out + 1] = seg -- 把 seg 写入 out[#out + 1]
		out[#out + 1] = s:sub(e + 1, e + k) -- 把 字符串:sub(e 加 1, e 加 下标 k) 写入 out[#out + 1]
		i = i + 2 * k -- 把 下标 i 加 2 乘 下标 k 存入 下标 i
	end -- 终点
	return table.concat(out) -- 返回 table.concat(out)
end -- 终点
assert(reverse_str("abcdefg", 2) == "bacdfeg") -- 断言校验
assert(reverse_str("abcd", 2) == "bacd") -- 断言校验
assert(reverse_str("abc", 1) == "abc") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
