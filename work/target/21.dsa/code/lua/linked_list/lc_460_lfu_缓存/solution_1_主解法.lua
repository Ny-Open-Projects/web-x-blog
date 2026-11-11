-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137295891
-- LeetCode 460. LFU缓存 — Lua 版（方案1）
local LfuSim = {} -- 把 {} 写入 local LfuSim
LfuSim.__index = LfuSim -- 把 LfuSim 写入 LfuSim.__index
function LfuSim.new(cap)
	return setmetatable({ cap = cap, vals = {}, freq = {}, stamp = {}, clock_ = 0 }, LfuSim)
end
function LfuSim:get(k) -- function LfuSim:get(下标 k)
	self.clock_ = self.clock_ + 1 -- 把 self.clock_ 加 1 写入 self.clock_
	if self.vals[k] ~= nil then -- 若 self.vals[下标 k] ~ 赋值为 nil then
		self.freq[k] = self.freq[k] + 1 -- 把 self.频次表[下标 k] 加 1 写入 self.freq[k]
		self.stamp[k] = self.clock_ -- 把 self.clock_ 写入 self.stamp[k]
		return self.vals[k] -- 返回 self.vals[下标 k]
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点
function LfuSim:put(k, v) -- function LfuSim:put(下标 k, 值)
	self.clock_ = self.clock_ + 1 -- 把 self.clock_ 加 1 写入 self.clock_
	if self.vals[k] ~= nil then -- 若 self.vals[下标 k] ~ 赋值为 nil then
		self.vals[k] = v -- 把 值 写入 self.vals[k]
		self.freq[k] = self.freq[k] + 1 -- 把 self.频次表[下标 k] 加 1 写入 self.freq[k]
		self.stamp[k] = self.clock_ -- 把 self.clock_ 写入 self.stamp[k]
		return -- return
	end -- 终点
	local n = 0 -- 把 0 写入 local n
	for _ in pairs(self.vals) do
		n = n + 1
	end -- 把 元素个数 加 1 终点 写入 for _ in pairs(self.vals) do n
	if self.cap > 0 and n == self.cap then -- 若 self.cap 超过 0 and 元素个数 等于 self.cap then
		local ek, ef, es = nil, math.huge, math.huge -- 把 nil, math.huge, math.huge 写入 local ek, ef, es
		for key, _ in pairs(self.vals) do -- 遍历取 _
			if self.freq[key] < ef or (self.freq[key] == ef and self.stamp[key] < es) then
				ef = self.freq[key]
				es = self.stamp[key]
				ek = key -- 把 self.频次表[key]; es 赋值为 self.stamp[key]; ek 赋值为 key 存入 ef
			end -- 终点
		end -- 终点
		if ek then
			self.vals[ek] = nil
			self.freq[ek] = nil
			self.stamp[ek] = nil
		end
	end -- 终点
	if self.cap > 0 then -- 若 self.cap 超过 0 then
		self.vals[k] = v
		self.freq[k] = 1
		self.stamp[k] = self.clock_
	end -- 终点
end -- 终点
local lfu = LfuSim.new(2) -- 把 LfuSim.new(2) 写入 local lfu
lfu:put(1, 1)
lfu:put(2, 2) -- lfu:put(1, 1); lfu:put(2, 2)
assert(lfu:get(1) == 1) -- 断言校验
lfu:put(3, 3) -- lfu:put(3, 3)
assert(lfu:get(2) == -1) -- 断言校验
assert(lfu:get(3) == 3) -- 断言校验
lfu:put(4, 4) -- lfu:put(4, 4)
assert(lfu:get(1) == -1) -- 断言校验
assert(lfu:get(3) == 3) -- 断言校验
assert(lfu:get(4) == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
