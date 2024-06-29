
(function () {
'use strict';
    var forms = document.querySelectorAll('.needs-validation');
        Array.prototype.slice.call(forms)
            .forEach(function (form) {
                form.addEventListener('submit', function (event) {
                    if (!form.checkValidity()) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                form.classList.add('was-validated');
            }, false);
        });
})();
     
$(document).ready(function(){
$('#registrationForm').submit(function(event){
        
    var formIsValid = true;
    $(this).find('input[type="text"], input[type="email"], input[type="password"], select').each(function(){
        if ($(this).val() === '') {
            formIsValid = false;
            return false; 
        }
    });

    if (formIsValid) {
        $('#successAlert').removeClass('d-none'); 
        event.preventDefault(); 
    }
    });
});
   