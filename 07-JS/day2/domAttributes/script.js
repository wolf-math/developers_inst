// Select the <a> element using its id
const linkElement = document.getElementById('dI');

// Get the value of each attribute
const hrefValue = linkElement.getAttribute('href');
const hreflangValue = linkElement.getAttribute('hreflang');
const relValue = linkElement.getAttribute('rel');
const targetValue = linkElement.getAttribute('target');
const typeValue = linkElement.getAttribute('type');

//
console.log('href:', hrefValue);
console.log('hreflang:', hreflangValue);
console.log('rel:', relValue);
console.log('target:', targetValue);
console.log('type:', typeValue);
