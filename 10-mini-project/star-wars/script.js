document.addEventListener('DOMContentLoaded', () => {
  const loadCharacterBtn = document.getElementById('loadCharacterBtn');
  const characterInfo = document.getElementById('characterInfo');
  const loading = document.getElementById('loading');

  loadCharacterBtn.addEventListener('click', () => {
    const randomId = Math.floor(Math.random() * 83) + 1;
    fetchCharacter(randomId);
  });

  function fetchCharacter(id) {
    characterInfo.innerHTML = '';
    loading.style.display = 'block';

    fetch(`https://www.swapi.tech/api/people/${id}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.result) {
          const character = data.result.properties;
          displayCharacter(character);
          fetchHomeworld(character.homeworld);
        } else {
          characterInfo.innerHTML = 'Character not found.';
        }
      })
      .catch((error) => {
        console.error('Error fetching character:', error);
        characterInfo.innerHTML = 'An error occurred.';
      })
      .finally(() => {
        loading.style.display = 'none';
      });
  }

  function fetchHomeworld(url) {
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        if (data.result) {
          const homeworld = data.result.properties.name;
          document.getElementById(
            'homeworld'
          ).textContent = `Homeworld: ${homeworld}`;
        }
      })
      .catch((error) => {
        console.error('Error fetching homeworld:', error);
      });
  }

  function displayCharacter(character) {
    characterInfo.innerHTML = `
      <h2>${character.name}</h2>
      <p>Height: ${character.height} cm</p>
      <p>Gender: ${character.gender}</p>
      <p>Birth Year: ${character.birth_year}</p>
      <p id="homeworld">Homeworld: Loading...</p>
    `;
  }
});
