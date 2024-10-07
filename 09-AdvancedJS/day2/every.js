const words = ['hello', 'hey', 'hola'];

// Check if all the elements of the array start with the letter 'h'

const wordsH = words.every((word) => word.charAt(0) === 'h');

console.log(wordsH);
