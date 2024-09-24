const styleButton = document.getElementById('jsstyle');
const styledDiv = document.getElementById('styledDiv');

styledDiv.addEventListener('click', function (e) {
  alert('Div is Clicked');
});

styleButton.addEventListener('mouseover', function () {
  styleButton.style.backgroundColor = 'lightblue';
  styleButton.style.color = 'white';
  styleButton.style.border = '2px solid darkblue';
  styleButton.style.cursor = 'pointer';
});

styleButton.addEventListener('mouseout', function () {
  styleButton.style.backgroundColor = '';
  styleButton.style.color = '';
  styleButton.style.border = '';
  styleButton.textContent = 'Style';
});

styleButton.addEventListener('click', function (e) {
  // alert('Button is Clicked');
  styleButton.style.backgroundColor = 'lightgreen';
  styleButton.textContent = 'Clicked Again!';
  e.stopPropagation(); // Prevent the click event from bubbling up to the div
});
