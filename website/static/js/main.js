
function toggleMenu() {
    document.getElementById("navLinks").classList.toggle("active");
}
const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");

document.querySelectorAll(".lightbox-img").forEach(img => {
    img.addEventListener("click", () => {
        lightbox.classList.add("show");
        lightboxImg.src = img.src;
        document.body.style.overflow = "hidden";
    });
});

function closeLightbox() {
    lightbox.classList.remove("show");
    document.body.style.overflow = "";
}

document.addEventListener("keydown", e => {
    if (e.key === "Escape") {
        closeLightbox();
    }
});






function filterImages(cat) {
    document.querySelectorAll('.lightbox-img').forEach(img=>{
        img.style.display = cat==='all'||img.classList.contains(cat)?'block':'none';
    });
}

document.querySelectorAll('.lightbox-img').forEach(img=>{
    img.onclick=()=>{
        document.getElementById('lightbox').style.display='flex';
        document.getElementById('lightbox-img').src=img.src;
    }
});

function closeLightbox(){
    document.getElementById('lightbox').style.display='none';
}

window.addEventListener('scroll',()=>{
    document.querySelectorAll('.reveal').forEach(el=>{
        if(el.getBoundingClientRect().top < window.innerHeight-100){
            el.classList.add('active');
        }
    });
});

window.addEventListener("load", () => {
    const heroText = document.querySelector(".hero-content");
    heroText.classList.add("show");
});
const reveals = document.querySelectorAll(".reveal");
window.addEventListener("load", revealOnLoadAndScroll);

window.addEventListener("scroll", () => {
    reveals.forEach(section => {
        const top = section.getBoundingClientRect().top;
        const trigger = window.innerHeight - 100;

        if (top < trigger) {
            section.classList.add("show");
        }
    });
});