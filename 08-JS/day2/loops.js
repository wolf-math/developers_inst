let names = ['john', 'sarah', 23, 'Rudolf', 34];

for (let i = 0; i < names.length; i++) {
  // Check if the current item is a string
  if (typeof names[i] === 'string') {
    // Check if the first letter is not uppercase
    if (names[i][0] !== names[i][0].toUpperCase()) {
      // Change the first letter to uppercase
      names[i] = names[i][0].toUpperCase() + names[i].slice(1);
    }
    // Display the name
    console.log(names[i]);
  }
}
