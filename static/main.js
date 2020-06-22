$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});

$(function () {
    $('#datetimepicker5').datetimepicker({
        format: 'YYYY-MM-DD'
    });
});

$(document).ready(function () {
    $("#success-alert").hide();
    $("#myWish").click(function showAlert() {
        $("#success-alert").alert();
        window.setTimeout(function () {
            $("#success-alert").alert('close');
        }, 3000);
    });
});