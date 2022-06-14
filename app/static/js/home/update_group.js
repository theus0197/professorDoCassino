document.getElementsByClassName('close-notification')[0].addEventListener('click', function() {
    notShow();
});

document.getElementsByClassName('status')[0].addEventListener('click', function() {
    var status = document.getElementsByClassName('status')[0];
    if(status.classList.contains('true')){
        status.classList.remove('true');
        status.classList.add('false');
    }else{
        status.classList.remove('false');
        status.classList.add('true');
    }
});

document.getElementsByName('type')[0].addEventListener('change', function() {
    if(document.getElementsByName('type')[0].value === 'VIP'){
        document.getElementsByClassName('info-limit')[0].style.display = 'none';
        document.getElementsByClassName('info-start')[0].style.display = 'none';
    }else{
        document.getElementsByClassName('info-limit')[0].style.display = 'block';
        document.getElementsByClassName('info-start')[0].style.display = 'block';
    }
})

document.getElementsByClassName('btn-update-button')[0].addEventListener('click', function() {
    var id = document.getElementsByClassName('btn-update-button')[0].getAttribute('id');
    var name = document.getElementsByName('name')[0].value;
    var type = document.getElementsByName('type')[0].value;
    var start = document.getElementsByName('start')[0].value;
    var limite = document.getElementsByName('limite')[0].value;
    var status = document.getElementsByClassName('status')[0];
    if(status.classList.contains('true')){
        status = true;
    }else{
        status = false;
    }
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/group/update');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        var response = JSON.parse(xhr.responseText);
        if(response.status){
            notShow();
            getGroups();
        }
    }
    xhr.send(JSON.stringify({
        'id': id,
        'status': status,
        'name': name,
        'type': type,
        'start': start,
        'limite': limite
    }));

});

function notShow(){
    document.getElementsByClassName('main-window')[0].style.display = 'none';
}

function getGroups(){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/group/get');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementsByClassName('manager-group-content')[0].innerHTML = xhr.responseText;
            var nameGroups = document.getElementsByClassName('name-group');
            for(var i = 0; i < nameGroups.length; i++){
                nameGroups[i].addEventListener('click', function(){
                    var id = this.getAttribute('id');
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', '/group/view');
                    xhr.onreadystatechange = function() {
                        var addGroup = document.getElementsByClassName('add_group');
                        if(addGroup.length > 0){
                            for(var i = 0; i < addGroup.length; i++){
                                addGroup[i].remove();
                            }
                        }
                        document.getElementsByClassName('main-window')[0].innerHTML = xhr.responseText;
                        document.getElementsByClassName('main-window')[0].style.display = 'flex';
                        var script = document.createElement('script');
                        script.src = '/static/js/home/update_group.js';
                        script.className = 'add_group';
                        document.getElementsByTagName('body')[0].appendChild(script);
                    };
                    xhr.send(JSON.stringify({
                        'id': id
                    }));
                });
            }
        }
    }
    xhr.send();          
}

var type = document.getElementsByName('type')[0];
if(type.value === 'VIP'){
    document.getElementsByClassName('info-limit')[0].style.display = 'none';
    document.getElementsByClassName('info-start')[0].style.display = 'none';
}else{
    document.getElementsByClassName('info-limit')[0].style.display = 'block';
    document.getElementsByClassName('info-start')[0].style.display = 'block';
}