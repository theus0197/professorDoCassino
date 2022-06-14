document.getElementsByClassName('btn-add')[0].addEventListener('click', function() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/group/add');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            try{
                var response = JSON.parse(xhr.responseText);
            }catch(e){
                var addGroup = document.getElementsByClassName('add_group');
                if(addGroup.length > 0){
                    for(var i = 0; i < addGroup.length; i++){
                        addGroup[i].remove();
                    }
                }
                document.getElementsByClassName('main-window')[0].innerHTML = xhr.responseText;
                document.getElementsByClassName('main-window')[0].style.display = 'flex';
                var script = document.createElement('script');
                script.src = '/static/js/home/add_group.js';
                script.className = 'add_group';
                document.getElementsByTagName('body')[0].appendChild(script);
            }
        }
    }
    xhr.send();
});

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

            var trashs = document.getElementsByClassName('trash');
            for(var i = 0; i < trashs.length; i++){
                trashs[i].addEventListener('click', function(){
                    var id = this.getAttribute('id');
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', '/group/delete');
                    xhr.setRequestHeader('Content-Type', 'application/json');
                    xhr.onreadystatechange = function() {
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            getGroups();
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

getGroups();