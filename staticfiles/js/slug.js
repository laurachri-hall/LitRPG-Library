  // Wait until the DOM is fully loaded
  document.addEventListener('DOMContentLoaded', function () {
      function slugify(text) {
          return text
              .toString()
              .toLowerCase()
              .trim()
              .replace(/[\s\W-]+/g, '-'); // Replace spaces and non-word characters with hyphens
      }

      const titleInput = document.getElementById('title');
      const slugInput = document.getElementById('slug');

      if (titleInput && slugInput) {
          titleInput.addEventListener('input', function (e) {
              const title = e.target.value;
              const slug = slugify(title);
              slugInput.value = slug; // Populate slug field dynamically
          });
      } else {
          console.error('Title or Slug input field not found.');
      }
  });