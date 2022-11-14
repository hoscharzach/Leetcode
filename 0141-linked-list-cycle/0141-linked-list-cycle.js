/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let curr = head
    while (curr) {
        if (curr.test === 1) return true
        
        curr.test = 1
        curr = curr.next
    }
    
    return false
};