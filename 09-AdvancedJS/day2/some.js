const words = ['wow', 'hey', 'bye'];

// Check if at least one element of the array starts with the letter 'h'

let startsWithH = words.some((word) => word.charAt(0) === 'h');

console.log(startsWithH);
