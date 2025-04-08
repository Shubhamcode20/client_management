function getCSRFToken() {
    let csrfToken = null;
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(cookie => {
            const trimmed = cookie.trim();
            if (trimmed.startsWith('csrftoken=')) {
                csrfToken = decodeURIComponent(trimmed.substring('csrftoken='.length));
            }
        });
    }
    return csrfToken;
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!(/^GET|HEAD|OPTIONS|TRACE$/.test(settings.type))) {
            xhr.setRequestHeader("X-CSRFToken", getCSRFToken());
        }
    }
});


$(document).ready(function() {
    function loadClients() {
        $.get('/api/clients/', function(data) {
            var tableBody = '';
            data.forEach(function(client) {
                tableBody += `<tr><td>${client.name}</td><td>${client.primary_number}</td><td>${client.country_code}</td><td>${client.created_at}</td></tr>`;
            });
            $('#clientsTable tbody').html(tableBody);
        });
    }

    loadClients();

    $('#clientForm').submit(function(e) {
        e.preventDefault();
        $.post('/clients/add/', $(this).serialize(), function(response) {
            if (response.status === 'success') {
                $('#clientModal').modal('hide');
                loadClients();
                $('#clientForm')[0].reset();
            }
        });
    });
});
