class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  // Getter
  get area() {
    return this.height * this.width;
  }

  // Setter
  set area(factor) {
    this.width = this.width * factor ** 0.5;
    this.height = this.height * factor ** 0.5;
  }
}

const rect = new Rectangle(10, 20);
console.log(rect.area);
rect.area = 5;
console.log(rect.area);
console.log(rect.height);
console.log(rect.width);
console.log(rect.height * rect.width);
console.log(rect.height * rect.width === rect.area);
