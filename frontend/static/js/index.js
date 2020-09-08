/**
 * Created by mukhinon on 8/28/20.
 */

function showAddCategory() {
    var show_add_category = document.getElementById('add_category');
    show_add_category.style.display = (show_add_category.style.display == 'none') ? '' : 'none';
}

function showAddTask() {
    var show_add_task = document.getElementById('add_task');
    show_add_task.style.display = (show_add_task.style.display == 'none') ? '' : 'none';
}

function addCategory() {
    var category = document.querySelector('[name="category"]');
    var show_add_category = document.getElementById('add_category');
    var msg = $('#message');
    $.ajax({
        url: '/add_category',
        data: {category: '@' + category.value}
    }).done(function (data) {
        msg.css('display', 'block');
        msg.append(data.message).fadeOut(5000);
        category.value = '';
        show_add_category.style.display = '';
    });
}

$(function () {
    $('input[name="task"]').attr('placeholder', 'Задача');
    $('input[name="finish_date_time"]').attr({'placeholder': 'Дата оповещения', 'type': 'datetime'});
    $('input[name="note"]').after($('<textarea name="note" id="id_note" cols=30 rows=3 placeholder="Заметка">'));
    $('input[name="note"]').remove();
});

var query = 2;
var all_task = document.querySelectorAll('.show_task');
for (let i = 0; i < all_task.length; i++) {
    all_task[i].onclick = function () {
        document.querySelector('.task_show').style.display = 'block';
        showTask('/' + query, function (data) {
            document.querySelector('.table_task_show').innerHTML =
                '{% for t in tasks %}' +
                '   <td class="col-sm-2">{{ t }}</td><td class="col-sm-2">{{ t.category }}</td>' +
                '{% endfor %}'
        });
    }
}
function showTask(url, callback) {
    var f = callback || function (data) {
        };
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            f(xhttp.responseText);
        }
    };
    xhttp.open('GET', url);
    xhttp.send();
}

// Фильтр по категориям
$('#query_category').on('click', function () {
    var category = $('#query_categories').val();
    var priority = $('#query_importance').val();
    var show_filter_table = document.getElementById('show-filter-table');
    show_filter_table.style.display = (show_filter_table.style.display == 'none') ? '' : 'none';
    $.ajax({
        url: '',
        data: {pk_category: category, pk_priority: priority}
    }).done(function (data) {
        $.each(data, function (key, value) {
            $('#task').append(`
              <tr>
                <td class="col-xs-1"><div style="background-color: ${value.color}; border-radius: 50%; width: 20px; height: 20px">&nbsp;</div></td>
                <td class="col-xs-2">${value.task}</td>
                <td class="col-sm-2">${value.parent}</td>
                <td class="col-sm-1">${value.create_date_time}</td>
                <td class="col-sm-1">${value.note}</td>
                <td class="col-sm-1">${value.finish_date_time}</td>
                <td class="col-sm-1"><a class="badge badge-dark link-center" href="/edit_task/${value.pk}">Редактировать</a></td>
              </tr>
          `)
        });
    });
    $('#task').html('');
});


//        let date_hour = [];
//        for(let i = 0; i < 24; i++){
//            date_hour.push(i);
//            }
//        console.log(date_hour);