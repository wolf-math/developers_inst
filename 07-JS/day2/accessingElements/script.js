// For each of the questions, find 2 WAYS of accessing :

// 1. The div DOM node?
// 2. The ul DOM node?
// 3. The second li (with Pete)?

// Accessing div

const divNode1 = document.body.firstElementChild;
const divNode2 = document.body.children[0];

console.log(divNode1 == divNode2);
console.log(divNode1);

// Accessing ul

const ulNode1 = document.body.firstElementChild.nextElementSibling;
const ulNode2 = document.body.children[1];

console.log(ulNode1 == ulNode2);
console.log(ulNode1);

// Accessing Pete

const liNode1 = document.body.children[1].lastElementChild;
const liNode2 = document.body.children[1].children[1];
