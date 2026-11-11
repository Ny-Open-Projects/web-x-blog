-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133547933
-- LeetCode 313. 超级丑数 — Lua 版（方案3）
local function nth_super_ugly_number(n, primes) -- local function nth_super_ugly_number(元素个数, primes)
	local ugly = {} -- 把 {} 写入 local ugly
	ugly[1] = 1 -- 把 1 写入 ugly[1]
	local idx, val = {}, {} -- 把 {}, {} 写入 local idx, val
	for k = 1, #primes do
		idx[k] = 1
		val[k] = primes[k]
	end
	for i = 2, n do -- 让 下标 i 从 2 走到 元素个数（Lua 1 基）
		local next = math.huge -- 把 math.huge 写入 local next
		for k = 1, #primes do
			if val[k] < next then
				next = val[k]
			end
		end
		ugly[i] = next -- 把 下一个 写入 ugly[i]
		for k = 1, #primes do -- 把 1, #primes do 写入 for k
			if val[k] == next then -- 若 值[下标 k] 等于 下一个 then
				idx[k] = idx[k] + 1 -- 把 idx[下标 k] 加 1 写入 idx[k]
				val[k] = ugly[idx[k]] * primes[k] -- 把 ugly[idx[下标 k]] 乘 primes[下标 k] 写入 val[k]
			end -- 终点
		end -- 终点
	end -- 终点
	return ugly[n] -- 返回 ugly[元素个数]
end -- 终点
assert(nth_super_ugly_number(12, { 2, 7, 13, 19 }) == 32) -- 断言校验
assert(nth_super_ugly_number(1, { 2, 7, 13, 19 }) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
