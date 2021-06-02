$(document).ready(function () {
    var list_qs = $('input[type="radio"]');
    for (var i = 0; i < list_qs.length; i++) {
        list_qs[i].addEventListener('change', function () {
            var id_ck = $(this).attr('id');
            var c = '.qs.qs-' + String(id_ck);
            var cheked = $(c)[0];
            cheked.style.backgroundColor = '#53808b';
        });
    }
});
$(document).ready(function () {
    var time_do = $('input[name="time-do"]');
    console.log('time-do: ', time_do);
    var m = parseInt($('#do-time').val())-1;
    var h = parseInt(m/60);
    m = m%60;
    var s = 60;
    function start() {
        if (s === -1) {
            m -= 1;
            s = 59;
            let temp = parseInt(time_do.val());
            time_do.val(temp+1);
            console.log(temp);
            console.log(time_do);
        }

        if (m === -1) {
            h -= 1;
            m = 59;
        }

        // Nếu số giờ = -1 tức là đã hết giờ, lúc này:
        //  - Dừng chương trình
        if (h == -1) {
            clearTimeout(timeout);
            $('#form-submit').submit();
        }

        /*BƯỚC 1: HIỂN THỊ ĐỒNG HỒ*/
        document.getElementById('h').innerText = h.toString();
        document.getElementById('m').innerText = m.toString();
        document.getElementById('s').innerText = s.toString();

        /*BƯỚC 1: GIẢM PHÚT XUỐNG 1 GIÂY VÀ GỌI LẠI SAU 1 GIÂY */
        timeout = setTimeout(function () {
            s--;
            start();
        }, 1000);
    }
    start();
});