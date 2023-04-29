import React from 'react'
import {useState} from 'react';
import NavigationBar from '../components/NavigationBar'
import TodaysForecast from '../components/TodaysForecast'
import axios from 'axios'




const HomePage = () => {
  const [searchVal, setSearchVal] = useState("")
  const [weatherData, setWeatherData] = useState("")
  const [locationData, setLocationData] = useState("")



  const displaySearch = ( searchVal ) => {
    setSearchVal(searchVal);
    console.log(searchVal);
    axios.get(`http://api.weatherapi.com/v1/current.json?key=72733a4a54444b9d88c211620232903 &q=${searchVal}&aqi=no`)
    .then(res => {
      setWeatherData(res.data.current)
      setLocationData(res.data.location)
      console.log(weatherData)
      console.log(locationData)
    })
    .catch(err => {
      console.log("Error for API call", err)
    })
}



  return (
    <div>  
        <NavigationBar onSearch={displaySearch}/>
        <TodaysForecast weatherData={weatherData} locationData={locationData}/>
    </div>
  )
}

export default HomePage