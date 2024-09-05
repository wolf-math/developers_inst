// volume = 4/3 pi r ** 3

const radForm = document.getElementById('MyForm');

radForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const radius = radForm.elements['radius'].value;

  // I tried to make this a try/catch, but Number(radius) returns NaN instead of error
  volume = Math.PI * Number(radius) ** 3;

  radForm.elements['volume'].value = volume;
});
