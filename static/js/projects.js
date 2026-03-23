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

    const projectCards = document.querySelectorAll('.featured-project');
    const visuals = document.querySelectorAll('.project-visual');
    const contentCards = document.querySelectorAll('.project-content');

    projectCards.forEach((card, index) => {
        card.style.transitionDelay = `${index * 90}ms`;
    });

    visuals.forEach((visual) => {
        visual.addEventListener('pointermove', (event) => {
            const rect = visual.getBoundingClientRect();
            const x = ((event.clientX - rect.left) / rect.width - 0.5) * 14;
            const y = ((event.clientY - rect.top) / rect.height - 0.5) * -14;

            visual.style.transform = `perspective(900px) rotateX(${y}deg) rotateY(${x}deg)`;
        });

        visual.addEventListener('pointerleave', () => {
            visual.style.transform = 'perspective(900px) rotateX(0deg) rotateY(0deg)';
        });
    });

    contentCards.forEach((card) => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-3px)';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
});
