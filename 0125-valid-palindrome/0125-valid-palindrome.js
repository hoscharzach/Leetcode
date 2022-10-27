/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const valid = 'abcdefghijklmnopqrstuvwxyz0123456789'
    
    const filtered = s.toLowerCase().split('').filter(el => valid.includes(el))
    const reverse = [...filtered]
    reverse.reverse()
    console.log(filtered, reverse)
    return filtered.join('') === reverse.join('')
};