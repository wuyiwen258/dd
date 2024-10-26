
window.onload = function(){

  fetch('http://127.0.0.1:8000/dashboard')
   .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
   .then(data => {
	   console.log(data)
	   const name1 = document.getElementById("name1");
	   console.log(data['name'])
	   name1.innerHTML = data["name"];
	   const id1 =document.getElementById("id1");
	   id1.innerHTML = data["id"];
	   const established1 = document.getElementById("established1");
	   established1.innerHTML = data["established"];
	   const links1 = document.getElementById("links1");
	   links1.innerHTML = data["links"];
	   const relationships1 = document.getElementById("relationships1");
	   relationships1.innerHTML = data["relationships"];
    })
   .catch(error => {
      console.error('Error fetching data:', error);
    });
};