// manipulate select
function modifySelect() {
  const selectElement = document.getElementById('school-type');

  // get 2nd Option
  const secondOptionValue = selectElement.options[1].value;
  console.log('Second Option Value:', secondOptionValue); // Outputs: "university"

  // add new option work
  const newOptionEnd = document.createElement('option');
  newOptionEnd.value = 'work';
  newOptionEnd.textContent = 'Work';
  selectElement.appendChild(newOptionEnd);

  // add a new option 'Primary School'
  const newOptionStart = document.createElement('option');
  newOptionStart.value = 'primaryschool';
  newOptionStart.textContent = 'Primary School';
  selectElement.insertBefore(newOptionStart, selectElement.firstChild);

  // change college

  // use selectedIndex
  selectElement.selectedIndex = 3; // Index of 'College' after adding 'Primary School' option

  // Method 2: Using `value` property
  // selectElement.value = 'college';

  // Method 3: Using `options` property and setting `selected` to true
  // selectElement.options[3].selected = true;

  // Function to alert the selected choice
  document
    .getElementById('alert-button')
    .addEventListener('click', function () {
      alert(
        'Selected Option: ' +
          selectElement.options[selectElement.selectedIndex].textContent
      );
    });
}

// Call the function to apply changes
modifySelect();
