-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130724108
-- LeetCode 67. 二进制求和 — Lua 版（方案1）
local function add_binary(a, b) -- local function add_binary(数组, b)
	local i, j = #a, #b -- 把 #数组, #b 写入 local i, j
	local carry = 0 -- 把 0 写入 local carry
	local out = {} -- 把 {} 写入 local out
	while i >= 1 or j >= 1 or carry > 0 do -- 把 1 or 下标 j 不低于 1 or carry 超过 0 do 写入 while i >
		local total = carry -- 把 carry 写入 local total
		if i >= 1 then
			total = total + (a:byte(i) - 48)
			i = i - 1
		end
		if j >= 1 then
			total = total + (b:byte(j) - 48)
			j = j - 1
		end
		out[#out + 1] = tostring(total % 2) -- 把 tostring(总和 对…取模 2) 写入 out[#out + 1]
		carry = math.floor(total / 2) -- 把 math.floor(总和 除以 2) 存入 carry
	end -- 终点
	return table.concat(out):reverse() -- 返回 table.concat(out):reverse()
end -- 终点
assert(add_binary("11", "1") == "100") -- 断言校验
assert(add_binary("1010", "1011") == "10101") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
