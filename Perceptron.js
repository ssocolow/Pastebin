function sign(n){
  if(n >= 0){
    return 1;
  }
  else {
   return -1; 
  }
}

class Perceptron {
  constructor(){
    this.weights = [];
    this.learning_rate = LEARNING_RATE;
    for(let i = 0; i < NUMBER_OF_WEIGHTS; i++){
      this.weights[i] = random(-1,1);
    }
  }
  guess(inputs){
    let sum = 0;
    for(let i = 0; i < this.weights.length; i++){
      sum += inputs[i] * this.weights[i];
    }
    let output = sign(sum);
    return output;
  }
  train(inputs, target){
    let guess = this.guess(inputs);
    let error = target - guess;
    
    //Tweaking the weights
    for(let i = 0; i < this.weights.length; i++){
      this.weights[i] += error * inputs[i] * this.learning_rate;
    }
    
  }
  guessY(x){
//     let m = this.weights[1] / this.weights[0];
//     let b = this.weights[2];
    
//     return m * x + b;
    let w0 = this.weights[0];
    let w1 = this.weights[1];
    let w2 = this.weights[2];
    
    return - (w0/w1) * x -(w2/w1);
    
  }
}
