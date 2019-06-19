function f(x){
  // y = mx + b
  return 0.3 * x + 0.4;
  
}

class Point {
  constructor(x,y){
    if(!x || !y){
    this.x = random(-1,1);
    this.y = random(-1,1);
  }else{
    this.x = x;
    this.y = y;
  }
    
    this.bias = 1;
    
    this.lineY = f(this.x);
    
    this.label = 0;
    
    if(this.y > this.lineY){
      this.label = 1;
    } else {
      this.label = -1;
    }
  }
  show(){
    stroke(0);
    if(this.label == 1){
      fill(255);
    }
    else {
      fill(0);
    }
    let px = this.pixelX();
    let py = this.pixelY();
    ellipse(px,py,8,8);
    
  }
  pixelX(){
    return map(this.x,-1,1,0,width);
  }
  pixelY(){
    return map(this.y,-1,1,height,0);
  }
  
  
  
}
