function cpf(v){
    if(v != ''){
        v=v.replace(/\D/g,"");
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
        v=v.replace(/(\d{3})(\d)/,"$1-$2");
    }
    return v;
}

document.getElementsByClassName('btn-add')[0].addEventListener('click', function() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/client/add');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            try{
                var response = JSON.parse(xhr.responseText);
            }catch(e){
                document.getElementsByClassName('main-window')[0].innerHTML = xhr.responseText;
                document.getElementsByClassName('main-window')[0].style.display = 'flex';
                add_test();
            }
        }
    }
    xhr.send();
});

function getClients(){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/get/client');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementsByClassName('manager-group-content')[0].innerHTML = xhr.responseText;
            var nameClients = document.getElementsByClassName('name-group');
            for(var i = 0; i < nameClients.length; i++){
                nameClients[i].addEventListener('click', function(){
                    var id = this.getAttribute('id');
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', '/view/client');
                    xhr.onreadystatechange = function() {
                        document.getElementsByClassName('main-window')[0].innerHTML = xhr.responseText;
                        document.getElementsByClassName('main-window')[0].style.display = 'flex';
                        update_test();
                    };
                    xhr.send(JSON.stringify({
                        'id': id
                    }));
                });
            }

            var trashs = document.getElementsByClassName('trash');
            for(var i = 0; i < trashs.length; i++){
                trashs[i].addEventListener('click', function(){
                    var id = this.getAttribute('id');
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', 'delete/client');
                    xhr.setRequestHeader('Content-Type', 'application/json');
                    xhr.onreadystatechange = function() {
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            window.location.reload();
                        }
                    }
                    xhr.send(JSON.stringify({
                        'id': id
                    }));
                });
            };
        }
    }
    xhr.send(); 
}

function update_test(){    
    document.getElementsByName('cpf')[0].addEventListener('keypress', function(e) {
        if(e.target.value.length >= 14) {
        }else{
            e.target.value = cpf(e.target.value);
        };
    });

    for (var i = 0; i < document.getElementsByClassName('status').length; i++) {
        document.getElementsByClassName('status')[i].addEventListener('click', function() {
            if (this.classList.contains('true')) {
                this.classList.remove('true');
                this.classList.add('false');
                this.dataset.id = 'false';
            } else {
                this.classList.remove('false');
                this.classList.add('true');
                this.dataset.id = 'true'
            }
        });
    }
    
    
    document.getElementsByClassName('btn-update-button')[0].addEventListener('click', function() {
        var id_ = document.getElementById('title-text-form').dataset.id;
        var name = document.getElementsByName('name')[0].value;
        var cpf = document.getElementsByName('cpf')[0].value;
        var email = document.getElementsByName('email')[0].value;
        var roleta_evo = document.getElementById('roleta-evo').dataset.id;
        var roleta_playtech = document.getElementById('roleta-playtech').dataset.id;
        var dados = document.getElementById('dados').dataset.id;
        var football_studio = document.getElementById('football-studio').dataset.id;
        var football_dice = document.getElementById('football-dice').dataset.id;
        var blaze = document.getElementById('blaze').dataset.id;
        var estrelabet = document.getElementById('estrelabet').dataset.id;
        var brxbet = document.getElementById('brxbet').dataset.id;
        var betano = document.getElementById('betano').dataset.id;
        var saurobet = document.getElementById('saurobet').dataset.id;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/update/client');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            var response = JSON.parse(xhr.responseText);
            if(response.status){
                alert('Alteração do cliente '+ name + ' foi realizado com sucesso!')
                window.location.reload();
            }
        }
        xhr.send(JSON.stringify({
            'id': id_,
            'name': name,
            'cpf': cpf,
            'email': email,
            'roleta-evo': roleta_evo,
            'roleta-playtech': roleta_playtech,
            'dados': dados,
            'football-studio': football_studio,
            'football-dice': football_dice,
            'blaze': blaze,
            'estrelabet': estrelabet,
            'brxbet': brxbet,
            'betano': betano,
            'saurobet': saurobet
        }));
    
    });

    document.getElementsByClassName('close-notification')[0].addEventListener('click', function() {
        notShow();
    });
    
    function notShow(){
        document.getElementsByClassName('main-window')[0].style.display = 'none';
    }
}

function add_test(){
    document.getElementsByName('cpf')[0].addEventListener('keypress', function(e) {
        if(e.target.value.length >= 14) {
        }else{
            e.target.value = cpf(e.target.value);
        };
    });

    document.getElementsByClassName('close-notification')[0].addEventListener('click', function() {
        notShow();
    });
    
    for (var i = 0; i < document.getElementsByClassName('status').length; i++) {
        console.log(i);
        document.getElementsByClassName('status')[i].addEventListener('click', function() {
            if (this.classList.contains('true')) {
                this.classList.remove('true');
                this.classList.add('false');
                this.dataset.id = 'false';
            } else {
                this.classList.remove('false');
                this.classList.add('true');
                this.dataset.id = 'true'
            }
        });
    }
    
    document.getElementsByClassName('btn-add-button')[0].addEventListener('click', function() {
        var name = document.getElementsByName('name')[0].value;
        var cpf = document.getElementsByName('cpf')[0].value;
        var email = document.getElementsByName('email')[0].value;
        var roleta_evo = document.getElementById('roleta-evo').dataset.id;
        var roleta_playtech = document.getElementById('roleta-playtech').dataset.id;
        var dados = document.getElementById('dados').dataset.id;
        var football_studio = document.getElementById('football-studio').dataset.id;
        var football_dice = document.getElementById('football-dice').dataset.id;
        var blaze = document.getElementById('blaze').dataset.id;
        var estrelabet = document.getElementById('estrelabet').dataset.id;
        var brxbet = document.getElementById('brxbet').dataset.id;
        var betano = document.getElementById('betano').dataset.id;
        var saurobet = document.getElementById('saurobet').dataset.id;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/add/newClient');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            var response = JSON.parse(xhr.responseText);
            if(response.status){
                window.location.reload();
            }
        }
        xhr.send(JSON.stringify({
            'name': name,
            'cpf': cpf,
            'email': email,
            'roleta-evo': roleta_evo,
            'roleta-playtech': roleta_playtech,
            'dados': dados,
            'football-studio': football_studio,
            'football-dice': football_dice,
            'blaze': blaze,
            'estrelabet': estrelabet,
            'brxbet': brxbet,
            'betano': betano,
            'saurobet': saurobet
        }));
    
    });
    
    function notShow(){
        document.getElementsByClassName('main-window')[0].style.display = 'none';
    }
}