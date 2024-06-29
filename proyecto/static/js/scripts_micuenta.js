document.getElementById('loginButton').addEventListener('click', function(event) {
    const nombreUsuario = document.getElementById('nombreUsuario');
    const contrasena = document.getElementById('contrasena');
    let isValid = true;

    // Validar nombre de usuario
    if (nombreUsuario.value.trim() === '') {
        nombreUsuario.classList.add('is-invalid');
        isValid = false;
    } else {
        nombreUsuario.classList.remove('is-invalid');
    }

    // Validar contraseña
    if (contrasena.value.trim() === '') {
        contrasena.classList.add('is-invalid');
        isValid = false;
    } else {
        contrasena.classList.remove('is-invalid');
    }

    // Evitar que se muestre el modal cuando los no haya validacion
    if (isValid) {
    var myModal = new bootstrap.Modal(document.getElementById('exampleModal'));
    myModal.show();
    }
});