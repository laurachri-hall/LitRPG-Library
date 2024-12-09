document.addEventListener('DOMContentLoaded', function () {
    // Like Review
    document.querySelectorAll('.like-review-btn').forEach(button => {
        button.addEventListener('click', function () {
            const reviewId = this.getAttribute('data-review-id');
            fetch(`/review/${reviewId}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                const likesCount = document.getElementById(`review-likes-${reviewId}`);
                likesCount.textContent = data.total_likes;
                this.querySelector('i').classList.toggle('fa-thumbs-up', data.liked);
                this.querySelector('i').classList.toggle('fa-thumbs-o-up', !data.liked);
            });
        });
    });

    // Like Comment
    document.querySelectorAll('.like-comment-btn').forEach(button => {
        button.addEventListener('click', function () {
            const commentId = this.getAttribute('data-comment-id');
            fetch(`/comment/${commentId}/like/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                const likesCount = document.getElementById(`comment-likes-${commentId}`);
                likesCount.textContent = data.total_likes;
                this.querySelector('i').classList.toggle('fa-thumbs-up', data.liked);
                this.querySelector('i').classList.toggle('fa-thumbs-o-up', !data.liked);
            });
        });
    });
});
