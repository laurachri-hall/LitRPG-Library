document.addEventListener('DOMContentLoaded', () => {
  // Handle review deletion
  const reviewDeleteBtns = document.getElementsByClassName("btn-danger");
  const reviewDeleteForm = document.getElementById("reviewDeleteForm");
  const reviewDeleteModal = new bootstrap.Modal(document.getElementById("reviewDeleteModal"));
  const reviewDeleteConfirm = document.getElementById("confirmReviewDelete");

  // Handle comment deletion
  const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  // For editing comments
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_content");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");

  // Review Deletion
  for (let button of reviewDeleteBtns) {
      button.addEventListener("click", (e) => {
          let reviewSlug = e.target.getAttribute("data-slug");
          if (reviewSlug) {
              reviewDeleteForm.action = `/review/${reviewSlug}/delete/`;  // Dynamically set the form's action
              reviewDeleteModal.show();
          } else {
              console.error("Review slug is missing!");
          }
      });
  }

  // Confirm review deletion
  reviewDeleteConfirm.addEventListener("click", () => {
      reviewDeleteForm.submit();  // Submit the form to trigger review deletion
  });

  // Edit comment functionality
  for (let button of editButtons) {
      button.addEventListener("click", (e) => {
          let commentId = e.target.getAttribute("comment_id");
          let commentContent = document.getElementById(`comment${commentId}`).innerText;
          commentText.value = commentContent;  // Set the comment text in the form field
          submitButton.innerText = "Update";  // Change the button text to "Update"
          commentForm.setAttribute("action", `/review/edit_comment/${commentId}/`);  // Dynamically set form action
      });
  }

  // Comment Deletion
  for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
          let commentId = e.target.getAttribute("comment_id");
          let reviewSlug = e.target.getAttribute("data-slug");
          deleteConfirm.href = `/review/${reviewSlug}/delete_comment/${commentId}/`;  // Set the correct URL for comment deletion
          deleteModal.show();
      });
  }

  // Star rating interaction (optional for interactive ratings)
  const ratingStars = document.querySelectorAll('.rating-stars i');
  if (ratingStars.length > 0) {
      ratingStars.forEach(star => {
          star.addEventListener('click', (e) => {
              const rating = e.target.getAttribute('data-rating');
              // You can send the selected rating value to the server via AJAX or form submission
              console.log(`Rating selected: ${rating}`);
          });
      });
  }
});