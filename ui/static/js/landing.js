document.addEventListener('DOMContentLoaded', function () {
  const menuToggle = document.querySelector('[data-collapse-toggle]');
  const menu = document.getElementById('mobile-menu-2');
  const menuIcon = menuToggle.querySelector('svg:first-child');
  const closeIcon = menuToggle.querySelector('svg:last-child');

  menuToggle.addEventListener('click', function () {
    const isExpanded = menu.classList.toggle('hidden');

    // Toggle icons
    if (isExpanded) {
      menuIcon.classList.remove('hidden');
      closeIcon.classList.add('hidden');
    } else {
      menuIcon.classList.add('hidden');
      closeIcon.classList.remove('hidden');
    }
  });
});
