document.addEventListener('DOMContentLoaded', function () {
    const imageInput = document.querySelector('input[type="file"]');
    const previewImage = document.getElementById('imagePreview');

    if (!imageInput || !previewImage) {
        console.error("Image input or preview image element is missing!");
        return;
    }

    const placeholderURL = previewImage.src;

    imageInput.addEventListener('change', function () {
        const file = this.files[0];
        console.log("File selected: ", file); // Debugging log for selected file

        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                console.log("FileReader result: ", e.target.result); // Debugging log for base64 string
                previewImage.src = e.target.result;
                previewImage.style.display = 'block'; // Ensure the preview is shown
            };
            reader.onerror = function (error) {
                console.error("Error reading file: ", error); // Debugging log for errors
            };
            reader.readAsDataURL(file); // Start reading the file
        } else {
            console.warn("No file selected, resetting preview.");
            previewImage.src = placeholderURL;
            previewImage.style.display = 'block';
        }
    });
});
