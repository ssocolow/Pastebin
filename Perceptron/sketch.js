let NUMBER_OF_WEIGHTS = 3; //If this is a perceptron, this should be 2
let NUMBER_OF_POINTS = 2000;
let LEARNING_RATE = 0.001;

//Trying to save data
let json = {};
let writer;

let correct = 0;

let points = [];

let b;

let training = false;


function setup() {
  createCanvas(400, 400);
  writer = createWriter('Perceptron_data.txt');

  //Making the points
  for (let i = 0; i < NUMBER_OF_POINTS; i++){
  	points[i] = new Point(); 
	}
  
  //Making the Perceptron
  b = new Perceptron();
  
  //Adding initial weights to JSON
  json.weights = b.weights;
  json.learning_rate = b.learning_rate;
}

function draw() {
  correct = 0;
  
  background(255);
  stroke(0);
  
    
  let x1 = -1;
  let y1 = f(x1);
  let x2 = 1;
  let y2 = f(x2);
  
  x1 = map(x1,-1,1,0,width);
  x2 = map(x2,-1,1,0,width);
  y1 = map(y1,-1,1,height,0);
  y2 = map(y2,-1,1,height,0);
  
  line(x1,y1,x2,y2);
  
  //ISSUE 
  //I could not get what the perceptron thought the line was to be drawn as a line on the screen
  
//   let p3 = new Point(1,b.guessY(1));
//   let p4 = new Point(-1,b.guessY(-1));
//   //print(p3.pixelX(),p3.pixelY())
  
//   line(p3.pixelX(),p3.pixelY(),p4.pixelX(),p4.pixelY());
  
  
  
//   //line(0,height,width,0);
  
  //Show points
  for(let point of points){
    point.show();
  }
  
  //Train the network for each of the points
  for(let pt of points){
    let inputs = [pt.x/width, pt.y/height, pt.bias];
    let target = pt.label;
   
    //Train it when mouse is clicked
    b.train(inputs, target);
    if(training){
  		b.train(inputs, target);
		}
  
    let guess = b.guess(inputs);
    if(guess == target) {
      fill(0,255,0);
      correct++;
    } else {
      fill(255,0,0);
    }
    noStroke();
    ellipse(pt.pixelX(),pt.pixelY(),4,4);
  }
  	//Stop it from training until the next mouse click
    training = false;
  	document.getElementById("error").innerHTML = correct +' / '+ str(NUMBER_OF_POINTS);
  	//document.getElementById("weights").innerHTML = b.weights;

  
}

function mousePressed(){

}
