function toggleMenu() {
    document.getElementById("navLinks").classList.toggle("active");
}

function filterImages(cat) {
    document.querySelectorAll('.lightbox-img').forEach(img => {
        img.style.display =
            cat === 'all' || img.classList.contains(cat) ? 'block' : 'none';
    });
}

document.querySelectorAll('.lightbox-img').forEach(img => {
    img.onclick = () => {
        document.getElementById('lightbox').style.display = 'flex';
        document.getElementById('lightbox-img').src = img.src;
    };
});

function closeLightbox() {
    document.getElementById('lightbox').style.display = 'none';
}


const revealElements = document.querySelectorAll(".reveal");

function revealOnLoadAndScroll() {
    revealElements.forEach(el => {
        const top = el.getBoundingClientRect().top;
        const trigger = window.innerHeight - 100;

        if (top < trigger) {
            el.classList.add("show");
        }
    });
}

window.addEventListener("load", revealOnLoadAndScroll);

window.addEventListener("scroll", revealOnLoadAndScroll);
window.addEventListener("load", () => {
    const hero = document.querySelector(".hero-content");
    if (hero) hero.classList.add("show");
});
