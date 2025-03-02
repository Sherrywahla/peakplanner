setTimeout(function () {
  const alerts = document.querySelectorAll('.p-4');
  alerts.forEach(alert => {
    alert.classList.add('opacity-0', 'transition-opacity', 'duration-500');
    setTimeout(() => alert.remove(), 500);
  });
}, 4000);
