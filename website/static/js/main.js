
function toggleMenu() {
    document.getElementById("navLinks").classList.toggle("active");
}

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

window.addEventListener("scroll", () => {
    reveals.forEach(section => {
        const top = section.getBoundingClientRect().top;
        const trigger = window.innerHeight - 100;

        if (top < trigger) {
            section.classList.add("show");
        }
    });
});