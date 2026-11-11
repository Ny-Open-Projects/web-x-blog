-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134537871
-- LeetCode 146. LRU缓存 — Lua 版（方案2）
local LruSim = {} -- 把 {} 写入 local LruSim
LruSim.__index = LruSim -- 把 LruSim 写入 LruSim.__index
function LruSim.new(cap)
	return setmetatable({ cap = cap, keys = {}, vals = {} }, LruSim)
end
function LruSim:get(k) -- function LruSim:get(下标 k)
	if self.vals[k] ~= nil then -- 若 self.vals[下标 k] ~ 赋值为 nil then
		for i, key in ipairs(self.keys) do -- 遍历取 key
			if key == k then
				table.remove(self.keys, i)
				break
			end -- 若 key 等于 下标 k then table 弹出 self.keys, 下标 i) break 终点
		end -- 终点
		self.keys[#self.keys + 1] = k -- 把 下标 k 写入 self.keys[#self.keys + 1]
		return self.vals[k] -- 返回 self.vals[下标 k]
	end -- 终点
	return -1 -- 返回 减 1
end -- 终点
function LruSim:put(k, v) -- function LruSim:put(下标 k, 值)
	if self.vals[k] ~= nil then -- 若 self.vals[下标 k] ~ 赋值为 nil then
		for i, key in ipairs(self.keys) do -- 遍历取 key
			if key == k then
				table.remove(self.keys, i)
				break
			end -- 若 key 等于 下标 k then table 弹出 self.keys, 下标 i) break 终点
		end -- 终点
	elseif #self.keys == self.cap then -- 把 赋值为 self.cap then 写入 elseif #self.keys
		local old = table.remove(self.keys, 1) -- 把 table 弹出 self.keys, 1) 写入 local old
		self.vals[old] = nil -- 把 nil 写入 self.vals[old]
	end -- 终点
	self.keys[#self.keys + 1] = k -- 把 下标 k 写入 self.keys[#self.keys + 1]
	self.vals[k] = v -- 把 值 写入 self.vals[k]
end -- 终点
local lru = LruSim.new(2) -- 把 LruSim.new(2) 写入 local lru
lru:put(1, 1)
lru:put(2, 2) -- lru:put(1, 1); lru:put(2, 2)
assert(lru:get(1) == 1) -- 断言校验
lru:put(3, 3) -- lru:put(3, 3)
assert(lru:get(2) == -1) -- 断言校验
lru:put(4, 4) -- lru:put(4, 4)
assert(lru:get(1) == -1) -- 断言校验
assert(lru:get(3) == 3) -- 断言校验
assert(lru:get(4) == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
