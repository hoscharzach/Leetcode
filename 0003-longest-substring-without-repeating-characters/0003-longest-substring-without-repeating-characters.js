/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
  if (s === "") return 0
  // initialize max length variable and current length
  let max = -Infinity
  let start = 0
  let current = 1
  // will have to keep one pointer on a letter while moving a second
  // to follow a subs
  let end = 1

  // if the subs ends, set highest to max of current and max, reset
  // current variable and end pointer
  while (s[start]) {
    let set = new Set()
    // if the next letter is different, increment current and move end up
    while (s[end] !== undefined && s[start] !== s[end]) {
      if (!set.has(s[end])) {
        set.add(s[end])
        current++
        end++
        max = Math.max(current, max)
      } else break
    }
    // else if they're the same, move start up and put end to start + 1
    // reset current and check length of current vs max then reset current
    start++
    end = start + 1
    max = Math.max(current, max)
    current = 1

  }

  return max
}