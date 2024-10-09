async function fetchData() {
  const fetch = (await import('node-fetch')).default;

  fetch('https://www.swapi.tech/api/people/1')
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
}

fetchData();
