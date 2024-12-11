$(document).ready(function() {
    $('.summernote').summernote({
        height: '100%', // Match the height in the widget configuration
        width: 300, // Ensure it adapts to the container
        toolbar: [
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['font', ['strikethrough', 'superscript', 'subscript']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['insert', ['link', 'picture', 'video']],
            ['view', ['fullscreen', 'codeview', 'help']]
        ]
    });
});