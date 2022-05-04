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
            {'data': 'driver.name'},
            {'data': 'relief.name'},
            {'data': 'start_date'},
            {'data': 'end_date'},
            {'data': 'created_by'},
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
    $('#btn-add').on('click', function () {
        $('input[name="action"]').val('add');
        $('#modal-relief-driver').modal('show');
    });
    /*Used for clean and reset the form when the modal is closed*/
    $('#modal-relief-driver').on('hidden.bs.modal', function () {
        $(this).find('#form-relief-driver')[0].reset();

    });
    /*Reset input in form modal*/
    resetModal('#modal-relief-driver', '#form-relief-driver');
    $('#table-list tbody')
        .on('click', '#btn-edit', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('select[name="driver"]').val(data.driver.id);
            $('select[name="relief"]').val(data.relief.id);
            $('input[name="start_date"]').val(data.start_date);
            $('input[name="end_date"]').val(data.end_date);
            $('#modal-relief-driver').modal('show');
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
        submitDataAjax(window.location.pathname, parameters, '#modal-relief-driver');
    });

});