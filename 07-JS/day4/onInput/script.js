function getvalue(event) {
  // Prevent the form from submitting and refreshing the page
  event.preventDefault();

  const form = document.getElementById('form1');

  const firstName = form.elements['fname'].value;
  const lastName = form.elements['lname'].value;

  // Display the values
  alert('First Name: ' + firstName + '\nLast Name: ' + lastName);

  console.log('First Name:', firstName);
  console.log('Last Name:', lastName);
}
