-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135256754
-- LeetCode 76. 最小覆盖子串 — Lua 版（方案3）
local function min_window(s, t) -- local function min_window(字符串, 另一字符串)
	if #s == 0 or #t == 0 then
		return ""
	end -- 若 #字符串 等于 0 or #另一字符串 等于 0 then return 「」 终点
	local target = {} -- 把 {} 写入 local target
	for i = 1, #t do -- 把 1, #另一字符串 do 写入 for i
		local c = t:sub(i, i) -- 把 另一字符串:sub(下标 i, 下标 i) 写入 local c
		target[c] = (target[c] or 0) + 1 -- 把 (目标值[字符] or 0) 加 1 写入 target[c]
	end -- 终点
	local required = 0 -- 把 0 写入 local required
	for _ in pairs(target) do
		required = required + 1
	end -- 把 required 加 1 终点 写入 for _ in pairs(target) do required
	local left, formed = 1, 0 -- 把 1, 0 写入 local left, formed
	local window = {} -- 把 {} 写入 local window
	local min_len, min_left = math.huge, 1 -- 把 math.huge, 1 写入 local min_len, min_left
	for right = 1, #s do -- 把 1, #字符串 do 写入 for right
		local c = s:sub(right, right) -- 把 字符串:sub(右边界, 右边界) 写入 local c
		window[c] = (window[c] or 0) + 1 -- 把 (window[字符] or 0) 加 1 写入 window[c]
		if target[c] and window[c] == target[c] then
			formed = formed + 1
		end
		while formed == required do -- 把 赋值为 required do 写入 while formed
			if right - left + 1 < min_len then -- 若 右边界 减 左边界 加 1 小于 min_len then
				min_len = right - left + 1 -- 把 右边界 减 左边界 加 1 存入 min_len
				min_left = left -- 把 左边界 存入 min_left
			end -- 终点
			local lc = s:sub(left, left) -- 把 字符串:sub(左边界, 左边界) 写入 local lc
			window[lc] = window[lc] - 1 -- 把 window[lc] 减 1 写入 window[lc]
			if target[lc] and window[lc] < target[lc] then
				formed = formed - 1
			end
			left = left + 1 -- 把 左边界 加 1 存入 左边界
		end -- 终点
	end -- 终点
	if min_len == math.huge then
		return ""
	end -- 若 min_len 等于 math.huge then return 「」 终点
	return s:sub(min_left, min_left + min_len - 1) -- 返回 字符串:sub(min_left, min_left 加 min_len 减 1)
end -- 终点
assert(min_window("ADOBECODEBANC", "ABC") == "BANC") -- 断言校验
assert(min_window("a", "a") == "a") -- 断言校验
assert(min_window("a", "aa") == "") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
