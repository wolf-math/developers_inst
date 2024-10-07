// Analyse the code below. Display the type of each rabbit and make them speak

class Rabbit {
  constructor(type) {
    this.type = type;
  }
  speak(line) {
    console.log(`The ${this.type} rabbit says, '${line}'`);
  }
}

let killerRabbit = new Rabbit('killer');
let blackRabbit = new Rabbit('black');

killerRabbit.speak('You are boring');
blackRabbit.speak('hi.');
