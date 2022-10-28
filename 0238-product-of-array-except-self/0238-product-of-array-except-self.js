/**
 * @param {number[]} nums
 * @return {number[]}
 */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  // keep track of everything on the left of the current index
  let left = []
  let leftTotal = 1

  // multiply everything to left of index
  for (let i = 0; i < nums.length; i++) {
    left[i] = leftTotal
    leftTotal *= nums[i]
  }

  // for [1, 2, 3, 4], this gives
  // [1, 1, 2, 6] so the 1 needs to be multiplied by every number except 1
  // which would happen if we multiplied every number backwards to the 1

  let rightTotal = 1
  // do another loop adding up the product the other way
  for (let i = nums.length - 1; i >= 0; i--) {
    left[i] *= rightTotal
    rightTotal *= nums[i]
  }

  return left
};
