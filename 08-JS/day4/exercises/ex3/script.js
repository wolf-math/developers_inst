// In the JS file:

// 1. Declare a global variable named allBoldItems.
let allBoldItems = document.querySelectorAll('strong');

// 2. Create a function called getBoldItems() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
// This is kinda unnecessary. I took care of this in step 1
function getBoldItems() {
  return document.querySelectorAll('strong');
}

// Create a function called highlight() that changes the color of all the bold text to blue.
function highlight() {
  allBoldItems.forEach((strong) => {
    strong.style.color = 'blue';
  });
}

// Create a function called returnItemsToDefault() that changes the color of all the bold text back to black.
function returnItemsToDefault() {
  allBoldItems.forEach((strong) => {
    strong.style.color = 'initial';
  });
}

// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function returnItemsToDefault() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example
allBoldItems.forEach((item) => {
  item.addEventListener('mouseenter', highlight);
  item.addEventListener('mouseleave', returnItemsToDefault);
});
