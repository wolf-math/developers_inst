// 1. Create a structured HTML file linked to a JS file

// 2. Write a Javascript function that takes a parameter: myAge

// 3. In the function, return the age of my mum (my mum is twice my age)

// 4. Call the function

// 5. In the global scope, console.log the result of the function

function myFunc(myAge) {
  let mum = myAge * 2;
  return mum;
}

let myMum = myFunc(436);

console.log(myMum);
