var slider0 = document.getElementById("slider0");
var slider1 = document.getElementById("slider1");
var slider2 = document.getElementById("slider2");

function check(){
    if(slider0.checked && slider1.checked && slider2.checked){
        setTimeout(function(){
            window.location.href = "page1.html";
        
        },600);
    }
}