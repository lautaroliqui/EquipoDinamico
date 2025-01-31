// static/js/theme.js
const temaOscuro = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "dark");
    document.querySelector("#sun-icon").style.display = "inline";
    document.querySelector("#moon-icon").style.display = "none";
    document.querySelector("#imagenDeFondo").style.opacity = 0.3;
}

const temaClaro = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "light");
    document.querySelector("#moon-icon").style.display = "inline";
    document.querySelector("#sun-icon").style.display = "none";
    document.querySelector("#imagenDeFondo").style.opacity = 0.5;
}

const inicializarTema = () => {
    if (document.querySelector("body").getAttribute("data-bs-theme") === "dark") {
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

