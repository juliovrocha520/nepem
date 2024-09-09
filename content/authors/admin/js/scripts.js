document.addEventListener('DOMContentLoaded', function() {
  let currentSlide = 0;

  function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-item');
    slides.forEach((slide, i) => {
      slide.style.display = i === index ? 'block' : 'none';
    });
  }

  function nextSlide() {
    const slides = document.querySelectorAll('.carousel-item');
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
  }

  function prevSlide() {
    const slides = document.querySelectorAll('.carousel-item');
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
  }

  // Initialize the carousel to show the first image
  showSlide(currentSlide);

  // Automatically cycle through slides every 3 seconds
  setInterval(nextSlide, 1000);
});
