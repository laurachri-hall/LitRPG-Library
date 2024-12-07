// Select the GIF element
const gifToggle = document.getElementById('gif-toggle');

// Add click event listener
gifToggle.addEventListener('click', () => {
  // Toggle between the static and animated sources
  const isAnimated = gifToggle.src.includes('hero.gif');
  gifToggle.src = isAnimated 
    ? '/static/images/hero.png' // Switch to the static image
    : '/static/images/hero.gif'; // Switch back to the animated GIF
});