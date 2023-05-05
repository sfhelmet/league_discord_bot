import {API_KEY, SUMMONER_NAMES} from './config.js';

async function generateTable() {
    console.log(SUMMONER_NAMES)
    let url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"


    for (let i = 0; i < SUMMONER_NAMES.length; i++) {
        let name = SUMMONER_NAMES[i];
        let endpoint = url + name + "?api_key=" + API_KEY
        fetch(endpoint)
          .then(response => response.json())
          .then(data => {
            const tableBody = document.getElementById('table-body');
            const row = document.createElement('tr');
            const col1 = document.createElement('td');
            col1.textContent = data.name;
            const col2 = document.createElement('td');
            col2.textContent = data.summonerLevel;
            const col3 = document.createElement('td');
            col3.textContent = "Platinum 4"
            const col4 = document.createElement('td');
            col4.textContent = "0"
            row.appendChild(col1);
            row.appendChild(col2);
            row.appendChild(col3);
            row.appendChild(col4);
            tableBody.appendChild(row);
      });
    }
    //     console.log(users);
    //     document.getElementById("demo").innerHTML = users.id;
    //     document.getElementById("fname").innerHTML = users.name;
    //     document.getElementById("flevel").innerHTML = users.summonerLevel;
    //     document.getElementById("ficon").innerHTML = users.profileIconId;
    // });
}

document.addEventListener("DOMContentLoaded", function(event) { 
    generateTable();
  });