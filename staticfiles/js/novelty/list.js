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
            {'data': 'bus.name'},
            {'data': 'start_hour'},
            {'data': 'end_hour'},
            {'data': 'start_date'},
            {'data': 'end_date'},
            {'data': 'description'},
            {'data': 'created_by'},
            {'data': 'description'},
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
        $('#modal-novelty').modal('show');
    });
    // /*Used for clean and reset the form when the modal is closed*/
    // $('#modal-novelty').on('hidden.bs.modal', function () {
    //     $(this).find('#form-novelty')[0].reset();
    //
    // });
    /*Reset input in form modal*/
    resetModal('#modal-novelty', '#form-novelty');
    $('#table-list tbody')
        .on('click', '#btn-edit', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('select[name="bus"]').val(data.bus.id);
            $('input[name="start_date"]').val(data.start_date);
            $('input[name="end_date"]').val(data.end_date);
            $('input[name="start_hour"]').val(data.start_hour);
            $('input[name="end_hour"]').val(data.end_hour);
            $('textarea[name="description"]').val(data.description);
            $('#modal-novelty').modal('show');
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
        submitDataAjax(window.location.pathname, parameters);
    });

});