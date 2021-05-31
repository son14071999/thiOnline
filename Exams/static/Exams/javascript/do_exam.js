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
    var m = parseInt($('#do-time').val());
    console.log(m);
    var h = parseInt(m/60);
    m = m%60;
    var s = 60;
    function start() {

        /*BƯỚC 1: CHUYỂN ĐỔI DỮ LIỆU*/
        // Nếu số giây = -1 tức là đã chạy ngược hết số giây, lúc này:
        //  - giảm số phút xuống 1 đơn vị
        //  - thiết lập số giây lại 59
        if (s === -1) {
            m -= 1;
            s = 59;
        }

        // Nếu số phút = -1 tức là đã chạy ngược hết số phút, lúc này:
        //  - giảm số giờ xuống 1 đơn vị
        //  - thiết lập số phút lại 59
        if (m === -1) {
            h -= 1;
            m = 59;
        }

        // Nếu số giờ = -1 tức là đã hết giờ, lúc này:
        //  - Dừng chương trình
        if (h == -1) {
            clearTimeout(timeout);
            alert('Hết giờ');
            return false;
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