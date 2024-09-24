function getvalue(event) {
  // Prevent the form from submitting and refreshing the page
  event.preventDefault();

  let form = document.forms[0];
  // let form = document.getElementById('form1');

  let firstName = form.elements['fname'].value;
  let lastName = form.elements['lname'].value;

  // Display the values
  alert('First Name: ' + firstName + '\nLast Name: ' + lastName);

  console.log('First Name:', firstName);
  console.log('Last Name:', lastName);
}
