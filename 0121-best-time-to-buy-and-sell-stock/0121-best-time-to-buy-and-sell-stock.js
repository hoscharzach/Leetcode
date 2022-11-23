/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {

    if (prices.length < 2) return 0

    let minPrice = prices[0]
    let maxProfit = 0

    for (let i = 1; i < prices.length; i++) {
        let currPrice = prices[i]
        let potentialProfit = currPrice - minPrice
        maxProfit = Math.max(maxProfit, potentialProfit)

        minPrice = Math.min(currPrice, minPrice)
    }

    return maxProfit
};