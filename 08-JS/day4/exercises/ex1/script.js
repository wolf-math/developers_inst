// 1. Using a DOM property, retrieve the h1 and console.log it.

const atchOne = document.querySelectorAll('h1')[0];
console.log(atchOne);

// Using DOM methods, remove the last paragraph in the <article> tag.

const parent = document.querySelectorAll('article')[0];
const lastPar = parent.lastElementChild;

console.log(lastPar);

parent.removeChild(lastPar);

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

const atchTwo = document.querySelectorAll('h2')[0];
atchTwo.addEventListener('click', () => {
  atchTwo.style.backgroundColor = 'red';
});

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

const atchThree = document.querySelectorAll('h3')[0];
atchThree.addEventListener('click', () => {
  atchThree.style.display = 'none';
});

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

const butt = document.getElementById('butt');
butt.addEventListener('click', () => {
  pees = document.querySelectorAll('p');
  pees.forEach((element) => {
    element.style.fontWeight = 'bold';
  });
});

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.
atchOne.addEventListener('mouseover', () => {
  let textSize = Math.floor(Math.random() * 101);
  atchOne.style.fontSize = `${textSize}px`;
});

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
pee3 = document.querySelectorAll('p')[2];

function addKeyframesAnimation() {
  // Create a style element
  const styleSheet = document.createElement('style');
  styleSheet.type = 'text/css';

  // Define keyframes animation
  const keyframes = `
@keyframes fadeOut {
   0% {opacity: 1;}
   100% {opacity: 0;} 
} 
`;

  styleSheet.innerHTML = keyframes;
  document.head.appendChild(styleSheet);
  pee3.style.animation = 'fadeOut 3s linear';
}
pee3.addEventListener('mouseover', () => {
  addKeyframesAnimation();
});
