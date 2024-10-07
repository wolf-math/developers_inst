// // Create a function to check the year given by the user

// // If the year is after 2000, you should display "You are in the 21st century", else you should display "You live in the Middle Age"

// function checkYear(year) {
//   return year > 2000
//     ? 'you are in the 21st century'
//     : 'You live in the Middle Age';
// }

// console.log(checkYear(1517));
// console.log(checkYear(2013));

// numbers();

// function numbers() {
//   for (var i = 0; i < 5; i += 1) {
//     console.log(i);
//   }
//   console.log(i);
// }

// Using arrow function and ternary operator create a calculator that returns the result of the calculus depending on the operator : +, - , * ,

// The function should be able to to take 2 numbers as parameters

// const calculator = (a, b, operator) => {
//   return operator === '+'
//     ? a + b
//     : operator === '-'
//     ? a - b
//     : operator === '*'
//     ? a * b
//     : a / b;
// };

// console.log(calculator(2, 3, '+'));
// console.log(calculator(2, 3, '-'));
// console.log(calculator(2, 3, '*'));
// console.log(calculator(2, 3, '/'));

// '5' == 5; // true
// '5' === 5; // false

// const hummus = function (factor) {
//   const ingredient = function (amount, unit, name) {
//     let ingredientAmount = amount * factor;
//     if (ingredientAmount > 1) {
//       unit += 's';
//     }
//     console.log(`${ingredientAmount} ${unit} ${name}`);
//   };
//   ingredient(1, 'can', 'chickpeas');
//   ingredient(0.25, 'cup', 'tahini');
//   ingredient(0.25, 'cup', 'lemon juice');
//   ingredient(1, 'clove', 'garlic');
//   ingredient(2, 'tablespoon', 'olive oil');
//   ingredient(0.5, 'teaspoon', 'cumin');
// };

// hummus(2);

// // function declaration
// function add() {
//   // set inital value of counter
//   let counter = 0;
//   // function plus inside parent function add
//   function plus() {
//     // counter incremented by 1
//     counter += 1;
//     // console log the counter value
//     console.log(counter);
//   }
//   // invoke plus
//   plus();
// }
// // invoke add
// add();
// add();
// add();
// add();

// let add = function () {
//   let counter = 0;
//   function calculus() {
//     counter += 1;
//     return counter;
//   }
//   return calculus;
// };

// let calc = add();

// console.log(calc());
// console.log(calc());
// console.log(calc());

// Analyse this code before executing it. Write explanatory comments

// // function g, takes arg n, returns n + 1
// const g = (n) => n + 1;
// // function f, takes arg n, returns n * 2
// const f = (n) => n * 2;
// // function h, takes arg x, compute g(x) and pass return value to f(x), and returns that value
// const h = (x) => f(g(x));

// console.log(h(20) === 42);

// let c = { greeting: 'Hey!' }; // KSKJDnvkjdfn029345
// let d;
// // spread operator
// d = { ...c };
// c.greeting = 'Hello';
// console.log(d.greeting);

// let myCar = new Object();
// myCar.make = 'Ford';
// myCar.model = 'Mustang';
// myCar.year = 1969;

// console.log(myCar);

// let myObj = new Object(),
//   str = 'myString',
//   rand = Math.random(),
//   obj = new Object();

// myObj.type = 'Dot syntax';
// myObj['date created'] = 'String with space';
// myObj[str] = 'String value';
// myObj[rand] = 'Random Number';
// myObj[obj] = 'Object';
// myObj[''] = 'Even an empty string';

// console.log(myObj);

const person = {
  name: 'Lydia',
  age: 21
};

for (const item in person) {
  console.log(person[item]);
}
