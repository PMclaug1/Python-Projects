import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { Container } from '@mui/material'

const bull = (
    <Box
      component="span"
      sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
    >
      •
    </Box>
  );


const TodaysForecast = (props) => {
  return (
    <div>
    <h1>Today's Weather in {props.locationData.name}, {props.locationData.region}</h1>
    <Container sx={{marginY: 5, display: 'flex', justifyContent: 'center'}}>
        {/* Current Date/Time */}
        <Card sx={{ width: '30%', height: '300px'}}>
            <CardContent sx={{alignItems: 'center', justifyContent:'center', marginTop:'100px'}}>
                <Typography variant="h5" component="div">
                {props.locationData.localtime}
                </Typography>
                <Typography variant="h5" component="div">
                </Typography>
            </CardContent>
        </Card>

        {/* Current Temperature */}
        <Card sx={{ width: '30%', height: '300px'}}>
            <CardContent sx={{marginTop:'50px'}}>
                {/* <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                Word of the Day
                </Typography> */}
                <Typography variant="p" component="div">
                Temperature 
                </Typography>
                <Typography variant="h3" component="div">
                {props.weatherData.temp_f}°
                </Typography>
                <Typography variant="p" component="div" sx={{marginTop:'20px'}}>
                Feels Like 
                </Typography>
                <Typography variant="h3" component="div">
                {props.weatherData.feelslike_f}°
                </Typography>
            </CardContent>
        </Card>
        {/* Current Condition */}
        <Card sx={{ width: '30%', height: '300px'}}>
            <CardMedia
                sx={{width: 1/2, height: 1/2, marginLeft: 9, marginTop: 3 }}
                image={props.weatherData.condition.icon}
                title="weather icon"
            />
            <CardContent>
                <Typography variant="h5">
                {props.weatherData.condition.text}
                </Typography>
            </CardContent>
        </Card>
    </Container>

    </div>
  )
}

export default TodaysForecast