const quizCategorySlug = JSON.parse(document.getElementById('slug').textContent); 
console.log(quizCategorySlug)

const options = document.getElementById('options');


const quizSocketProtocol = window.location.protocol === "https:" ? 'wss://' : 'ws://';

const url = quizSocketProtocol + window.location.host + '/ws/quiz/' + `${quizCategorySlug}` + '/';

console.log(url)

const quizSocket = new WebSocket(url); 

const questionText = document.getElementById("questionText");


quizSocket.onmessage = (event) => { 
	data = JSON.parse(event.data);
	console.log(data);

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

renderQuestion = (data) => { 
	console.log(data);
	questionText.textContent = data['question'];
	for (i = 0;i<data['options'].length;i++){
		optionElement = createOptionElement();
		optionElement.value = data['options'][i];
		options.appendChild(optionElement);

	}


}

createOptionElement = () => { 
	element = document.createElement('button');
	element.classList.add('btn');
	element.classList.add('btn-outline-dark');
	return element
}

