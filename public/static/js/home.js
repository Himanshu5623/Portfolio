document.addEventListener('DOMContentLoaded', () => {
    const revealItems = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15 });

    revealItems.forEach(item => {
        revealObserver.observe(item);
    });

    const cards = document.querySelectorAll('.mini-card, .stat-card, .project-card, .cta-card');

    cards.forEach((card, index) => {
        card.style.transitionDelay = `${index * 80}ms`;
    });
});
