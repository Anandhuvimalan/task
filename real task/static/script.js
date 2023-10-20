$(document).ready(function(){
    $('#department').change(function(){
        var departmentId = $(this).val();
        $.ajax({
            url: '/get_courses/',
            type: 'GET',
            data: {'department_id': departmentId},
            success: function(data){
                $('#course').empty();
                $.each(data.courses, function(key, value){
                    $('#course').append('<option value="' + key + '">' + value + '</option>');
                });
                $('#course').prop('disabled', false);
            }
        });
    });
});

(function () {
    'use strict';
    window.addEventListener('load', function () {
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();