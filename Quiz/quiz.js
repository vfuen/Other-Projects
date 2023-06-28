var start = function(){
	
	var correct = 0;
	var incorrect = 0;
	var question = "none";
	var input = "none";
	var answer = "none";



	var ask = function(onClick){
		input = prompt(question);
};

var score = function(){
	if(input == answer){
		correct = correct+1;
		alert("correct");
	}else{
		incorrect = incorrect+1;
		alert("incorrect");
	}
};


var points = function(){
	ask();
	score();
};

alert("welcome to my quiz, you will be answering 10 questions.");


question = "What is 3 + 11?";
answer = "14";
points();
question = "What is 24*3?";
answer = "72";
points();
question = "How many letters are in JavaScript";
answer = "9";
points();
question = "How many characters is extended ASCII";
answer = "256";
points();
question = "What is the binary code for a in ASCII ";
answer = "1100001";
points();


alert("Well done! You got " + correct + " out of 5 correct!");



}



