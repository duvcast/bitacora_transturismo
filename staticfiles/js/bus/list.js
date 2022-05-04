var tableList;

function getDataTable() {
    tableList = $('#table-list').DataTable({
        responsive: true,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'action': 'list'},
            dataSrc: ''
        },
        columns: [
            {'data': 'id'},
            {'data': 'name'},
            {'data': 'code'},
            {'data': 'plate'},
            {'data': 'brand'},
            {'data': 'model'},
            {'data': 'driver.name'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<button type="button" id="btn-edit" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></button> ';
                    buttons += '<button type="button" id="btn-delete" class="btn btn-danger btn-xs btn-flat" ><i class="fas fa-trash"></i></button>';
                    return buttons;
                },
            },
            {
                "targets": [0],
                "visible": false
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {
    getDataTable();

    $('#table-list tbody')
        .on('click', '#btn-edit', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="name"]').val(data.name);
            $('input[name="id"]').val(data.id);
            $('select[name="driver"]').val(data.driver.id);
            $('#modal-bus').modal('show');
        })
        .on('click', '#btn-delete', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submitDataAjax(window.location.pathname, parameters);
        });
    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        $('#modal-bus').modal('hide');
        submitDataAjax(window.location.pathname, parameters);
    });
});