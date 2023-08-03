document.getElementsByClassName('btn-add')[0].addEventListener('click', function() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/group/add');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            try{
                var response = JSON.parse(xhr.responseText);
            }catch(e){
                /*var addGroup = document.getElementsByClassName('add_group');
                if(addGroup.length > 0){
                    for(var i = 0; i < addGroup.length; i++){
                        addGroup[i].remove();
                    }
                }
                var script = document.createElement('script');
                script.src = '/static/js/home/add_group.js';
                script.className = 'add_group';
                document.getElementsByTagName('body')[0].appendChild(script);*/
                document.getElementsByClassName('main-window')[0].innerHTML = xhr.responseText;
                document.getElementsByClassName('main-window')[0].style.display = 'flex';
                add_test();
            }
        }
    }
    xhr.send();
});

function getGroups(){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/group/get/crazy');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementsByClassName('manager-group-content')[0].innerHTML = xhr.responseText;
            var nameGroups = document.getElementsByClassName('name-group');
            for(var i = 0; i < nameGroups.length; i++){
                nameGroups[i].addEventListener('click', function(){
                    var id = this.getAttribute('id');
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', '/group/view/crazy');
                    xhr.onreadystatechange = function() {
                        document.getElementsByClassName('main-window')[0].innerHTML = xhr.responseText;
                        document.getElementsByClassName('main-window')[0].style.display = 'flex';
                        /*var addGroup = document.getElementsByClassName('add_group');
                        if(addGroup.length > 0){
                            for(var i = 0; i < addGroup.length; i++){
                                addGroup[i].remove();
                            }
                        }*/
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
                    xhr.open('POST', '/group/delete/crazy');
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
        xhr.open('POST', '/group/update/crazy');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            var response = JSON.parse(xhr.responseText);
            if(response.status){
                window.location.reload();
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
    
    var type = document.getElementsByName('type')[0];
    if(type.value === 'VIP'){
        document.getElementsByClassName('info-limit')[0].style.display = 'none';
        document.getElementsByClassName('info-start')[0].style.display = 'none';
    }else{
        document.getElementsByClassName('info-limit')[0].style.display = 'block';
        document.getElementsByClassName('info-start')[0].style.display = 'block';
    }
}

function add_test(){
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
    
    document.getElementsByClassName('btn-add-button')[0].addEventListener('click', function() {
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
        xhr.open('POST', '/group/new/add/crazy');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            var response = JSON.parse(xhr.responseText);
            if(response.status){
                window.location.reload();
            }
        }
        xhr.send(JSON.stringify({
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
}