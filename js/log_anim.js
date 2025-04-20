const singInBtn = document.querySelector('.singin-btn');
const singUpBtn = document.querySelector('.singup-btn');
const formBox = document.querySelector('.form_box');

singUpBtn.addEventListener('click', function() {
    formBox.classList.add('active');
});

singInBtn.addEventListener('click', function() {
    formBox.classList.remove('active');
});