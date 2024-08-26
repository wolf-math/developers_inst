for (let i = 0; i <= 15; i++) {
  if (i % 2 === 0) {
    document.getElementById('output').innerHTML += i + ' is even<br>';
  } else {
    document.getElementById('output').innerHTML += i + ' is odd<br>';
  }
}
