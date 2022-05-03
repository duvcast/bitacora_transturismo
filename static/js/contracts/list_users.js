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
            {'data': 'name_entity'},
            {'data': 'phone'},
            {'data': 'extension'},
            {'data': 'nit'},
            {'data': 'type_contractor'},
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
        $('#modal-user-contract').modal('show');
    });
    // $('#btn-add-fixed-contract').on('click', function () {
    //     $('input[name="action"]').val('add');
    //     $('#modal-user-contractor').modal('show');
    // });
    resetModal('#modal-user-contract', '#form-user-contract');
    // resetModal('#modal-user-contractor', '#form-user-contractor');

    $('#table-list tbody')
        .on('click', '#btn-edit', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="name_entity"]').val(data.name_entity);
            $('input[name="phone"]').val(data.phone);
            $('input[name="extension"]').val(data.extension);
            $('input[name="nit"]').val(data.nit);
            $('select[name="type_contractor"]').val(data.type_contractor);
            $('#modal-user-contract').modal('show');
        })
        .on('click', '#btn-delete', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submitDataAjax(window.location.pathname, parameters, '#modal-user-contract');
        });
    $('#form-user-contract').on('submit', function (e) {
        e.preventDefault();
        var parametersUser = new FormData(this);
        submitDataAjax(window.location.pathname, parametersUser, '#modal-user-contract');

    });
    // $('#form-user-contractor').on('submit', function (e) {
    //     e.preventDefault();
    //     var formDataUser = document.getElementById('form-user-contractor')
    //     var parametersUser = new FormData(formDataUser);
    //     submitDataAjax('/contracts/user-contracts/', parametersUser, '#modal-user-contractor');
    //
    // });
});