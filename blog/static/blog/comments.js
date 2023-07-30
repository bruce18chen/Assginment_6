const likeButtons = document.querySelectorAll('.like-button');
const dislikeButtons = document.querySelectorAll('.dislike-button');

likeButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        const commentId = button.dataset.commentId;
        fetch(`/comments/${commentId}/like`, {
            method: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
        })
        .then(response => response.json())
        .then(data => {
            const likesSpan = document.getElementById(`likes-count-${commentId}`);
            likesSpan.innerText = data.likes;
        });
    });
});

dislikeButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        const commentId = button.dataset.commentId;
        fetch(`/comments/${commentId}/dislike`, {
            method: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
        })
        .then(response => response.json())
        .then(data => {
            const dislikesSpan = document.getElementById(`dislikes-count-${commentId}`);
            dislikesSpan.innerText = data.dislikes;
        });
    });
});
