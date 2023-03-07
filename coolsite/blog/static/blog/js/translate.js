document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('tr_form').addEventListener('submit', function(e) {
        e.preventDefault();

        var form = document.getElementById('tr_form');

        var url = e.submitter.formAction;

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
                //    document.getElementById('tr_lcase').innerText =xmlHttp.response.result_lcase;
                }
            }
        xmlHttp.open("post", url);
        xmlHttp.send(formData);
    });
});
