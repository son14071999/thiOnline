$(document).ready(function () {
    let btn;
    let btns = $('.button-exam .btn-exam');
    for (btn = 0; btn < btns.length; btn++) {
        btns[btn].addEventListener('click', function (e) {
            console.log($(this));
            $('.button-exam .btn-exam').each(function () {
                $(this).removeClass('active-exam');
            });
            let id_active = $(this).attr('id');
            console.log(id_active);
            $(this).addClass('active-exam');
            $('.create-exam .info').each(function () {
                if ($(this).attr('class') == id_active) {
                    $(this).css('display', 'block');
                } else {
                    $(this).css('display', 'none');
                }
            });
        });
    }


});
$(document).ready(function () {
    $('.add-question img').click(function () {
        let number = $('.info-question>.line>label');
        number = number[number.length - 1].innerHTML;
        number = parseInt(number.replace('Câu ', '').replace(':', '')) + 1;
        console.log(number);
        let add =
            '                    <div class="line">\n' +
            '                        <label for="question">Câu ' + number + ': </label>\n' +
            '                        <textarea name="question" id="question" rows="3"></textarea>\n' +
            '                    </div>\n' +
            '                   <div className="line">\n' +
            '                           <input type="file" name="image-'+ number +'" id="image-exam" accept="image/png, image/jpeg">\n' +
            '                   </div>\n' +
            '                    <div class="line answers">\n' +
            '                        <div style="font-size: 1.2rem;"> Đáp án:</div>\n' +
            '                        <div class="answer">\n' +
            '                            <label for="A-' + number + '">A: </label>\n' +
            '                            <input type="text" name="answer-A-' + number + '" id="A-' + number + '">\n' +
            '                        </div>\n' +
            '                        <div class="answer">\n' +
            '                            <label for="B-' + number + '">B: </label>\n' +
            '                            <input type="text" name="answer-B-' + number + '" id="B-' + number + '">\n' +
            '                        </div>\n' +
            '                        <div class="answer">\n' +
            '                            <label for="C-' + number + '">C: </label>\n' +
            '                            <input type="text" name="answer-C-' + number + '" id="C-' + number + '">\n' +
            '                        </div>\n' +
            '                        <div class="answer">\n' +
            '                            <label for="D-' + number + '">D: </label>\n' +
            '                            <input type="text" name="answer-A-' + number + '" id="D-' + number + '">\n' +
            '                        </div>\n' +
            '                    </div>\n' +
            '                    <div class="line correct-answer">\n' +
            '                        <div style="margin-bottom: 2rem">\n' +
            '                            Đáp án đúng?\n' +
            '                        </div>\n' +
            '                        <div>\n' +
            '                            <label for="A-' + number + '-radio">A: </label>\n' +
            '                            <input type="radio" name="correct-answer" id="A-' + number + '-radio" value="A">\n' +
            '                            <label for="B-' + number + '-radio">B: </label>\n' +
            '                            <input type="radio" name="correct-answer" id="B-' + number + '-radio" value="B">\n' +
            '                            <label for="C-' + number + '-radio">C: </label>\n' +
            '                            <input type="radio" name="correct-answer" id="C-' + number + '-radio" value="C">\n' +
            '                            <label for="D-' + number + '-radio">D: </label>\n' +
            '                            <input type="radio" name="correct-answer" id="D-' + number + '-radio" value="D">\n' +
            '                        </div>\n' +
            '                    </div>';

        let div = document.createElement("div");
        div.className += 'info-question';
        div.innerHTML = add;
        let cr_q = $('.create-questions .wrapper')[0];
        cr_q.appendChild(div);
    });
    $('.remove-question img').click(function () {
        let questions = $('.create-questions>.wrapper>.info-question');
        if (questions.length > 5) {
            questions[questions.length - 1].remove();
        }
    });
});
