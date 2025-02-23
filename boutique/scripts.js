// Animation GSAP pour la navbar
gsap.from(".navbar", { duration: 1, y: -50, opacity: 0, ease: "power2.out" });

// Ajoute un effet de transition smooth au défilement
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute("href")).scrollIntoView({
                behavior: "smooth"
            });
        });
    });
});
