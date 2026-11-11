-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/138290964
-- LeetCode 482. 密钥格式化 — Lua 版（方案1）
local function license_key_formatting(s, k) -- local function license_key_formatting(字符串, 下标 k)
	local cleaned = {} -- 把 {} 写入 local cleaned
	s:gsub("[^-]", function(c)
		cleaned[#cleaned + 1] = c:upper()
	end)
	local n = #cleaned -- 把 #cleaned 写入 local n
	if n == 0 then
		return ""
	end -- 若 元素个数 等于 0 then return 「」 终点
	local out = {} -- 把 {} 写入 local out
	local first = n % k -- 把 元素个数 对…取模 下标 k 写入 local first
	local idx = 1 -- 把 1 写入 local idx
	if first > 0 then -- 若 first 超过 0 then
		for _ = 1, first do -- 让 _ 从 1 走到 first（Lua 1 基）
			out[#out + 1] = cleaned[idx] -- 把 cleaned[idx] 写入 out[#out + 1]
			idx = idx + 1 -- 把 idx 加 1 存入 idx
		end -- 终点
		if idx <= n then
			out[#out + 1] = "-"
		end -- 若 idx 不超过 元素个数 then out[#out 加 1] 赋值为 「 减 」 终点
	end -- 终点
	while idx <= n do -- 把 元素个数 do 写入 while idx <
		for _ = 1, k do -- 让 _ 从 1 走到 下标 k（Lua 1 基）
			out[#out + 1] = cleaned[idx] -- 把 cleaned[idx] 写入 out[#out + 1]
			idx = idx + 1 -- 把 idx 加 1 存入 idx
		end -- 终点
		if idx <= n then
			out[#out + 1] = "-"
		end -- 若 idx 不超过 元素个数 then out[#out 加 1] 赋值为 「 减 」 终点
	end -- 终点
	return table.concat(out) -- 返回 table.concat(out)
end -- 终点
assert(license_key_formatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W") -- 断言校验
assert(license_key_formatting("2-5g-3-J", 2) == "2-5G-3J") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
