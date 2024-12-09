document.addEventListener('DOMContentLoaded', function () {
    const imageInput = document.querySelector('input[type="file"]');
    const previewImage = document.getElementById('imagePreview');

    if (!imageInput || !previewImage) {
        return; // Exit if elements are not found
    }

    const placeholderURL = previewImage.src;

    imageInput.addEventListener('change', function () {
        const file = this.files[0];

        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                previewImage.src = e.target.result; // Set the preview image
                previewImage.style.display = 'block'; // Ensure it is visible
            };
            reader.readAsDataURL(file);
        } else {
            previewImage.src = placeholderURL; // Reset to placeholder if no file selected
            previewImage.style.display = 'block';
        }
    });
});
