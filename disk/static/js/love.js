var step;
for (step = 0; step < 5; step++) {
    function changeCnt(str) {
        var elem = document.getElementById('before&after');
        var str = '<style type="text/css">\
        p.new::after {\
              content: "'+ str + '";\
        }\
        </style>';
        elem.innerHTML = str;

    }
    setTimeout(function () { changeCnt('Любовь'); }, 1000);
    setTimeout(function () { changeCnt('Смерть'); }, 2000);
    setTimeout(function () { changeCnt('и'); }, 3000);
    setTimeout(function () { changeCnt('Роботы'); }, 4000);
    setTimeout(function () { changeCnt('Пока!'); }, 5000);

}