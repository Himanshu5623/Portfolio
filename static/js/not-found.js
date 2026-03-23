document.addEventListener('DOMContentLoaded', () => {
    const revealItems = document.querySelectorAll('.reveal');
    revealItems.forEach(item => {
        item.classList.add('is-visible');
    });
});
