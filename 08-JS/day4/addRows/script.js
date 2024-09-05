function insertRow() {
  let table = document.getElementById('sampleTable');

  // Insert a new row at the end of the table
  let newRow = table.insertRow(-1);

  // Insert new cells in the new row
  let cell1 = newRow.insertCell(0);
  let cell2 = newRow.insertCell(1);

  // Add text to the new cells
  cell1.textContent = 'New cell1';
  cell2.textContent = 'New cell2';
}
