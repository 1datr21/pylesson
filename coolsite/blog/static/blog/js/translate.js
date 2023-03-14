document.addEventListener('DOMContentLoaded', function() {

    function translate_text()
    {
        var form = document.getElementById('tr_form');

        var url = form.action;

        var elements = form.querySelectorAll('input,textarea');
        var formData = new FormData();
        for(var i=0; i<elements.length; i++)
        {
            formData.append(elements[i].name, elements[i].value);
        }
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.responseType = 'json';
        xmlHttp.onreadystatechange = function()
            {
                if(xmlHttp.readyState == 4 && xmlHttp.status == 200)
                {
                    //console.log(xmlHttp.response);
                    document.getElementById('tr_ucase').innerText =xmlHttp.response.result;
                    document.getElementById('tr_lcase').innerText =xmlHttp.response.result_lcase;
                }
            }
        xmlHttp.open("post", url);
        xmlHttp.send(formData);
    }
    document.getElementById('tr_form').onsubmit = function(e) {
        e.preventDefault();
        translate_text();
        return false;
    };



    document.getElementById('id_content').addEventListener('input', function(e) {
        translate_text();
    });
});
