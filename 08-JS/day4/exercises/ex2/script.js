// Retrieve the form and console.log it.

const nameForm = document.querySelectorAll('form')[0];
console.log(nameForm);

// Retrieve the inputs by their id and console.log them.

const fname = document.getElementById('fname');
const lname = document.getElementById('lname');

// I did too much! commented it out.

// fname.addEventListener('input', (e) => {
//   console.log(e.target.value);
// });

// lname.addEventListener('input', (e) => {
//   console.log(e.target.value);
// });

// Retrieve the inputs by their name attribute and console.log them.

const nmForm = document.forms[0];
const fName = nmForm['fname'];
const lName = nmForm['lname'];

fName.addEventListener('input', (e) => {
  console.log(e.target.value);
});

lName.addEventListener('input', (e) => {
  console.log(e.target.value);
});

// When the user submits the form (ie. submit event listener)

// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :

// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>

nmForm.addEventListener('submit', (e) => {
  e.preventDefault();

  const first = e.target[0].value;
  const last = e.target[1].value;

  uList = document.getElementsByClassName('usersAnswer')[0];
  uList.innerHTML += `<li>${first}</li>`;
  uList.innerHTML += `<li>${last}</li>`;
});
