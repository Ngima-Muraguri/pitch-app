let ham = document.getElementById('hamburger');
let links = document.getElementById('menu');

ham.addEventListener('click', () => {
    links.classList.toggle('active');
})
