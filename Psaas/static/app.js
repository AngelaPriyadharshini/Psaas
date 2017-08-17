//GET

document.addEventListener("DOMContentLoaded", function () {

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', 'http://localhost:5000/orders', true);
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200) {
                var obj = JSON.parse(xmlhttp.responseText);
                var jsobj = obj.orders;
                var names = jsobj.sort(function (a, b) {
                    return (new Date(b.ordered_on)) - (new Date(a.ordered_on))
                });
                var panel = document.getElementsByClassName("card")[0];
                for (var i = 0; i < names.length; i++) {
                    var dv = document.createElement("div");
                    dv.classList.add("card-child")
                    var h5 = document.createElement("span");
                    h5.innerHTML = names[i].ordered_by;
                    dv.appendChild(h5);
                    var item = document.createElement("span");
                    item.innerHTML = names[i].items;
                    item.classList.add("item-span");
                    dv.appendChild(item);
                    var count = document.createElement("span");
                    count.innerHTML = names[i].count;
                    count.classList.add("num-span");
                    dv.appendChild(count);
                    var p = document.createElement("p");
                    var rawdate = JSON.stringify(names[i].ordered_on);
                    p.innerHTML = rawdate.substring(1, rawdate.length - 5);
                    dv.appendChild(p);
                    panel.appendChild(dv);
                    var br = document.createElement("br");
                    panel.appendChild(br)
                }
                console.log(names);
            }
        }
    };
    xmlhttp.send(null);
});


//POST 

function makeOrder() {
    var elements = document.getElementById("json-form").elements;
    var obj = {};
    for (var i = 0 ; i < 3 ; i++) {
        var item = elements.item(i);
        obj[item.name] = item.value;
    }
    var data = JSON.stringify(obj);
    console.log(data);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            alert("Order successfully added!");
        }
    }
    xmlhttp.open("POST", "http://localhost:5000/orders", true);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send(data);
    console.log(data);
}