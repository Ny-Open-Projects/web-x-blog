-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135917076
-- LeetCode 567. 字符串的排列 — Lua 版（方案3）
local function check_inclusion(s1, s2) -- local function check_inclusion(s1, s2)
	local m, n = #s1, #s2 -- 把 #s1, #s2 写入 local m, n
	if m > n then
		return false
	end -- 若 映射表 超过 元素个数 then return false 终点
	local s1c, s2c = {}, {} -- 把 {}, {} 写入 local s1c, s2c
	for i = 1, m do -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
		local c1 = s1:byte(i) - 97 -- 把 s1:byte(下标 i) 减 97 写入 local c1
		local c2 = s2:byte(i) - 97 -- 把 s2:byte(下标 i) 减 97 写入 local c2
		s1c[c1] = (s1c[c1] or 0) + 1 -- 把 (s1c[c1] or 0) 加 1 写入 s1c[c1]
		s2c[c2] = (s2c[c2] or 0) + 1 -- 把 (s2c[c2] or 0) 加 1 写入 s2c[c2]
	end -- 终点
	local function eq() -- local function eq()
		for k, v in pairs(s1c) do -- 遍历取 值
			if (s2c[k] or 0) ~= v then
				return false
			end -- 若 s2c[下标 k] or 0) ~ 赋值为 值 then return false 终点
		end -- 终点
		for k, v in pairs(s2c) do -- 遍历取 值
			if (s1c[k] or 0) ~= v then
				return false
			end -- 若 s1c[下标 k] or 0) ~ 赋值为 值 then return false 终点
		end -- 终点
		return true -- 返回 true
	end -- 终点
	if eq() then
		return true
	end -- 若 eq() then return true 终点
	for i = m + 1, n do -- 把 映射表 加 1, 元素个数 do 写入 for i
		local c2 = s2:byte(i) - 97 -- 把 s2:byte(下标 i) 减 97 写入 local c2
		local c0 = s2:byte(i - m) - 97 -- 把 s2:byte(下标 i 减 映射表) 减 97 写入 local c0
		s2c[c2] = (s2c[c2] or 0) + 1 -- 把 (s2c[c2] or 0) 加 1 写入 s2c[c2]
		s2c[c0] = (s2c[c0] or 0) - 1 -- 把 (s2c[c0] or 0) 减 1 写入 s2c[c0]
		if s2c[c0] == 0 then
			s2c[c0] = nil
		end -- 若 s2c[c0] 等于 0 then s2c[c0] 赋值为 nil 终点
		if eq() then
			return true
		end -- 若 eq() then return true 终点
	end -- 终点
	return false -- 返回 false
end -- 终点
assert(check_inclusion("ab", "eidbaooo") == true) -- 断言校验
assert(check_inclusion("ab", "eidboaoo") == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
