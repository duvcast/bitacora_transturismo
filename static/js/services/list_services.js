var tableList;
var tableScheduleList;

function getDataTable() {
    tableList = $('#table-list').DataTable({
        destroy: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'action': 'list'},
            dataSrc: ''
        },
        columns: [
            {'data': 'id'},
            {'data': 'contract.contractor_for.name'},
            {'data': 'route_name'},
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
                    var buttons = '<button type="button"  id="btn-create-schedule" class="btn btn-success btn-xs btn-flat" ><i class="fas fa-plus"></i></button> ';
                    buttons += '<button type="button" id="btn-see" class="btn btn-primary btn-xs btn-flat" ><i class="fas fa-eye"></i></button> ';
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
        $('#modal-service').modal('show');
    });

    resetModal('#modal-service', '#form-service');
    resetModal('#modal-schedule', '#form-schedule');

    $('#table-list tbody')
        .on('click', '#btn-create-schedule', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            console.log(data)
            $('input[name="action"]').val('add_schedule');
            $('input[name="id"]').val(data.id);
            $('#modal-schedule').modal('show');
        })
        .on('click', '#btn-see', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            tableScheduleList = $('#table-schedules-list').DataTable({
                destroy: true,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {'action': 'list_schedule', 'id': data.id},
                    dataSrc: ''
                },
                columns: [
                    {'data': 'id'},
                    {'data': 'name'},
                    {'data': 'bus.name'},
                    {'data': 'start_hour'},
                    {'data': 'end_hour'},
                    {'data': 'quantity_fleet'},
                    {'data': 'created_by'},
                    {'data': 'id'},
                ],
                columnDefs: [
                    {
                        targets: [-1],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            var buttons = '<button type="button" id="btn-edit-schedule" class="btn btn-warning btn-xs btn-flat" ><i class="fas fa-edit"></i></button> ';
                            buttons += '<button type="button" id="btn-delete-schedule" class="btn btn-danger btn-xs btn-flat" ><i class="fas fa-trash"></i></button>';
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
            $('#modal-schedules-list').modal('show');
        })
        .on('click', '#btn-edit', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('select[name="contract"]').val(data.contract.id);
            $('input[name="route_name"]').val(data.route_name);
            $('input[name="start_date"]').val(data.start_date);
            $('input[name="end_date"]').val(data.end_date);
            $('#modal-service').modal('show');
        })
        .on('click', '#btn-delete', function () {
            /*Responsive use*/
            var tr = tableList.cell($(this).closest('td, li')).index();
            var data = tableList.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete');
            parameters.append('id', data.id);
            submitDataAjax(window.location.pathname, parameters);
        })


    $('#table-schedules-list tbody').on('click', '#btn-edit-schedule', function () {
        var tr = tableScheduleList.cell($(this).closest('td, li')).index();
        var data = tableScheduleList.row(tr.row).data();
        $('input[name="action"]').val('edit_schedule');
        $('input[name="id"]').val(data.id);
        $('select[name="bus"]').val(data.bus.id);
        $('input[name="start_hour"]').val(data.start_hour);
        $('input[name="end_hour"]').val(data.end_hour);
        $('input[name="quantity_fleet"]').val(data.quantity_fleet);
        $('#modal-schedule').modal('show');

    })
        .on('click', '#btn-delete-schedule', function () {
            /*Responsive use*/
            var tr = tableScheduleList.cell($(this).closest('td, li')).index();
            var data = tableScheduleList.row(tr.row).data();
            var parameters = new FormData();
            parameters.append('action', 'delete_schedule');
            parameters.append('id', data.id);
            submitDataAjax(window.location.pathname, parameters);
        })

    $('#form-service').on('submit', function (e) {
        e.preventDefault();
        var parametersFixed = new FormData(this);
        submitDataAjax(window.location.pathname, parametersFixed);

    });
    $('#form-schedule').on('submit', function (e) {
        e.preventDefault();
        var formDataUser = document.getElementById('form-schedule')
        var parametersUser = new FormData(formDataUser);
        submitDataAjax(window.location.pathname, parametersUser, '#modal-schedule');

    });
});