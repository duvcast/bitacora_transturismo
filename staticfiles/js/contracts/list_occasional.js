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
            {'data': 'contractor_by'},
            {'data': 'nit'},
            {'data': 'address'},
            {'data': 'city'},
            {'data': 'name_contact'},
            {'data': 'phone_contact'},
            {'data': 'destiny'},
            {'data': 'hour_service'},
            {'data': 'date_service'},
            {'data': 'capacity'},
            {'data': 'date_departure'},
            {'data': 'date_arrival'},
            {'data': 'nro_spreadsheet'},
            {'data': 'reservation'},
            {'data': 'observations'},
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
        $('#modal-occasional-contract').modal('show');
    });
    // $('#btn-add-fixed-contract').on('click', function () {
    //     $('input[name="action"]').val('add');
    //     $('#modal-user-contractor').modal('show');
    // });
    resetModal('#modal-occasional-contract', '#form-occasional-contract');
    // resetModal('#modal-user-contractor', '#form-user-contractor');

    $('#table-list tbody')
        .on('click', '#btn-edit', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="contractor_by"]').val(data.contractor_by);
            $('input[name="start_date"]').val(data.start_date);
            $('input[name="nit"]').val(data.nit);
            $('input[name="address"]').val(data.address);
            $('input[name="city"]').val(data.city);
            $('input[name="name_contact"]').val(data.name_contact);
            $('input[name="phone_contact"]').val(data.phone_contact);
            $('input[name="destiny"]').val(data.destiny);
            $('input[name="hour_service"]').val(data.hour_service);
            $('input[name="date_service"]').val(data.date_service);
            $('input[name="capacity"]').val(data.capacity);
            $('input[name="date_departure"]').val(data.date_departure);
            $('input[name="date_arrival"]').val(data.date_arrival);
            $('input[name="nro_spreadsheet"]').val(data.nro_spreadsheet);
            $('input[name="reservation"]').val(data.reservation);
            $('textarea[name="observations"]').val(data.observations);
            $('#modal-occasional-contract').modal('show');
        })
        .on('click', '#btn-delete', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submitDataAjax(window.location.pathname, parameters, '#modal-occasional-contract');
        });
    $('#form-occasional-contract').on('submit', function (e) {
        e.preventDefault();
        var parametersFixed = new FormData(this);
        submitDataAjax(window.location.pathname, parametersFixed, '#modal-occasional-contract');

    });
    // $('#form-user-contractor').on('submit', function (e) {
    //     e.preventDefault();
    //     var formDataUser = document.getElementById('form-user-contractor')
    //     var parametersUser = new FormData(formDataUser);
    //     submitDataAjax('/contracts/user-contracts/', parametersUser, '#modal-user-contractor');
    //
    // });
});