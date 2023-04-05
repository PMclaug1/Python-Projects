import React, { useState } from 'react'
import axios from 'axios'

const Homepage = () => {
    const [searchValue, setSearchValue] = useState("")
    const [weatherData, setWeatherData] = useState("")
    const [locationData, setLocationData] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()
        axios.get(`http://api.weatherapi.com/v1/current.json?key=72733a4a54444b9d88c211620232903 &q=${searchValue}&aqi=no`)
        .then(res => {
            setWeatherData(res.data.current)
            setLocationData(res.data.location)
            console.log(weatherData)
        })
        .catch(err=>{
            console.log("Error for API call", err)
        })    
    }

    return (
        <div>
            <h1>Enter a city or zip code </h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>City or Zip</label>
                    <input type="text" onChange={(e) => { setSearchValue(e.target.value) }} />
                </div>
                <div>
                    <button type='submit'>Search</button> |
                </div>
            </form>
            <div>
                <h3>{locationData.name}</h3>
                <h3>{weatherData.temp_f}</h3>
                <h3>{weatherData.feelslike_f}</h3>

            </div>
        </div>
    )
}

export default Homepage

