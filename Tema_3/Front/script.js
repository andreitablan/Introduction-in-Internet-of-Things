document.addEventListener('DOMContentLoaded', function() {
  console.log("DOM loaded");
  fetchAndDisplayData();
  setInterval(fetchAndDisplayData, 2000); 
});
let lastSensorsData = null;
function fetchAndDisplayData() {
  fetch('http://127.0.0.1:5001/sensors_data',{method: 'GET'})
  .then(function(response){
    return response.json();
})
  .then(function(json){
      console.log(json); 
      let placeholder = document.querySelector("#data-output");
      var need_alert = json.raise_alert;    
      var sensorsData = json.sensors_data;
      let out="";
      for (var i = 0; i < sensorsData.length; i++) {
        var entry = sensorsData[i];
        out += `
           <tr>
              <td>${entry[0]}</td>
              <td>${entry[1]}</td>
              <td>${entry[2]}</td>
              <td>${entry[3]}</td>
           </tr>
        `;
      }
      placeholder.innerHTML = out;
      if(lastSensorsData == null || (lastSensorsData.length != sensorsData.length)){
        if (need_alert) {
          setTimeout(function() {
            alert("Someone is at your house! Check the cameras!");
          }, 2000);
        }
    }
      lastSensorsData = sensorsData;
    })
    .catch(function(error) {
      console.log(error);
      setTimeout(fetchAndDisplayData, 5000);
    });
}

