let party = [
  {
    desert: 'Chocolate Mousse',
    calories: 30
  },
  {
    desert: 'Apple Pie',
    calories: 15
  },
  {
    desert: 'Croissant',
    calories: 50
  },
  {
    desert: 'Strawberry Icecream',
    calories: 5
  }
];

const reducedParty = party.reduce((acc, val) => {
  return val.desert != 'Apple Pie' ? val.calories + acc : 0 + acc;
}, 0);

console.log(reducedParty);
