#!/usr/bin/node
class Rectangle{
    
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

    print() {
      if (Object.keys(this).length === 0) {
        console.log("Empty object");
      } else {
        for (let i = 0; i < this.height; i++) {
          console.log("X".repeat(this.width));
        }
      }
    }


  rotate() {
    if (Object.keys(this).length !== 0) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double() {
    if (Object.keys(this).length !== 0) {
      this.width *= 2;
      this.height *= 2;
    }
  }
    
}

module.exports = Rectangle;