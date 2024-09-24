let styleButton = document.getElementById('jsstyle');

// anonymous callback
styleButton.addEventListener('mouseover', () => {
  styleButton.style.backgroundColor = 'lightblue';
  styleButton.style.color = 'white';
  styleButton.style.border = '2px solid darkblue';
  styleButton.style.cursor = 'pointer';
});

styleButton.addEventListener('mouseout', function () {
  styleButton.style.backgroundColor = '';
  styleButton.style.color = '';
  styleButton.style.border = '';
});

// named callback
styleButton.addEventListener('click', clickFunction);

function clickFunction() {
  styleButton.style.backgroundColor = 'green';
  styleButton.style.color = 'white';
  styleButton.style.border = '2px solid darkgreen';
  styleButton.textContent = 'Clicked!';
  console.log('YOU PRESSED THE BUTTON!!!!');
  console.log('WHY DID YOU PRESS IT???');
  console.log('OH THE HUMANITY!!!');
}
