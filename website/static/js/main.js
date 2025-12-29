/* =========================
   MOBILE NAVBAR
========================= */
function toggleMenu() {
    document.getElementById("navLinks").classList.toggle("active");
}

/* =========================
   PORTFOLIO FILTERS
========================= */
function filterImages(category) {
    document.querySelectorAll(".lightbox-img").forEach(img => {
        img.style.display =
            category === "all" || img.classList.contains(category)
                ? "block"
                : "none";
    });
}

/* =========================
   LIGHTBOX (IMMERSIVE)
========================= */
const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");

document.querySelectorAll(".lightbox-img").forEach(img => {
    img.addEventListener("click", () => {
        lightbox.classList.add("show");
        lightboxImg.src = img.src;
        document.body.style.overflow = "hidden"; // lock background scroll
    });
});

function closeLightbox() {
    lightbox.classList.remove("show");
    document.body.style.overflow = "";
}

/* Close lightbox on ESC */
document.addEventListener("keydown", e => {
    if (e.key === "Escape") {
        closeLightbox();
    }
});

/* =========================
   SCROLL REVEAL ANIMATIONS
========================= */
const reveals = document.querySelectorAll(".reveal");

function handleScrollReveal() {
    reveals.forEach(el => {
        const top = el.getBoundingClientRect().top;
        const trigger = window.innerHeight - 100;

        if (top < trigger) {
            el.classList.add("show");
        }
    });
}

window.addEventListener("scroll", handleScrollReveal);
window.addEventListener("load", handleScrollReveal);

/* =========================
   HERO TEXT ANIMATION
========================= */
window.addEventListener("load", () => {
    const heroText = document.querySelector(".hero-content");
    if (heroText) {
        heroText.classList.add("show");
    }
});
