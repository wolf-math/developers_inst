let add = (function () {
  let counter = 0;
  function calculus() {
    counter += 1;
    return counter;
  }
  return calculus;
})();

console.log(add());
console.log(add());
console.log(add());
