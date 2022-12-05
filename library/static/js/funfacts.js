import { translate } from './translate.js';

function request(url) {
    return new Promise((resolve, reject) => {
        fetch(url).then(function (response) {
            return response.json();
        }).then(function (data) {
            resolve(data);
        }).catch(function (err) {
            reject(err);
        });
    });
}


async function factAboutNumber(number) {
    let url = `http://numbersapi.com/${number}?json`;
    let body = await request(url);
    
    // añadir lógica para agregar elementos al html

    return body;
}

async function createFunFact(number) {
    let funfact = document.getElementById('fun-fact');
    let numberFact = await factAboutNumber(number);

    try {
        let transalatedFact = await translate(numberFact.text, 'EN', 'ES');
        console.log(transalatedFact);
        transalatedFact = JSON.parse(transalatedFact);

        if (funfact.hasChildNodes()) {
            funfact.removeChild(funfact.childNodes[0]);
            funfact.appendChild(document.createTextNode(transalatedFact.text));
        } else {
            funfact.appendChild(document.createTextNode(transalatedFact.text));
        }
        
    } catch (error) {
        
        if (funfact.hasChildNodes()) {
            funfact.removeChild(funfact.childNodes[0]);
            funfact.appendChild(document.createTextNode(numberFact.text));
        } else {
            funfact.appendChild(document.createTextNode(numberFact.text));
        }
        
        console.log(error);
    }


}


setInterval(function () {
    let number = Math.floor(Math.random() * 100);
    createFunFact(number);
}, 7 * 1000);








