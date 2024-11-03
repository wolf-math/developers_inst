const getJoke = () => {
  fetch('https://api.chucknorris.io/jokes/random?category=dev')
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('not funny');
      }
    })
    .then((obj) => {
      console.log(obj);
      console.log(obj.value);
    })
    .catch(function (error) {
      console.log(`We got the error ${error}`);
    });
};

getJoke();
