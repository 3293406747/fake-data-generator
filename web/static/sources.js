document.addEventListener('DOMContentLoaded', function() {
  document.getElementById("create").addEventListener('click', async function() {
    var mySelect = document.getElementById("choose");
    var index = mySelect.selectedIndex;
    var text = mySelect.options[index].text;
    var list = document.getElementById("list");
    var span = document.createElement("span");

    var url = 'http://127.0.0.1:5000/data?target=' + encodeURI(mySelect.value);
    try {
      var response = await fetch(url);
      var data =  await response.json();
    } catch (error) {
      console.log(error)
    };

    span.innerText = text+": "+data["value"]+"\n";
    list.appendChild(span);

    // fetch(url)
    //   .then(response => response.json())
    //   .then(data => {
    //     span.innerText = text+": "+data["value"]+"\n";
    //     list.appendChild(span);
    //   })
    //   .catch(error => {
    //     console.log(error);
    //   });
  });

  document.getElementById("clear").addEventListener('click', function() {
    var list = document.getElementById("list");
    list.remove();
    var new_list = document.createElement("div");
    new_list["id"] = "list";
    document.querySelector("body").appendChild(new_list);
    var mySelect = document.getElementById("choose");
    
    mySelect.selectedIndex = 0;
  });
});