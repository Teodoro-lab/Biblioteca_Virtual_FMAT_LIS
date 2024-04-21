let submitButton = document.querySelector(".coment-form input[type=submit]");
let feedback = document.querySelector(".submit_feedback");
let form_coment = document.querySelector(".coment-form textarea");

function setFeedback(message, color) {
    feedback.style.visibility = "visible";
    feedback.style.color = color;
    feedback.innerHTML = message;
}

let seconds = 4 * 1000;

submitButton.addEventListener("click", function (event) {
    // prevents the submit from triggering to quickly and not allowing the feedback to be shown
    event.preventDefault();  

    if (form_coment.value === "") {
        setFeedback("Escribe un comentario por favor!", "red");
        setTimeout(function () {
            feedback.style.visibility = "hidden";
        }, seconds);
    } else {
        setFeedback("¡Muchas gracias por tus comentarios. Los tomaremos en cuenta!", "#4FCFFF");
        setTimeout(function () {
            feedback.style.visibility = "hidden";
            let form = document.querySelector('.coment-form');
            form.submit();
        }, seconds);
    }
});