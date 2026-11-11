-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138771574
-- LeetCode 93. 复原IP地址 — Lua 版（方案1）
local function valid_seg(s) -- local function valid_seg(字符串)
	if #s == 0 or #s > 3 then
		return false
	end -- 若 #字符串 等于 0 or #字符串 超过 3 then return false 终点
	if #s > 1 and s:sub(1, 1) == "0" then
		return false
	end -- 若 #字符串 超过 1 and 字符串:sub(1, 1) 等于 「0」 then return false 终点
	return tonumber(s) <= 255 -- 返回 tonumber(字符串) 不超过 255
end -- 终点
local function restore_ip_addresses(s) -- local function restore_ip_addresses(字符串)
	local res = {} -- 把 {} 写入 local res
	local n = #s -- 把 #字符串 写入 local n
	if n < 4 or n > 12 then
		return res
	end -- 若 元素个数 小于 4 or 元素个数 超过 12 then return 结果 终点
	for a = 1, 3 do -- 让 数组 从 1 走到 3（Lua 1 基）
		for b = 1, 3 do -- 让 b 从 1 走到 3（Lua 1 基）
			for c = 1, 3 do -- 让 字符 从 1 走到 3（Lua 1 基）
				local d = n - a - b - c -- 把 元素个数 减 数组 减 b 减 字符 写入 local d
				if d >= 1 and d <= 3 then -- 若 d 不低于 1 and d 不超过 3 then
					local s1 = s:sub(1, a) -- 把 字符串:sub(1, 数组) 写入 local s1
					local s2 = s:sub(a + 1, a + b) -- 把 字符串:sub(数组 加 1, 数组 加 b) 写入 local s2
					local s3 = s:sub(a + b + 1, a + b + c) -- 把 字符串:sub(数组 加 b 加 1, 数组 加 b 加 字符) 写入 local s3
					local s4 = s:sub(a + b + c + 1) -- 把 字符串:sub(数组 加 b 加 字符 加 1) 写入 local s4
					if valid_seg(s1) and valid_seg(s2) and valid_seg(s3) and valid_seg(s4) then
						res[#res + 1] = s1 .. "." .. s2 .. "." .. s3 .. "." .. s4 -- 把 s1 .. 「.」 .. s2 .. 「.」 .. s3 .. 「.」 .. s4 写入 res[#res + 1]
					end -- 终点
				end -- 终点
			end -- 终点
		end -- 终点
	end -- 终点
	return res -- 返回 结果
end -- 终点
local got = restore_ip_addresses("25525511135") -- 把 restore_ip_addresses(「25525511135」) 写入 local got
assert(#got == 2 and got[1] == "255.255.11.135" and got[2] == "255.255.111.35") -- 断言校验
local g2 = restore_ip_addresses("0000") -- 把 restore_ip_addresses(「0000」) 写入 local g2
assert(#g2 == 1 and g2[1] == "0.0.0.0") -- 断言校验
assert(#restore_ip_addresses("abc") == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
