const temaOscuro = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "dark");
    document.querySelector("#icono_modo").setAttribute("class", "bi bi-sun-fill"); // Cambia al ícono del sol

    const botonModoOscuro = document.querySelector("#boton_modo_oscuro");
    botonModoOscuro.style.animation = "iluminacionBoton 1s infinite";
}

const temaClaro = () => {
    document.querySelector("body").setAttribute("data-bs-theme", "light");
    document.querySelector("#icono_modo").setAttribute("class", "bi bi-moon-fill"); // Cambia al ícono de la luna
}

const cambiarTema = () => {
    const cuerpo = document.querySelector("body");
    const icono = document.querySelector("#icono_modo");

    if (cuerpo.getAttribute("data-bs-theme") === "light") {
        temaOscuro();
    } else {
        temaClaro();
    }
}
