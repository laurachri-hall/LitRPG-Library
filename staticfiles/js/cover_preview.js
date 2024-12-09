    document.addEventListener('DOMContentLoaded', function () {
        const imageInput = document.querySelector('input[type="file"]');
        const previewImage = document.getElementById('imagePreview');

        imageInput.addEventListener('change', function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    previewImage.src = e.target.result;
                    previewImage.style.display = 'block'; // Show the preview
                };
                reader.readAsDataURL(file);
            } else {
                previewImage.style.display = 'none'; // Hide the preview if no file
                previewImage.src = 'static/images/cover_placeholder.png';
            }
        });
    });