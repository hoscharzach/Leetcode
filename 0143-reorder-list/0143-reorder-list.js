/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    let currNode = head;
    let listArr = []
    let i = 0;
    while(currNode){
        listArr.push(currNode);
        currNode = currNode.next;
        i++
    }
    
    console.log(listArr)
    let orderedArr = []
    
    for (let i = 0; i < listArr.length / 2; i++) {
        orderedArr.push(listArr[i])
        orderedArr.push(listArr[listArr.length - 1 - i])
    }
    
    console.log(orderedArr)
    for (let i = 0; i < orderedArr.length; i++) {
        let curr = orderedArr[i]
        let next = orderedArr[i + 1]
        
        next ? curr.next = next : curr.next = null
    }
    
    return orderedArr[0]
//     let resultsArr = [];
//     // let half
//     // if (listArr.length % 2 === 0) {
//     //     half = listArr.length / 2
//     // } else {
//     //     half = 
//     // }
//     for(let i = 0; i < Math.floor(listArr.size / 2); i++){
//         if (i = Math.floor(listArr.size / 2)) {
//             resultsArr.push(listArr.get(i))
//             return
//         } else {
//             resultsArr.push(listArr.get(i), listArr.get((listArr.size - 1) - i))
//         }  
//     }
//     console.log(resultsArr)
    
//     for(let i = 0; i < resultsArr.length - 1; i++){
//         resultsArr[i + 1].next = null;
//         resultsArr[i].next = resultsArr[i + 1];
//     }
    
//     return resultsArr[i];
};