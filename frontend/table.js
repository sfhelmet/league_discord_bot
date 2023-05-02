import {API_KEY, SUMMONER_NAMES} from './config.js';

async function getNames() {
    console.log(SUMMONER_NAMES)
    let promises = [];
    let result = [];

    for (let i = 0; i < SUMMONER_NAMES.length; i++) {
        let name = SUMMONER_NAMES[i];
        let url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?" + API_KEY
        promises.push(fetch(url).then(response => {return response.json();}));
    }

    const data = await Promise.all(promises);
    console.log(data)
    //     console.log(users);
    //     document.getElementById("demo").innerHTML = users.id;
    //     document.getElementById("fname").innerHTML = users.name;
    //     document.getElementById("flevel").innerHTML = users.summonerLevel;
    //     document.getElementById("ficon").innerHTML = users.profileIconId;
}

document.addEventListener("DOMContentLoaded", function(event) { 
    // getNames();
  });