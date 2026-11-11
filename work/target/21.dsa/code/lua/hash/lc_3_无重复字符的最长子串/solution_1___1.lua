-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004189
-- LeetCode 3. 无重复字符的最长子串 — Lua 版（方案1）
local function length_of_longest_substring(s) -- local function length_of_longest_substring(字符串)
	local set = {} -- 把 {} 写入 local set
	local left, max_len = 1, 0 -- 把 1, 0 写入 local left, max_len
	for right = 1, #s do -- 把 1, #字符串 do 写入 for right
		local c = s:sub(right, right) -- 把 字符串:sub(右边界, 右边界) 写入 local c
		while set[c] do -- while set[字符] do
			set[s:sub(left, left)] = nil -- 把 nil 写入 set[s:sub(left, left)]
			left = left + 1 -- 把 左边界 加 1 存入 左边界
		end -- 终点
		set[c] = true -- 把 true 写入 set[c]
		local len = right - left + 1 -- 把 右边界 减 左边界 加 1 写入 local len
		if len > max_len then
			max_len = len
		end -- 若 长度 超过 max_len then max_len 赋值为 长度 终点
	end -- 终点
	return max_len -- 返回 max_len
end -- 终点
assert(length_of_longest_substring("abcabcbb") == 3) -- 断言校验
assert(length_of_longest_substring("bbbbb") == 1) -- 断言校验
assert(length_of_longest_substring("pwwkew") == 3) -- 断言校验
assert(length_of_longest_substring("") == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
