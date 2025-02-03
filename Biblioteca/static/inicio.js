// static/js/inicio.js
const inicializarImagenDeFondo = () => {
    const theme = localStorage.getItem("theme");
    const imagenDeFondo = document.querySelector("#imagenDeFondo");
    if (imagenDeFondo) {
        if (theme === "dark") {
            imagenDeFondo.style.opacity = 0.3;
        } else {
            imagenDeFondo.style.opacity = 0.5;
        }
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    inicializarImagenDeFondo();
});
