/* Open and close navbar <mode mobile> */

const navbar = document.querySelector('.mobile-menu');
const body = document.querySelector('body');

navbar.addEventListener('click',() => {
    navbar.classList.contains("bi-list")
    ? navbar.classList.replace("bi-list", "bi-x")
    : navbar.classList.replace("bi-x", "bi-list");
    body.classList.toggle("nav-menu-active")
});

const navItem = document.querySelectorAll(".nav-item");

navItem.forEach((item) => {
    item.addEventListener("click", () => {
        if (body.classList.contains("nav-menu-active")) {
            body.classList.remove("nav-menu-active");
            navbar.classList.replace("bi-x", "bi-list");
        }
    });
});

const item = document.querySelectorAll("[data-anime]");

const animeScroll = () => {
  const windowTop = window.pageYOffset + window.innerHeight * 0.85 ;

    item.forEach((element) => {
        if (windowTop > element.offsetTop) {
            element.classList.add("animate");
            } else {
            element.classList.remove("animate");
        }
    });
};

animeScroll();

window.addEventListener("scroll", ()=>{
    animeScroll();
})