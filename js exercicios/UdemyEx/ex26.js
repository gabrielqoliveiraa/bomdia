const listNumbers = [1, 5, 8, 9, 10, 15];
(listNumbers.sort((a,b) => a > b ? 1 : -1))

console.log(listNumbers[0], listNumbers[listNumbers.length - 1])
