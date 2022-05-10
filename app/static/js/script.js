let pop = document.getElementById('pop');
let close = document.getElementById('close');
let dis = document.getElementById('display');
let form = document.getElementById('form');




dis.addEventListener('click', () => {
    pop.style.display = 'flex';
})
close.addEventListener('click', (e) => {
    pop.style.display = 'none';

    e.preventDefault();
})

form.addEventListener('submit', () => {
    alert('Pitch Published')
})