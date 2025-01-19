$(document).ready(function() {
    const API_URL = 'https://smartsave-cgw1.onrender.com';

    $('#prediction-form').submit(function(e) {
        e.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            url: `${API_URL}/predict`,  // Updated to use full URL
            type: 'POST',
            data: formData,
            success: function(response) {
                $('#result').html('Predicted Price: €' + response.predicted_price.toFixed(2) + 
                                '<br>Recommended Action: ' + response.action);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
                $('#result').html('An error occurred: ' + error);
            }
        });
    });
});