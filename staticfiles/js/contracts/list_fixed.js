var tableList;


function getDataTable() {
    tableList = $('#table-list').DataTable({
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'action': 'list'},
            dataSrc: ''
        },
        columns: [
            {'data': 'id'},
            {'data': 'type_contract'},
            {'data': 'contractor_by.name'},
            {'data': 'contractor_for.name'},
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
                    var buttons = '<button type="button" id="btn-see" class="btn btn-info btn-xs btn-flat"><i class="fas fa-eye"></i></button> ';
                    buttons += '<button type="button" id="btn-edit" class="btn btn-warning btn-xs btn-flat" ><i class="fas fa-edit"></i></button> ';
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
        $('#modal-fixed-contract').modal('show');
    });
    // $('#btn-add-fixed-contract').on('click', function () {
    //     $('input[name="action"]').val('add');
    //     $('#modal-user-contractor').modal('show');
    // });
    resetModal('#modal-fixed-contract', '#form-fixed-contract');
    // resetModal('#modal-user-contractor', '#form-user-contractor');

    $('#table-list tbody')
        .on('click', '#btn-edit', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('select[name="contractor_by"]').val(data.contractor_by.id);
            $('select[name="contractor_for"]').val(data.contractor_for.id);
            $('input[name="start_date"]').val(data.start_date);
            $('input[name="end_date"]').val(data.end_date);
            $('#modal-fixed-contract').modal('show');
        })
        .on('click', '#btn-delete', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submitDataAjax(window.location.pathname, parameters, '#modal-fixed-contract');
        })

    $('#form-fixed-contract').on('submit', function (e) {
        e.preventDefault();
        var parametersFixed = new FormData(this);
        submitDataAjax(window.location.pathname, parametersFixed, '#modal-fixed-contract');

    });
    // $('#form-user-contractor').on('submit', function (e) {
    //     e.preventDefault();
    //     var formDataUser = document.getElementById('form-user-contractor')
    //     var parametersUser = new FormData(formDataUser);
    //     submitDataAjax('/contracts/user-contracts/', parametersUser, '#modal-user-contractor');
    //
    // });
});