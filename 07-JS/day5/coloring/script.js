// colors table and pixels table are similar.
// can they be made with the same function?

let selectedColor = 'white';

function createColorsPallette() {
  // 16 colors
  const colorPalette = [
    '#FF0000',
    '#008000',
    '#0000FF',
    '#FFFF00',
    '#00FFFF',
    '#FF00FF',
    '#FFA500',
    '#800080',
    '#00FF00',
    '#FFC0CB',
    '#008080',
    '#000080',
    '#800000',
    '#808080',
    '#000000',
    '#FFFFFF'
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
function createPixels(x = 30, y = 30) {
  let table = document.getElementById('pixels-table');

  for (let i = 0; i < y; i++) {
    newRow = table.insertRow(-1);
    for (let j = 0; j < x; j++) {
      let cell = newRow.insertCell(j);
      cell.id = `pixel-${i}-${j}`;
      cell.className = 'pixel';

      // let isClicked = false;

      // cell.addEventListener('mousedown', () => {
      //   console.log('MOUSEDOWN!');
      //   isClicked = true;
      // });

      // cell.addEventListener('mouseup', () => {
      //   isClicked = false;
      // });

      // cell.addEventListener('mouseenter', () => {
      //   console.log(`${isClicked}`);
      //   cell.style.backgroundColor = selectedColor;
      //   if (isClicked) {
      //     console.log(`onMouseenter with isClicked: ${isClicked}`);
      //   }
      // });

      // cell.style.backgroundColor = selectedColor;

      cell.addEventListener('click', () => {
        cell.style.backgroundColor = selectedColor;
      });
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
createPixels(50, 30);
