let addressNumber = 5;
let addressStreet = 'BenYehuda';
let country = 'Israel';

let globalAddress =
  'I live on ' + addressStreet + ' ' + addressNumber + ', in ' + country;

alert(globalAddress);

document.getElementById('address').textContent = globalAddress;

console.log(globalAddress);

console.log('SUPER SECRET MESSAGE!!!');
