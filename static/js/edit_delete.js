// Initialize for review deletion
const reviewDeleteBtns = document.getElementsByClassName("btn-danger");  // Buttons for deleting reviews
const reviewDeleteForm = document.getElementById("reviewDeleteForm");  // The form for review deletion
const reviewDeleteModal = new bootstrap.Modal(document.getElementById("reviewDeleteModal"));
const reviewDeleteConfirm = document.getElementById("confirmReviewDelete");

// For editing comments
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

// For deleting comments
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// When the review delete button is clicked
for (let button of reviewDeleteBtns) {
  button.addEventListener("click", (e) => {
    // Get the review slug from the data-slug attribute
    let reviewSlug = e.target.getAttribute("data-slug");
    if (reviewSlug) {
      // Set the form's action URL for deletion
      reviewDeleteForm.action = `/review/${reviewSlug}/delete/`;  
      reviewDeleteModal.show();  // Show the modal
    } else {
      console.error("Review slug is missing!");
    }
  });
}

// When the confirm button is clicked, submit the form to delete the review
reviewDeleteConfirm.addEventListener("click", () => {
  reviewDeleteForm.submit();  // Submit the form to trigger review deletion
});

// When the confirm button is clicked, submit the form to delete the review
reviewDeleteConfirm.addEventListener("click", () => {
  reviewDeleteForm.submit();  // Submit the form to trigger review deletion
});


// Initializes edit functionality for the provided edit buttons
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}/`);
  });
}

// Initializes deletion functionality for the provided delete buttons
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let reviewSlug = e.target.getAttribute("data-slug");  // Ensure you pass the reviewSlug for each comment
    deleteConfirm.href = `/review/${reviewSlug}/delete_comment/${commentId}/`;  // Updated URL pattern for comment deletion
    deleteModal.show();
  });
}