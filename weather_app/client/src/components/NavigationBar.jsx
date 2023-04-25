import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import AdbIcon from '@mui/icons-material/Adb';
import { Link } from 'react-router-dom';
import { styled, alpha } from '@mui/material/styles';
import InputBase from '@mui/material/InputBase';
import SearchIcon from '@mui/icons-material/Search';
import Container from '@mui/material/Container';
import axios from 'axios';
import { useState } from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';



const NavigationBar = () => {

  const [searchValue, setSearchValue] = useState("")
  const [weatherData, setWeatherData] = useState("")
  const [locationData, setLocationData] = useState("")

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log(searchValue)
    axios.get(`http://api.weatherapi.com/v1/current.json?key=72733a4a54444b9d88c211620232903 &q=${searchValue}&aqi=no`)
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

  const bull = (
    <Box
      component="span"
      sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
    >
      •
    </Box>
  );

  //Material UI styling for Search Bar
  const Search = styled('div')(({ theme }) => ({
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: alpha(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: alpha(theme.palette.common.white, 0.25),
    },
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing(1),
      width: '20%',
    },
  }));
  //Material UI styling for Search Bar
  const SearchIconWrapper = styled('div')(({ theme }) => ({
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  }));
  //Material UI styling for Search Bar
  const StyledInputBase = styled(InputBase)(({ theme }) => ({
    color: 'inherit',
    '& .MuiInputBase-input': {
      padding: theme.spacing(1, 1, 1, 0),
      // vertical padding + font size from searchIcon
      paddingLeft: `calc(1em + ${theme.spacing(4)})`,
      transition: theme.transitions.create('width'),
      width: '100%',
    },
  }));

  return (
    //Header Bar
    <>
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar>
            <AdbIcon />
            <Typography variant="h6" noWrap component="a" href="/"
              sx={{ mr: 2, fontFamily: 'monospace', fontWeight: 700, letterSpacing: '.3rem', color: 'inherit', textDecoration: 'none', }}>
              LOGO
            </Typography>
            <Typography variant="h5" component="div" sx={{ flexGrow: 1, marginRight: 6 }}>
              WeatherAPI
            </Typography>
            <Button color="inherit"><Link to={"/login"}>Login</Link></Button>
          </Toolbar>
        </AppBar>
      </Box>
      {/* Search Bar */}
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar sx={{ justifyContent: "center" }}>
            {/* <Search> */}
              {/* <SearchIconWrapper>
                <SearchIcon />
              </SearchIconWrapper> */}
              <form onSubmit={handleSubmit}>
                <input type="text" onChange={(e) => { setSearchValue(e.target.value) }} />
              </form>
            {/* </Search> */}
          </Toolbar>
        </AppBar>
      </Box>
      {/* Navigation Bar */}
      <AppBar position="static">
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'flex' }, justifyContent: "center" }}>
              {/* onClick={sendInquiry} */}
              <Button sx={{ my: 2, color: 'white', display: 'block' }}>Today</Button>
              <Button sx={{ my: 2, color: 'white', display: 'block' }}>Hourly</Button>
              <Button sx={{ my: 2, color: 'white', display: 'block' }}>10-Day</Button>
              <Button sx={{ my: 2, color: 'white', display: 'block' }}>Weekend</Button>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
      <div>
        <h1>Today's Weather in {locationData.name}, {locationData.region}</h1>
        <Container sx={{ marginY: 5, display: 'flex', justifyContent: 'center' }}>
          {/* Current Date/Time */}
          <Card sx={{ width: '30%', height: '300px' }}>
            <CardContent sx={{ alignItems: 'center', justifyContent: 'center', marginTop: '100px' }}>
              <Typography variant="h5" component="div">
                {locationData.localtime}
              </Typography>
            </CardContent>
          </Card>

          {/* Current Temperature */}
          <Card sx={{ width: '30%', height: '300px' }}>
            <CardContent sx={{ marginTop: '50px' }}>
              {/* <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                Word of the Day
                </Typography> */}
              <Typography variant="p" component="div">
                Temperature
              </Typography>
              <Typography variant="h3" component="div">
                {weatherData.temp_f}
              </Typography>
              <Typography variant="p" component="div" sx={{ marginTop: '20px' }}>
                Feels Like
              </Typography>
              <Typography variant="h3" component="div">
                {weatherData.feelslike_f}
              </Typography>
            </CardContent>
          </Card>
          {/* Current Condition */}
          <Card sx={{ width: '30%', height: '300px' }}>
            <CardMedia
              sx={{ width: 1 / 2, height: 1 / 2, marginLeft: 9, marginTop: 3 }}
              image={weatherData.condition.icon}
              title="weather icon"
            />
            <CardContent>
              <Typography variant="h5">
                {weatherData.condition.text}
              </Typography>
            </CardContent>
          </Card>
        </Container>

      </div>
    </>
  );
}

export default NavigationBar
