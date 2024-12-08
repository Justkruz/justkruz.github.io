
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
const overlay = document.querySelector('.overlay');

// Toggle navigation and overlay visibility
navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('show');
  overlay.style.display = navLinks.classList.contains('show') ? 'block' : 'none';
});

// Close navigation when overlay is clicked
overlay.addEventListener('click', () => {
  navLinks.classList.remove('show');
  overlay.style.display = 'none';
});
