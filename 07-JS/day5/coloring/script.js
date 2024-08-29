// colors table and pixels table are similar.
// can they be made with the same function?

let selectedColor = 'white';

function createColorsPallette() {
  // 16 colors
  const colorPalette = [
    '#FF0000', // Red
    '#008000', // Green
    '#0000FF', // Blue
    '#FFFF00', // Yellow
    '#00FFFF', // Cyan
    '#FF00FF', // Magenta
    '#FFA500', // Orange
    '#800080', // Purple
    '#00FF00', // Lime
    '#FFC0CB', // Pink
    '#008080', // Teal
    '#000080', // Navy
    '#800000', // Maroon
    '#808080', // Gray
    '#000000', // Black
    '#FFFFFF' // White
  ];

  // Get the table element
  let table = document.getElementById('color-selector-table');
  let idIndex = 0;

  // Create the color palette in the table
  for (let i = 0; i < 8; i++) {
    let newRow = table.insertRow(-1);
    for (let j = 0; j < 2; j++) {
      let cell = newRow.insertCell(j);
      cell.id = `color-${i}-${j}-${idIndex}`;
      cell.className = 'color';
      cell.style.backgroundColor = colorPalette[idIndex];
      cell.addEventListener('click', () => {
        selectedColor = cell.style.backgroundColor;
      });
      idIndex++;
    }
  }
}

// make pixels table
// todo: make it dynamic based on screen size
function createPixels(x, y, id) {
  let table = document.getElementById(id);

  for (let i = 0; i < y; i++) {
    newRow = table.insertRow(-1);
    for (let j = 0; j < x; j++) {
      let cell = newRow.insertCell(j);
      cell.id = `pixel-${i}-${j}`;
      cell.className = 'pixel';

      let isClicked = false;
      let isHovered = false;

      cell.addEventListener('click', () => {
        isClicked = true;
        if (isClicked && isHovered) {
          console.log('onClick: clicked and hovered');
          cell.style.backgroundColor = selectedColor;
        }
      });

      // Mouseover event listener
      cell.addEventListener('mouseover', () => {
        isHovered = true;
        if (isClicked && isHovered) {
          console.log('onMouseover: clicked and hovered');
          cell.style.backgroundColor = selectedColor;
        }
      });

      cell.addEventListener('mouseout', () => {
        isHovered = false;
        isClicked = false;
      });

      // cell.addEventListener('click', () => {
      //   cell.style.backgroundColor = selectedColor;
      // });
    }
  }
}

const clearButton = document.getElementById('clear');
clearButton.addEventListener('click', () => {
  const pixels = document.getElementsByClassName('pixel');
  [...pixels].forEach((pixel) => {
    pixel.style.backgroundColor = 'white';
  });
});

createColorsPallette();
createPixels(25, 30, 'pixels-table');
