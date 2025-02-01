// static/js/theme.js
const temaOscuro = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "dark");
    document.querySelector("#moon-icon").style.display = "none";
    document.querySelector("#sun-icon").style.display = "inline";
    localStorage.setItem("theme", "dark");
}

const temaClaro = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "light");
    document.querySelector("#moon-icon").style.display = "inline";
    document.querySelector("#sun-icon").style.display = "none";
    localStorage.setItem("theme", "light");
}

const inicializarTema = () => {
    const theme = localStorage.getItem("theme");
    if (theme === "dark") {
        temaOscuro();
    } else {
        temaClaro();
    }
}

const cambiarTema = () => {
    if (document.querySelector("body").getAttribute("data-bs-theme") === "light") {
        temaOscuro();
    } else {
        temaClaro();
    }
}

// Inicializar el estado de los iconos según el tema actual
document.addEventListener('DOMContentLoaded', (event) => {
    inicializarTema();
    document.querySelector("#dl-icon").addEventListener("click", cambiarTema);
});

document.querySelector(".menu-btn").addEventListener("click",()=>{
    document.querySelector(".nav-menu").classList.toggle("show");
});