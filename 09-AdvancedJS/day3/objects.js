// Exercise
// Use the methods above to :

// Count how many keys and values are in the object below
// Display : "The x# key is : --- The x# value is : ---".

let myObj = {
  name: 'John',
  lastName: 'Doe',
  age: 25,
  friends: ['Mark', 'Lucie', 'Ana']
};

// how many keys:
const objKeys = Object.keys(myObj);
console.log(`there are ${objKeys.length} keys`);

// how many values:
const objValues = Object.values(myObj);
console.log(`there are ${objValues.length} values`);

for (let [key, value] of Object.entries(myObj)) {
  let keyIndex = objKeys.indexOf(key);
  let valueIndex = objValues.indexOf(value);
  console.log(
    `The ${keyIndex} key is : ${key}. The ${valueIndex} value is : ${value}`
  );
}
