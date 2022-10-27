/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // iterate through and place righty into stack for every lefty
    // if the next one is not a lefty, pop one off the stack and compare it
    // It has to match the top of stack or else it isn't valid
    
    const stack = []
    
    for (let i = 0; i < s.length; i++) {
        let a = s[i]
        if (a === '(') stack.push(')')
        else if (a === '{') stack.push('}')
        else if (a === '[') stack.push(']')
        else {
            let b = stack.pop()
            if (a !== b) return false
        }
    }
    
    return stack.length === 0
};