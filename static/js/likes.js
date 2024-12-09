// Function to handle like button click for reviews
document.querySelectorAll('.like-review-btn').forEach(button => {
    button.addEventListener('click', function () {
        const reviewId = this.dataset.reviewId; // Get the review ID from data attribute
        const url = `/review/${reviewId}/like/`; // Construct the URL with the review ID

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.liked) {
                this.classList.add('liked'); // Add a visual cue for liked state
            } else {
                this.classList.remove('liked');
            }
            // Update like count
            document.querySelector(`#review-likes-${reviewId}`).textContent = data.total_likes;
        })
        .catch(error => console.error('Error:', error));
    });
});

// Function to handle like button click for comments
document.querySelectorAll('.like-comment-btn').forEach(button => {
    button.addEventListener('click', function () {
        const commentId = this.dataset.commentId; // Get the comment ID from data attribute
        const url = `/comment/${commentId}/like/`; // Construct the URL with the comment ID

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.liked) {
                this.classList.add('liked'); // Add a visual cue for liked state
            } else {
                this.classList.remove('liked');
            }
            // Update like count
            document.querySelector(`#comment-likes-${commentId}`).textContent = data.total_likes;
        })
        .catch(error => console.error('Error:', error));
    });
});

// Helper function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
