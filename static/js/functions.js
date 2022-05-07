$(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
        }
    })
});

function message_error(obj) {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }
    Swal.fire({
        title: 'Error',
        html: html,
        icon: 'error'
    })

}

function submitDataAjax(url, parameters, idModal) {
    $.ajax({
        url: url,
        type: 'POST',
        data: parameters,
        dataType: 'json',
        processData: false,  // tell jQuery not to process the data
        contentType: false,   // tell jQuery not to set contentType
    }).done(function (data) {
        console.log(data);
        if (!data.hasOwnProperty('error')) {
            $(idModal).modal('hide')
            tableList.ajax.reload();
            tableScheduleList.ajax.reload();
            return false;
        }
        message_error(data.error);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    })

}

/*Used for clean and reset the form when the modal is closed*/
function resetModal(idModal, idForm) {
    $(idModal).on('hidden.bs.modal', function () {
        $(this).find(idForm)[0].reset();
    });
}

// <script>
//
//         function getData() {
//             $("#buses-table").DataTable({
//                 responsive: true,
//                 autoWidth: true
//             })
//         }
//
//         getData();
//
//         {% comment %} $('#contracts-table tbody ').on('click', 'tr', function () {
//              console.log(table.row(this).data()[0]);
//          });{% endcomment %}
//
//         function showModalEdit(driverId, driverName) {
//             document.getElementById("id-bus-input").value = driverId;
//             document.getElementById("input-bus-name").value = driverName;
//             $('#modal-assign-driver').modal('show');
//         }
//
//         $('#form-assign-driver').on('submit', function (e) {
//
//             e.preventDefault();
//
//             var serializedData = $(this).serialize();
//             $.ajax({
//                 url: "{% url 'administremos:drivers' %}",
//                 type: 'POST',
//                 data: serializedData,
//                 success: function () {
//                     $('#modal-assign-driver').modal('hide');
//                     location.reload();
//                 }
//             })
//         })
//
//
//         function showModalDelete(busId) {
//             document.getElementById("id-bus-delete").value = busId;
//             $('#modal-unassign-driver').modal('show');
//         }
//
//         $('#form-delete-driver').on('submit', function (e) {
//
//             e.preventDefault();
//
//             var serializedData = $(this).serialize();
//             $.ajax({
//                 url: "{% url 'administremos:remove_driver' %}",
//                 type: 'POST',
//                 data: serializedData,
//                 success: function () {
//                     $('#modal-unassign-driver').modal('hide');
//                     location.reload();
//                 }
//             })
//         });
//         $('#btn-close').on('click', function () {
//             $('#modal-unassign-driver').modal('hide');
//         })
//
//     </script>
