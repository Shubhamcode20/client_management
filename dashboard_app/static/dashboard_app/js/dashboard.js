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

// Bootstrap Table Ajax Handler
window.ajaxRequest = function (params) {
    const url = '/api/clients/';
    $.get(`${url}?${$.param(params.data)}`).then(function (res) {
        params.success(res);
    });
};

$(document).ready(function () {
    // Initialize Bootstrap Table (in case it's not auto-init)
    $('#clientTable').bootstrapTable();

    // Handle form submission to add client
    $('#clientForm').submit(function (e) {
        e.preventDefault();
        $.post('/clients/add/', $(this).serialize(), function (response) {
            if (response.status === 'success') {
                $('#clientModal').modal('hide');
                $('#clientForm')[0].reset();
                $('#clientTable').bootstrapTable('refresh'); // Refresh table
            } else {
                alert('Failed to add client');
            }
        }).fail(function () {
            alert('Error submitting form. CSRF token might be missing.');
        });
    });
});
