let like = document.querySelector('.postlike');
let likecount = document.querySelector('.postlikecount');
let dislike = document.querySelector('.postdislike');
let dislikecount = document.querySelector('.postdislikecount');
like.addEventListener('click', () => {
    likecount.value = parseInt(likecount.value) + 1;
});
dislike.addEventListener('click', () => {
    dislikecount.value = parseInt(dislikecount.value) + 1;
});
