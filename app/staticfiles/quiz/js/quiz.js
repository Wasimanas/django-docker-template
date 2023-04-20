

const quizCategorySlug = JSON.parse(document.getElementById('slug').textContent); 

const quizSocketProtocol = window.location.protocol === "https:" ? 'wss://' : 'ws://';


const url = quizSocketProtocol + window.location.host + '/ws/quiz/' + `${quizCategorySlug}` + '/';

const quizSocket = new WebSocket(url); 


quizSocket.onmessage = (event) => { 
	data = JSON.parse(event.data);

	if (data['action'] === 'question') { 
		renderQuestion(data);
	}
	else if (data['action'] === 'questionReported' ){ 
		questionReported();
	}
	else if (data['action'] === 'verifyAnswer') {
		verifyAnswer(data);
	}


}


nextQuestion = (data) => { 
	document.getElementById('optionElements').innerHTML = '';

	quizSocket.send(JSON.stringify({"action":"nextQuestion"}))
}



renderOptionElements = (data) => {  
	optionData = data['options'];
	for(option in optionData) { 
		const optionElement = document.createElement('button');
		optionElement.classList.add('btn');
		if (data['action'] === 'verifyAnswer') {
		optionElement.textContent = optionData[option][0]
			optionElement.classList.remove('btn-outline-seconary');
			optionElement.disabled = true;
			if (data['options'][option][1])
			{
			
			optionElement.classList.add('btn-outline-success'); 
			} 
			else { 
				optionElement.classList.add('btn-outline-danger');
			}
		}
		else {
		optionElement.textContent = optionData[option]
		optionElement.classList.add('btn-outline-secondary');
		}
		optionElement.addEventListener('click',submitAnswer);
		document.querySelector('.optionElements').appendChild(optionElement);

	}
}

renderQuestion = (data) => { 
	renderOptionElements(data);
	document.getElementById('questionText').innerHTML = data['question']; 



}

submitAnswer  = (event) => {  
	event.preventDefault();
	answerText = event.target.textContent;
	quizSocket.send(JSON.stringify({"action":"submitAnswer"}))


}


verifyAnswer = (data) =>{ 
	document.getElementById('solutionParentContainer').style.display = 'block';
	document.getElementById('solutionContainer').innerHTML = data['solution'];     
	document.getElementById('optionElements').innerHTML = '';
renderOptionElements(data)
	}




document.getElementById('nextButton').addEventListener('click',nextQuestion)
