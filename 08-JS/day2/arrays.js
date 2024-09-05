let pets = ['cat', 'dog', 'fish', 'rabbit', 'cow'];

console.log(pets[1]);

pets.push('horse');

let rabbitIndex = pets.indexOf('rabbit'); // Find the index of 'rabbit'
pets.splice(rabbitIndex, 1);

console.log(pets.length);

console.log(pets);
