-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
-- LeetCode 65. 有效数字 — Lua 版

-- 方案3（线性扫描）
local function is_number(s) -- local function is_number(字符串)
	local t = s:match("^%s*(.-)%s*$") -- 等价于 TS 的 trim()
	if #t == 0 then
		return false
	end -- 若 #另一字符串 等于 0 then return false 终点
	local has_dot = false -- 把 false 写入 local has_dot
	local has_e = false -- 把 false 写入 local has_e
	local has_digit = false -- 把 false 写入 local has_digit
	for i = 1, #t do -- 把 1, #另一字符串 do 写入 for i
		local c = t:sub(i, i) -- 把 另一字符串:sub(下标 i, 下标 i) 写入 local c
		if c == "." then -- 若 字符 等于 「.」 then
			if has_dot or has_e then
				return false
			end -- 若 has_dot or has_e then return false 终点
			has_dot = true -- 把 true 存入 has_dot
		elseif c == "e" or c == "E" then -- 把 赋值为 「e」 or 字符 等于 「e」 then 写入 elseif c
			if has_e or not has_digit then
				return false
			end -- 若 has_e or not has_digit then return false 终点
			has_e = true -- 把 true 存入 has_e
			has_digit = false -- 把 false 存入 has_digit
		elseif c == "+" or c == "-" then -- 把 赋值为 「 加 」 or 字符 等于 「 加 」 then 写入 elseif c
			local prev = t:sub(i - 1, i - 1) -- 把 另一字符串:sub(下标 i 减 1, 下标 i 减 1) 写入 local prev
			if i > 1 and prev ~= "e" and prev ~= "E" then
				return false
			end
		elseif c:match("%d") then -- elseif 字符:match(「 对…取模 d」) then
			has_digit = true -- 把 true 存入 has_digit
		else -- 否则
			return false -- 返回 false
		end -- 终点
	end -- 终点
	return has_digit -- 返回 has_digit
end -- 终点

assert(is_number("abc") == false, "isNumber('abc') should be false") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
