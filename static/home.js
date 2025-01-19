$(document).ready(function() {
    $('#prediction-form').submit(function(e) {
        e.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            url: '/predict',
            type: 'POST',
            data: formData,
            success: function(response) {
                $('#result').html('Predicted Price: $' + response.predicted_price.toFixed(2) + 
                                  '<br>Recommended Action: ' + response.action);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
                $('#result').html('An error occurred: ' + xhr.responseText);
            }
        });
    });
});
