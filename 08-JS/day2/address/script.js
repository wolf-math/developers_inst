let names = ['john', 'sarah', 23, 'Rudolf', 34];
// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if its first letter is in uppercase. If not, change it to uppercase and then display the name.

// 2. Write a JavaScript for loop that will go through the variable names
// if the item is not a string, go out of the loop.
// if the item is a string, display it.

for (let name of names) {
  if (typeof name != 'string') {
    break;
  } else if (typeof name == 'string') {
    console.log(name);
  }
}
