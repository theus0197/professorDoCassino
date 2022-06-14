document.getElementById('password').addEventListener('keypress', function(event) {
    if(event.key === 'Enter'){
        login();
    };
});

document.getElementsByClassName('card-login-button')[0].addEventListener('click', function() {
    login();
});

function login(){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/login', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.status) {
                window.location.href = '/';
            } else {
                alert(response.message);
            }
        } else {
            alert('Erro ao realizar a chamada!');
        }
    };
    xhr.send(JSON.stringify({
        'username': document.getElementById('username').value,
        'password': document.getElementById('password').value
    }));
}