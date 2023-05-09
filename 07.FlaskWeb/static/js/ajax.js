// AJAX(Asynchronous Javascript and XML)
// Web page의 일부분만 변경하는 방법

function changeQuote() {
    $.ajax({
        type: 'GET',
        url: '/change_quote', 
        data: ' ',              // 서버로 전달할 데이터
        success: function(msg) {        // msg: 서버로부터 받은 데이터
            $('#quoteMsg').html(msg);
        }
    });
}
let ad = false;
function changeProfile() {
    if (!ad) {
        $('#addrInput').attr('class', 'mt-2'); 
        ad = !ad;
    } else {
        $('#addrInput').attr('class', 'mt-2 d-none');
        ad = !ad;
    }
}
    function changeAddr() {
        $('#addrInput').attr('class', 'mt-2');      // input box가 보이게
    }
    function addrSubmit() {
        $('#addrInput').attr('class', 'mt-2 d-none');   // input box가 안보이게
        let addr = $('#addrInputTag').val();
        $.ajax({
            type: 'GET',
            url: '/change_addr',
            data: {addr: addr},
            success: function(msg) {
                $('#addr').html(msg);
            }
        });
    }

function changeWeather() {
    let addr = $('#addr').text();
    $.ajax({
        type: 'GET',
        url: '/weather',
        data: {addr: addr},
        success: function(result) {
            $('#weather').html(result);
        }
    });
}


let flag = false;
function changeProfile() {
    if (!flag) {
        $('#imageInput').attr('class', 'mt-2'); 
        flag = !flag;
    } else {
        $('#imageInput').attr('class', 'mt-2 d-none');
        flag = !flag;
    }
}
  function imageSubmit() {
    let imageInputVal = $('#image')[0];
    let formData = new FormData();
    formData.append('image', imageInputVal.files[0]);
    $.ajax({
        type: 'POST',
        url: '/change_profile',
        data: formData,
        processData: false,
        contentType: false,
        success: function(result) {
            $('#imageInput').attr('class', 'mt-2 d-none');
            let fname = 'http://127.0.0.1:5000/static/data/profile.png?q=' + result;
            $('#profile').attr('src', fname);
        }
    });
  }