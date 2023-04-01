const URL = "http://api.weatherapi.com/v1/current.json?key=72733a4a54444b9d88c211620232903 &q="


function getCurrent(event) {
    event.preventDefault()
    const weatherResultDiv = document.querySelector("#weatherResult")
    const currentWeather = document.querySelector("#currentWeather").value
    console.log(currentWeather)
    weatherResultDiv.innerHTML = "Loading..."
    fetch(URL + currentWeather)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            weatherResultDiv.innerHTML = `
            <h3> Location ${data.location.name}</h3>
            <h4> Current Temp ${data.current.temp_f}</h4>
            `
        })
        .catch(err => console.log(err))
}


